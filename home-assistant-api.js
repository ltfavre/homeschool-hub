import {readingsForDay,readingText,readingLink} from './page-readings-core.js';
import { addSchoolExtras, completeAssignment, signedFileRoute } from './ha-school.js';
import { subjectLabels, taskPrefixes, subjectsForDay, curriculumForDay, taskForSubject } from './curriculum-schedule.js';
// Home Assistant can read student agendas and update subject completion only.
const reply = (body, status = 200) => Response.json(body, {status, headers: {'cache-control': 'private, no-store', 'x-content-type-options': 'nosniff'}});
const hash = async value => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(value))), byte => byte.toString(16).padStart(2, '0')).join('');
const random = () => Array.from(crypto.getRandomValues(new Uint8Array(32)), byte => byte.toString(16).padStart(2, '0')).join('');
const validDate = value => /^\d{4}-\d{2}-\d{2}$/.test(value || '') && !isNaN(new Date(value + 'T12:00:00Z')) && new Date(value + 'T12:00:00Z').toISOString().slice(0, 10) === value;
const shift = (date, days) => {const d = new Date(date + 'T12:00:00Z'); d.setUTCDate(d.getUTCDate() + days); return d.toISOString().slice(0, 10);};
const today = () => new Intl.DateTimeFormat('en-CA', {timeZone: 'America/Chicago', year: 'numeric', month: '2-digit', day: '2-digit'}).format(new Date());
async function schema(db) {
  await db.prepare(`CREATE TABLE IF NOT EXISTS family_ha_connections (
    id TEXT PRIMARY KEY, token_hash TEXT NOT NULL UNIQUE, owner_id TEXT NOT NULL,
    created_at INTEGER NOT NULL, revoked_at INTEGER
  )`).run();
}
export async function manageHomeAssistant(request, env, user) {
  if (user.role !== 'parent') return reply({error: 'Parent access required'}, 403);
  await schema(env.DB);
  if (request.method === 'GET') return reply({connections: (await env.DB.prepare('SELECT id,created_at FROM family_ha_connections WHERE owner_id=? AND revoked_at IS NULL ORDER BY created_at DESC').bind(user.id).all()).results});
  if (request.method !== 'POST') return reply({error: 'Method not allowed'}, 405);
  const body = await request.json().catch(() => null);
  if (body?.action === 'create') {
    const token = random(), id = crypto.randomUUID();
    await env.DB.prepare('INSERT INTO family_ha_connections(id,token_hash,owner_id,created_at) VALUES(?,?,?,?)').bind(id, await hash(token), user.id, Math.floor(Date.now()/1000)).run();
    return reply({id, token, scope: ['student_agendas:read', 'subject_completion:write', 'assignments:check_off', 'shared_documents:read']});
  }
  if (body?.action === 'revoke' && typeof body.id === 'string') {
    await env.DB.prepare('UPDATE family_ha_connections SET revoked_at=? WHERE id=? AND owner_id=?').bind(Math.floor(Date.now()/1000), body.id, user.id).run();
    return reply({ok: true});
  }
  return reply({error: 'Invalid action'}, 400);
}
export async function homeAssistantApi(request, env, assetJson) {
  // Signed file links open on the family tablet without a key or login.
  const fileMatch = new URL(request.url).pathname.match(/^\/api\/home-assistant\/file\/([a-f0-9]{24})$/);
  if (fileMatch && (request.method === 'GET' || request.method === 'HEAD')) {
    if (!env.DB) return reply({error: 'Database unavailable'}, 503);
    return signedFileRoute(request, env, fileMatch[1]);
  }
  const token = (request.headers.get('authorization') || '').match(/^Bearer ([a-f0-9]{64})$/)?.[1];
  if (!token) return reply({error: 'A school connection key is required.'}, 401);
  if (!env.DB) return reply({error: 'Database unavailable'}, 503);
  let connection;
  try {connection = await env.DB.prepare("SELECT c.id FROM family_ha_connections c JOIN family_users u ON u.id=c.owner_id WHERE c.token_hash=? AND c.revoked_at IS NULL AND u.active=1 AND u.role='parent'").bind(await hash(token)).first();}
  catch (error) {if (/no such table.*family_ha_connections/i.test(String(error.message))) return reply({error: 'School connection key is not valid.'}, 401); throw error;}
  if (!connection) return reply({error: 'School connection key is not valid.'}, 401);
  const url = new URL(request.url);
  if (url.pathname === '/api/home-assistant/agenda' && request.method === 'GET') {
    const start = url.searchParams.get('start') || today();
    if (!validDate(start)) return reply({error: 'Invalid start date'}, 400);
    const end = url.searchParams.get('end') || shift(start, 35);
    if (!validDate(end) || end < start || (Date.parse(end)-Date.parse(start))/86400000 > 92) return reply({error: 'Use a date range of 93 days or fewer.'}, 400);
    const [users, days, library, completion] = await Promise.all([
      env.DB.prepare("SELECT id,display_name,grade FROM family_users WHERE role='student' AND active=1 ORDER BY grade,id").all(),
      assetJson(request, env, '/daily-packets.json'), assetJson(request, env, '/planner-resources.json'),
      env.DB.prepare("SELECT user_id,school_date,subject,completed,curriculum FROM family_curriculum_completion WHERE school_date>=? AND school_date<=? ").bind(start, end).all()
    ]);
    const done = new Set(completion.results.filter(row => row.completed === 1).map(row => `${row.user_id}|${row.school_date}|${row.subject}|${row.curriculum}`));
    const labels = subjectLabels;
    const prefixes = taskPrefixes;
    const students = users.results.map(student => ({...student, items: []}));
    for (const date of Object.keys(days).filter(date => date >= start && date <= end).sort()) for (const student of students) {
      const day = days[date]?.[student.grade]; if (!day) continue;
      const mapping = library.weeks[`${student.grade}-${day.module}-${day.week}`];
      if (!mapping) throw Error('Curriculum resources unavailable');
      for (const subject of subjectsForDay(day,mapping)) { const plan=mapping[subject];
        const uid = `${student.id}|${date}|${subject}`;
        const task = taskForSubject(day,subject);
        const assigned=readingsForDay(plan,date).map(r=>{const b=readingLink(r,library.resources);return b?`${b.title}: ${readingText(b)}\n${new URL(b.url,url.origin).href}${b.note?'\n'+b.note:''}`:''}).join('\n\n');
        const links = plan.resources.map(id => library.resources[id]).filter(Boolean).map(resource => `${resource.title}: ${new URL(resource.url,url.origin).href}`).join('\n');
        student.items.push({uid, student_id: student.id, date, subject, summary: `${student.display_name} · ${plan.display_name || labels[subject] || subject}: ${plan.daily?.[date] || plan.topic}`, completed: done.has(uid+'|'+curriculumForDay(day)),
          description: `${day.lesson_context||''}\n${task || day.tasks}\n\n${day.integration||''}\n\nAssigned reading:\n${assigned}\n\n${links}\n\nAgenda: ${url.origin}/agenda?date=${date}\nWorksheets: ${url.origin}/daily-print?date=${date}&grade=${student.grade}&kind=work\nLesson guide: ${url.origin}/daily-print?date=${date}&grade=${student.grade}&kind=guide`});
      }
    }
    await addSchoolExtras(request, env, assetJson, students, today(), url.origin);
    return reply({today: today(), start, end, students, features: ['assignments', 'reading', 'documents']});
  }
  if (url.pathname === '/api/home-assistant/completion' && request.method === 'POST') {
    if (!(request.headers.get('content-type') || '').startsWith('application/json') || Number(request.headers.get('content-length') || 0) > 16384) return reply({error: 'Invalid request'}, 400);
    const body = await request.json().catch(() => null);
    if (body && body.assignment_id !== undefined) {
      if (typeof body.student_id !== 'string' || typeof body.completed !== 'boolean' || !Number.isInteger(Number(body.assignment_id))) return reply({error: 'Invalid task'}, 400);
      return completeAssignment(env, body);
    }
    if (!body || !validDate(body.date) || !['math','ela','science','social','spanish','art','life','computer','skills','review'].includes(body.subject) || typeof body.student_id !== 'string' || typeof body.completed !== 'boolean') return reply({error: 'Invalid task'}, 400);
    const student = await env.DB.prepare("SELECT id,grade FROM family_users WHERE id=? AND role='student' AND active=1").bind(body.student_id).first();
    if (!student) return reply({error: 'Student not found'}, 404);
    const days = await assetJson(request, env, '/daily-packets.json');
    const day=days[body.date]?.[student.grade];
    if (!day) return reply({error: 'No teaching day scheduled'}, 400);
    if(day.subjects&&!day.subjects.includes(body.subject))return reply({error:'Subject is not scheduled on this date'},400);
    await env.DB.prepare("INSERT INTO family_curriculum_completion(user_id,school_date,subject,completed,updated_at,curriculum) VALUES(?,?,?,?,?,?) ON CONFLICT(user_id,school_date,subject,curriculum) DO UPDATE SET completed=excluded.completed,updated_at=excluded.updated_at").bind(body.student_id,body.date,body.subject,body.completed?1:0,Math.floor(Date.now()/1000),curriculumForDay(day)).run();
    return reply({ok: true});
  }
  return reply({error: 'Not found'}, 404);
}
