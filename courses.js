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
    const t = $("lmsTodo");
    t.replaceChildren();
    for (const item of todo.slice(0, 10)) {
      const li = el("li");
      const a = el("a", item.text);
      a.href = item.date ? L.agendaUrl(ctx, item.date) : L.courseUrl(ctx, item.c, "#modules");
      li.append(a, el("span", item.date ? "Today" : "Past", "lms-chip"));
      t.append(li);
    }
    if (!todo.length) t.append(el("li", ctx.daily[ctx.today]?.[ctx.student.grade] ? "Everything for today is done." : "No lessons scheduled today.", "muted"));

    const soon = [];
    const horizon = new Date(ctx.today + "T12:00:00Z");
    horizon.setUTCDate(horizon.getUTCDate() + 28);
    const end = horizon.toISOString().slice(0, 10);
    for (const date of Object.keys(ctx.daily).sort()) {
      if (date < ctx.today || date > end) continue;
      const rec = ctx.daily[date]?.[ctx.student.grade];
      if (rec?.assessment) soon.push({ date, text: `${L.assessLabel(rec.assessment)} · Module ${rec.module}`, kind: "Test" });
    }
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

  (async () => {
    try {
      const ctx = await L.load();
      $("status").textContent = "";
      render(ctx);
    } catch (e) {
      $("status").textContent = e.message;
    }
  })();
})();
