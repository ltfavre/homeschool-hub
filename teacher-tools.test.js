// End-to-end tests for uploads, assignments, submissions and grading settings.
// Runs the real Worker against an in-memory SQLite database that mimics Cloudflare D1.
import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { DatabaseSync } from 'node:sqlite';
import worker from './_worker.js';

const ORIGIN = 'https://venvlearning.test';

// Minimal D1 stand-in: prepare/bind/first/all/run and batch (as a transaction).
function d1() {
  const db = new DatabaseSync(':memory:');
  const val = (v) => (v === undefined ? null : typeof v === 'boolean' ? Number(v) : v);
  const stmt = (sql, params = []) => ({
    bind: (...p) => stmt(sql, p.map(val)),
    first: async () => db.prepare(sql).get(...params) ?? null,
    all: async () => ({ results: db.prepare(sql).all(...params) }),
    run: async () => { const r = db.prepare(sql).run(...params); return { meta: { changes: Number(r.changes), last_row_id: Number(r.lastInsertRowid) } }; },
    _sync: () => { const r = db.prepare(sql).run(...params); return { meta: { changes: Number(r.changes), last_row_id: Number(r.lastInsertRowid) } }; },
  });
  return {
    raw: db,
    prepare: (sql) => stmt(sql),
    batch: async (list) => { db.exec('BEGIN'); try { const out = list.map((s) => s._sync()); db.exec('COMMIT'); return out; } catch (e) { db.exec('ROLLBACK'); throw e; } },
  };
}

const sha = async (t) => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t))), (b) => b.toString(16).padStart(2, '0')).join('');

async function setup() {
  const DB = d1();
  const schema = await readFile(new URL('./schema.sql', import.meta.url), 'utf8');
  for (const s of schema.split(';').map((x) => x.trim()).filter(Boolean)) DB.raw.exec(s);
  const users = [['parent-1', 'parent@example.com', 'Parent', 'parent', null], ['student-4', 'kid4', 'Ava', 'student', '4'], ['student-7', 'kid7', 'Ben', 'student', '7']];
  const tokens = {};
  for (const [id, username, name, role, grade] of users) {
    DB.raw.prepare('INSERT INTO family_users(id,username,display_name,role,grade,password_hash,password_salt,active) VALUES(?,?,?,?,?,?,?,1)').run(id, username, name, role, grade, 'x', 'y');
    tokens[id] = id.replace(/[^a-f0-9]/g, '').padEnd(64, 'a').slice(0, 64);
    DB.raw.prepare('INSERT INTO family_sessions(token_hash,user_id,expires_at) VALUES(?,?,?)').run(await sha(tokens[id]), id, Math.floor(Date.now() / 1000) + 3600);
  }
  const ASSETS = { async fetch(req) { const p = new URL(req.url).pathname; try { return new Response(await readFile(new URL('.' + (p === '/' ? '/index.html' : /\.[a-z]+$/.test(p) ? p : p + '.html'), import.meta.url))); } catch { return new Response('Not found', { status: 404 }); } } };
  const env = { DB, ASSETS };
  const call = (who, path, { method = 'GET', body, headers = {} } = {}) => {
    const h = { cookie: `venv_session=${tokens[who]}`, ...headers };
    if (method !== 'GET') { h.origin ??= ORIGIN; if (body !== undefined && !(body instanceof Uint8Array)) h['content-type'] ??= 'application/json'; }
    return worker.fetch(new Request(ORIGIN + path, { method, headers: h, body: body instanceof Uint8Array ? body : body === undefined ? undefined : JSON.stringify(body) }), env, {});
  };
  const upload = (who, name, bytes, query = '', headers = {}) => call(who, '/api/family/files?' + query, { method: 'POST', body: bytes, headers: { 'x-venv-upload': '1', 'x-file-name': encodeURIComponent(name), ...headers } });
  return { env, call, upload };
}

const bytes = (n, seed = 7) => { const b = new Uint8Array(n); for (let i = 0; i < n; i++) b[i] = (i * 31 + seed) % 256; return b; };

test('parent assigns work with an attachment; only that grade sees and downloads it', async () => {
  const { call, upload } = await setup();
  const big = bytes(1_300_000); // spans three D1 chunks
  const up = await upload('parent-1', 'Fractions worksheet.pdf', big, 'kind=attachment&subject=math');
  assert.equal(up.status, 201);
  const file = (await up.json()).file;
  assert.equal(file.size, big.length);
  const made = await call('parent-1', '/api/family/assignments', { method: 'POST', body: { title: 'Fraction practice', grade: '4', subject: 'math', category: 'work', due_date: '2026-10-30', points: 20, instructions: 'Do problems 1-10.', attachments: [file.id] } });
  assert.equal(made.status, 201);
  const id = (await made.json()).id;

  const four = await (await call('student-4', '/api/family/assignments')).json();
  assert.equal(four.assignments.length, 1);
  assert.equal(four.assignments[0].attachments[0].id, file.id);
  const dl = await call('student-4', file.url);
  assert.equal(dl.status, 200);
  assert.equal(dl.headers.get('content-type'), 'application/pdf');
  assert.deepEqual(new Uint8Array(await dl.arrayBuffer()), big);

  assert.equal((await (await call('student-7', '/api/family/assignments')).json()).assignments.length, 0);
  assert.equal((await call('student-7', file.url)).status, 404);

  // Hidden assignments disappear for the student and their attachments become private again.
  await call('parent-1', '/api/family/assignments', { method: 'POST', body: { id, title: 'Fraction practice', grade: '4', subject: 'math', category: 'work', due_date: '2026-10-30', points: 20, attachments: [file.id], published: false } });
  assert.equal((await (await call('student-4', '/api/family/assignments')).json()).assignments.length, 0);
  assert.equal((await call('student-4', file.url)).status, 404);
});

test('student turns in text and a photo; parent grades and returns it with feedback', async () => {
  const { call, upload } = await setup();
  const id = (await (await call('parent-1', '/api/family/assignments', { method: 'POST', body: { title: 'Lab report', grade: '7', subject: 'science', category: 'project', due_date: '2026-11-02', points: 50 } })).json()).id;
  assert.equal((await call('student-7', '/api/family/submissions', { method: 'POST', body: { assignment_id: id, body: '' } })).status, 400, 'empty work is refused');
  const pic = await upload('student-7', 'lab photo.jpg', bytes(2048), `assignment_id=${id}`);
  assert.equal(pic.status, 201);
  const picFile = (await pic.json()).file;
  assert.equal(picFile.kind, 'submission');
  assert.equal((await call('student-7', '/api/family/submissions', { method: 'POST', body: { assignment_id: id, body: 'My hypothesis was correct.' } })).status, 200);
  assert.equal((await call('student-4', picFile.url)).status, 404, 'another student cannot open it');

  const view = await (await call('parent-1', '/api/family/assignments?student=student-7')).json();
  const sub = view.assignments[0].submissions[0];
  assert.equal(sub.status, 'submitted');
  assert.equal(sub.body, 'My hypothesis was correct.');
  assert.equal(sub.files[0].id, picFile.id);
  assert.equal((await call('parent-1', picFile.url)).status, 200);

  assert.equal((await call('parent-1', '/api/family/grades', { method: 'POST', body: { student_id: 'student-7', key: `C|${id}`, subject: 'science', category: 'project', date: '2026-11-02', title: 'Lab report', points: 45, possible: 50, comment: 'Strong data table.' } })).status, 200);
  assert.equal((await call('parent-1', '/api/family/submissions', { method: 'POST', body: { assignment_id: id, student_id: 'student-7', status: 'returned', feedback: 'Great work. Label your axes next time.' } })).status, 200);

  const mine = await (await call('student-7', '/api/family/assignments')).json();
  assert.equal(mine.assignments[0].submissions[0].status, 'returned');
  assert.match(mine.assignments[0].submissions[0].feedback, /Label your axes/);
  const grades = await (await call('student-7', '/api/family/grades')).json();
  assert.equal(grades.rows.find((r) => r.k === `C|${id}`).p, 45);
  assert.equal((await upload('student-7', 'late.pdf', bytes(10), `assignment_id=${id}`)).status, 409, 'graded work is locked');

  // Deleting the assignment removes its grade and the student's files.
  assert.equal((await call('parent-1', '/api/family/assignments', { method: 'POST', body: { delete_id: id } })).status, 200);
  assert.equal((await (await call('student-7', '/api/family/grades')).json()).rows.length, 0);
  assert.equal((await call('parent-1', picFile.url)).status, 404);
});

test('library documents respect who they are shared with', async () => {
  const { call, upload } = await setup();
  const doc = (await (await upload('parent-1', 'Field trip permission.pdf', bytes(500), 'kind=document&audience=7&title=Field%20trip%20form')).json()).file;
  const priv = (await (await upload('parent-1', 'Transcript notes.docx', bytes(500), 'kind=document&audience=private')).json()).file;
  assert.equal(doc.title, 'Field trip form');
  const seven = (await (await call('student-7', '/api/family/files')).json()).files.map((f) => f.id);
  const four = (await (await call('student-4', '/api/family/files')).json()).files.map((f) => f.id);
  assert.deepEqual(seven, [doc.id]);
  assert.deepEqual(four, []);
  assert.equal((await call('student-7', priv.url)).status, 404);
  assert.equal((await call('parent-1', `/api/family/files/${doc.id}`, { method: 'POST', body: { audience: 'both' } })).status, 200);
  assert.deepEqual((await (await call('student-4', '/api/family/files')).json()).files.map((f) => f.id), [doc.id]);
  assert.equal((await call('student-4', `/api/family/files/${doc.id}`, { method: 'POST', body: { delete: true } })).status, 403);
  assert.equal((await call('parent-1', `/api/family/files/${doc.id}`, { method: 'POST', body: { delete: true } })).status, 200);
  assert.equal((await call('student-4', doc.url)).status, 404);
});

test('uploads refuse cross-site requests, unsafe types, and student library uploads', async () => {
  const { upload, call } = await setup();
  assert.equal((await upload('parent-1', 'a.pdf', bytes(10), 'kind=document', { 'x-venv-upload': '0' })).status, 403);
  assert.equal((await upload('parent-1', 'a.pdf', bytes(10), 'kind=document', { origin: 'https://evil.example' })).status, 403);
  assert.equal((await upload('parent-1', 'page.html', bytes(10), 'kind=document')).status, 415);
  assert.equal((await upload('parent-1', 'pic.svg', bytes(10), 'kind=document')).status, 415);
  assert.equal((await upload('student-4', 'notes.pdf', bytes(10), 'kind=document')).status, 403, 'students only upload to an assignment');
  assert.equal((await call('student-4', '/api/family/assignments', { method: 'POST', body: { title: 'x', grade: '4', subject: 'math', category: 'work', due_date: '2026-10-30', points: 5 } })).status, 403);
  const txt = (await (await upload('parent-1', 'notes.txt', new TextEncoder().encode('<script>alert(1)</script>'), 'kind=document')).json()).file;
  const r = await call('parent-1', txt.url + '?download=1');
  assert.match(r.headers.get('content-disposition'), /^attachment/);
  assert.equal(r.headers.get('x-content-type-options'), 'nosniff');
});

test('grading settings are parent-only and validated', async () => {
  const { call } = await setup();
  const good = { weights: { work: 30, quiz: 20, test: 30, project: 20 }, defaultPossible: { work: 10, quiz: 20, test: 50, project: 100 }, scale: [[93, 'A'], [85, 'B'], [75, 'C'], [65, 'D']] };
  assert.equal((await call('student-4', '/api/family/settings/grading', { method: 'POST', body: good })).status, 403);
  assert.equal((await call('parent-1', '/api/family/settings/grading', { method: 'POST', body: { ...good, weights: { work: 0, quiz: 0, test: 0, project: 0 } } })).status, 400);
  assert.equal((await call('parent-1', '/api/family/settings/grading', { method: 'POST', body: good })).status, 200);
  const saved = (await (await call('student-4', '/api/family/settings/grading')).json()).grading;
  assert.equal(saved.weights.project, 20);
  assert.deepEqual(saved.scale.at(-1), [0, 'F'], 'an F floor is added');
});

test('students can open the new Library and Assignments pages; server code stays private', async () => {
  const { call } = await setup();
  for (const p of ['/library', '/assignments', '/library.js', '/assignments.js', '/files.js', '/reading-list.json']) assert.equal((await call('student-4', p)).status, 200, p);
  assert.equal((await call('parent-1', '/teacher-tools.js')).status, 404);
  assert.equal((await call('parent-1', '/tools/build-reading-list.py')).status, 404);
});

test('Home Assistant shows assignments, readings and shared files, and checks work off', async () => {
  const { env, call, upload } = await setup();
  // A school connection key, created the same way the parent page does.
  const key = await (await call('parent-1', '/api/family/home-assistant-token', { method: 'POST', body: { action: 'create' } })).json();
  const ha = (path, opts = {}) => worker.fetch(new Request(ORIGIN + path, { method: opts.method || 'GET', headers: { authorization: 'Bearer ' + key.token, ...(opts.body ? { 'content-type': 'application/json' } : {}) }, body: opts.body ? JSON.stringify(opts.body) : undefined }), env, {});
  const sheet = (await (await upload('parent-1', 'Map practice.pdf', bytes(300), 'kind=attachment')).json()).file;
  const privateDoc = (await (await upload('parent-1', 'Taxes.pdf', bytes(50), 'kind=document&audience=private')).json()).file;
  const shared = (await (await upload('parent-1', 'Field trip.pdf', bytes(70), 'kind=document&audience=both')).json()).file;
  const today = new Intl.DateTimeFormat('en-CA', { timeZone: 'America/Chicago' }).format(new Date());
  const id = (await (await call('parent-1', '/api/family/assignments', { method: 'POST', body: { title: 'Label the regions map', grade: '4', subject: 'social', category: 'work', due_date: today, points: 10, attachments: [sheet.id], allow_submission: false } })).json()).id;
  await call('parent-1', '/api/family/assignments', { method: 'POST', body: { title: 'Hidden draft', grade: '4', subject: 'math', category: 'work', due_date: today, points: 10, published: false } });

  const agenda = await (await ha(`/api/home-assistant/agenda?start=${today}&end=${today}`)).json();
  const ava = agenda.students.find((s) => s.id === 'student-4'), ben = agenda.students.find((s) => s.id === 'student-7');
  assert.deepEqual(ava.assignments.map((a) => a.summary), ['Label the regions map']);
  assert.equal(ben.assignments.length, 0);
  assert.equal(ava.assignments[0].status, 'due_today');
  assert.ok(ava.reading.books.length >= 1, 'current module reading');
  assert.deepEqual(ava.documents.map((d) => d.title), ['Field trip']);

  // Signed links open without a login; tampering or private files do not.
  const link = ava.assignments[0].attachments[0].url;
  const open = await worker.fetch(new Request(link), env, {});
  assert.equal(open.status, 200);
  assert.equal((await open.arrayBuffer()).byteLength, 300);
  assert.equal((await worker.fetch(new Request(link.replace(/s=(.)/, (m, c) => 's=' + (c === '0' ? '1' : '0'))), env, {})).status, 403);
  assert.equal((await worker.fetch(new Request(link.replace(sheet.id, privateDoc.id)), env, {})).status, 403);
  assert.equal((await worker.fetch(new Request(ava.documents[0].url), env, {})).status, 200);

  // Checking it off on the tablet shows as turned in for the parent; unchecking takes it back.
  assert.equal((await ha('/api/home-assistant/completion', { method: 'POST', body: { student_id: 'student-4', assignment_id: id, completed: true } })).status, 200);
  const view = await (await call('parent-1', '/api/family/assignments?student=student-4')).json();
  assert.equal(view.assignments.find((a) => a.id === id).submissions[0].status, 'submitted');
  assert.equal((await ha('/api/home-assistant/completion', { method: 'POST', body: { student_id: 'student-7', assignment_id: id, completed: true } })).status, 404, 'other grade');
  await ha('/api/home-assistant/completion', { method: 'POST', body: { student_id: 'student-4', assignment_id: id, completed: false } });
  assert.equal((await (await ha(`/api/home-assistant/agenda?start=${today}&end=${today}`)).json()).students.find((s) => s.id === 'student-4').assignments[0].completed, false);
  // Once graded, the checkmark is locked.
  await call('parent-1', '/api/family/grades', { method: 'POST', body: { student_id: 'student-4', key: `C|${id}`, subject: 'social', category: 'work', date: today, title: 'Label the regions map', points: 9, possible: 10 } });
  assert.equal((await ha('/api/home-assistant/completion', { method: 'POST', body: { student_id: 'student-4', assignment_id: id, completed: false } })).status, 409);
  const graded = (await (await ha(`/api/home-assistant/agenda?start=${today}&end=${today}`)).json()).students.find((s) => s.id === 'student-4').assignments[0];
  assert.equal(graded.status, 'graded'); assert.equal(graded.score, 9);
  assert.equal((await ha('/api/home-assistant/agenda', {})).status, 200);
  assert.equal((await worker.fetch(new Request(ORIGIN + '/api/home-assistant/agenda'), env, {})).status, 401, 'key required');
});
