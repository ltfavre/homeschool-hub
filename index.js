const json = (data, status = 200) =>
  new Response(JSON.stringify(data, null, 2), {
    status,
    headers: { "content-type": "application/json; charset=utf-8" },
  });

const parseBody = async (request) => {
  try { return await request.json(); }
  catch { return null; }
};

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
