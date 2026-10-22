window.LMS = (() => {
  const NAMES = { math: "Math", ela: "ELA", science: "Physical Sciences", social: "Social Studies", spanish: "Spanish", art: "Art", life: "Human Sciences", computer: "Computer Science", skills: "Life Skills" };
  const ORDER = ["math", "ela", "science", "social", "spanish", "art", "life", "computer", "skills"];
  const CORE = ["math", "ela", "science", "social"];
  const el = (tag, text = "", cls = "") => {
    const n = document.createElement(tag);
    if (text) n.textContent = text;
    if (cls) n.className = cls;
    return n;
  };
  const fmt = (iso, o = { month: "short", day: "numeric" }) => new Date(iso + "T12:00:00Z").toLocaleDateString("en-US", { timeZone: "UTC", ...o });
  const day = (iso) => fmt(iso, { weekday: "short", month: "short", day: "numeric" });

  async function json(path, opts) {
    const r = await fetch(path, opts);
    if (r.status === 401 || r.redirected) { location.replace("/login"); throw new Error("Please sign in."); }
    if (!r.ok) throw new Error(`Could not load ${path} (${r.status})`);
    return r.json();
  }

  async function load() {
    const meRes = await json("/api/family/me");
    const me = meRes.user;
    const [daily, library] = await Promise.all([json("/daily-packets.json"), json("/planner-resources.json")]);
    let events = [];
    try { events = (await json("/school-events.json")).events || []; } catch { events = []; }
    const students = me.role === "parent" ? (await json("/api/family/users")).users.filter((u) => u.role === "student") : [me];
    const wanted = new URLSearchParams(location.search).get("student");
    const student = students.find((s) => s.id === wanted) || students[0];
    const ctx = { me, today: meRes.today, daily, library, events, students, student, progress: new Map() };
    await loadProgress(ctx);
    return ctx;
  }

  async function loadProgress(ctx) {
    const q = ctx.me.role === "parent" ? `?student=${encodeURIComponent(ctx.student.id)}` : "";
    const data = await json("/api/family/progress" + q);
    ctx.progress = new Map((data.rows || []).filter((r) => r.c === 1).map((r) => [`${r.d}|${r.s}`, true]));
  }

  const subjectsOn = (rec, mapping) => rec.subjects || Object.keys(mapping);

  function courses(ctx) {
    const grade = ctx.student.grade;
    const found = new Set();
    for (const date of Object.keys(ctx.daily)) {
      const rec = ctx.daily[date]?.[grade];
      if (!rec) continue;
      const mapping = ctx.library.weeks[`${grade}-${rec.module}-${rec.week}`] || {};
      for (const s of subjectsOn(rec, mapping)) if (s !== "review" && mapping[s]) found.add(s);
    }
    // Skip stub subjects that only appear for a week or two (for example the Spanish intro).
    const count = (s) => Object.keys(ctx.daily).filter((d) => { const rec = ctx.daily[d]?.[grade]; const m = rec && ctx.library.weeks[`${grade}-${rec.module}-${rec.week}`]; return m?.[s] && subjectsOn(rec, m).includes(s); }).length;
    return ORDER.filter((s) => found.has(s) && count(s) >= 15).map((s) => ({ grade, subject: s, name: NAMES[s] || s }));
  }

  function unitName(ctx, s) {
    const readings = s?.readings || [];
    for (const r of readings) {
      const m = (ctx.library.resources[r.resource_id]?.title || "").match(/^Unit\s+\d+\s+-\s+(.+?)\s+-\s+(?:Student|Core|Activity|Teacher|Alignment)/i);
      if (m) return m[1];
    }
    const first = ctx.library.resources[readings[0]?.resource_id]?.title;
    return first && !/student booklet/i.test(first) ? first.replace(/\s+-\s+(Full )?Student.*$/i, "") : "";
  }

  function pagesText(r) {
    const a = r.printed || r.pdf;
    if (!a) return "";
    return `${r.printed ? "printed " : "PDF "}pp. ${a[0] === a[1] ? a[0] : a[0] + "–" + a[1]}`;
  }

  // Modules → weeks → days for one course, with resources and progress.
  function modules(ctx, subject) {
    const grade = ctx.student.grade;
    const weeks = new Map();
    for (const date of Object.keys(ctx.daily).sort()) {
      const rec = ctx.daily[date]?.[grade];
      if (!rec) continue;
      const key = `${rec.module}-${rec.week}`;
      const mapping = ctx.library.weeks[`${grade}-${key}`] || {};
      if (!weeks.has(key)) weeks.set(key, { module: rec.module, week: rec.week, days: [], assessments: [], mapping, start: date, end: date });
      const w = weeks.get(key);
      w.end = date;
      if (subjectsOn(rec, mapping).includes(subject) && mapping[subject]) w.days.push({ date, subject, done: ctx.progress.has(`${date}|${subject}`) });
      if (rec.assessment && CORE.includes(subject)) w.assessments.push({ date, id: rec.assessment });
    }
    const mods = new Map();
    for (const w of weeks.values()) {
      if (!w.days.length) continue;
      const s = w.mapping[subject];
      w.topic = s.topic;
      w.unit = unitName(ctx, s);
      const used = new Set();
      w.readings = (s.readings || []).map((r) => {
        used.add(r.resource_id);
        const res = ctx.library.resources[r.resource_id];
        return res ? { title: r.section || res.title, book: res.title, url: res.url.split("#")[0] + (r.pdf ? "#page=" + r.pdf[0] : ""), pages: pagesText(r) } : null;
      }).filter(Boolean);
      w.extras = (s.resources || []).filter((id) => !used.has(id)).map((id) => ({ ...ctx.library.resources[id], id })).filter((r) => r.title && r.url && !r.teacher_only);
      w.done = w.days.filter((d) => d.done).length;
      if (!mods.has(w.module)) mods.set(w.module, { module: w.module, weeks: [] });
      mods.get(w.module).weeks.push(w);
    }
    return [...mods.values()].map((m) => ({ ...m, total: m.weeks.reduce((n, w) => n + w.days.length, 0), done: m.weeks.reduce((n, w) => n + w.done, 0) }));
  }

  function stats(mods, today) {
    const days = mods.flatMap((m) => m.weeks.flatMap((w) => w.days));
    const weeks = mods.flatMap((m) => m.weeks);
    const current = weeks.find((w) => today >= w.start && today <= w.end) || weeks.find((w) => w.start > today) || weeks[weeks.length - 1];
    const next = days.find((d) => !d.done && d.date >= today) || null;
    const overdue = days.filter((d) => !d.done && d.date < today).length;
    return { total: days.length, done: days.filter((d) => d.done).length, current, next, overdue };
  }

  const assessLabel = (id) => (/-test$/.test(id) ? "Module test" : "Weekly quiz");

  function bar(done, total) {
    const wrap = el("div", "", "lms-bar");
    wrap.setAttribute("role", "progressbar");
    wrap.setAttribute("aria-valuemin", "0");
    wrap.setAttribute("aria-valuemax", String(total));
    wrap.setAttribute("aria-valuenow", String(done));
    const fill = el("span");
    fill.style.width = total ? Math.round((done / total) * 100) + "%" : "0%";
    wrap.append(fill);
    return wrap;
  }

  function studentSwitcher(ctx, onChange) {
    if (ctx.me.role !== "parent" || ctx.students.length < 2) return null;
    const label = el("label", "Viewing as ", "lms-switch");
    const sel = el("select");
    for (const s of ctx.students) {
      const o = el("option", `${s.display_name} · Grade ${s.grade}`);
      o.value = s.id;
      if (s.id === ctx.student.id) o.selected = true;
      sel.append(o);
    }
    sel.onchange = () => onChange(sel.value);
    label.append(sel);
    return label;
  }

  const courseUrl = (ctx, c, hash = "") => `/course?grade=${c.grade}&subject=${c.subject}${ctx.me.role === "parent" ? "&student=" + encodeURIComponent(ctx.student.id) : ""}${hash}`;
  const agendaUrl = (ctx, date) => `/agenda?date=${date}${ctx.me.role === "parent" ? "&student=" + encodeURIComponent(ctx.student.id) : ""}`;

  return { NAMES, el, fmt, day, load, loadProgress, courses, modules, stats, assessLabel, bar, studentSwitcher, courseUrl, agendaUrl, json };
})();
