// Runs the Tutor's curriculum tools against the real data and a full tutoring turn against a stand-in for Claude.
// Needs the knowledge files (npm run setup, or npm run knowledge) but no API key.
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {loadKnowledge, toolsFor} from './knowledge.js';
import {Conversations, tutorTurn} from './tutor.js';
import {systemPrompt} from './prompt.js';

const DATA = process.env.TUTOR_DATA_DIR || path.join(os.homedir(), 'VenvLearningTutor');
const K = loadKnowledge(DATA);
const g4 = {id: 'grade4', grade: 4, name: 'Ava'}, g7 = {id: 'grade7', grade: 7, name: 'Mia'};

test('schedule shows the day\'s lessons, Reader pages, and Friday checks for the right grade', () => {
  const t = toolsFor(K, g7);
  const [tue] = t.run.get_schedule({start_date: '2026-11-03'});
  assert.equal(tue.school_day, true);
  const ela = tue.todo.find(x => x.subject.startsWith('ELA'));
  assert.equal(ela.title, 'Lesson 1.5: Connotation and Denotation');
  assert.ok(ela.tasks.some(s => /A Christmas Carol, Stave One \(second section\)/.test(s)));
  assert.ok(!JSON.stringify(tue).includes('Spanish'));
  const week = t.run.get_schedule({start_date: '2026-11-02', end_date: '2026-11-08'});
  assert.equal(week.length, 7);
  assert.ok(week[4].checks_and_tests_today.some(s => /Weekly Check/.test(s)));
  assert.equal(week[5].school_day, false);
  assert.equal(toolsFor(K, g4).run.get_schedule({start_date: '2026-11-03'})[0].todo.find(x => x.subject.startsWith('ELA')).tasks.some(s => /King Arthur/.test(s)), true);
  assert.equal(t.run.get_schedule({start_date: '2026-11-01', end_date: '2027-01-01'}).length, 14);
});

test('lessons, search, Reader, and checks are scoped to the child\'s grade', () => {
  const t7 = toolsFor(K, g7), t4 = toolsFor(K, g4);
  const L = t7.run.get_lesson({subject: 'ela', lesson: '1.1'});
  assert.equal(L.title, "Reading Dickens's Language"); assert.equal(L.date, '2026-10-27');
  assert.ok(L.workbook.length && L.workbook[0].items[0].answer);
  assert.match(t4.run.get_lesson({subject: 'math', lesson: '1.1'}).title, /Place Value/);
  assert.ok(t7.run.find_lessons({query: 'connotation denotation'}).some(x => x.lesson === '1.5' && x.subject === 'ela'));
  assert.ok(t4.run.find_lessons({query: 'fractions'}).every(x => x.subject));
  const parts = t7.run.read_reader({});
  assert.ok(parts['A Christmas Carol'].some(s => s.startsWith('Stave Five')));
  assert.ok(!('King Arthur and the Round Table' in parts));
  const s1 = t7.run.read_reader({part: 'Christmas Carol', section: 'Stave One (first section)'});
  assert.match(s1.text, /^MARLEY was dead/); assert.ok(s1.more.next_offset > 0);
  assert.equal(t7.run.read_reader({part: 'Christmas Carol', section: 'Stave One (first section)', offset: s1.more.next_offset}).text.length > 0, true);
  const c = t7.run.get_check_or_test({subject: 'ela', title: 'Unit 1 Test'});
  assert.equal(c.kind, 'test'); assert.ok(c.sections.length);
  assert.ok(t7.run.get_lesson({subject: 'ela', lesson: '99.9'}).error);
});

test('the prompt fits each child\'s age and states the hints-only rule', () => {
  const p4 = systemPrompt(g4), p7 = systemPrompt(g7);
  assert.match(p4, /4th grade/); assert.match(p4, /Ava/); assert.match(p7, /7th grade/);
  for (const p of [p4, p7]) { assert.match(p, /Never give the answer to an assigned problem/); assert.match(p, /trusted adult/); }
  assert.equal(systemPrompt(g7), p7, 'stable for prompt caching');
});

// A stand-in for client.beta.messages.stream: replays scripted assistant messages and records each request.
function fakeClient(script) {
  const requests = [];
  return {requests, beta: {messages: {stream(params) {
    requests.push(JSON.parse(JSON.stringify(params)));
    const msg = script.shift(); const handlers = {};
    return {on(ev, fn) { (handlers[ev] ||= []).push(fn); return this; },
      async finalMessage() { for (const b of msg.content) if (b.type === 'text') for (const fn of handlers.text || []) fn(b.text); return msg; }};
  }}}};
}

test('a tutoring turn runs the tools, streams text, and saves an append-only history', async () => {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'tutor-')), convs = new Conversations(dir);
  const client = fakeClient([
    {stop_reason: 'tool_use', usage: {input_tokens: 10, output_tokens: 5}, content: [{type: 'text', text: 'Let me check.'}, {type: 'tool_use', id: 'tu1', name: 'get_schedule', input: {start_date: '2026-11-03'}}]},
    {stop_reason: 'end_turn', usage: {input_tokens: 20, output_tokens: 8, cache_read_input_tokens: 15}, content: [{type: 'text', text: 'Today you have **Lesson 1.5**.'}]},
    {stop_reason: 'tool_use', usage: {}, content: [{type: 'tool_use', id: 'tu2', name: 'get_lesson', input: {subject: 'history', lesson: '1'}}]},
    {stop_reason: 'end_turn', usage: {}, content: [{type: 'text', text: 'Which subject?'}]},
  ]);
  const conv = convs.create(g7), events = [], emit = e => events.push(e);
  await tutorTurn({client, child: g7, tools: toolsFor(K, g7), conv, message: 'What do I have today?', emit});
  convs.save(conv);
  const req = client.requests[0];
  assert.equal(req.model, 'claude-opus-5-5'); assert.equal(req.fallbacks, 'default'); assert.deepEqual(req.betas, ['server-side-fallback-2026-07-01']);
  assert.equal(req.messages[1].role, 'system'); assert.match(req.messages[1].content, /^Today is/);
  assert.ok(req.tools.every(t => t.eager_input_streaming));
  const toolResult = client.requests[1].messages.at(-1).content[0];
  assert.equal(toolResult.tool_use_id, 'tu1'); assert.match(toolResult.content, /Connotation and Denotation/);
  assert.ok(events.some(e => e.type === 'status' && /schedule/.test(e.text)));
  assert.equal(conv.transcript.at(-1).text, 'Let me check.\n\nToday you have **Lesson 1.5**.');
  assert.equal(conv.usage.cache_read, 15);
  // second turn: same day, no new date note; an invalid tool input comes back as an error result
  const before = JSON.stringify(conv.api);
  await tutorTurn({client, child: g7, tools: toolsFor(K, g7), conv, message: 'Help with history', emit});
  assert.ok(JSON.stringify(client.requests[2].messages).startsWith(before.slice(0, -1)), 'history is append-only');
  assert.equal(client.requests[2].messages.filter(m => m.role === 'system').length, 1);
  assert.equal(client.requests[3].messages.at(-1).content[0].is_error, true);
  assert.equal(convs.list('grade7')[0].turns, 1);
  assert.equal(convs.load('grade7', conv.id).transcript.length, 2);
  assert.throws(() => convs.load('../x', conv.id) ?? convs.file('../x', conv.id));
});

test('a refusal is replaced with a kind redirect', async () => {
  const conv = new Conversations(fs.mkdtempSync(path.join(os.tmpdir(), 'tutor-'))).create(g4);
  const client = fakeClient([{stop_reason: 'refusal', usage: {}, content: []}]);
  const out = await tutorTurn({client, child: g4, tools: toolsFor(K, g4), conv, message: 'something off limits', emit: () => {}});
  assert.match(out, /talk over with your parent/); assert.equal(conv.api.at(-1).role, 'assistant');
});
