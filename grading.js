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
    for (const h of ["Course", "Daily work", "Quizzes", "Tests", "Projects", "Overall", "Letter", "Graded"]) hr.append(el("th", h));
    thead.append(hr);
    const tbody = el("tbody");
    const rows = [["Course", "Daily work %", "Quizzes %", "Tests %", "Projects %", "Overall %", "Letter", "Items graded"]];
    let sum = 0, n = 0;
    const cell = (c) => (c ? `${L.pct1(c.pct)}%` : "–");
    for (const c of courses) {
      const g = L.courseGrade(ctx, c.subject);
      const tr = el("tr");
      const th = el("td"); const a = el("a", c.name); a.href = L.courseUrl(ctx, c, "#grades"); th.append(a);
      tr.append(th, el("td", cell(g.byCat.work), "num"), el("td", cell(g.byCat.quiz), "num"), el("td", cell(g.byCat.test), "num"), el("td", cell(g.byCat.project), "num"), el("td", g.pct === null ? "–" : `${L.pct1(g.pct)}%`, "num"), el("td", g.letter || "–"), el("td", String(g.n), "num"));
      tbody.append(tr);
      rows.push([c.name, cell(g.byCat.work), cell(g.byCat.quiz), cell(g.byCat.test), cell(g.byCat.project), g.pct === null ? "" : L.pct1(g.pct), g.letter, g.n]);
      if (g.pct !== null) { sum += g.pct; n++; }
    }
    table.append(thead, tbody);
    root.append(table);
    root.append(el("p", n ? `Average across graded courses: ${L.pct1(sum / n)}% (${L.letter(ctx, sum / n)})` : "No grades entered yet. Use the To grade tab.", "muted"));
    const w = ctx.config.weights;
    root.append(el("p", `Weights: daily work ${w.work}%, quizzes ${w.quiz}%, tests ${w.test}%, projects ${w.project ?? 0}%. Change them on the Settings tab.`, "muted lms-small"));
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
      if (i.assignment) { const sub = i.assignment.submissions?.[0]; const a = el("a", sub?.status === "submitted" ? "View turned-in work" : "Open assignment", "lms-small"); a.href = `/assignments?student=${encodeURIComponent(ctx.student.id)}#a${i.assignment.id}`; main.append(el("br"), a); }
      li.append(main, L.gradeEditor(ctx, i, render));
      list.append(li);
    }
    root.append(list);
  }

  // Category weights, default "out of" values and the letter scale, saved for the whole family.
  function settings(root) {
    const cfg = ctx.config, cats = [["work", "Daily work"], ["quiz", "Quizzes"], ["test", "Tests"], ["project", "Projects"]];
    root.append(el("h2", "Grading settings"));
    root.append(el("p", "Weights are rescaled over the categories that have grades, so a course with no projects yet is not penalized. These settings apply to every student.", "muted"));
    const form = el("form", "", "card lms-settings");
    const table = el("table", "", "lms-gb lms-settings-table");
    const head = el("tr"); for (const h of ["Category", "Weight (%)", "Default “out of”"]) head.append(el("th", h));
    const thead = el("thead"); thead.append(head);
    const tbody = el("tbody"); const inputs = {};
    for (const [k, name] of cats) {
      const tr = el("tr"), w = el("input"), d = el("input");
      for (const [i, v, lab] of [[w, cfg.weights[k] ?? 0, `${name} weight`], [d, cfg.defaultPossible[k] ?? 10, `${name} default points`]]) { i.type = "number"; i.min = "0"; i.max = i === w ? "100" : "1000"; i.step = "any"; i.value = v; i.required = true; i.setAttribute("aria-label", lab); }
      inputs[k] = { w, d };
      const c1 = el("td"); c1.append(w); const c2 = el("td"); c2.append(d);
      tr.append(el("th", name), c1, c2); tbody.append(tr);
    }
    table.append(thead, tbody);
    const total = el("p", "", "muted lms-small");
    const sum = () => { const t = cats.reduce((n, [k]) => n + (Number(inputs[k].w.value) || 0), 0); total.textContent = `Weights add up to ${Math.round(t * 10) / 10}%. They don't need to total 100; each counts in proportion.`; };
    for (const [k] of cats) inputs[k].w.oninput = sum; sum();
    form.append(el("h3", "Categories"), table, total, el("h3", "Letter scale"));
    const scale = el("div", "", "lms-scale"); const rows = [];
    const addRow = (min = "", letter = "") => {
      const r = el("div", "", "lms-scale-row"), m = el("input"), l = el("input"), x = el("button", "Remove", "secondary lms-small");
      m.type = "number"; m.min = "0"; m.max = "100"; m.step = "any"; m.value = min; m.setAttribute("aria-label", "Minimum percent"); m.required = true;
      l.maxLength = 3; l.value = letter; l.setAttribute("aria-label", "Letter"); l.required = true; l.className = "lms-letter";
      x.type = "button"; x.onclick = () => { if (rows.length > 2) { r.remove(); rows.splice(rows.indexOf(r), 1); } };
      r.append(l, el("span", "at or above"), m, el("span", "%"), x); r._m = m; r._l = l; rows.push(r); scale.append(r);
    };
    for (const [min, letter] of cfg.scale) addRow(min, letter);
    const more = el("button", "Add a letter (e.g., B+)", "secondary"); more.type = "button"; more.onclick = () => addRow();
    const save = el("button", "Save settings"); save.type = "submit";
    const reset = el("button", "Restore defaults", "secondary"); reset.type = "button";
    const msg = el("p", "", "lms-small"); msg.setAttribute("role", "status");
    const actions = el("div", "", "lms-actions"); actions.append(save, reset);
    form.append(scale, more, actions, msg);
    const post = (payload) => L.json("/api/family/settings/grading", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(payload) });
    form.onsubmit = async (e) => {
      e.preventDefault(); save.disabled = true; msg.textContent = "Saving…";
      const payload = { weights: {}, defaultPossible: {}, scale: rows.map((r) => [Number(r._m.value), r._l.value.trim()]) };
      for (const [k] of cats) { payload.weights[k] = Number(inputs[k].w.value); payload.defaultPossible[k] = Number(inputs[k].d.value); }
      try { const r = await post(payload); ctx.config = { ...ctx.config, ...r.grading }; msg.textContent = "Saved. Grades everywhere now use these settings."; render(); } catch (err) { msg.textContent = err.message.includes("400") ? "Check the numbers: weights 0–100 with at least one above zero, and a letter for every row." : err.message; } finally { save.disabled = false; }
    };
    reset.onclick = async () => { reset.disabled = true; try { await post({ reset: true }); location.reload(); } catch (err) { msg.textContent = err.message; reset.disabled = false; } };
    root.append(form);
  }

  function render() {
    $("tabBook").setAttribute("aria-pressed", String(tab === "book"));
    $("tabQueue").setAttribute("aria-pressed", String(tab === "queue"));
    $("tabSettings").setAttribute("aria-pressed", String(tab === "settings"));
    const root = $("view");
    const y = scrollY;
    root.replaceChildren();
    ({ book: gradebook, queue, settings })[tab](root);
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
      $("tabSettings").onclick = () => { tab = "settings"; render(); };
      if (location.hash === "#settings") tab = "settings";
      render();
    } catch (e) {
      $("status").textContent = e.message;
    }
  })();
})();
