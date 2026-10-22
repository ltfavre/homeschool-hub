(() => {
  const L = window.LMS, { el } = L;
  const $ = (id) => document.getElementById(id);
  const params = new URLSearchParams(location.search);
  let ctx, course, mods;

  const link = (text, url, cls = "") => {
    const a = el("a", text, cls);
    a.href = url;
    if (/^https?:/i.test(url)) { a.target = "_blank"; a.rel = "noopener noreferrer"; }
    return a;
  };

  function refresh() {
    mods = L.modules(ctx, course.subject);
  }

  function resourceList(w) {
    const ul = el("ul", "", "lms-res");
    for (const r of w.readings) {
      const li = el("li");
      li.append(el("span", "Read", "lms-chip"), link(r.title, r.url), el("span", [r.pages, r.book].filter(Boolean).join(" · "), "muted lms-small"));
      ul.append(li);
    }
    for (const r of w.extras) {
      const li = el("li");
      li.append(el("span", /trip/i.test(r.kind || "") ? "Trip" : /video/i.test(r.kind || "") ? "Video" : "Link", "lms-chip"), link(r.title, r.url), el("span", r.provider || "", "muted lms-small"));
      ul.append(li);
    }
    return ul;
  }

  function dayRow(d, w, i) {
    const li = el("li", "", "lms-row" + (d.done ? " is-done" : ""));
    const canMark = ctx.me.role === "parent" || d.date <= ctx.today;
    const btn = el("button", d.done ? "✓" : "", "lms-check");
    btn.type = "button";
    btn.setAttribute("aria-pressed", String(d.done));
    btn.setAttribute("aria-label", `${d.done ? "Mark not done" : "Mark done"}: ${L.day(d.date)}`);
    btn.disabled = !canMark;
    btn.onclick = async () => {
      btn.disabled = true;
      try {
        await L.json("/api/family/completion", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ student_id: ctx.student.id, date: d.date, subject: d.subject, completed: !d.done }) });
        await L.loadProgress(ctx);
        refresh();
        render(true);
      } catch (e) {
        $("status").textContent = e.message;
        btn.disabled = false;
      }
    };
    const label = el("div", "", "lms-row-main");
    label.append(el("strong", `Lesson ${i + 1}`), el("span", ` · ${L.day(d.date)}`, "muted"));
    if (d.date === ctx.today) label.append(el("span", "Today", "lms-chip lms-chip-now"));
    li.append(btn, label, link("Open lesson", L.agendaUrl(ctx, d.date), "lms-open"));
    return li;
  }

  function weekBlock(w) {
    const sec = el("section", "", "lms-week");
    const head = el("div", "", "lms-week-head");
    head.append(el("h4", `Week ${w.week}: ${w.topic}`), el("p", `${L.fmt(w.start)}–${L.fmt(w.end)}${w.unit ? " · " + w.unit : ""} · ${w.done}/${w.days.length} done`, "muted lms-small"));
    sec.append(head);
    const ul = el("ul", "", "lms-rows");
    w.days.forEach((d, i) => ul.append(dayRow(d, w, i)));
    for (const a of w.assessments) {
      const li = el("li", "", "lms-row lms-row-test");
      const lab = el("div", "", "lms-row-main");
      lab.append(el("strong", L.assessLabel(a.id)), el("span", ` · ${L.day(a.date)}`, "muted"));
      li.append(el("span", "", "lms-check lms-check-test"), lab, link("Student PDF", `/assessments/${a.id}-student.pdf`, "lms-open"));
      ul.append(li);
    }
    sec.append(ul);
    if (w.readings.length || w.extras.length) {
      const d = el("details", "", "lms-details");
      d.append(el("summary", `Readings & resources (${w.readings.length + w.extras.length})`), resourceList(w));
      sec.append(d);
    }
    return sec;
  }

  function viewModules(root) {
    const st = L.stats(mods, ctx.today);
    for (const m of mods) {
      const d = el("details", "", "lms-module");
      d.open = st.current ? st.current.module === m.module : m === mods[0];
      const s = el("summary");
      s.append(el("span", `Module ${m.module}`, "lms-module-title"), el("span", `${m.done}/${m.total} lessons`, "muted lms-small"));
      d.append(s, L.bar(m.done, m.total));
      for (const w of m.weeks) d.append(weekBlock(w));
      root.append(d);
    }
  }

  function viewHome(root) {
    const st = L.stats(mods, ctx.today);
    const banner = el("section", "", "lms-banner");
    banner.dataset.subject = course.subject;
    banner.append(el("p", `GRADE ${course.grade}`, "eyebrow"), el("h2", course.name), L.bar(st.done, st.total), el("p", `${st.done} of ${st.total} lessons done`, "muted lms-small"));
    root.append(banner);

    const grid = el("div", "", "lms-two");
    const next = el("section", "", "card");
    next.append(el("p", "UP NEXT", "eyebrow"));
    if (st.next) {
      const w = mods.flatMap((m) => m.weeks).find((x) => x.days.some((d) => d.date === st.next.date));
      next.append(el("h3", w.topic), el("p", `${L.day(st.next.date)} · Module ${w.module}, Week ${w.week}${w.unit ? " · " + w.unit : ""}`, "muted"));
      const row = el("p", "", "lms-actions");
      row.append(link("Open lesson", L.agendaUrl(ctx, st.next.date), "lms-btn"));
      if (ctx.me.role === "parent") row.append(link("Lesson guide & printing", `/daily-print?date=${st.next.date}&grade=${course.grade}`, "lms-btn lms-btn-2"));
      next.append(row);
    } else next.append(el("p", "All lessons in this course are done.", "muted"));
    grid.append(next);

    const soon = el("section", "", "card");
    soon.append(el("p", "COMING UP", "eyebrow"));
    const ul = el("ul", "", "lms-list");
    const items = [];
    for (const m of mods) for (const w of m.weeks) for (const a of w.assessments) if (a.date >= ctx.today) items.push({ date: a.date, text: `${L.assessLabel(a.id)} · Module ${w.module}`, kind: "Test" });
    for (const e of ctx.events) if (e.date >= ctx.today && (e.grade === "both" || String(e.grade) === String(course.grade))) items.push({ date: e.date, text: e.title, kind: e.type === "field trip" ? "Trip" : "Event" });
    items.sort((a, b) => a.date.localeCompare(b.date));
    for (const it of items.slice(0, 5)) {
      const li = el("li");
      li.append(el("span", it.text), el("span", L.day(it.date), "muted lms-small"), el("span", it.kind, "lms-chip"));
      ul.append(li);
    }
    if (!items.length) ul.append(el("li", "Nothing scheduled.", "muted"));
    soon.append(ul);
    grid.append(soon);
    root.append(grid);

    if (st.current) {
      const cur = el("section", "", "card");
      cur.append(el("p", `THIS WEEK · MODULE ${st.current.module}, WEEK ${st.current.week}`, "eyebrow"), el("h3", st.current.topic));
      if (st.current.unit) cur.append(el("p", st.current.unit, "muted"));
      if (st.current.readings.length || st.current.extras.length) cur.append(resourceList(st.current));
      root.append(cur);
    }
  }

  function viewResources(root) {
    const groups = new Map();
    const seen = new Set();
    const add = (g, item) => {
      const k = g + "|" + item.url;
      if (seen.has(k)) return;
      seen.add(k);
      if (!groups.has(g)) groups.set(g, []);
      groups.get(g).push(item);
    };
    for (const m of mods) for (const w of m.weeks) {
      for (const r of w.readings) add("Books & readings", { title: r.book, url: r.url.split("#")[0], note: `Module ${w.module}, Week ${w.week}` });
      for (const r of w.extras) add(/trip/i.test(r.kind || "") ? "Field trips" : /video/i.test(r.kind || "") ? "Videos" : "Worksheets & activities", { title: r.title, url: r.url, note: `${r.provider || ""} · Module ${w.module}, Week ${w.week}` });
    }
    for (const [g, items] of [...groups.entries()].sort((a, b) => a[0].localeCompare(b[0]))) {
      const card = el("section", "", "card");
      card.append(el("h3", `${g} (${items.length})`));
      const ul = el("ul", "", "lms-res");
      for (const it of items) {
        const li = el("li");
        li.append(link(it.title, it.url), el("span", it.note, "muted lms-small"));
        ul.append(li);
      }
      card.append(ul);
      root.append(card);
    }
    if (!groups.size) root.append(el("p", "No resources are linked to this course yet.", "muted"));
  }

  function render(keepScroll) {
    const tab = ["home", "modules", "resources"].includes(location.hash.slice(1)) ? location.hash.slice(1) : "home";
    for (const a of document.querySelectorAll(".lms-menu [data-tab]")) if (a.dataset.tab === tab) a.setAttribute("aria-current", "page"); else a.removeAttribute("aria-current");
    const y = scrollY;
    const root = $("lmsView");
    root.replaceChildren();
    ({ home: viewHome, modules: viewModules, resources: viewResources })[tab](root);
    if (keepScroll) scrollTo(0, y);
  }

  (async () => {
    try {
      ctx = await L.load();
      const subject = params.get("subject");
      course = L.courses(ctx).find((c) => c.subject === subject);
      if (!course) { $("status").textContent = "That course isn't available for this student."; return; }
      document.title = `${course.name} · VenvLearning`;
      $("courseTitle").textContent = course.name;
      $("crumb").textContent = `GRADE ${course.grade} · ${ctx.student.display_name.toUpperCase()}`;
      const q = ctx.me.role === "parent" ? `?student=${encodeURIComponent(ctx.student.id)}` : "";
      for (const a of document.querySelectorAll(".lms-menu [data-tab]")) a.href = `${location.pathname}${location.search}${a.getAttribute("href")}`;
      document.querySelector(".lms-back").href = "/courses" + q;
      if (ctx.me.role === "parent") { const s = $("menuSyllabus"); s.hidden = false; s.href = "/syllabus"; }
      $("status").textContent = "";
      refresh();
      render();
      window.addEventListener("hashchange", () => render());
    } catch (e) {
      $("status").textContent = e.message;
    }
  })();
})();
