const json = (data, status = 200) =>
  new Response(JSON.stringify(data, null, 2), {
    status,
    headers: { "content-type": "application/json; charset=utf-8" },
  });

const parseBody = async (request) => {
  try { return await request.json(); }
  catch { return null; }
};


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

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (!url.pathname.startsWith("/api/")) {
      return env.ASSETS.fetch(request);
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
