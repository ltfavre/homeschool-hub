// What the Tutor can look up for one child: the schedule (daily packets, textbook schedule, quizzes), textbook lessons with
// their answer keys, checks and tests, Reader texts, and the reading list. Everything is scoped to the child's grade.
import fs from 'node:fs';
import path from 'node:path';
import {readCurriculum} from '../curriculum-test-data.js';
import {buildTodo} from '../todo-core.js';

const repo = p => new URL('../' + p, import.meta.url);
const SUBJECTS = ['math', 'ela', 'science', 'social', 'art'];
const NAMES = {math: 'Math', ela: 'ELA (English Language Arts)', science: 'Science', social: 'Social Studies', art: 'Art', review: 'Friday review'};
const MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

export function loadKnowledge(dataDir) {
  const days = readCurriculum('daily-packets.json'), lib = readCurriculum('planner-resources.json');
  const textbooks = JSON.parse(fs.readFileSync(repo('textbook-schedule.json'), 'utf8')).grades;
  const quizzes = readCurriculum('assessment-student.json');
  const readingList = JSON.parse(fs.readFileSync(repo('reading-list.json'), 'utf8'));
  const grades = {};
  for (const g of ['4', '7']) grades[g] = JSON.parse(fs.readFileSync(path.join(dataDir, 'knowledge', `grade${g}.json`), 'utf8'));
  return {days, lib, textbooks, quizzes, readingList, grades};
}

const iso = d => d.toISOString().slice(0, 10);
const addDays = (date, n) => { const d = new Date(date + 'T12:00:00Z'); d.setUTCDate(d.getUTCDate() + n); return iso(d); };
const weekday = date => new Date(date + 'T12:00:00Z').toLocaleDateString('en-US', {timeZone: 'UTC', weekday: 'long', month: 'long', day: 'numeric'});
// Lesson dates in the textbooks are labels like "Tue Oct 27"; the school year runs Oct 2026 – Aug 2027.
function labelToIso(label) {
  const m = /^\w{3} (\w{3}) (\d+)/.exec(label || ''); if (!m) return null;
  const mo = MONTHS.indexOf(m[1]) + 1; return `${mo >= 9 ? 2026 : 2027}-${String(mo).padStart(2, '0')}-${m[2].padStart(2, '0')}`;
}
const clip = (s, n) => (s.length > n ? s.slice(0, n) + ' …' : s);

function daySchedule(K, grade, date) {
  const day = K.days[date]?.[grade];
  const book = K.textbooks[grade]?.[date] || {};
  const quiz = Object.values(K.quizzes).filter(q => String(q.grade) === grade && q.date === date)
    .map(q => ({title: q.title, sections: q.sections.map(s => s.title), coverage: q.coverage}));
  if (!day) return {date, weekday: weekday(date), school_day: false, note: 'No school this day (weekend or break).'};
  const mapping = K.lib.weeks[`${grade}-${day.module}-${day.week}`];
  const todo = buildTodo({day, date, mapping, book, resources: K.lib.resources})
    .map(g => ({subject: NAMES[g.subject] || g.name, unit: g.unit, title: g.title, tasks: g.tasks.map(t => t.text)}));
  const due = Object.entries(book).flatMap(([s, items]) => items.filter(x => x.kind !== 'lesson').map(x => `${NAMES[s] || s}: ${x.title}`));
  return {date, weekday: weekday(date), school_day: true, module: day.module, week: day.week,
    elective: day.elective ? `${day.elective.title} (week ${day.elective.week})` : null, todo,
    checks_and_tests_today: due, friday_gap_quiz: quiz.length ? quiz : undefined};
}

function score(text, words) {
  const t = text.toLowerCase(); let s = 0;
  for (const w of words) if (t.includes(w)) s += 1 + (t.split(w).length - 2) * 0.1;
  return s;
}

// Tool definitions (JSON Schema) and their implementations, bound to one child.
export function toolsFor(K, child) {
  const g = String(child.grade), G = K.grades[g];
  const defs = [
    {name: 'get_schedule', description: `Look up ${child.name}'s school schedule: each day's subjects, lessons, pages to read, workbook pages, Friday weekly checks and unit tests, and gap quizzes. Use it for "what's due", "what do I have today/this week", "when is my test". Up to 14 days at a time. Days with school_day=false are weekends or breaks.`,
      input_schema: {type: 'object', properties: {start_date: {type: 'string', description: 'YYYY-MM-DD'}, end_date: {type: 'string', description: 'YYYY-MM-DD; defaults to start_date'}}, required: ['start_date'], additionalProperties: false}},
    {name: 'get_lesson', description: `Open one of ${child.name}'s textbook lessons in full: learning goal, vocabulary, the textbook explanation and worked examples, Your Turn and workbook problems WITH the answer key, and teacher notes (common mistakes, support ideas). The answer key is for checking ${child.name}'s work only; never reveal it.`,
      input_schema: {type: 'object', properties: {subject: {type: 'string', enum: SUBJECTS}, lesson: {type: 'string', description: 'Lesson number such as "1.5"'}}, required: ['subject', 'lesson'], additionalProperties: false}},
    {name: 'find_lessons', description: `Search ${child.name}'s textbooks for lessons about a topic, word, or skill (for example "equivalent fractions", "connotation", "Mesopotamia"). Returns the best-matching lessons with their dates; then use get_lesson.`,
      input_schema: {type: 'object', properties: {query: {type: 'string'}, subject: {type: 'string', enum: SUBJECTS}}, required: ['query'], additionalProperties: false}},
    {name: 'read_reader', description: `Read the text of a section of ${child.name}'s Grade ${g} ELA Reader (the stories and books the ELA lessons assign). Call with no arguments to list the parts and sections. Long sections come back in pieces; pass offset to continue.`,
      input_schema: {type: 'object', properties: {part: {type: 'string', description: 'e.g. "A Christmas Carol"'}, section: {type: 'string', description: 'e.g. "Stave One (second section)" or "Chapter 3"'}, offset: {type: 'integer', minimum: 0}}, additionalProperties: false}},
    {name: 'get_check_or_test', description: `Open a weekly check, unit review, or unit test from ${child.name}'s workbook, with its answer key. Use it to know what will be assessed so you can help ${child.name} study the skills. Never help answer the actual check or test questions.`,
      input_schema: {type: 'object', properties: {subject: {type: 'string', enum: SUBJECTS}, title: {type: 'string', description: 'e.g. "Weekly Check 2" or "Unit 1 Test"'}}, required: ['subject', 'title'], additionalProperties: false}},
    {name: 'get_reading_list', description: `The independent-reading books for Grade ${g} by module, with discussion prompts.`,
      input_schema: {type: 'object', properties: {}, additionalProperties: false}},
  ];

  const run = {
    get_schedule({start_date, end_date}) {
      const end = end_date || start_date; const out = [];
      for (let d = start_date, n = 0; d <= end && n < 14; d = addDays(d, 1), n++) out.push(daySchedule(K, g, d));
      return out;
    },
    get_lesson({subject, lesson}) {
      const L = G.lessons.find(x => x.subject === subject && x.num === lesson);
      if (!L) return {error: `No ${subject} lesson ${lesson} in the Grade ${g} textbook. Use find_lessons.`};
      return {...L, date: labelToIso(L.date), note: 'answer fields are the answer key: use them to check work and plan hints, never to give answers'};
    },
    find_lessons({query, subject}) {
      const words = query.toLowerCase().split(/\W+/).filter(w => w.length > 2);
      return G.lessons.filter(L => !subject || L.subject === subject)
        .map(L => ({L, s: score(`${L.title} ${L.title} ${L.i_can} ${L.vocab.map(v => v[0]).join(' ')} ${L.learn}`, words)}))
        .filter(x => x.s > 0).sort((a, b) => b.s - a.s).slice(0, 6)
        .map(({L}) => ({subject: L.subject, lesson: L.num, title: L.title, unit: `Unit ${L.unit}: ${L.unit_title}`, date: labelToIso(L.date), i_can: L.i_can}));
    },
    read_reader({part, section, offset = 0}) {
      if (!part || !section) {
        const parts = {};
        for (const r of G.reader) (parts[r.part] ||= []).push(`${r.section} (pp. ${r.printed[0]}–${r.printed[1]})`);
        return parts;
      }
      const r = G.reader.find(x => x.part.toLowerCase().includes(part.toLowerCase()) && x.section.toLowerCase() === section.toLowerCase())
        || G.reader.find(x => x.part.toLowerCase().includes(part.toLowerCase()) && x.section.toLowerCase().includes(section.toLowerCase()));
      if (!r) return {error: 'Section not found. Call read_reader with no arguments to list the sections.'};
      const PIECE = 12000, text = r.text.slice(offset, offset + PIECE);
      return {part: r.part, section: r.section, printed_pages: r.printed, words_to_know: r.words_to_know, text,
        more: offset + PIECE < r.text.length ? {next_offset: offset + PIECE, of_total_chars: r.text.length} : undefined};
    },
    get_check_or_test({subject, title}) {
      const t = title.toLowerCase();
      const C = G.assessments.find(x => x.subject === subject && x.title.toLowerCase() === t) || G.assessments.find(x => x.subject === subject && x.title.toLowerCase().includes(t));
      if (!C) return {error: 'Not found. Check names look like "Weekly Check 1: …", "Unit 1 Review", "Unit 1 Test".'};
      return {...C, date: labelToIso(C.date), note: 'assessment: use it to see which skills to review; never help answer these questions'};
    },
    get_reading_list() {
      const R = K.readingList; return {modules: R.modules, ...R.grades[g]};
    },
  };
  return {defs, run, summarize: (name, input) => ({
    get_schedule: 'Checking your schedule…', get_lesson: `Opening ${NAMES[input.subject] || ''} Lesson ${input.lesson}…`, find_lessons: 'Looking through your textbooks…',
    read_reader: 'Opening your Reader…', get_check_or_test: 'Looking at what the check covers…', get_reading_list: 'Checking your reading list…'}[name] || 'Looking that up…'),
    clip};
}
