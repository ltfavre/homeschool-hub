// One tutoring turn: send the conversation to Claude, run the curriculum tools it asks for, stream the reply back,
// and save the conversation (the full API history plus a readable transcript for the parent page).
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import Anthropic from '@anthropic-ai/sdk';
import {systemPrompt, dateNote} from './prompt.js';

export const MODEL = 'claude-opus-5-5';
const MAX_TOOL_ROUNDS = 8;
const REFUSAL_REPLY = "That's a question to talk over with your parent. Want to get back to your schoolwork? I'm happy to help with any subject.";

export class Conversations {
  constructor(dataDir) { this.dir = path.join(dataDir, 'chats'); }
  file(childId, id) {
    if (!/^[a-z0-9-]+$/.test(childId) || !/^[0-9a-f-]{36}$/.test(id)) throw new Error('bad conversation id');
    return path.join(this.dir, childId, id + '.json');
  }
  create(child) {
    const now = new Date().toISOString();
    return {id: crypto.randomUUID(), child: child.id, child_name: child.name, grade: child.grade, started: now, updated: now, title: '', api: [], transcript: [], usage: {input: 0, output: 0, cache_read: 0}};
  }
  load(childId, id) {
    try { return JSON.parse(fs.readFileSync(this.file(childId, id), 'utf8')); } catch { return null; }
  }
  save(conv) {
    const f = this.file(conv.child, conv.id); fs.mkdirSync(path.dirname(f), {recursive: true});
    fs.writeFileSync(f + '.tmp', JSON.stringify(conv)); fs.renameSync(f + '.tmp', f);
  }
  list(childId) {
    const d = path.join(this.dir, childId); if (!fs.existsSync(d)) return [];
    return fs.readdirSync(d).filter(f => f.endsWith('.json')).map(f => {
      const c = JSON.parse(fs.readFileSync(path.join(d, f), 'utf8'));
      return {id: c.id, child: c.child, child_name: c.child_name, title: c.title, started: c.started, updated: c.updated, turns: c.transcript.filter(t => t.role === 'student').length};
    }).sort((a, b) => b.updated.localeCompare(a.updated));
  }
}

function validInput(def, input) {
  if (!input || typeof input !== 'object' || Array.isArray(input)) return false;
  const props = def.input_schema.properties || {};
  for (const k of def.input_schema.required || []) if (input[k] === undefined) return false;
  for (const [k, v] of Object.entries(input)) {
    const p = props[k]; if (!p) return false;
    if (p.type === 'string' && typeof v !== 'string') return false;
    if (p.type === 'integer' && !Number.isInteger(v)) return false;
    if (p.enum && !p.enum.includes(v)) return false;
  }
  return true;
}

// emit({type: 'text', delta} | {type: 'status', text} | {type: 'error', text})
export async function tutorTurn({client, child, tools, conv, message, emit}) {
  const now = new Date();
  const today = now.toDateString();
  conv.api.push({role: 'user', content: message});
  // The date goes in as a system message at the start of a conversation and whenever the day changes.
  if (conv.last_date !== today) { conv.api.push({role: 'system', content: dateNote(now)}); conv.last_date = today; }
  conv.transcript.push({role: 'student', text: message, at: now.toISOString()});
  if (!conv.title) conv.title = message.slice(0, 80);

  const defs = tools.defs.map(d => ({...d, eager_input_streaming: true}));
  let answer = '';
  for (let round = 0; round < MAX_TOOL_ROUNDS; round++) {
    const stream = client.beta.messages.stream({
      model: MODEL, max_tokens: 16000,
      betas: ['server-side-fallback-2026-07-01'], fallbacks: 'default',
      thinking: {type: 'adaptive'}, output_config: {effort: 'medium'},
      cache_control: {type: 'ephemeral'},
      system: systemPrompt(child), tools: defs, messages: conv.api,
    });
    stream.on('text', delta => { answer += delta; emit({type: 'text', delta}); });
    let msg;
    try {
      msg = await stream.finalMessage();
    } catch (err) {
      if (err instanceof Anthropic.APIError) throw err;
      if (round + 1 < MAX_TOOL_ROUNDS) continue;          // a tool input that wasn't parseable JSON: re-issue the turn
      throw err;
    }
    const u = msg.usage || {};
    conv.usage.input += (u.input_tokens || 0) + (u.cache_creation_input_tokens || 0); conv.usage.output += u.output_tokens || 0; conv.usage.cache_read += u.cache_read_input_tokens || 0;

    if (msg.stop_reason === 'refusal') {
      emit({type: 'text', delta: (answer ? '\n\n' : '') + REFUSAL_REPLY});
      conv.api.push({role: 'assistant', content: [{type: 'text', text: REFUSAL_REPLY}]});
      answer += (answer ? '\n\n' : '') + REFUSAL_REPLY;
      break;
    }
    conv.api.push({role: 'assistant', content: msg.content});
    const uses = msg.content.filter(b => b.type === 'tool_use');
    if (msg.stop_reason !== 'tool_use' || !uses.length) break;

    const results = [];
    for (const use of uses) {
      const def = tools.defs.find(d => d.name === use.name);
      if (!def || !validInput(def, use.input)) {
        results.push({type: 'tool_result', tool_use_id: use.id, is_error: true, content: `Invalid input for ${use.name}: ${JSON.stringify(use.input)}`});
        continue;
      }
      emit({type: 'status', text: tools.summarize(use.name, use.input)});
      try {
        results.push({type: 'tool_result', tool_use_id: use.id, content: JSON.stringify(tools.run[use.name](use.input))});
      } catch (e) {
        results.push({type: 'tool_result', tool_use_id: use.id, is_error: true, content: String(e.message || e)});
      }
    }
    conv.api.push({role: 'user', content: results});
    if (answer && !/\s$/.test(answer)) { answer += '\n\n'; emit({type: 'text', delta: '\n\n'}); }
  }
  conv.transcript.push({role: 'tutor', text: answer.trim(), at: new Date().toISOString()});
  conv.updated = new Date().toISOString();
  return answer;
}
