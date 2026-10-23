(() => {
  const L = window.LMS, { el } = L;
  const $ = (id) => document.getElementById(id);

  function render(ctx) {
    const first = ctx.student.display_name;
    $("lmsHello").textContent = ctx.me.role === "parent" ? `${first}'s courses` : `Welcome back, ${first}`;
    $("lmsSub").textContent = `Grade ${ctx.student.grade} · ${L.fmt(ctx.today, { weekday: "long", month: "long", day: "numeric" })}`;
    $("lmsSwitch").replaceChildren(L.studentSwitcher(ctx, (id) => { const u = new URL(location.href); u.searchParams.set("student", id); location.href = u; }) || "");

    const cards = $("lmsCourses");
    cards.replaceChildren();
    const todo = [];
    for (const c of L.courses(ctx)) {
      const mods = L.modules(ctx, c.subject);
      const st = L.stats(mods, ctx.today);
      const card = el("article", "", "lms-card");
      card.dataset.subject = c.subject;
      const a = el("a", "", "lms-card-link");
      a.href = L.courseUrl(ctx, c);
      a.setAttribute("aria-label", `${c.name}, Grade ${c.grade}`);
      const band = el("div", "", "lms-card-band");
      const body = el("div", "", "lms-card-body");
      body.append(el("p", `GRADE ${c.grade}`, "eyebrow"), el("h3", c.name));
      if (st.current) {
        body.append(el("p", `Module ${st.current.module} · Week ${st.current.week}`, "lms-strong"), el("p", st.current.topic, "muted lms-topic"));
      }
      body.append(L.bar(st.done, st.total), el("p", `${st.done} of ${st.total} lessons done`, "muted lms-small"));
      const gr = L.courseGrade(ctx, c.subject);
      if (gr.pct !== null) body.append(el("p", `Grade: ${gr.letter} · ${L.pct1(gr.pct)}%`, "lms-strong"));
      if (st.overdue) body.append(el("p", `${st.overdue} past lesson${st.overdue === 1 ? "" : "s"} not marked done`, "lms-flag"));
      a.append(band, body);
      card.append(a);
      cards.append(card);
      const today = mods.flatMap((m) => m.weeks.flatMap((w) => w.days)).find((d) => d.date === ctx.today);
      if (today && !today.done) todo.push({ c, text: `${c.name}: ${st.current?.topic || "today's lesson"}`, date: ctx.today });
      else if (st.overdue) todo.push({ c, text: `${c.name}: ${st.overdue} past lesson${st.overdue === 1 ? "" : "s"} to mark`, date: "" });
    }
    // Teacher-created assignments: due soon or missing (student), turned in and waiting (parent).
    const asUrl = (a) => `/assignments${ctx.me.role === "parent" ? "?student=" + encodeURIComponent(ctx.student.id) : ""}#a${a.id}`;
    const week = new Date(ctx.today + "T12:00:00Z"); week.setUTCDate(week.getUTCDate() + 7);
    const weekEnd = week.toISOString().slice(0, 10);
    const asTodo = [];
    for (const a of ctx.assignments || []) {
      if (!a.published) continue;
      const st = L.assignmentState(ctx, a);
      if (ctx.me.role === "parent" ? st.code === "submitted" : ["late", "today"].includes(st.code) || (st.code === "open" && a.due_date <= weekEnd)) {
        asTodo.push({ a, text: `${L.NAMES[a.subject] || a.subject}: ${a.title}`, chip: ctx.me.role === "parent" ? "To grade" : st.code === "open" ? `Due ${L.fmt(a.due_date, { weekday: "short" })}` : st.label });
      }
    }
    const t = $("lmsTodo");
    t.replaceChildren();
    for (const item of asTodo.slice(0, 6)) {
      const li = el("li");
      const a = el("a", item.text); a.href = asUrl(item.a);
      li.append(a, el("span", item.chip, "lms-chip" + (item.chip === "Missing" ? " as-late" : "")));
      t.append(li);
    }
    for (const item of todo.slice(0, 10)) {
      const li = el("li");
      const a = el("a", item.text);
      a.href = item.date ? L.agendaUrl(ctx, item.date) : L.courseUrl(ctx, item.c, "#modules");
      li.append(a, el("span", item.date ? "Today" : "Past", "lms-chip"));
      t.append(li);
    }
    if (!todo.length && !asTodo.length) t.append(el("li", ctx.daily[ctx.today]?.[ctx.student.grade] ? "Everything for today is done." : "No lessons scheduled today.", "muted"));

    const soon = [];
    const horizon = new Date(ctx.today + "T12:00:00Z");
    horizon.setUTCDate(horizon.getUTCDate() + 28);
    const end = horizon.toISOString().slice(0, 10);
    for (const date of Object.keys(ctx.daily).sort()) {
      if (date < ctx.today || date > end) continue;
      const rec = ctx.daily[date]?.[ctx.student.grade], as = L.assessOn(ctx, date);
      if (as) soon.push({ date, text: `${L.assessLabel(as)} · Module ${rec?.module ?? ""}`, kind: "Test" });
    }
    for (const a of ctx.assignments || []) if (a.published && a.due_date > ctx.today && a.due_date <= end) soon.push({ date: a.due_date, text: `${a.title} (${L.NAMES[a.subject] || a.subject})`, kind: "Due" });
    for (const e of ctx.events) if (e.date >= ctx.today && e.date <= end && (e.grade === "both" || String(e.grade) === String(ctx.student.grade))) soon.push({ date: e.date, text: e.title, kind: e.type === "field trip" ? "Trip" : "Event" });
    soon.sort((a, b) => a.date.localeCompare(b.date));
    const s = $("lmsSoon");
    s.replaceChildren();
    for (const item of soon.slice(0, 8)) {
      const li = el("li");
      li.append(el("span", item.text), el("span", `${L.day(item.date)}`, "muted lms-small"), el("span", item.kind, "lms-chip"));
      s.append(li);
    }
    if (!soon.length) s.append(el("li", "Nothing scheduled in the next four weeks.", "muted"));
  }

  async function announcements(ctx) {
    const box = $("lmsAnn");
    const load = async () => {
      const data = await L.json("/api/family/announcements");
      box.replaceChildren();
      const forStudent = (a) => a.grade === "both" || String(a.grade) === String(ctx.student.grade);
      const list = (data.announcements || []).filter((a) => ctx.me.role === "parent" || forStudent(a)).slice(0, 8);
      for (const a of list) {
        const item = el("article", "", "lms-ann" + (a.pinned ? " is-pinned" : ""));
        item.append(el("strong", (a.pinned ? "📌 " : "") + a.title));
        item.append(el("p", `${new Date(a.created_at * 1000).toLocaleDateString("en-US", { month: "short", day: "numeric" })}${ctx.me.role === "parent" ? " · " + (a.grade === "both" ? "Everyone" : "Grade " + a.grade) : ""}`, "muted lms-small"));
        if (a.body) item.append(el("p", a.body, "lms-ann-body"));
        if (ctx.me.role === "parent") {
          const del = el("button", "Delete", "secondary lms-small"); del.type = "button";
          del.onclick = async () => { del.disabled = true; await L.json("/api/family/announcements", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ delete_id: a.id }) }); load(); };
          item.append(del);
        }
        box.append(item);
      }
      if (!list.length) box.append(el("p", "No announcements.", "muted"));
      if (ctx.me.role === "parent") box.append(composer());
    };
    const composer = () => {
      const d = el("details", "", "lms-details");
      d.append(el("summary", "Post an announcement"));
      const f = el("form", "", "lms-ann-form");
      const t = el("input"); t.placeholder = "Title"; t.maxLength = 120; t.required = true; t.setAttribute("aria-label", "Title");
      const b = el("textarea"); b.rows = 3; b.maxLength = 2000; b.placeholder = "Message"; b.setAttribute("aria-label", "Message");
      const g = el("select"); g.setAttribute("aria-label", "Who is it for");
      for (const [v, n] of [["both", "Everyone"], ["4", "Grade 4"], ["7", "Grade 7"]]) { const o = el("option", n); o.value = v; g.append(o); }
      const pl = el("label", " Pin to top"); const pin = el("input"); pin.type = "checkbox"; pl.prepend(pin);
      const go = el("button", "Post"); go.type = "submit";
      const msg = el("span", "", "lms-small muted"); msg.setAttribute("role", "status");
      f.append(t, b, g, pl, go, msg);
      f.onsubmit = async (e) => {
        e.preventDefault(); go.disabled = true; msg.textContent = "Posting…";
        try { await L.json("/api/family/announcements", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ title: t.value, body: b.value, grade: g.value, pinned: pin.checked }) }); await load(); } catch (err) { msg.textContent = err.message; go.disabled = false; }
      };
      d.append(f);
      return d;
    };
    try { await load(); } catch (e) { box.textContent = e.message; }
  }

  (async () => {
    try {
      const ctx = await L.load();
      $("status").textContent = "";
      render(ctx);
      announcements(ctx);
    } catch (e) {
      $("status").textContent = e.message;
    }
  })();
})();
