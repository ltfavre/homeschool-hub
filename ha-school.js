// What Home Assistant shows the kids: teacher-created assignments, this module's reading,
// and shared documents. Files are opened through short-lived signed links, so a shared
// family tablet never needs a VenvLearning login.
import { ensureTeacherTables, fileResponse } from './teacher-tools.js';

const LINK_DAYS = 7;
const enc = new TextEncoder();
const hex = (buf) => Array.from(new Uint8Array(buf), (b) => b.toString(16).padStart(2, '0')).join('');
const epoch = () => Math.floor(Date.now() / 1000);

async function linkKey(db) {
  let row = await db.prepare("SELECT value FROM family_settings WHERE key='ha_link_secret'").first();
  if (!row) {
    const secret = hex(crypto.getRandomValues(new Uint8Array(32)));
    await db.prepare("INSERT OR IGNORE INTO family_settings(key,value,updated_at) VALUES('ha_link_secret',?,?)").bind(secret, epoch()).run();
    row = await db.prepare("SELECT value FROM family_settings WHERE key='ha_link_secret'").first();
  }
  return crypto.subtle.importKey('raw', enc.encode(row.value), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign', 'verify']);
}
const sign = async (key, id, exp) => hex(await crypto.subtle.sign('HMAC', key, enc.encode(`${id}.${exp}`)));

// Rotating every week keeps the URL stable for days (so dashboards don't flicker) but bounded.
export async function signedFileUrl(origin, key, id) {
  const week = 86400 * LINK_DAYS, exp = (Math.floor(epoch() / week) + 2) * week;
  return `${origin}/api/home-assistant/file/${id}?e=${exp}&s=${await sign(key, id, exp)}`;
}

export async function signedFileRoute(request, env, id) {
  const url = new URL(request.url), exp = Number(url.searchParams.get('e')), sig = url.searchParams.get('s') || '';
  if (!/^[a-f0-9]{24}$/.test(id) || !Number.isFinite(exp) || exp < epoch() || !/^[a-f0-9]{64}$/.test(sig)) return Response.json({ error: 'This link has expired. Refresh the dashboard.' }, { status: 403 });
  await ensureTeacherTables(env.DB);
  const key = await linkKey(env.DB);
  const ok = await crypto.subtle.verify('HMAC', key, Uint8Array.from(sig.match(/../g), (h) => parseInt(h, 16)), enc.encode(`${id}.${exp}`));
  if (!ok) return Response.json({ error: 'This link is not valid.' }, { status: 403 });
  // Only files that are still shared with a student (not private documents or student work).
  const f = await env.DB.prepare("SELECT * FROM family_files WHERE id=? AND kind IN ('document','attachment')").bind(id).first();
  if (!f || (f.kind === 'document' && f.audience === 'private')) return Response.json({ error: 'File not found' }, { status: 404 });
  return fileResponse(request, env, f);
}

function moduleFor(list, today) {
  const mods = Object.entries(list.modules).map(([n, m]) => ({ n: Number(n), ...m })).sort((a, b) => a.n - b.n);
  return mods.find((m) => today <= m.end) || mods[mods.length - 1];
}
const bookOut = (b) => ({ title: b.title, author: b.author, role: b.role, why: b.why, prompts: b.prompts, note: b.note || '', url: b.links[0]?.url || '', read_online: b.links[1]?.url || b.links[0]?.url || '' });

// Adds `assignments`, `reading` and `documents` to each student in the agenda response.
const GRADES_TABLE = "CREATE TABLE IF NOT EXISTS family_grades (student_id TEXT NOT NULL, item_key TEXT NOT NULL, subject TEXT NOT NULL, category TEXT NOT NULL, title TEXT NOT NULL, school_date TEXT NOT NULL, points REAL NOT NULL, possible REAL NOT NULL, comment TEXT NOT NULL DEFAULT '', updated_at INTEGER NOT NULL, PRIMARY KEY (student_id, item_key))";

export async function addSchoolExtras(request, env, assetJson, students, today, origin) {
  const db = env.DB;
  await ensureTeacherTables(db);
  await db.prepare(GRADES_TABLE).run();
  const key = await linkKey(db);
  let list = null;
  try { list = await assetJson(request, env, '/reading-list.json'); } catch { list = null; }
  const recent = new Date(today + 'T12:00:00Z'); recent.setUTCDate(recent.getUTCDate() - 14);
  const since = recent.toISOString().slice(0, 10);
  const fileCache = new Map();
  const fileOut = async (f) => ({ title: f.title, name: f.name, url: await signedFileUrl(origin, key, f.id) });
  const files = async (ids) => {
    const out = [];
    for (const id of ids) {
      if (!fileCache.has(id)) fileCache.set(id, await db.prepare("SELECT id,title,name FROM family_files WHERE id=?").bind(id).first());
      const f = fileCache.get(id); if (f) out.push(await fileOut(f));
    }
    return out;
  };
  for (const s of students) {
    const rows = (await db.prepare(`SELECT a.*, sub.status AS sub_status, sub.feedback AS feedback, g.points AS score, g.possible AS possible, g.comment AS comment
      FROM family_assignments a
      LEFT JOIN family_submissions sub ON sub.assignment_id=a.id AND sub.student_id=?
      LEFT JOIN family_grades g ON g.student_id=? AND g.item_key='C|'||a.id
      WHERE a.grade=? AND a.published=1 ORDER BY a.due_date, a.id`).bind(s.id, s.id, String(s.grade)).all()).results || [];
    s.assignments = [];
    for (const a of rows) {
      const graded = a.score !== null && a.score !== undefined || a.sub_status === 'returned';
      const done = graded || a.sub_status === 'submitted';
      if (done && a.due_date < since) continue; // keep the list short: finished work drops off after two weeks
      const attachments = await files(JSON.parse(a.attachments || '[]'));
      const status = graded ? 'graded' : done ? 'turned_in' : a.due_date < today ? 'late' : a.due_date === today ? 'due_today' : 'assigned';
      let description = a.instructions || '';
      if (attachments.length) description += `${description ? '\n\n' : ''}Attachments:\n${attachments.map((f) => `${f.title}: ${f.url}`).join('\n')}`;
      if (graded && a.score !== null && a.score !== undefined) description += `\n\nScore: ${a.score} / ${a.possible}${a.comment ? ' · ' + a.comment : ''}`;
      if (a.feedback) description += `\n\nFeedback: ${a.feedback}`;
      if (!a.allow_submission && !done) description += '\n\nHand this in on paper, then check it off.';
      s.assignments.push({
        uid: `assignment|${a.id}|${s.id}`, assignment_id: a.id, student_id: s.id, date: a.due_date, subject: a.subject, category: a.category,
        summary: a.title, description: description.trim(), points: a.points, completed: done, locked: graded, status,
        score: graded && a.score !== null && a.score !== undefined ? a.score : null, possible: a.possible ?? a.points, feedback: a.feedback || '', attachments,
      });
    }
    s.documents = [];
    const docs = (await db.prepare("SELECT id,title,name,subject,created_at FROM family_files WHERE kind='document' AND audience IN ('both',?) ORDER BY created_at DESC LIMIT 25").bind(String(s.grade)).all()).results || [];
    for (const d of docs) s.documents.push({ ...(await fileOut(d)), subject: d.subject, added: new Date(d.created_at * 1000).toISOString().slice(0, 10) });
    if (list && list.grades[String(s.grade)]) {
      const g = list.grades[String(s.grade)], cur = moduleFor(list, today), next = list.modules[String(cur.n + 1)];
      s.reading = {
        module: cur.n, module_label: cur.label, dates: cur.dates, pace: g.pace,
        books: g.books.filter((b) => b.module === cur.n).map(bookOut),
        up_next: next ? { module_label: next.label, dates: next.dates, books: g.books.filter((b) => b.module === cur.n + 1).map(bookOut) } : null,
        library_picks: g.library.filter((b) => b.modules.includes(cur.n)).map((b) => ({ title: b.title, author: b.author, why: b.why, url: b.links[0]?.url || '' })),
        full_list: `${origin}/library#reading`,
      };
    }
  }
}

// A checkmark from Home Assistant turns the assignment in (or takes it back).
export async function completeAssignment(env, body) {
  const db = env.DB;
  await ensureTeacherTables(db);
  await db.prepare(GRADES_TABLE).run();
  const student = await db.prepare("SELECT id,grade FROM family_users WHERE id=? AND role='student' AND active=1").bind(String(body.student_id || '')).first();
  if (!student) return Response.json({ error: 'Student not found' }, { status: 404 });
  const a = await db.prepare('SELECT * FROM family_assignments WHERE id=? AND grade=? AND published=1').bind(Number(body.assignment_id), String(student.grade)).first();
  if (!a) return Response.json({ error: 'Assignment not found' }, { status: 404 });
  const sub = await db.prepare('SELECT status FROM family_submissions WHERE assignment_id=? AND student_id=?').bind(a.id, student.id).first();
  const graded = await db.prepare("SELECT 1 FROM family_grades WHERE student_id=? AND item_key=?").bind(student.id, 'C|' + a.id).first();
  if (sub?.status === 'returned' || graded) return Response.json({ error: 'This assignment was already graded.' }, { status: 409 });
  if (body.completed) {
    await db.prepare("INSERT INTO family_submissions(assignment_id,student_id,body,status,submitted_at) VALUES(?,?,?,'submitted',?) ON CONFLICT(assignment_id,student_id) DO UPDATE SET status='submitted',submitted_at=excluded.submitted_at,body=CASE WHEN family_submissions.body='' THEN excluded.body ELSE family_submissions.body END")
      .bind(a.id, student.id, 'Checked off on the family dashboard (Home Assistant).', epoch()).run();
  } else {
    await db.prepare("UPDATE family_submissions SET status='draft' WHERE assignment_id=? AND student_id=?").bind(a.id, student.id).run();
  }
  return Response.json({ ok: true }, { headers: { 'cache-control': 'no-store' } });
}
