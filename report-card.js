(() => {
  const L = window.LMS, { el } = L;
  const $ = (id) => document.getElementById(id);
  let ctx, att = new Map();

  const days = () => Object.keys(ctx.daily).filter((d) => ctx.daily[d]?.[ctx.student.grade]).sort();

  function periods() {
    const g = ctx.student.grade, first = new Map();
    for (const d of days()) { const m = ctx.daily[d][g].module; const x = first.get(m) || { from: d, to: d }; x.to = d; first.set(m, x); }
    const out = [{ id: "year", label: "Year to date", from: days()[0], to: ctx.today }];
    for (const [m, r] of first) if (r.from <= ctx.today) out.push({ id: "m" + m, label: `Module ${m} (${L.fmt(r.from)}–${L.fmt(r.to)})`, from: r.from, to: r.to });
    return out;
  }

  function render(period) {
    const range = { from: period.from, to: period.to };
    $("rcWho").textContent = `${ctx.student.display_name} · Grade ${ctx.student.grade}`;
    $("rcWhen").textContent = `School year 2026–27 · ${period.id === "year" ? "Year to date through " + L.fmt(ctx.today, { month: "long", day: "numeric", year: "numeric" }) : period.label}`;
    const tbody = $("rcRows");
    tbody.replaceChildren();
    let sum = 0, n = 0;
    const cell = (c) => (c ? `${L.pct1(c.pct)}%` : "–");
    for (const c of L.courses(ctx)) {
      const g = L.courseGrade(ctx, c.subject, range);
      const tr = el("tr");
      tr.append(el("td", c.name), el("td", cell(g.byCat.work), "num"), el("td", cell(g.byCat.quiz), "num"), el("td", cell(g.byCat.test), "num"), el("td", g.pct === null ? "Not graded" : `${L.pct1(g.pct)}%`, "num"), el("td", g.letter || "–"));
      tbody.append(tr);
      if (g.pct !== null) { sum += g.pct; n++; }
    }
    $("rcAvg").textContent = n ? `Overall average: ${L.pct1(sum / n)}% (${L.letter(ctx, sum / n)}) across ${n} graded course${n === 1 ? "" : "s"}.` : "No grades have been entered for this period.";
    const sched = days().filter((d) => d >= range.from && d <= range.to && d <= ctx.today);
    const rows = sched.map((d) => att.get(d)).filter(Boolean);
    const attended = rows.filter((r) => r.s !== "absent").length, absent = rows.filter((r) => r.s === "absent").length;
    const hours = rows.reduce((a, r) => a + (r.h || 0), 0);
    $("rcAtt").textContent = rows.length ? `${attended} day${attended === 1 ? "" : "s"} attended, ${absent} absent, out of ${sched.length} scheduled school days${hours ? `. ${L.pct1(hours)} hours logged.` : "."}${rows.length < sched.length ? ` (${sched.length - rows.length} days not yet recorded.)` : ""}` : "No attendance recorded for this period.";
    const w = ctx.config.weights;
    $("rcScale").textContent = `Grading scale: ${ctx.config.scale.map(([min, l], i) => `${l} ${i === 0 ? min + "%+" : min + "%+"}`).join(", ")}. Course grade weights: daily work ${w.work}%, quizzes ${w.quiz}%, tests ${w.test}%.`;
  }

  (async () => {
    try {
      ctx = await L.load();
      if (ctx.me.role !== "parent") { location.replace("/courses"); return; }
      const data = await L.json(`/api/family/attendance?student=${encodeURIComponent(ctx.student.id)}`);
      att = new Map((data.rows || []).map((r) => [r.d, r]));
      $("status").textContent = "";
      $("rcPaper").hidden = false;
      $("lmsSwitch").append(L.studentSwitcher(ctx, (id) => { const u = new URL(location.href); u.searchParams.set("student", id); location.href = u; }) || "");
      const list = periods(), sel = $("rcPeriod");
      for (const p of list) { const o = el("option", p.label); o.value = p.id; sel.append(o); }
      sel.onchange = () => render(list.find((p) => p.id === sel.value));
      $("rcPrint").onclick = () => window.print();
      render(list[0]);
    } catch (e) {
      $("status").textContent = e.message;
    }
  })();
})();
