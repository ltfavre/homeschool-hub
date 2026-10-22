(() => {
  const L = window.LMS, { el } = L;
  const $ = (id) => document.getElementById(id);
  let ctx, tab = "book", subject = "all";

  function gradebook(root) {
    const courses = L.courses(ctx);
    root.append(el("h2", `${ctx.student.display_name} · Grade ${ctx.student.grade}`));
    const bar = el("div", "", "lms-toolbar");
    const csv = el("button", "Download CSV", "secondary"); csv.type = "button";
    const print = el("button", "Print", "secondary"); print.type = "button"; print.onclick = () => window.print();
    bar.append(csv, print);
    root.append(bar);
    const table = el("table", "", "lms-gb");
    const thead = el("thead"), hr = el("tr");
    for (const h of ["Course", "Daily work", "Quizzes", "Tests", "Overall", "Letter", "Graded"]) hr.append(el("th", h));
    thead.append(hr);
    const tbody = el("tbody");
    const rows = [["Course", "Daily work %", "Quizzes %", "Tests %", "Overall %", "Letter", "Items graded"]];
    let sum = 0, n = 0;
    const cell = (c) => (c ? `${L.pct1(c.pct)}%` : "–");
    for (const c of courses) {
      const g = L.courseGrade(ctx, c.subject);
      const tr = el("tr");
      const th = el("td"); const a = el("a", c.name); a.href = L.courseUrl(ctx, c, "#grades"); th.append(a);
      tr.append(th, el("td", cell(g.byCat.work), "num"), el("td", cell(g.byCat.quiz), "num"), el("td", cell(g.byCat.test), "num"), el("td", g.pct === null ? "–" : `${L.pct1(g.pct)}%`, "num"), el("td", g.letter || "–"), el("td", String(g.n), "num"));
      tbody.append(tr);
      rows.push([c.name, cell(g.byCat.work), cell(g.byCat.quiz), cell(g.byCat.test), g.pct === null ? "" : L.pct1(g.pct), g.letter, g.n]);
      if (g.pct !== null) { sum += g.pct; n++; }
    }
    table.append(thead, tbody);
    root.append(table);
    root.append(el("p", n ? `Average across graded courses: ${L.pct1(sum / n)}% (${L.letter(ctx, sum / n)})` : "No grades entered yet. Use the To grade tab.", "muted"));
    const w = ctx.config.weights;
    root.append(el("p", `Weights: daily work ${w.work}%, quizzes ${w.quiz}%, tests ${w.test}%. Change them in grading-config.json.`, "muted lms-small"));
    csv.onclick = () => {
      const text = rows.map((r) => r.map((v) => `"${String(v).replaceAll('"', '""')}"`).join(",")).join("\n");
      const a = document.createElement("a");
      a.href = URL.createObjectURL(new Blob([text], { type: "text/csv" }));
      a.download = `grades-${ctx.student.display_name.replace(/\W+/g, "-")}-${ctx.today}.csv`;
      a.click();
      URL.revokeObjectURL(a.href);
    };
  }

  function queue(root) {
    const courses = L.courses(ctx);
    const bar = el("div", "", "lms-toolbar");
    const label = el("label", "Course ");
    const sel = el("select");
    for (const [v, t] of [["all", "All courses"], ...courses.map((c) => [c.subject, c.name])]) { const o = el("option", t); o.value = v; o.selected = v === subject; sel.append(o); }
    sel.onchange = () => { subject = sel.value; render(); };
    label.append(sel); bar.append(label);
    root.append(bar);
    const pending = courses.filter((c) => subject === "all" || c.subject === subject).flatMap((c) => L.items(ctx, c.subject)).filter((i) => i.date <= ctx.today && !ctx.grades.has(i.key)).sort((a, b) => b.date.localeCompare(a.date) || a.subject.localeCompare(b.subject));
    root.append(el("p", `${pending.length} item${pending.length === 1 ? "" : "s"} waiting to be graded${pending.length > 40 ? " (showing the 40 most recent)" : ""}.`, "muted"));
    const list = el("ul", "", "lms-rows");
    for (const i of pending.slice(0, 40)) {
      const li = el("li", "", "lms-row lms-row-grade");
      const main = el("div", "", "lms-row-main");
      main.append(el("strong", `${L.NAMES[i.subject]}: ${i.title}`), el("span", ` · ${L.day(i.date)}`, "muted"));
      li.append(main, L.gradeEditor(ctx, i, render));
      list.append(li);
    }
    root.append(list);
  }

  function render() {
    $("tabBook").setAttribute("aria-pressed", String(tab === "book"));
    $("tabQueue").setAttribute("aria-pressed", String(tab === "queue"));
    const root = $("view");
    const y = scrollY;
    root.replaceChildren();
    (tab === "book" ? gradebook : queue)(root);
    scrollTo(0, y);
  }

  (async () => {
    try {
      ctx = await L.load();
      if (ctx.me.role !== "parent") { location.replace("/courses"); return; }
      $("status").textContent = "";
      $("lmsSwitch").append(L.studentSwitcher(ctx, (id) => { const u = new URL(location.href); u.searchParams.set("student", id); location.href = u; }) || "");
      $("tabBook").onclick = () => { tab = "book"; render(); };
      $("tabQueue").onclick = () => { tab = "queue"; render(); };
      render();
    } catch (e) {
      $("status").textContent = e.message;
    }
  })();
})();
