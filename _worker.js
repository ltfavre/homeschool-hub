import {readingsForDay,readingLink,cleanTaskText} from './page-readings-core.js';
import { subjectsForDay, curriculumForDay, taskForSubject, studentResourceLibrary } from './curriculum-schedule.js';
import { curriculumAsset, curriculumJson } from './curriculum-assets.js';
import { homeAssistantApi, manageHomeAssistant } from "./home-assistant-api.js";
import { isTeacherToolsPath, teacherToolsRoute } from "./teacher-tools.js";
import { isWishlistPath, wishlistRoute } from "./wishlist.js";
import {
  mapTasksToUsers,
  normalizeVenvlearningPayload,
  VENVLEARNING_TASK_SOURCE
} from "./venvlearning-sync.js";

const json = (data, status = 200) =>
  new Response(JSON.stringify(data, null, 2), {
    status,
    headers: { "content-type": "application/json; charset=utf-8" },
  });

const parseBody = async (request) => {
  try { return await request.json(); }
  catch { return null; }
};
const rawAsset = (request, env) => {
  if (env && env.ASSETS && typeof env.ASSETS.fetch === "function") {
    return env.ASSETS.fetch(request);
  }
  return fetch(request);
};
const fetchAsset = (request, env) => curriculumAsset(request, env, rawAsset);


const clean = (v) => {
  if (v === undefined || v === null) return null;
  const s = String(v).trim();
  return s === "" ? null : s;
};

const toInt = (v) => {
  if (v === undefined || v === null || v === "") return null;
  const n = Number(v);
  return Number.isInteger(n) ? n : null;
};

const toNumber = (v) => {
  if (v === undefined || v === null || v === "") return null;
  const n = Number(v);
  return Number.isFinite(n) ? n : null;
};

const isoDate = (v) => {
  const s = clean(v);
  return s && /^\\d{4}-\\d{2}-\\d{2}$/.test(s) ? s : null;
};

const authOK = (request, env) => {
  if (!env.IMPORT_TOKEN) return false;
  const auth = request.headers.get("authorization") || "";
  return auth === `Bearer ${env.IMPORT_TOKEN}`;
};

const venvSyncAuthOK = (request, env) => {
  if (!env.VENVLEARNING_SYNC_TOKEN) return false;
  const auth = request.headers.get("authorization") || "";
  const headerToken = request.headers.get("x-venvlearning-sync-token") || "";
  return auth === `Bearer ${env.VENVLEARNING_SYNC_TOKEN}` || headerToken === env.VENVLEARNING_SYNC_TOKEN;
};

const parseJsonEnv = (raw, fallback) => {
  const value = clean(raw);
  if (!value) return fallback;
  try {
    return JSON.parse(value);
  } catch {
    return fallback;
  }
};

const isDateOnly = (value) => /^\d{4}-\d{2}-\d{2}$/.test(String(value || ""));

const sanitizeDateRange = (startDateRaw, endDateRaw) => {
  const today = new Date().toISOString().slice(0, 10);
  const start = isDateOnly(startDateRaw) ? String(startDateRaw) : today;
  const end = isDateOnly(endDateRaw) ? String(endDateRaw) : start;
  if (start > end) return { start_date: end, end_date: start };
  return { start_date: start, end_date: end };
};

async function ensureFamilyTaskTables(db) {
  await execSql(db, `
    CREATE TABLE IF NOT EXISTS family_daily_tasks (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      source TEXT NOT NULL,
      external_id TEXT NOT NULL,
      user_id TEXT NOT NULL,
      title TEXT NOT NULL,
      due_date TEXT NOT NULL,
      status TEXT NOT NULL DEFAULT 'pending',
      payload_json TEXT,
      last_synced_at INTEGER NOT NULL,
      created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
      updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    );
    CREATE UNIQUE INDEX IF NOT EXISTS idx_family_daily_tasks_source_external_user
      ON family_daily_tasks(source, external_id, user_id);
    CREATE INDEX IF NOT EXISTS idx_family_daily_tasks_user_due
      ON family_daily_tasks(user_id, due_date);
    CREATE TABLE IF NOT EXISTS family_sync_log (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      source TEXT NOT NULL,
      started_at INTEGER NOT NULL,
      finished_at INTEGER,
      ok INTEGER NOT NULL DEFAULT 0,
      summary_json TEXT,
      error_message TEXT
    );
    CREATE TABLE IF NOT EXISTS family_grades (
      student_id TEXT NOT NULL,
      item_key TEXT NOT NULL,
      subject TEXT NOT NULL,
      category TEXT NOT NULL,
      title TEXT NOT NULL,
      school_date TEXT NOT NULL,
      points REAL NOT NULL,
      possible REAL NOT NULL,
      comment TEXT NOT NULL DEFAULT '',
      updated_at INTEGER NOT NULL,
      PRIMARY KEY (student_id, item_key)
    );
    CREATE TABLE IF NOT EXISTS family_announcements (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      body TEXT NOT NULL,
      grade TEXT NOT NULL DEFAULT 'both',
      pinned INTEGER NOT NULL DEFAULT 0,
      author TEXT NOT NULL DEFAULT '',
      created_at INTEGER NOT NULL
    );
    CREATE TABLE IF NOT EXISTS family_attendance (
      student_id TEXT NOT NULL,
      school_date TEXT NOT NULL,
      status TEXT NOT NULL,
      hours REAL,
      note TEXT NOT NULL DEFAULT '',
      updated_at INTEGER NOT NULL,
      PRIMARY KEY (student_id, school_date)
    );
    `);
}
async function maybeEnsureFamilyAuthTables(db, env){
  if(clean(env.FAMILY_SCHEMA_SELF_HEAL)!=="1") return;
  try{
    await ensureFamilyAuthTablesImpl(db);
  }catch(error){
    console.error('Auth schema self-heal failed', String(error&&error.message||''));
  }
}
async function ensureFamilyAuthTablesImpl(db){
  await execSql(db, `
    CREATE TABLE IF NOT EXISTS family_users (
      id TEXT PRIMARY KEY,
      username TEXT NOT NULL UNIQUE,
      display_name TEXT NOT NULL,
      role TEXT NOT NULL,
      grade TEXT,
      password_hash TEXT,
      password_salt TEXT,
      active INTEGER NOT NULL DEFAULT 1
    );
    CREATE TABLE IF NOT EXISTS family_sessions (
      token_hash TEXT PRIMARY KEY,
      user_id TEXT NOT NULL,
      expires_at INTEGER NOT NULL
    );
    CREATE INDEX IF NOT EXISTS idx_family_sessions_user_id ON family_sessions(user_id);
    CREATE INDEX IF NOT EXISTS idx_family_sessions_expires_at ON family_sessions(expires_at);
    CREATE TABLE IF NOT EXISTS family_invites (
      token_hash TEXT PRIMARY KEY,
      user_id TEXT NOT NULL,
      expires_at INTEGER NOT NULL
    );
    CREATE INDEX IF NOT EXISTS idx_family_invites_user_id ON family_invites(user_id);
    CREATE TABLE IF NOT EXISTS family_login_limits (
      bucket TEXT PRIMARY KEY,
      attempts INTEGER NOT NULL DEFAULT 0,
      expires_at INTEGER NOT NULL
    );
    CREATE TABLE IF NOT EXISTS family_curriculum_completion (
      user_id TEXT NOT NULL,
      school_date TEXT NOT NULL,
      subject TEXT NOT NULL,
      completed INTEGER NOT NULL DEFAULT 0,
      updated_at INTEGER NOT NULL,
      curriculum TEXT NOT NULL DEFAULT 'khan-primary-v1',
      PRIMARY KEY (user_id, school_date, subject, curriculum)
    );
    CREATE INDEX IF NOT EXISTS idx_family_curriculum_completion_date ON family_curriculum_completion(school_date);
`);
}
async function execSql(db, sql){
  // D1 exec splits on newlines, so multiline DDL must use prepared statements.
  // These static schema definitions contain no semicolons inside SQL literals.
  const statements=sql
    .split(";")
    .map((s)=>s.trim())
    .filter(Boolean);
  if(typeof db.batch === "function"){
    await db.batch(statements.map((statement)=>db.prepare(statement)));
    return;
  }
  for(const statement of statements){
    await db.prepare(statement).run();
  }
}

async function fetchVenvlearningTasks(env, startDate, endDate) {
  const baseUrl = clean(env.VENVLEARNING_API_BASE_URL);
  const adapterUrl = clean(env.VENVLEARNING_ADAPTER_URL);
  const authToken = clean(env.VENVLEARNING_API_TOKEN);
  if (!adapterUrl && !baseUrl) {
    throw new Error("VenvLearning source is not configured. Set VENVLEARNING_API_BASE_URL or VENVLEARNING_ADAPTER_URL.");
  }
  if (!authToken) {
    throw new Error("VenvLearning source is missing credentials. Set VENVLEARNING_API_TOKEN.");
  }

  const endpoint = adapterUrl || `${baseUrl.replace(/\/$/, "")}/daily-tasks`;
  const url = new URL(endpoint);
  url.searchParams.set("start_date", startDate);
  url.searchParams.set("end_date", endDate);
  const response = await fetch(url.toString(), {
    method: "GET",
    headers: {
      authorization: `Bearer ${authToken}`,
      accept: "application/json"
    }
  });
  if (!response.ok) {
    throw new Error(`VenvLearning request failed (${response.status}) at ${url.pathname}`);
  }
  const contentType = response.headers.get("content-type") || "";
  if (!contentType.toLowerCase().includes("application/json")) {
    throw new Error("VenvLearning response was not JSON. Configure VENVLEARNING_ADAPTER_URL for non-API integrations.");
  }
  return response.json();
}

async function syncVenvlearningDailyTasks(env, syncRange) {
  const startedAt = epoch();
  await ensureFamilyTaskTables(env.DB);
  const logInsert = await env.DB.prepare(
    "INSERT INTO family_sync_log(source, started_at, ok) VALUES(?,?,0)"
  ).bind(VENVLEARNING_TASK_SOURCE, startedAt).run();
  const logId = logInsert.meta.last_row_id;

  try {
    const usersResult = await env.DB.prepare(
      "SELECT id,username,display_name,grade FROM family_users WHERE role='student' AND active=1"
    ).all();
    const users = usersResult.results || [];
    if (!users.length) {
      throw new Error("No active student accounts are available for VenvLearning task mapping.");
    }

    const payload = await fetchVenvlearningTasks(env, syncRange.start_date, syncRange.end_date);
    const normalized = normalizeVenvlearningPayload(payload);
    const mapping = parseJsonEnv(env.VENVLEARNING_STUDENT_MAP, {});
    const mapped = mapTasksToUsers(normalized.tasks, users, mapping);

    let inserted = 0;
    let updated = 0;
    for (const task of mapped.mapped) {
      const existing = await env.DB.prepare(
        "SELECT id FROM family_daily_tasks WHERE source=? AND external_id=? AND user_id=? LIMIT 1"
      ).bind(task.source, task.external_id, task.user_id).first();

      if (existing) {
        await env.DB.prepare(`
          UPDATE family_daily_tasks
          SET title=?, due_date=?, status=?, payload_json=?, last_synced_at=?, updated_at=CURRENT_TIMESTAMP
          WHERE id=?
        `).bind(task.title, task.due_date, task.status, task.payload_json, startedAt, existing.id).run();
        updated++;
      } else {
        await env.DB.prepare(`
          INSERT INTO family_daily_tasks(source,external_id,user_id,title,due_date,status,payload_json,last_synced_at)
          VALUES(?,?,?,?,?,?,?,?)
        `).bind(task.source, task.external_id, task.user_id, task.title, task.due_date, task.status, task.payload_json, startedAt).run();
        inserted++;
      }
    }

    const summary = {
      source: VENVLEARNING_TASK_SOURCE,
      start_date: syncRange.start_date,
      end_date: syncRange.end_date,
      fetched: normalized.total,
      inserted,
      updated,
      invalid: normalized.errors.length,
      unmapped: mapped.unmapped.length
    };

    await env.DB.prepare(`
      UPDATE family_sync_log
      SET ok=1, finished_at=?, summary_json=?
      WHERE id=?
    `).bind(epoch(), JSON.stringify(summary), logId).run();

    console.info("VenvLearning sync summary", summary);
    return {
      ok: true,
      summary,
      errors: normalized.errors,
      unmapped: mapped.unmapped.map((task) => ({
        title: task.title,
        assignee: task.assignee,
        due_date: task.due_date,
        external_id: task.external_id
      }))
    };
  } catch (error) {
    const message = error && error.message ? error.message : "Unknown sync failure";
    await env.DB.prepare(`
      UPDATE family_sync_log
      SET finished_at=?, error_message=?
      WHERE id=?
    `).bind(epoch(), message, logId).run();
    console.error("VenvLearning sync failed", message);
    throw error;
  }
}

async function resolveStudent(db, row) {
  if (row.student_id) {
    const found = await db.prepare("SELECT id,name,grade FROM students WHERE id=? AND active=1")
      .bind(Number(row.student_id)).first();
    if (found) return found;
  }
  const name = clean(row.student_name || row.student);
  const grade = clean(row.grade);
  if (name) {
    const found = await db.prepare("SELECT id,name,grade FROM students WHERE lower(name)=lower(?) AND active=1 LIMIT 1")
      .bind(name).first();
    if (found) return found;
  }
  if (grade) {
    const found = await db.prepare("SELECT id,name,grade FROM students WHERE grade=? AND active=1 ORDER BY id LIMIT 1")
      .bind(grade).first();
    if (found) return found;
  }
  return null;
}

async function resolveSubject(db, row) {
  if (row.subject_id) {
    const found = await db.prepare("SELECT id,name FROM subjects WHERE id=?")
      .bind(Number(row.subject_id)).first();
    if (found) return found;
  }
  const name = clean(row.subject);
  if (!name) return null;
  let found = await db.prepare("SELECT id,name FROM subjects WHERE lower(name)=lower(?) LIMIT 1")
    .bind(name).first();
  if (found) return found;
  await db.prepare("INSERT OR IGNORE INTO subjects(name) VALUES (?)").bind(name).run();
  return await db.prepare("SELECT id,name FROM subjects WHERE lower(name)=lower(?) LIMIT 1")
    .bind(name).first();
}

async function upsertLesson(db, row, defaults={}) {
  const student = await resolveStudent(db,row);
  const subject = await resolveSubject(db,row);
  if (!student) throw new Error("Could not resolve student");
  if (!subject) throw new Error("Could not resolve subject");
  const title=clean(row.title), date=isoDate(row.lesson_date || row.date);
  if (!title) throw new Error("title is required");
  if (!date) throw new Error("lesson_date/date must be YYYY-MM-DD");
  const externalId=clean(row.external_id);
  const status=clean(row.status) || clean(defaults.status) || "planned";
  const sourceName=clean(row.source_name) || clean(defaults.source_name);
  if (externalId) {
    const existing=await db.prepare("SELECT id FROM lessons WHERE external_id=? LIMIT 1").bind(externalId).first();
    if (existing) {
      await db.prepare(`UPDATE lessons SET student_id=?,subject_id=?,title=?,lesson_date=?,segment=?,week=?,objective=?,instructions=?,resource_url=?,source_name=?,estimated_minutes=?,status=?,updated_at=CURRENT_TIMESTAMP WHERE id=?`)
        .bind(student.id,subject.id,title,date,toInt(row.segment),toInt(row.week),clean(row.objective),clean(row.instructions),clean(row.resource_url),sourceName,toInt(row.estimated_minutes),status,existing.id).run();
      return {action:"updated",id:existing.id,external_id:externalId};
    }
  }
  const result=await db.prepare(`INSERT INTO lessons (external_id,student_id,subject_id,title,lesson_date,segment,week,objective,instructions,resource_url,source_name,estimated_minutes,status) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)`)
    .bind(externalId,student.id,subject.id,title,date,toInt(row.segment),toInt(row.week),clean(row.objective),clean(row.instructions),clean(row.resource_url),sourceName,toInt(row.estimated_minutes),status).run();
  return {action:"inserted",id:result.meta.last_row_id,external_id:externalId};
}

async function upsertAssignment(db,row,defaults={}) {
  const student=await resolveStudent(db,row);
  const subject=await resolveSubject(db,row);
  if (!student) throw new Error("Could not resolve student");
  if (!subject) throw new Error("Could not resolve subject");
  const title=clean(row.title), date=isoDate(row.due_date || row.date);
  if (!title) throw new Error("title is required");
  if (!date) throw new Error("due_date/date must be YYYY-MM-DD");
  let lessonId=toInt(row.lesson_id);
  if (!lessonId && row.lesson_external_id) {
    const lesson=await db.prepare("SELECT id FROM lessons WHERE external_id=? LIMIT 1").bind(clean(row.lesson_external_id)).first();
    if (lesson) lessonId=lesson.id;
  }
  const externalId=clean(row.external_id);
  const status=clean(row.status) || clean(defaults.status) || "assigned";
  if (externalId) {
    const existing=await db.prepare("SELECT id FROM assignments WHERE external_id=? LIMIT 1").bind(externalId).first();
    if (existing) {
      await db.prepare(`UPDATE assignments SET lesson_id=?,student_id=?,subject_id=?,title=?,due_date=?,instructions=?,resource_url=?,points_possible=?,status=?,updated_at=CURRENT_TIMESTAMP WHERE id=?`)
        .bind(lessonId,student.id,subject.id,title,date,clean(row.instructions),clean(row.resource_url),toNumber(row.points_possible),status,existing.id).run();
      return {action:"updated",id:existing.id,external_id:externalId};
    }
  }
  const result=await db.prepare(`INSERT INTO assignments (external_id,lesson_id,student_id,subject_id,title,due_date,instructions,resource_url,points_possible,status) VALUES (?,?,?,?,?,?,?,?,?,?)`)
    .bind(externalId,lessonId,student.id,subject.id,title,date,clean(row.instructions),clean(row.resource_url),toNumber(row.points_possible),status).run();
  return {action:"inserted",id:result.meta.last_row_id,external_id:externalId};
}

const legacy = {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (!url.pathname.startsWith("/api/")) {
      return fetchAsset(request, env);
    }

    try {
      if (url.pathname === "/api/health") {
        return json({ ok: true, app: "homeschool-hub" });
      }

      if (url.pathname === "/api/bootstrap" && request.method === "GET") {
        const [students, subjects] = await Promise.all([
          env.DB.prepare("SELECT id,name,grade FROM students WHERE active=1 ORDER BY grade").all(),
          env.DB.prepare("SELECT id,name FROM subjects ORDER BY name").all(),
        ]);
        return json({ students: students.results, subjects: subjects.results });
      }


      if (url.pathname === "/api/import" && request.method === "POST") {
        if (!authOK(request, env)) return json({ error: "Unauthorized" }, 401);
        const body = await parseBody(request);
        if (!body || !Array.isArray(body.records)) return json({ error: "Body must be JSON with a records array" }, 400);
        if (body.records.length === 0) return json({ error: "records array is empty" }, 400);
        if (body.records.length > 500) return json({ error: "Maximum 500 records per import" }, 413);

        const defaults = body.defaults || {};
        const dryRun = body.dry_run === true;
        const results = [];
        let inserted=0, updated=0, failed=0;

        for (let i=0;i<body.records.length;i++) {
          const row=body.records[i] || {};
          const type=(clean(row.record_type || row.type || "lesson") || "lesson").toLowerCase();
          try {
            if (!["lesson","assignment"].includes(type)) throw new Error("record_type must be lesson or assignment");
            if (dryRun) {
              const student=await resolveStudent(env.DB,row), subject=await resolveSubject(env.DB,row);
              if (!student) throw new Error("Could not resolve student");
              if (!subject) throw new Error("Could not resolve subject");
              if (!clean(row.title)) throw new Error("title is required");
              const d=type === "lesson" ? isoDate(row.lesson_date || row.date) : isoDate(row.due_date || row.date);
              if (!d) throw new Error(`${type === "lesson" ? "lesson_date" : "due_date"}/date must be YYYY-MM-DD`);
              results.push({row:i+1,record_type:type,action:"valid",external_id:clean(row.external_id)});
              continue;
            }
            const out= type === "lesson" ? await upsertLesson(env.DB,row,defaults) : await upsertAssignment(env.DB,row,defaults);
            if (out.action === "inserted") inserted++;
            if (out.action === "updated") updated++;
            results.push({row:i+1,record_type:type,...out});
          } catch (error) {
            failed++;
            results.push({row:i+1,record_type:type,action:"failed",external_id:clean(row.external_id),error:error.message || "Import failed"});
          }
        }
        return json({ok:failed===0,dry_run:dryRun,summary:{total:body.records.length,inserted,updated,failed},results}, failed===body.records.length ? 400 : 200);
      }

      if (url.pathname === "/api/lessons" && request.method === "GET") {
        const start = url.searchParams.get("start") || "0000-01-01";
        const end = url.searchParams.get("end") || "9999-12-31";
        const student = url.searchParams.get("student");

        let sql = `
          SELECT l.*, s.name AS student_name, sub.name AS subject_name
          FROM lessons l
          JOIN students s ON s.id=l.student_id
          JOIN subjects sub ON sub.id=l.subject_id
          WHERE l.lesson_date BETWEEN ? AND ?`;
        const params = [start, end];

        if (student) {
          sql += " AND l.student_id=?";
          params.push(Number(student));
        }
        sql += " ORDER BY l.lesson_date, s.grade, sub.name";

        const result = await env.DB.prepare(sql).bind(...params).all();
        return json(result.results);
      }

      if (url.pathname === "/api/lessons" && request.method === "POST") {
        const b = await parseBody(request);
        if (!b?.student_id || !b?.subject_id || !b?.title || !b?.lesson_date) {
          return json({ error: "student_id, subject_id, title, and lesson_date are required" }, 400);
        }

        const result = await env.DB.prepare(`
          INSERT INTO lessons
          (student_id,subject_id,title,lesson_date,segment,week,objective,instructions,resource_url,source_name,estimated_minutes,status)
          VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
        `).bind(
          b.student_id, b.subject_id, b.title, b.lesson_date,
          b.segment ?? null, b.week ?? null, b.objective ?? null,
          b.instructions ?? null, b.resource_url ?? null,
          b.source_name ?? null, b.estimated_minutes ?? null,
          b.status ?? "planned"
        ).run();

        return json({ ok: true, id: result.meta.last_row_id }, 201);
      }

      if (url.pathname === "/api/assignments" && request.method === "GET") {
        const start = url.searchParams.get("start") || "0000-01-01";
        const end = url.searchParams.get("end") || "9999-12-31";
        const result = await env.DB.prepare(`
          SELECT a.*, s.name AS student_name, sub.name AS subject_name
          FROM assignments a
          JOIN students s ON s.id=a.student_id
          JOIN subjects sub ON sub.id=a.subject_id
          WHERE a.due_date BETWEEN ? AND ?
          ORDER BY a.due_date, s.grade, sub.name
        `).bind(start, end).all();
        return json(result.results);
      }

      if (url.pathname === "/api/assignments" && request.method === "POST") {
        const b = await parseBody(request);
        if (!b?.student_id || !b?.subject_id || !b?.title || !b?.due_date) {
          return json({ error: "student_id, subject_id, title, and due_date are required" }, 400);
        }

        const result = await env.DB.prepare(`
          INSERT INTO assignments
          (lesson_id,student_id,subject_id,title,due_date,instructions,resource_url,points_possible,status)
          VALUES (?,?,?,?,?,?,?,?,?)
        `).bind(
          b.lesson_id ?? null, b.student_id, b.subject_id, b.title, b.due_date,
          b.instructions ?? null, b.resource_url ?? null, b.points_possible ?? null,
          b.status ?? "assigned"
        ).run();

        return json({ ok: true, id: result.meta.last_row_id }, 201);
      }

      return json({ error: "Not found" }, 404);
    } catch (error) {
      return json({ error: error.message || "Server error" }, 500);
    }
  },
};

const familyJson=(data,status=200,extra={})=>new Response(JSON.stringify(data),{status,headers:{'content-type':'application/json;charset=utf-8','cache-control':'no-store','x-content-type-options':'nosniff',...extra}});
const epoch=()=>Math.floor(Date.now()/1000);
const randomToken=()=>Array.from(crypto.getRandomValues(new Uint8Array(32)),b=>b.toString(16).padStart(2,'0')).join('');
const digest=async text=>Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(text))),b=>b.toString(16).padStart(2,'0')).join('');
const passwordHash=async(password,salt)=>{const key=await crypto.subtle.importKey('raw',new TextEncoder().encode(password),'PBKDF2',false,['deriveBits']);return Array.from(new Uint8Array(await crypto.subtle.deriveBits({name:'PBKDF2',salt:new TextEncoder().encode(salt),iterations:100000,hash:'SHA-256'},key,256)),b=>b.toString(16).padStart(2,'0')).join('');};
const equalHash=(a,b)=>{let d=a.length^b.length;for(let i=0;i<Math.max(a.length,b.length);i++)d|=(a.charCodeAt(i)||0)^(b.charCodeAt(i)||0);return d===0;};
const publicUser=u=>({id:u.id,username:u.username,display_name:u.display_name,role:u.role,grade:u.grade,ready:!!u.password_hash});
const sessionSameSite = (env) => {
  const configured = (clean(env.FAMILY_SESSION_SAMESITE) || "").toLowerCase();
  if (configured === "none" || configured === "lax" || configured === "strict") return configured;
  return clean(env.FAMILY_EMBED_IN_HA) === "1" ? "none" : "strict";
};
const sessionCookieName = (env) => {
  const configured = clean(env.FAMILY_SESSION_COOKIE_NAME);
  return configured || "__Host-venv_session";
};
const sessionCookieSecure = (env) => {
  const configured = (clean(env.FAMILY_SESSION_SECURE) || "").toLowerCase();
  if (configured === "0" || configured === "false" || configured === "no") return false;
  return true;
};
const sessionCookiePartitioned = (env) => {
  const configured = (clean(env.FAMILY_SESSION_PARTITIONED) || "").toLowerCase();
  if (configured === "1" || configured === "true" || configured === "yes") return true;
  if (configured === "0" || configured === "false" || configured === "no") return false;
  return clean(env.FAMILY_EMBED_IN_HA) === "1";
};
const cookie=(token,env,maxAge=604800)=>{
  const secure=sessionCookieSecure(env);
  const sameSite=sessionSameSite(env);
  const safeCookieName=(!secure && sessionCookieName(env).startsWith("__Host-")) ? "venv_session" : sessionCookieName(env);
  const attrs=[`${safeCookieName}=${token}`,"Path=/","HttpOnly",`SameSite=${sameSite}`,`Max-Age=${maxAge}`];
  if(secure) attrs.push("Secure");
  if(secure && sameSite === "none" && sessionCookiePartitioned(env)) attrs.push("Partitioned");
  return attrs.join("; ");
};
const frameAncestors = (env) => {
  const configured = clean(env.FAMILY_ALLOWED_FRAME_ANCESTORS);
  if (configured) return configured;
  return "'self' http://homeassistant.local http://homeassistant.local:8123 https://homeassistant.local https://homeassistant.local:8123 http://localhost:8123 https://localhost:8123 http://127.0.0.1:8123 https://127.0.0.1:8123";
};
const sessionTokenFromCookieHeader=(cookieHeader,env)=>{
  const names=[sessionCookieName(env),"__Host-venv_session","venv_session"];
  for(const name of names){
    const escaped=name.replace(/[.*+?^${}()|[\]\\]/g,"\\$&");
    const token=(cookieHeader||"").match(new RegExp(`(?:^|;\\s*)${escaped}=([a-f0-9]{64})(?:;|$)`))?.[1];
    if(token)return token;
  }
  return null;
};
async function familyUser(request,env){
 const t=sessionTokenFromCookieHeader(request.headers.get('cookie')||'',env);
 if(!t)return null;
 try{
  return await env.DB.prepare('SELECT u.* FROM family_sessions s JOIN family_users u ON u.id=s.user_id WHERE s.token_hash=? AND s.expires_at>? AND u.active=1').bind(await digest(t),epoch()).first();
 }catch(error){
  const message=String(error&&error.message||'');
  if(/no such column:\s*u\.active/i.test(message)){
   return env.DB.prepare('SELECT u.* FROM family_sessions s JOIN family_users u ON u.id=s.user_id WHERE s.token_hash=? AND s.expires_at>?').bind(await digest(t),epoch()).first();
  }
  console.error('Session lookup failed; treating as signed out', message);
  return null;
 }
}
async function sessionResponse(user,env){const t=randomToken();await env.DB.prepare('INSERT INTO family_sessions(token_hash,user_id,expires_at) VALUES(?,?,?)').bind(await digest(t),user.id,epoch()+604800).run();return familyJson({user:publicUser(user),redirect:user.role==='parent'?'/planner':'/agenda'},200,{'set-cookie':cookie(t,env)});}
async function assetJson(request,env,path){return curriculumJson(new Request(new URL(path,request.url)),env,rawAsset);}
function centralDate(){return new Intl.DateTimeFormat('en-CA',{timeZone:'America/Chicago',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());}
function safeDate(d){if(!/^\d{4}-\d{2}-\d{2}$/.test(d))return false;const value=new Date(d+'T12:00:00Z');return !isNaN(value)&&value.toISOString().slice(0,10)===d;}
async function rateLimit(request,env,username){
 for(const key of ['ip:'+ (request.headers.get('cf-connecting-ip')||'unknown'),'user:'+username]){
  const bucket=await digest(key)+':'+Math.floor(epoch()/900);
  try{
   const r=await env.DB.prepare('INSERT INTO family_login_limits(bucket,attempts,expires_at) VALUES(?,1,?) ON CONFLICT(bucket) DO UPDATE SET attempts=attempts+1 RETURNING attempts').bind(bucket,epoch()+1800).first();
   if(r.attempts>20)return false;
  }catch(error){
   console.error('Login rate-limit unavailable; continuing', String(error&&error.message||''));
   return true;
  }
 }
 return true;
}
async function findUserByUsername(env,username){
 try{
  return await env.DB.prepare('SELECT * FROM family_users WHERE username=? AND active=1').bind(username).first();
 }catch(error){
  const message=String(error&&error.message||'');
  if(/no such column:\s*active/i.test(message)){
   return env.DB.prepare('SELECT * FROM family_users WHERE username=? LIMIT 1').bind(username).first();
  }
  throw error;
 }
}
async function authRoute(request,env,user,url){
 const path=url.pathname,method=request.method;
 if(method!=='GET'&&method!=='HEAD'){
  if(request.headers.get('origin')!==url.origin||!(request.headers.get('content-type')||'').startsWith('application/json'))return familyJson({error:'Please use the website form.'},403);
  if(Number(request.headers.get('content-length')||0)>16384)return familyJson({error:'Request too large'},413);
 }
 if(path==='/api/family/login'&&method==='POST'){
  const b=await parseBody(request);
  if(!b||typeof b!=='object')return familyJson({error:'Invalid JSON body'},400);
  const username=String(b.username||'').trim().toLowerCase().slice(0,200),password=String(b.password||'');
  if(password.length>256||!await rateLimit(request,env,username))return familyJson({error:'Too many attempts. Try again in 15 minutes.'},429);
  const u=await findUserByUsername(env,username);
  const hash=await passwordHash(password,u?.password_salt||'invalid-account-comparison-salt');
  if(!u?.password_hash||!equalHash(hash,u.password_hash))return familyJson({error:'Username or password did not match. Children: ask a parent to set your password if this is your first login.'},401);
  return sessionResponse(u,env);
 }
 if(path==='/api/family/activate'&&method==='POST'){
  const b=await parseBody(request);if(!b||!/^[a-f0-9]{64}$/.test(b.token||'')||typeof b.password!=='string'||b.password.length<12||b.password.length>256)return familyJson({error:'Use the setup link and a password with at least 12 characters.'},400);
  if(!await rateLimit(request,env,'activation'))return familyJson({error:'Try again in 15 minutes.'},429);
  const h=await digest(b.token),invite=await env.DB.prepare('SELECT * FROM family_invites WHERE token_hash=? AND expires_at>?').bind(h,epoch()).first();if(!invite)return familyJson({error:'This setup link has expired or was already used.'},400);
  const salt=randomToken(),hash=await passwordHash(b.password,salt);
  const result=await env.DB.batch([env.DB.prepare('UPDATE family_users SET password_hash=?,password_salt=? WHERE id=? AND EXISTS(SELECT 1 FROM family_invites WHERE token_hash=? AND expires_at>?)').bind(hash,salt,invite.user_id,h,epoch()),env.DB.prepare('DELETE FROM family_invites WHERE token_hash=?').bind(h),env.DB.prepare('DELETE FROM family_sessions WHERE user_id=?').bind(invite.user_id)]);
  if(result[0].meta.changes!==1)return familyJson({error:'Setup link was already used.'},400);
  return sessionResponse(await env.DB.prepare('SELECT * FROM family_users WHERE id=?').bind(invite.user_id).first(),env);
 }
 if(path==='/api/family/venvlearning/sync'&&method==='POST'){
  const tokenAuthorized=venvSyncAuthOK(request,env);
  if(!tokenAuthorized){
   if(!user)return familyJson({error:'Please sign in.'},401);
   if(user.role!=='parent')return familyJson({error:'Parent access required'},403);
  }
  const body=await parseBody(request) || {};
  const range=sanitizeDateRange(body.start_date,body.end_date);
  try{
   const result=await syncVenvlearningDailyTasks(env,range);
   return familyJson(result);
  }catch(error){
   return familyJson({ok:false,error:error.message||'VenvLearning sync failed'},502);
  }
 }
 if(!user)return familyJson({error:'Please sign in.'},401);
 if(path==='/api/family/home-assistant-token')return manageHomeAssistant(request,env,user);
 if(path==='/api/family/me'&&method==='GET')return familyJson({user:publicUser(user),today:centralDate()});
 if(path==='/api/family/reset-link'&&method==='POST'){
  if(user.role!=='parent')return familyJson({error:'Parent access required'},403);
  const b=await parseBody(request);if(!b)return familyJson({error:'Invalid JSON body'},400);
  const target=await env.DB.prepare("SELECT id FROM family_users WHERE id=? AND role='parent' AND active=1").bind(String(b.id||'')).first();
  if(!target)return familyJson({error:'Parent account not found'},404);
  const token=randomToken();await env.DB.batch([env.DB.prepare('DELETE FROM family_invites WHERE user_id=?').bind(target.id),env.DB.prepare('INSERT INTO family_invites(token_hash,user_id,expires_at) VALUES(?,?,?)').bind(await digest(token),target.id,epoch()+3600)]);
  return familyJson({url:url.origin+'/login#invite='+token});
 }
 if(path==='/api/family/logout'&&method==='POST'){const t=sessionTokenFromCookieHeader(request.headers.get('cookie')||'',env);if(t)await env.DB.prepare('DELETE FROM family_sessions WHERE token_hash=?').bind(await digest(t)).run();return familyJson({ok:true},200,{'set-cookie':cookie('',env,0)});}
 if(path==='/api/family/users'&&method==='GET'){if(user.role!=='parent')return familyJson({error:'Parent access required'},403);return familyJson({users:(await env.DB.prepare('SELECT * FROM family_users WHERE active=1 ORDER BY role,grade,username').all()).results.map(publicUser)});}
 if(path==='/api/family/account'&&method==='POST'){
  if(user.role!=='parent')return familyJson({error:'Parent access required'},403);const b=await parseBody(request);if(!b)return familyJson({error:'Invalid JSON body'},400);const target=await env.DB.prepare('SELECT * FROM family_users WHERE id=? AND active=1').bind(String(b.id||'')).first();if(!target)return familyJson({error:'Account not found'},404);
  if(target.role==='parent'&&target.id!==user.id)return familyJson({error:'Each parent manages their own password.'},403);
  const name=String(b.display_name||'').trim().slice(0,60),username=String(b.username||'').trim().toLowerCase();if(!name||!username||username.length>200||!/^[-a-z0-9@._+]+$/.test(username))return familyJson({error:'Enter a name and valid email or username.'},400);
  if(target.role==='parent'&&username!==target.username)return familyJson({error:'Parent email changes require account verification.'},400);
  if(b.password){if(typeof b.password!=='string'||b.password.length<12||b.password.length>256)return familyJson({error:'Use at least 12 characters for the password.'},400);
   if(target.role==='parent'&&!equalHash(await passwordHash(String(b.current_password||''),target.password_salt),target.password_hash))return familyJson({error:'Current password did not match'},403);
   const salt=randomToken();await env.DB.batch([env.DB.prepare('UPDATE family_users SET username=?,display_name=?,password_hash=?,password_salt=? WHERE id=?').bind(username,name,await passwordHash(b.password,salt),salt,target.id),env.DB.prepare('DELETE FROM family_sessions WHERE user_id=?').bind(target.id)]);
  }else await env.DB.prepare('UPDATE family_users SET username=?,display_name=? WHERE id=?').bind(username,name,target.id).run();
  return familyJson({ok:true,signed_out:!!b.password&&target.id===user.id});
 }
 if(path==='/api/family/agenda'&&method==='GET'){
  const date=url.searchParams.get('date')||centralDate();if(!safeDate(date))return familyJson({error:'Invalid date'},400);
  const target=user.role==='parent'?await env.DB.prepare("SELECT * FROM family_users WHERE id=? AND role='student' AND active=1").bind(url.searchParams.get('student')||'student-4').first():user;if(!target)return familyJson({error:'Student not found'},404);
  await ensureFamilyTaskTables(env.DB);
  const days=await assetJson(request,env,'/daily-packets.json');const activeDay=days[date]?.[target.grade];const activeVersion=curriculumForDay(activeDay);
  const [library,exams,completion,venvTasks]=await Promise.all([assetJson(request,env,'/planner-resources.json'),assetJson(request,env,'/assessment-student.json'),env.DB.prepare("SELECT subject,completed FROM family_curriculum_completion WHERE user_id=? AND school_date=? AND curriculum=?").bind(target.id,date,activeVersion).all(),env.DB.prepare("SELECT title,status,source,external_id,due_date,updated_at FROM family_daily_tasks WHERE user_id=? AND due_date=? ORDER BY CASE status WHEN 'overdue' THEN 0 WHEN 'pending' THEN 1 WHEN 'in_progress' THEN 2 WHEN 'completed' THEN 3 WHEN 'cancelled' THEN 4 ELSE 5 END, title").bind(target.id,date).all()]);
  const dailyTasks=(venvTasks.results||[]).map(t=>({title:t.title,status:t.status,source:t.source,external_id:t.external_id,due_date:t.due_date,updated_at:t.updated_at}));
  const d=days[date]?.[target.grade];if(!d)return familyJson({student:publicUser(target),date,teaching:false,next_date:Object.keys(days).sort().find(x=>x>date)||null,daily_tasks:dailyTasks});
  const mapping=library.weeks[`${target.grade}-${d.module}-${d.week}`],subjects=subjectsForDay(d,mapping).map(key=>{const s=mapping[key];return ({key,name:s.display_name,category:s.category,task:taskForSubject(d,key),topic:s.topic,readings:readingsForDay(s,date).map(r=>readingLink(r,library.resources)).filter(Boolean),mode:s.mode,primary:s.primary,gap_note:s.gap_note,resources:s.resources.map(id=>library.resources[id]),completed:completion.results.some(r=>r.subject===key&&r.completed===1)});});
  return familyJson({student:publicUser(target),date,teaching:true,module:d.module,week:d.week,tasks:cleanTaskText(d.tasks),goals:d.goals,integration:d.integration||'',elective:d.elective||null,lesson_context:d.lesson_context||'',curriculum:curriculumForDay(d),subjects,assessment:d.assessment?{title:exams[d.assessment].title,student_pdf:'/assessments/'+d.assessment+'-student.pdf'}:null,primary_assessments:d.primary_assessments||[],print_url:'/daily-print?date='+date+'&grade='+target.grade,daily_tasks:dailyTasks});
 }
 if(path==='/api/family/progress'&&method==='GET'){
  const target=user.role==='parent'?await env.DB.prepare("SELECT * FROM family_users WHERE id=? AND role='student' AND active=1").bind(url.searchParams.get('student')||'student-4').first():user;if(!target)return familyJson({error:'Student not found'},404);
  const rows=await env.DB.prepare("SELECT school_date AS d,subject AS s,completed AS c FROM family_curriculum_completion WHERE user_id=? AND completed=1").bind(target.id).all();
  return familyJson({student:publicUser(target),rows:rows.results||[]});
 }
 if(path==='/api/family/announcements'&&method==='GET'){
  await ensureFamilyTaskTables(env.DB);
  const rows=user.role==='parent'?await env.DB.prepare("SELECT id,title,body,grade,pinned,author,created_at FROM family_announcements ORDER BY pinned DESC,created_at DESC LIMIT 100").all():await env.DB.prepare("SELECT id,title,body,grade,pinned,author,created_at FROM family_announcements WHERE grade IN ('both',?) ORDER BY pinned DESC,created_at DESC LIMIT 50").bind(String(user.grade)).all();
  return familyJson({announcements:rows.results||[]});
 }
 if(path==='/api/family/announcements'&&method==='POST'){
  if(user.role!=='parent')return familyJson({error:'Parent access required'},403);
  await ensureFamilyTaskTables(env.DB);
  const b=await parseBody(request);if(!b)return familyJson({error:'Invalid JSON body'},400);
  if(b.delete_id!==undefined){await env.DB.prepare('DELETE FROM family_announcements WHERE id=?').bind(Number(b.delete_id)).run();return familyJson({ok:true});}
  const title=String(b.title||'').trim().slice(0,120),body=String(b.body||'').trim().slice(0,2000),grade=String(b.grade||'both');
  if(!title||!['both','4','7'].includes(grade))return familyJson({error:'Add a title and choose who it is for.'},400);
  await env.DB.prepare('INSERT INTO family_announcements(title,body,grade,pinned,author,created_at) VALUES(?,?,?,?,?,?)').bind(title,body,grade,b.pinned?1:0,String(user.display_name||'').slice(0,60),epoch()).run();
  return familyJson({ok:true});
 }
 if(path==='/api/family/attendance'&&method==='GET'){
  if(user.role!=='parent')return familyJson({error:'Parent access required'},403);
  await ensureFamilyTaskTables(env.DB);
  const target=await env.DB.prepare("SELECT * FROM family_users WHERE id=? AND role='student' AND active=1").bind(url.searchParams.get('student')||'student-4').first();if(!target)return familyJson({error:'Student not found'},404);
  const rows=await env.DB.prepare("SELECT school_date AS d,status AS s,hours AS h,note AS n FROM family_attendance WHERE student_id=? ORDER BY school_date").bind(target.id).all();
  return familyJson({student:publicUser(target),rows:rows.results||[]});
 }
 if(path==='/api/family/attendance'&&method==='POST'){
  if(user.role!=='parent')return familyJson({error:'Parent access required'},403);
  await ensureFamilyTaskTables(env.DB);
  const b=await parseBody(request);if(!b)return familyJson({error:'Invalid JSON body'},400);
  const target=await env.DB.prepare("SELECT * FROM family_users WHERE id=? AND role='student' AND active=1").bind(String(b.student_id||'')).first();if(!target)return familyJson({error:'Student not found'},404);
  const entries=Array.isArray(b.entries)?b.entries.slice(0,250):[];if(!entries.length)return familyJson({error:'Nothing to save'},400);
  const days=await assetJson(request,env,'/daily-packets.json');const stmts=[];
  for(const e of entries){
   const date=String(e.date||'');if(!safeDate(date)||!days[date]?.[target.grade])return familyJson({error:'Not a scheduled school day: '+date},400);
   if(e.clear===true){stmts.push(env.DB.prepare('DELETE FROM family_attendance WHERE student_id=? AND school_date=?').bind(target.id,date));continue;}
   const status=String(e.status||'');if(!['present','absent','partial'].includes(status))return familyJson({error:'Invalid status'},400);
   const hours=e.hours===null||e.hours===undefined||e.hours===''?null:Number(e.hours);if(hours!==null&&(!Number.isFinite(hours)||hours<0||hours>24))return familyJson({error:'Hours must be between 0 and 24'},400);
   stmts.push(env.DB.prepare("INSERT INTO family_attendance(student_id,school_date,status,hours,note,updated_at) VALUES(?,?,?,?,?,?) ON CONFLICT(student_id,school_date) DO UPDATE SET status=excluded.status,hours=excluded.hours,note=excluded.note,updated_at=excluded.updated_at").bind(target.id,date,status,hours,String(e.note||'').slice(0,300),epoch()));
  }
  await env.DB.batch(stmts);return familyJson({ok:true,saved:stmts.length});
 }
 if(path==='/api/family/grades'&&method==='GET'){
  await ensureFamilyTaskTables(env.DB);
  const target=user.role==='parent'?await env.DB.prepare("SELECT * FROM family_users WHERE id=? AND role='student' AND active=1").bind(url.searchParams.get('student')||'student-4').first():user;if(!target)return familyJson({error:'Student not found'},404);
  const rows=await env.DB.prepare("SELECT item_key AS k,subject AS s,category AS c,title AS t,school_date AS d,points AS p,possible AS m,comment AS n FROM family_grades WHERE student_id=? ORDER BY school_date,item_key").bind(target.id).all();
  return familyJson({student:publicUser(target),rows:rows.results||[]});
 }
 if(path==='/api/family/grades'&&method==='POST'){
  if(user.role!=='parent')return familyJson({error:'Parent access required'},403);
  await ensureFamilyTaskTables(env.DB);
  const b=await parseBody(request);if(!b)return familyJson({error:'Invalid JSON body'},400);
  const target=await env.DB.prepare("SELECT * FROM family_users WHERE id=? AND role='student' AND active=1").bind(String(b.student_id||'')).first();if(!target)return familyJson({error:'Student not found'},404);
  const key=String(b.key||''),subject=String(b.subject||''),category=String(b.category||''),date=String(b.date||'');
  if(!/^[A-Za-z0-9|:_.-]{1,90}$/.test(key)||!['math','ela','science','social','spanish','art','life','computer','skills'].includes(subject)||!['work','quiz','test','project'].includes(category)||!safeDate(date))return familyJson({error:'Invalid grade item'},400);
  if(b.clear===true){await env.DB.prepare('DELETE FROM family_grades WHERE student_id=? AND item_key=?').bind(target.id,key).run();return familyJson({ok:true});}
  const points=Number(b.points),possible=Number(b.possible),title=String(b.title||'').slice(0,160),comment=String(b.comment||'').slice(0,500);
  if(!Number.isFinite(points)||!Number.isFinite(possible)||points<0||possible<=0||possible>1000||points>possible*2||!title)return familyJson({error:'Enter a score and a total above zero.'},400);
  await env.DB.prepare("INSERT INTO family_grades(student_id,item_key,subject,category,title,school_date,points,possible,comment,updated_at) VALUES(?,?,?,?,?,?,?,?,?,?) ON CONFLICT(student_id,item_key) DO UPDATE SET points=excluded.points,possible=excluded.possible,comment=excluded.comment,title=excluded.title,updated_at=excluded.updated_at").bind(target.id,key,subject,category,title,date,points,possible,comment,epoch()).run();
  return familyJson({ok:true});
 }
 if(path==='/api/family/completion'&&method==='POST'){
  const b=await parseBody(request);if(!b)return familyJson({error:'Invalid JSON body'},400);const id=user.role==='parent'?String(b.student_id||''):user.id;if(!safeDate(String(b.date||''))||!['math','ela','science','social','spanish','art','life','computer','skills','review'].includes(b.subject)||typeof b.completed!=='boolean')return familyJson({error:'Invalid task'},400);
  const target=await env.DB.prepare("SELECT * FROM family_users WHERE id=? AND role='student' AND active=1").bind(id).first();if(!target)return familyJson({error:'Student not found'},404);const days=await assetJson(request,env,'/daily-packets.json');const scheduledDay=days[b.date]?.[target.grade];if(!scheduledDay)return familyJson({error:'No teaching day scheduled'},400);if(scheduledDay.subjects&&!scheduledDay.subjects.includes(b.subject))return familyJson({error:'Subject is not scheduled on this date'},400);
  await env.DB.prepare("INSERT INTO family_curriculum_completion(user_id,school_date,subject,completed,updated_at,curriculum) VALUES(?,?,?,?,?,?) ON CONFLICT(user_id,school_date,subject,curriculum) DO UPDATE SET completed=excluded.completed,updated_at=excluded.updated_at").bind(id,b.date,b.subject,b.completed?1:0,epoch(),curriculumForDay(scheduledDay)).run();return familyJson({ok:true});
 }
 return familyJson({error:'Not found'},404);
}
async function familyFetch(request,env,ctx){
 const url=new URL(request.url),path=decodeURIComponent(url.pathname);
 // Source/config files must never be delivered as public static assets.
 if(/\/(?:index\.js|_worker\.js|family-server\.js|teacher-tools\.js|wishlist\.js|ha-school\.js|home-assistant-api\.js|schema\.sql|wrangler\.jsonc|package\.json|README\.md|\.dev|\.git|tools\/)/i.test(path))return new Response('Not found',{status:404});
 const publicPaths=['/login','/login.html','/login.js','/forgot-password','/forgot-password.html','/family.css','/styles.css','/brand.css','/ux.js','/favicon.ico'];
 if(publicPaths.includes(path))return fetchAsset(request, env);
 if(url.pathname.startsWith('/api/home-assistant/'))return homeAssistantApi(request,env,assetJson);
 if(url.pathname.startsWith('/api/family/')){
  if(!env.DB||typeof env.DB.prepare!=='function')return familyJson({error:'Database is not configured for this environment.'},503);
  await maybeEnsureFamilyAuthTables(env.DB, env);
  const user=await familyUser(request,env);
  if(isWishlistPath(path))return wishlistRoute(request,env,user,url,assetJson);
  if(isTeacherToolsPath(path))return teacherToolsRoute(request,env,user,url,{ensureBaseTables:ensureFamilyTaskTables});
  return authRoute(request,env,user,url);
 }
 const user=await familyUser(request,env);
 if(!user)return path.startsWith('/api/')?familyJson({error:'Please sign in.'},401):new Response(null,{status:302,headers:{location:'/login','cache-control':'no-store'}});
 if(path.startsWith('/api/')&&!['GET','HEAD'].includes(request.method)&&(request.headers.get('origin')!==url.origin||!(request.headers.get('content-type')||'').startsWith('application/json')))return familyJson({error:'Please use the website form.'},403);
 if(path==='/'&&user.role==='student')return new Response(null,{status:302,headers:{location:'/courses','cache-control':'no-store'}});
 if(user.role==='student'){
  const allowed=['/courses','/courses.html','/courses.js','/course','/course.html','/course.js','/lms.js','/lms.css','/school-events.json','/grading-config.json','/calendar','/calendar.html','/calendar.js','/packet-renderer.js','/packet-files.js','/materials.css','/vendor/pdf-lib.min.js','/page-readings.js','/agenda','/agenda.html','/agenda.js','/account-nav.js','/daily-print','/daily-print.html','/daily-print.js','/daily-print.css','/print-download.js','/planner-resources.json','/khan-ui.js','/khan-ui.css','/books','/books.html','/books.js','/books-library.json','/core-knowledge','/core-knowledge.html','/core-knowledge.js','/core-knowledge-units.json','/brand.css','/assignments','/assignments.html','/assignments.js','/library','/library.html','/library.js','/files.js','/reading-list.json'];
  if(path==='/planner-resources.json')return familyJson(studentResourceLibrary(await assetJson(request,env,path)));
  if(path==='/daily-packets.json'){const data=await assetJson(request,env,path);return familyJson(Object.fromEntries(Object.entries(data).map(([date,g])=>[date,{[user.grade]:g[user.grade]}])));}
  if(path==='/assessment-student.json'){const data=await assetJson(request,env,path);return familyJson(Object.fromEntries(Object.entries(data).filter(([,e])=>String(e.grade)===user.grade)));}
  const pdf=path.match(/^\/assessments\/(?:(?:khan|eight)-)?g([47])-m[1-9]-(?:w[1-3]-quiz|test)-student\.pdf$/);
  const booklet=path.match(/^\/downloads\/integrated\/grade([47])-(?:art|life|computer|skills)(?:-[a-z0-9]+)?-student\.pdf$/);
  if(!allowed.includes(path)&&!(pdf&&pdf[1]===user.grade)&&!(booklet&&booklet[1]===user.grade))return familyJson({error:'Parent access required'},403);
  if(/^\/daily-print(?:\.html)?$/.test(path)&&(url.searchParams.get('key')==='1'||url.searchParams.get('kind')==='keys'||url.searchParams.get('grade')!==user.grade)){url.searchParams.delete('key');if(url.searchParams.get('kind')==='keys')url.searchParams.set('kind','work');url.searchParams.set('grade',user.grade);return new Response(null,{status:302,headers:{location:url.pathname+url.search,'cache-control':'no-store'}});}
 }
 const response=path.startsWith('/api/')?await legacy.fetch(request,env,ctx):await fetchAsset(request, env);
 const secured=new Response(response.body,response);secured.headers.set('cache-control','private, no-store');secured.headers.set('x-content-type-options','nosniff');secured.headers.set('referrer-policy','same-origin');secured.headers.set('content-security-policy',`frame-ancestors ${frameAncestors(env)}`);secured.headers.delete('x-frame-options');return secured;
}
export default {async fetch(request,env,ctx){try{return await familyFetch(request,env,ctx)}catch(e){console.error('Family request failed',{name:e&&e.name,message:e&&e.message,stack:e&&e.stack});return familyJson({error:'This page could not load. Please try again.'},500)}}};
