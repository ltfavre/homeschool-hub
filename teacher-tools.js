// Teacher tools: file uploads (documents, assignment attachments, student submissions),
// teacher-created assignments, online submissions, and grading settings.
//
// Storage: files go to an R2 bucket when the Worker has a FILES binding; otherwise they are
// stored in D1 as base64 chunks, so the feature works with no extra Cloudflare setup.

export const MAX_UPLOAD_BYTES = 25 * 1024 * 1024;
const CHUNK_BYTES = 512 * 1024; // ~700 KB of base64 per row, well under D1's 2 MB row limit
const SUBJECTS = ['math', 'ela', 'science', 'social', 'spanish', 'art', 'life', 'computer', 'skills'];
const CATEGORIES = ['work', 'quiz', 'test', 'project'];
const AUDIENCES = ['private', '4', '7', 'both'];

// Extension → type. Anything else (HTML, SVG, scripts, executables) is refused.
const TYPES = {
  pdf: 'application/pdf', png: 'image/png', jpg: 'image/jpeg', jpeg: 'image/jpeg', gif: 'image/gif', webp: 'image/webp', heic: 'image/heic',
  txt: 'text/plain', csv: 'text/csv', rtf: 'application/rtf', md: 'text/plain',
  doc: 'application/msword', docx: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  xls: 'application/vnd.ms-excel', xlsx: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  ppt: 'application/vnd.ms-powerpoint', pptx: 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
  odt: 'application/vnd.oasis.opendocument.text', ods: 'application/vnd.oasis.opendocument.spreadsheet', odp: 'application/vnd.oasis.opendocument.presentation',
  epub: 'application/epub+zip', mp3: 'audio/mpeg', m4a: 'audio/mp4', wav: 'audio/wav', mp4: 'video/mp4', mov: 'video/quicktime', zip: 'application/zip',
};
// Types a browser may show in a tab. Everything else downloads.
const INLINE = new Set(['application/pdf', 'image/png', 'image/jpeg', 'image/gif', 'image/webp', 'text/plain', 'audio/mpeg', 'audio/mp4', 'audio/wav', 'video/mp4']);

const json = (data, status = 200) => new Response(JSON.stringify(data), { status, headers: { 'content-type': 'application/json;charset=utf-8', 'cache-control': 'no-store', 'x-content-type-options': 'nosniff' } });
const epoch = () => Math.floor(Date.now() / 1000);
const newId = () => Array.from(crypto.getRandomValues(new Uint8Array(12)), (b) => b.toString(16).padStart(2, '0')).join('');
const text = (v, max) => String(v ?? '').trim().slice(0, max);
function safeDate(d) { if (!/^\d{4}-\d{2}-\d{2}$/.test(d)) return false; const v = new Date(d + 'T12:00:00Z'); return !isNaN(v) && v.toISOString().slice(0, 10) === d; }
export function fileType(name) { const ext = String(name).toLowerCase().match(/\.([a-z0-9]{1,5})$/)?.[1]; return ext && TYPES[ext] ? TYPES[ext] : null; }
const cleanName = (n) => String(n || '').replace(/[\\/\u0000-\u001f"<>|:*?]+/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 140) || 'file';

export function toBase64(bytes) {
  let s = '';
  for (let i = 0; i < bytes.length; i += 0x8000) s += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000));
  return btoa(s);
}
export function fromBase64(b64) { const s = atob(b64); const out = new Uint8Array(s.length); for (let i = 0; i < s.length; i++) out[i] = s.charCodeAt(i); return out; }

const SCHEMA = `
CREATE TABLE IF NOT EXISTS family_files (
  id TEXT PRIMARY KEY,
  owner_id TEXT NOT NULL,
  kind TEXT NOT NULL,
  title TEXT NOT NULL,
  name TEXT NOT NULL,
  mime TEXT NOT NULL,
  size INTEGER NOT NULL,
  storage TEXT NOT NULL,
  chunks INTEGER NOT NULL DEFAULT 0,
  audience TEXT NOT NULL DEFAULT 'private',
  subject TEXT NOT NULL DEFAULT '',
  note TEXT NOT NULL DEFAULT '',
  assignment_id INTEGER,
  created_at INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_family_files_kind ON family_files(kind, audience);
CREATE INDEX IF NOT EXISTS idx_family_files_assignment ON family_files(assignment_id, owner_id);
CREATE TABLE IF NOT EXISTS family_file_chunks (
  file_id TEXT NOT NULL,
  idx INTEGER NOT NULL,
  data TEXT NOT NULL,
  PRIMARY KEY (file_id, idx)
);
CREATE TABLE IF NOT EXISTS family_assignments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  grade TEXT NOT NULL,
  subject TEXT NOT NULL,
  category TEXT NOT NULL,
  title TEXT NOT NULL,
  instructions TEXT NOT NULL DEFAULT '',
  due_date TEXT NOT NULL,
  points REAL NOT NULL,
  allow_submission INTEGER NOT NULL DEFAULT 1,
  published INTEGER NOT NULL DEFAULT 1,
  attachments TEXT NOT NULL DEFAULT '[]',
  created_by TEXT NOT NULL DEFAULT '',
  created_at INTEGER NOT NULL,
  updated_at INTEGER NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_family_assignments_grade_due ON family_assignments(grade, due_date);
CREATE TABLE IF NOT EXISTS family_submissions (
  assignment_id INTEGER NOT NULL,
  student_id TEXT NOT NULL,
  body TEXT NOT NULL DEFAULT '',
  status TEXT NOT NULL DEFAULT 'submitted',
  feedback TEXT NOT NULL DEFAULT '',
  submitted_at INTEGER,
  returned_at INTEGER,
  PRIMARY KEY (assignment_id, student_id)
);
CREATE TABLE IF NOT EXISTS family_settings (
  key TEXT PRIMARY KEY,
  value TEXT NOT NULL,
  updated_at INTEGER NOT NULL
)`;
export async function ensureTeacherTables(db) {
  await db.batch(SCHEMA.split(';').map((s) => s.trim()).filter(Boolean).map((s) => db.prepare(s)));
}

const PATHS = /^\/api\/family\/(files(?:\/[a-f0-9]{24})?|assignments|submissions|settings\/grading)$/;
export const isTeacherToolsPath = (path) => PATHS.test(path);

async function studentById(db, id) { return db.prepare("SELECT * FROM family_users WHERE id=? AND role='student' AND active=1").bind(String(id || '')).first(); }
async function studentForGrade(db, grade) { return db.prepare("SELECT * FROM family_users WHERE grade=? AND role='student' AND active=1 ORDER BY id LIMIT 1").bind(String(grade)).first(); }
const publicFile = (f) => ({ id: f.id, title: f.title, name: f.name, mime: f.mime, size: f.size, kind: f.kind, audience: f.audience, subject: f.subject, note: f.note, assignment_id: f.assignment_id, owner_id: f.owner_id, created_at: f.created_at, url: '/api/family/files/' + f.id });

// May this user open this file?
export async function canRead(db, user, f) {
  if (user.role === 'parent') return true;
  if (f.kind === 'submission') return f.owner_id === user.id;
  if (f.kind === 'document' && (f.audience === 'both' || f.audience === String(user.grade))) return true;
  // Any file a published assignment for the student's grade links to.
  const hit = await db.prepare("SELECT 1 FROM family_assignments WHERE grade=? AND published=1 AND attachments LIKE ? LIMIT 1").bind(String(user.grade), `%"${f.id}"%`).first();
  return !!hit;
}

async function readFileBody(env, f) {
  if (f.storage === 'r2') { const obj = await env.FILES.get('files/' + f.id); return obj ? obj.body : null; }
  const db = env.DB; let i = 0;
  return new ReadableStream({
    async pull(controller) {
      if (i >= f.chunks) { controller.close(); return; }
      const row = await db.prepare('SELECT data FROM family_file_chunks WHERE file_id=? AND idx=?').bind(f.id, i++).first();
      if (!row) { controller.error(new Error('File data missing')); return; }
      controller.enqueue(fromBase64(row.data));
    },
  });
}

async function deleteFiles(env, ids) {
  if (!ids.length) return;
  const db = env.DB, stmts = [];
  for (const id of ids) {
    stmts.push(db.prepare('DELETE FROM family_file_chunks WHERE file_id=?').bind(id), db.prepare('DELETE FROM family_files WHERE id=?').bind(id));
    if (env.FILES && typeof env.FILES.delete === 'function') await env.FILES.delete('files/' + id).catch(() => {});
  }
  await db.batch(stmts);
}

async function upload(request, env, user, url) {
  const q = url.searchParams, db = env.DB;
  const declared = Number(request.headers.get('content-length') || 0);
  if (declared > MAX_UPLOAD_BYTES) return json({ error: 'Files can be up to 25 MB.' }, 413);
  const name = cleanName(decodeURIComponent(request.headers.get('x-file-name') || q.get('name') || ''));
  const mime = fileType(name);
  if (!mime) return json({ error: 'That file type is not allowed. Use PDF, Word, Excel, PowerPoint, images, text, audio or video.' }, 415);
  let kind = String(q.get('kind') || 'document'), audience = 'private', subject = '', assignmentId = null;
  if (user.role === 'parent') {
    if (!['document', 'attachment'].includes(kind)) return json({ error: 'Unknown upload type' }, 400);
    audience = AUDIENCES.includes(q.get('audience')) ? q.get('audience') : 'private';
    subject = SUBJECTS.includes(q.get('subject')) ? q.get('subject') : '';
  } else {
    // Students may only upload work for an assignment that accepts submissions.
    kind = 'submission';
    const a = await db.prepare('SELECT * FROM family_assignments WHERE id=? AND grade=? AND published=1').bind(Number(q.get('assignment_id')), String(user.grade)).first();
    if (!a || !a.allow_submission) return json({ error: 'This assignment does not accept uploads.' }, 403);
    const sub = await db.prepare('SELECT status FROM family_submissions WHERE assignment_id=? AND student_id=?').bind(a.id, user.id).first();
    if (sub?.status === 'returned') return json({ error: 'This work was already graded.' }, 409);
    const count = await db.prepare("SELECT COUNT(*) AS n FROM family_files WHERE kind='submission' AND assignment_id=? AND owner_id=?").bind(a.id, user.id).first();
    if ((count?.n || 0) >= 10) return json({ error: 'Up to 10 files per assignment.' }, 400);
    assignmentId = a.id; subject = a.subject;
  }
  const bytes = new Uint8Array(await request.arrayBuffer());
  if (!bytes.length) return json({ error: 'The file is empty.' }, 400);
  if (bytes.length > MAX_UPLOAD_BYTES) return json({ error: 'Files can be up to 25 MB.' }, 413);
  const id = newId(), title = text(q.get('title'), 160) || name.replace(/\.[^.]+$/, ''), note = text(q.get('note'), 500);
  let storage = 'd1', chunks = 0;
  if (env.FILES && typeof env.FILES.put === 'function') {
    await env.FILES.put('files/' + id, bytes, { httpMetadata: { contentType: mime } });
    storage = 'r2';
  } else {
    const stmts = [];
    for (let off = 0; off < bytes.length; off += CHUNK_BYTES) stmts.push(db.prepare('INSERT INTO family_file_chunks(file_id,idx,data) VALUES(?,?,?)').bind(id, chunks++, toBase64(bytes.subarray(off, off + CHUNK_BYTES))));
    for (let i = 0; i < stmts.length; i += 10) await db.batch(stmts.slice(i, i + 10));
  }
  await db.prepare('INSERT INTO family_files(id,owner_id,kind,title,name,mime,size,storage,chunks,audience,subject,note,assignment_id,created_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)')
    .bind(id, user.id, kind, title, name, mime, bytes.length, storage, chunks, audience, subject, note, assignmentId, epoch()).run();
  return json({ file: publicFile(await db.prepare('SELECT * FROM family_files WHERE id=?').bind(id).first()) }, 201);
}

async function download(request, env, user, id) {
  const f = await env.DB.prepare('SELECT * FROM family_files WHERE id=?').bind(id).first();
  if (!f || !(await canRead(env.DB, user, f))) return json({ error: 'File not found' }, 404);
  return fileResponse(request, env, f);
}

// Stream a stored file with safe headers. Callers check permission first.
export async function fileResponse(request, env, f) {
  const body = await readFileBody(env, f);
  if (!body) return json({ error: 'File data missing' }, 404);
  const inline = INLINE.has(f.mime) && new URL(request.url).searchParams.get('download') !== '1';
  const headers = {
    'content-type': f.mime, 'content-length': String(f.size), 'cache-control': 'private, no-store', 'x-content-type-options': 'nosniff',
    'content-disposition': `${inline ? 'inline' : 'attachment'}; filename="${f.name.replace(/[^\x20-\x7e]/g, '_')}"; filename*=UTF-8''${encodeURIComponent(f.name)}`,
  };
  if (!inline) headers['content-security-policy'] = "sandbox; default-src 'none'";
  return new Response(body, { headers });
}

async function assignmentRows(db, user, url) {
  if (user.role === 'parent') {
    const sid = url.searchParams.get('student');
    if (sid) { const s = await studentById(db, sid); if (!s) return { error: json({ error: 'Student not found' }, 404) }; return { student: s, rows: (await db.prepare('SELECT * FROM family_assignments WHERE grade=? ORDER BY due_date, id').bind(String(s.grade)).all()).results || [] }; }
    return { student: null, rows: (await db.prepare('SELECT * FROM family_assignments ORDER BY due_date, id').all()).results || [] };
  }
  return { student: user, rows: (await db.prepare('SELECT * FROM family_assignments WHERE grade=? AND published=1 ORDER BY due_date, id').bind(String(user.grade)).all()).results || [] };
}

async function listAssignments(env, user, url) {
  const db = env.DB, got = await assignmentRows(db, user, url);
  if (got.error) return got.error;
  const ids = [...new Set(got.rows.flatMap((a) => JSON.parse(a.attachments || '[]')))];
  const files = new Map();
  for (let i = 0; i < ids.length; i += 50) {
    const part = ids.slice(i, i + 50);
    for (const f of (await db.prepare(`SELECT * FROM family_files WHERE id IN (${part.map(() => '?').join(',')})`).bind(...part).all()).results || []) files.set(f.id, publicFile(f));
  }
  // Submissions: one student's (student view or parent with ?student), or all of them (parent overview).
  let subs = [], subFiles = [];
  if (got.student) {
    subs = (await db.prepare('SELECT * FROM family_submissions WHERE student_id=?').bind(got.student.id).all()).results || [];
    subFiles = (await db.prepare("SELECT * FROM family_files WHERE kind='submission' AND owner_id=?").bind(got.student.id).all()).results || [];
  } else if (user.role === 'parent') {
    subs = (await db.prepare('SELECT * FROM family_submissions').all()).results || [];
    subFiles = (await db.prepare("SELECT * FROM family_files WHERE kind='submission'").all()).results || [];
  }
  const assignments = got.rows.map((a) => {
    const mine = subs.filter((s) => s.assignment_id === a.id);
    return {
      id: a.id, grade: a.grade, subject: a.subject, category: a.category, title: a.title, instructions: a.instructions, due_date: a.due_date, points: a.points,
      allow_submission: !!a.allow_submission, published: !!a.published, key: 'C|' + a.id, created_at: a.created_at, updated_at: a.updated_at,
      attachments: JSON.parse(a.attachments || '[]').map((id) => files.get(id)).filter(Boolean),
      submissions: mine.map((s) => ({ student_id: s.student_id, body: s.body, status: s.status, feedback: s.feedback, submitted_at: s.submitted_at, returned_at: s.returned_at, files: subFiles.filter((f) => f.assignment_id === a.id && f.owner_id === s.student_id).map(publicFile) })),
      pending_files: got.student ? subFiles.filter((f) => f.assignment_id === a.id && !mine.length).map(publicFile) : [],
    };
  });
  return json({ student: got.student ? { id: got.student.id, grade: got.student.grade, display_name: got.student.display_name } : null, assignments });
}

async function saveAssignment(env, user, b) {
  const db = env.DB;
  if (b.delete_id !== undefined) {
    const id = Number(b.delete_id), a = await db.prepare('SELECT * FROM family_assignments WHERE id=?').bind(id).first();
    if (!a) return json({ error: 'Assignment not found' }, 404);
    const subFiles = ((await db.prepare("SELECT id FROM family_files WHERE kind='submission' AND assignment_id=?").bind(id).all()).results || []).map((r) => r.id);
    await deleteFiles(env, subFiles);
    await db.batch([db.prepare('DELETE FROM family_submissions WHERE assignment_id=?').bind(id), db.prepare('DELETE FROM family_grades WHERE item_key=?').bind('C|' + id), db.prepare('DELETE FROM family_assignments WHERE id=?').bind(id)]);
    return json({ ok: true });
  }
  const title = text(b.title, 160), instructions = text(b.instructions, 5000), grade = String(b.grade || ''), subject = String(b.subject || ''), category = String(b.category || ''), due = String(b.due_date || '');
  const points = Number(b.points);
  if (!title) return json({ error: 'Give the assignment a title.' }, 400);
  if (!['4', '7'].includes(grade) || !SUBJECTS.includes(subject) || !CATEGORIES.includes(category) || !safeDate(due)) return json({ error: 'Choose a grade, subject, type and due date.' }, 400);
  if (!Number.isFinite(points) || points <= 0 || points > 1000) return json({ error: 'Points must be between 1 and 1000.' }, 400);
  const wanted = Array.isArray(b.attachments) ? [...new Set(b.attachments.map(String))].filter((x) => /^[a-f0-9]{24}$/.test(x)).slice(0, 20) : [];
  let attachments = [];
  if (wanted.length) attachments = ((await db.prepare(`SELECT id FROM family_files WHERE kind IN ('document','attachment') AND id IN (${wanted.map(() => '?').join(',')})`).bind(...wanted).all()).results || []).map((r) => r.id);
  attachments = wanted.filter((id) => attachments.includes(id));
  const vals = [grade, subject, category, title, instructions, due, points, b.allow_submission === false ? 0 : 1, b.published === false ? 0 : 1, JSON.stringify(attachments)];
  if (b.id) {
    const r = await db.prepare('UPDATE family_assignments SET grade=?,subject=?,category=?,title=?,instructions=?,due_date=?,points=?,allow_submission=?,published=?,attachments=?,updated_at=? WHERE id=?').bind(...vals, epoch(), Number(b.id)).run();
    if (!r.meta?.changes) return json({ error: 'Assignment not found' }, 404);
    // Keep the gradebook entry in step with the assignment.
    await db.prepare('UPDATE family_grades SET title=?,subject=?,category=?,school_date=? WHERE item_key=?').bind(title, subject, category, due, 'C|' + Number(b.id)).run();
    return json({ ok: true, id: Number(b.id) });
  }
  const r = await db.prepare('INSERT INTO family_assignments(grade,subject,category,title,instructions,due_date,points,allow_submission,published,attachments,created_by,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)').bind(...vals, String(user.display_name || ''), epoch(), epoch()).run();
  return json({ ok: true, id: r.meta?.last_row_id }, 201);
}

async function saveSubmission(env, user, b) {
  const db = env.DB, id = Number(b.assignment_id);
  if (user.role === 'parent') {
    // Return graded work with feedback, or reopen it for the student.
    const s = await studentById(db, b.student_id); if (!s) return json({ error: 'Student not found' }, 404);
    const a = await db.prepare('SELECT * FROM family_assignments WHERE id=? AND grade=?').bind(id, String(s.grade)).first(); if (!a) return json({ error: 'Assignment not found' }, 404);
    const status = b.status === 'reopen' ? 'reopened' : 'returned';
    await db.prepare("INSERT INTO family_submissions(assignment_id,student_id,body,status,feedback,returned_at) VALUES(?,?,'',?,?,?) ON CONFLICT(assignment_id,student_id) DO UPDATE SET status=excluded.status,feedback=excluded.feedback,returned_at=excluded.returned_at")
      .bind(id, s.id, status, text(b.feedback, 2000), status === 'returned' ? epoch() : null).run();
    return json({ ok: true });
  }
  const a = await db.prepare('SELECT * FROM family_assignments WHERE id=? AND grade=? AND published=1').bind(id, String(user.grade)).first();
  if (!a) return json({ error: 'Assignment not found' }, 404);
  if (!a.allow_submission) return json({ error: 'This assignment is not turned in online.' }, 400);
  const prev = await db.prepare('SELECT status FROM family_submissions WHERE assignment_id=? AND student_id=?').bind(id, user.id).first();
  if (prev?.status === 'returned') return json({ error: 'This work was already graded.' }, 409);
  if (Array.isArray(b.remove_files) && b.remove_files.length) {
    const own = ((await db.prepare("SELECT id FROM family_files WHERE kind='submission' AND assignment_id=? AND owner_id=?").bind(id, user.id).all()).results || []).map((r) => r.id);
    await deleteFiles(env, b.remove_files.map(String).filter((x) => own.includes(x)));
  }
  if (b.unsubmit === true) {
    await db.prepare("UPDATE family_submissions SET status='draft' WHERE assignment_id=? AND student_id=?").bind(id, user.id).run();
    return json({ ok: true });
  }
  const body = text(b.body, 20000);
  const files = await db.prepare("SELECT COUNT(*) AS n FROM family_files WHERE kind='submission' AND assignment_id=? AND owner_id=?").bind(id, user.id).first();
  if (!body && !(files?.n > 0)) return json({ error: 'Write an answer or attach a file before turning it in.' }, 400);
  await db.prepare("INSERT INTO family_submissions(assignment_id,student_id,body,status,submitted_at) VALUES(?,?,?,'submitted',?) ON CONFLICT(assignment_id,student_id) DO UPDATE SET body=excluded.body,status='submitted',submitted_at=excluded.submitted_at")
    .bind(id, user.id, body, epoch()).run();
  return json({ ok: true });
}

export const DEFAULT_GRADING = { weights: { work: 40, quiz: 25, test: 35, project: 15 }, defaultPossible: { work: 10, quiz: 20, test: 50, project: 100 }, scale: [[90, 'A'], [80, 'B'], [70, 'C'], [60, 'D'], [0, 'F']] };
export function validGrading(b) {
  const w = b?.weights, scale = b?.scale;
  if (!w || typeof w !== 'object') return null;
  const weights = {};
  for (const c of CATEGORIES) { const n = Number(w[c] ?? 0); if (!Number.isFinite(n) || n < 0 || n > 100) return null; weights[c] = Math.round(n * 10) / 10; }
  if (!Object.values(weights).some((n) => n > 0)) return null;
  if (!Array.isArray(scale) || scale.length < 2 || scale.length > 13) return null;
  const s = scale.map(([min, letter]) => [Number(min), text(letter, 3)]);
  if (s.some(([m, l]) => !Number.isFinite(m) || m < 0 || m > 100 || !l)) return null;
  s.sort((a, b2) => b2[0] - a[0]);
  if (s[s.length - 1][0] !== 0) s.push([0, 'F']);
  const dp = {};
  for (const c of CATEGORIES) { const n = Number(b.defaultPossible?.[c] ?? DEFAULT_GRADING.defaultPossible[c]); dp[c] = Number.isFinite(n) && n > 0 && n <= 1000 ? n : DEFAULT_GRADING.defaultPossible[c]; }
  return { weights, defaultPossible: dp, scale: s };
}

export async function teacherToolsRoute(request, env, user, url, { ensureBaseTables } = {}) {
  if (!user) return json({ error: 'Please sign in.' }, 401);
  const path = url.pathname, method = request.method, db = env.DB;
  const isUpload = path === '/api/family/files' && method === 'POST';
  if (method !== 'GET' && method !== 'HEAD') {
    // Same-origin only. Uploads also need a custom header, which other sites cannot send.
    if (request.headers.get('origin') !== url.origin) return json({ error: 'Please use the website form.' }, 403);
    if (isUpload ? request.headers.get('x-venv-upload') !== '1' : !(request.headers.get('content-type') || '').startsWith('application/json')) return json({ error: 'Please use the website form.' }, 403);
    if (!isUpload && Number(request.headers.get('content-length') || 0) > 65536) return json({ error: 'Request too large' }, 413);
  }
  if (ensureBaseTables) await ensureBaseTables(db); // family_grades, used when an assignment is deleted
  await ensureTeacherTables(db);
  const body = async () => { try { return await request.json(); } catch { return null; } };

  if (isUpload) return upload(request, env, user, url);
  const fileMatch = path.match(/^\/api\/family\/files\/([a-f0-9]{24})$/);
  if (fileMatch && (method === 'GET' || method === 'HEAD')) return download(request, env, user, fileMatch[1]);

  if (path === '/api/family/files' && method === 'GET') {
    // Library documents (and, for parents, reusable assignment attachments).
    const rows = user.role === 'parent'
      ? (await db.prepare("SELECT * FROM family_files WHERE kind IN ('document','attachment') ORDER BY created_at DESC LIMIT 500").all()).results || []
      : (await db.prepare("SELECT * FROM family_files WHERE kind='document' AND audience IN ('both',?) ORDER BY created_at DESC LIMIT 500").bind(String(user.grade)).all()).results || [];
    return json({ files: rows.map(publicFile), storage: env.FILES ? 'r2' : 'd1', max_bytes: MAX_UPLOAD_BYTES });
  }
  if (path === '/api/family/files' && method === 'POST') return json({ error: 'Not found' }, 404);
  if (fileMatch && method === 'POST') {
    if (user.role !== 'parent') return json({ error: 'Parent access required' }, 403);
    const b = await body(); if (!b) return json({ error: 'Invalid JSON body' }, 400);
    const f = await db.prepare('SELECT * FROM family_files WHERE id=?').bind(fileMatch[1]).first(); if (!f) return json({ error: 'File not found' }, 404);
    if (b.delete === true) { await deleteFiles(env, [f.id]); return json({ ok: true }); }
    const audience = AUDIENCES.includes(b.audience) ? b.audience : f.audience, subject = b.subject === '' || SUBJECTS.includes(b.subject) ? b.subject : f.subject;
    const kind = f.kind === 'submission' ? f.kind : (b.kind === 'document' || b.kind === 'attachment' ? b.kind : f.kind);
    await db.prepare('UPDATE family_files SET title=?,audience=?,subject=?,note=?,kind=? WHERE id=?').bind(text(b.title, 160) || f.title, audience, subject ?? '', b.note === undefined ? f.note : text(b.note, 500), kind, f.id).run();
    return json({ ok: true });
  }

  if (path === '/api/family/assignments' && method === 'GET') return listAssignments(env, user, url);
  if (path === '/api/family/assignments' && method === 'POST') {
    if (user.role !== 'parent') return json({ error: 'Parent access required' }, 403);
    const b = await body(); if (!b) return json({ error: 'Invalid JSON body' }, 400);
    return saveAssignment(env, user, b);
  }
  if (path === '/api/family/submissions' && method === 'POST') {
    const b = await body(); if (!b) return json({ error: 'Invalid JSON body' }, 400);
    return saveSubmission(env, user, b);
  }

  if (path === '/api/family/settings/grading' && method === 'GET') {
    const row = await db.prepare("SELECT value,updated_at FROM family_settings WHERE key='grading'").first();
    return json({ grading: row ? JSON.parse(row.value) : null, updated_at: row?.updated_at || null });
  }
  if (path === '/api/family/settings/grading' && method === 'POST') {
    if (user.role !== 'parent') return json({ error: 'Parent access required' }, 403);
    const b = await body(); if (!b) return json({ error: 'Invalid JSON body' }, 400);
    if (b.reset === true) { await db.prepare("DELETE FROM family_settings WHERE key='grading'").run(); return json({ ok: true }); }
    const g = validGrading(b); if (!g) return json({ error: 'Weights must be 0–100 (at least one above zero) and every letter needs a minimum percent.' }, 400);
    await db.prepare("INSERT INTO family_settings(key,value,updated_at) VALUES('grading',?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value,updated_at=excluded.updated_at").bind(JSON.stringify(g), epoch()).run();
    return json({ ok: true, grading: g });
  }
  return json({ error: 'Not found' }, 404);
}
