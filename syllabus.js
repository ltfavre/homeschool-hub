(() => {
  const $ = (id) => document.getElementById(id);
  const el = (tag, text = "", cls = "") => {
    const n = document.createElement(tag);
    if (text) n.textContent = text;
    if (cls) n.className = cls;
    return n;
  };
  const SUBJECTS = [["math", "Math"], ["ela", "ELA"], ["science", "Science"], ["social", "Social Studies"]];
  const EXTRA = [["art", "Art"], ["life", "Human Sciences"], ["computer", "Computer Science"], ["skills", "Life Skills"]];
  const fmt = (iso, opts = { month: "short", day: "numeric" }) =>
    new Date(iso + "T12:00:00Z").toLocaleDateString("en-US", { timeZone: "UTC", ...opts });
  let daily, library, events = [], today = "";

  async function json(path) {
    const r = await fetch(path);
    if (r.status === 401 || r.redirected) { location.replace("/login"); throw new Error("Please sign in."); }
    if (!r.ok) throw new Error(`Could not load ${path} (${r.status})`);
    return r.json();
  }

  function unitName(mapping, subject) {
    const readings = mapping?.[subject]?.readings || [];
    for (const r of readings) {
      const title = library.resources[r.resource_id]?.title || "";
      const m = title.match(/^Unit\s+\d+\s+-\s+(.+?)\s+-\s+(?:Student|Core|Activity|Teacher|Alignment)/i);
      if (m) return m[1];
    }
    const first = library.resources[readings[0]?.resource_id]?.title;
    return first ? first.replace(/\s+-\s+(Full )?Student.*$/i, "") : "";
  }

  function buildWeeks(grade) {
    const weeks = new Map();
    for (const date of Object.keys(daily).sort()) {
      const rec = daily[date]?.[grade];
      if (!rec) continue;
      const key = `${rec.module}-${rec.week}`;
      if (!weeks.has(key)) weeks.set(key, { module: rec.module, week: rec.week, days: [], elective: rec.elective, active_subjects: rec.subjects });
      weeks.get(key).days.push({ date, assessment: rec.assessment, subjects:rec.subjects });
    }
    return [...weeks.values()].map((w) => {
      const mapping = library.weeks[`${grade}-${w.module}-${w.week}`] || {};
      w.start = w.days[0].date;
      w.end = w.days[w.days.length - 1].date;
      w.mapping = mapping;w.active_subjects=new Set(w.days.flatMap(d=>d.subjects||[]));
      w.assessments = w.days.filter((d) => d.assessment).map((d) => ({ date: d.date, id: d.assessment }));
      return w;
    });
  }

  function assessLabel(a) {
    if (/-test$/.test(a.id)) return "Module test";
    if (/-w\d-quiz$/.test(a.id)) return "Weekly quiz";
    return "Assessment";
  }

  function render() {
    const grade = $("sylGrade").value;
    const weeks = buildWeeks(grade);
    const current = weeks.find((w) => today >= w.start && today <= w.end) || weeks.find((w) => w.start > today);
    const idx = weeks.indexOf(current);
    const evs = events.filter((e) => e.grade === "both" || String(e.grade) === grade).sort((a, b) => a.date.localeCompare(b.date));

    // Where are we now
    const now = $("sylNow");
    now.replaceChildren(el("p", `GRADE ${grade} · WHERE WE ARE`, "eyebrow"));
    const grid = el("div", "", "syl-now-grid");
    const block = (label, w) => {
      const b = el("div", "", "syl-now-block");
      b.append(el("h3", label));
      if (!w) { b.append(el("p", "Nothing scheduled.", "muted")); return b; }
      b.append(el("p", `Module ${w.module} · Week ${w.week} · ${fmt(w.start)}–${fmt(w.end)}`, "syl-strong"));
      const ul = el("ul");
      for (const [id, name] of SUBJECTS) {
        const t = w.mapping[id]?.topic;
        if (t) { const unit = unitName(w.mapping, id); ul.append(el("li", `${name}: ${t}${unit ? " (" + unit + ")" : ""}`)); }
      }
      if(w.elective)ul.append(el("li",`Elective: ${w.elective.title} · ${w.elective.topic} · week ${w.elective.week}/6`));b.append(ul);
      if (w.assessments.length) b.append(el("p", w.assessments.map((a) => `${assessLabel(a)} ${fmt(a.date, { weekday: "short", month: "short", day: "numeric" })}`).join(" · "), "syl-test"));
      return b;
    };
    grid.append(block(today >= (current?.start || "") ? "This week" : "Starts soon", current), block("Next week", weeks[idx + 1]));
    const upcoming = [];
    for (const w of weeks) for (const a of w.assessments) if (a.date >= today && /-test$/.test(a.id)) upcoming.push(`Module ${w.module} test — ${fmt(a.date, { weekday: "short", month: "short", day: "numeric" })}`);
    for (const e of evs) if (e.date >= today) upcoming.push(`${e.type}: ${e.title} — ${fmt(e.date, { weekday: "short", month: "short", day: "numeric" })}`);
    const up = el("div", "", "syl-now-block");
    up.append(el("h3", "Coming up"));
    const ul = el("ul");
    for (const u of upcoming.slice(0, 5)) ul.append(el("li", u));
    if (!upcoming.length) ul.append(el("li", "Friday taught-work checks and the active elective continue. No additional events scheduled."));
    up.append(ul);
    grid.append(up);
    now.append(grid);

    // Module overview
    const modWrap = $("sylModules");
    modWrap.replaceChildren(el("h2", `Grade ${grade} · Year at a glance`));
    const table = el("table", "", "syl-table");
    const head = el("tr");
    for (const h of ["Module", "Dates", "Module test", "Units"]) head.append(el("th", h));
    const th1 = el("thead"); th1.append(head); table.append(th1);
    const body = el("tbody");
    const mods = [...new Set(weeks.map((w) => w.module))];
    for (const m of mods) {
      const ws = weeks.filter((w) => w.module === m);
      const test = ws.flatMap((w) => w.assessments).find((a) => /-test$/.test(a.id));
      const tr = el("tr");
      if (current && current.module === m) tr.className = "is-now";
      tr.append(el("td", `Module ${m}`), el("td", `${fmt(ws[0].start)} – ${fmt(ws[ws.length - 1].end)}`),
        el("td", test ? fmt(test.date, { weekday: "short", month: "short", day: "numeric" }) : "—"));
      const units = el("td");
      for (const [id, name] of SUBJECTS) {
        const names = [...new Set(ws.map((w) => unitName(w.mapping, id)).filter(Boolean))];
        if (names.length) units.append(el("div", `${name}: ${names.join("; ")}`));
      }
      tr.append(units);
      body.append(tr);
    }
    table.append(body);
    modWrap.append(table);

    // Week by week
    const wk = $("sylWeeks");
    wk.replaceChildren(el("h2", `Grade ${grade} · Week by week`));
    const t2 = el("table", "", "syl-table syl-weeks");
    const h2 = el("tr");
    for (const h of ["Week", "Dates", ...SUBJECTS.map((s) => s[1]), "Elective / Friday checks / events"]) h2.append(el("th", h));
    const th2 = el("thead"); th2.append(h2); t2.append(th2);
    const b2 = el("tbody");
    let prevEnd = "";
    for (const w of weeks) {
      if (prevEnd) {
        const gap = (new Date(w.start) - new Date(prevEnd)) / 86400000;
        if (gap > 4) {
          const br = el("tr", "", "syl-break");
          const td = el("td", `Break · ${fmt(prevEnd)} → ${fmt(w.start)} (no school days scheduled)`);
          td.colSpan = 7;
          br.append(td);
          b2.append(br);
        }
      }
      prevEnd = w.end;
      const tr = el("tr");
      if (w === current) tr.className = "is-now";
      tr.append(el("td", `M${w.module} · W${w.week}`), el("td", `${fmt(w.start)}–${fmt(w.end)}`));
      for (const [id] of SUBJECTS) {
        const td = el("td");
        const t = w.mapping[id]?.topic;
        if (t) {
          td.append(el("div", t, "syl-topic"));
          const unit = unitName(w.mapping, id);
          if (unit) td.append(el("div", unit, "syl-unit"));
        }
        tr.append(td);
      }
      const notes = el("td");if(w.elective)notes.append(el("div",`${w.elective.title} · week ${w.elective.week}/6: ${w.elective.topic}`),el("div","Friday: taught-work check + elective reflection"));
      for (const a of w.assessments) notes.append(el("div", `${assessLabel(a)} · ${fmt(a.date, { weekday: "short", month: "short", day: "numeric" })}`, "syl-test"));
      for (const e of evs.filter((e) => e.date >= w.start && e.date <= w.end)) notes.append(el("div", `${e.type}: ${e.title} · ${fmt(e.date, { weekday: "short", month: "short", day: "numeric" })}`, "syl-event"));
      tr.append(notes);
      b2.append(tr);
    }
    t2.append(b2);
    wk.append(t2);

    // Notes: other subjects
    const notes = $("sylNotes");
    notes.replaceChildren(el("h2", "Rotating electives"),
      el("p", "From October 26, one elective meets Monday–Thursday in six-instructional-week blocks. Art & Art History is first. Daily guides list the active course and exact pages; inactive electives are not assigned or tested."));
    const ex = el("p", "", "muted");
    ex.textContent = `From October 26, Fridays check taught Math and ELA plus the active elective, with projects, field trips, independent study or catch-up. Daily Math and ELA replace the earlier alternating foundation schedule. Field trips, projects and no-school days appear above once they are added to school-events.json.`;
    notes.append(ex);
    $("status").textContent = `Grade ${grade}: ${weeks.length} weeks, ${weeks[0] ? fmt(weeks[0].start, { month: "short", day: "numeric", year: "numeric" }) : ""} to ${weeks.length ? fmt(weeks[weeks.length - 1].end, { month: "short", day: "numeric", year: "numeric" }) : ""}.`;
  }

  async function init() {
    try {
      const me = await json("/api/family/me");
      if (me.user.role !== "parent") { location.replace("/agenda"); return; }
      today = me.today;
      [daily, library] = await Promise.all([json("/daily-packets.json"), json("/planner-resources.json")]);
      try { events = (await json("/school-events.json")).events || []; } catch { events = []; }
      $("sylGrade").onchange = render;
      $("sylPrint").onclick = () => window.print();
      render();
    } catch (e) {
      $("status").textContent = e.message;
    }
  }
  init();
})();
