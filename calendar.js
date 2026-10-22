(() => {
  const L = window.LMS, { el } = L;
  const $ = (id) => document.getElementById(id);
  let ctx, month, selected;

  const ymd = (y, m, d) => `${y}-${String(m + 1).padStart(2, "0")}-${String(d).padStart(2, "0")}`;
  const eventsOn = (date) => ctx.events.filter((e) => e.date === date && (e.grade === "both" || String(e.grade) === String(ctx.student.grade)));

  function dayInfo(date) {
    const rec = ctx.daily[date]?.[ctx.student.grade];
    if (!rec) return { rec: null, subjects: [], events: eventsOn(date) };
    const mapping = ctx.library.weeks[`${ctx.student.grade}-${rec.module}-${rec.week}`] || {};
    const keys = (rec.subjects || Object.keys(mapping)).filter((k) => mapping[k]);
    const subjects = keys.map((k) => ({ id: k, topic: mapping[k].topic, done: ctx.progress.has(`${date}|${k}`) }));
    return { rec, subjects, events: eventsOn(date), mapping };
  }

  function renderDetail() {
    const box = $("calDetail");
    box.replaceChildren();
    if (!selected) { box.append(el("p", "Select a day to see its lessons.", "muted")); return; }
    const info = dayInfo(selected);
    box.append(el("p", L.day(selected).toUpperCase(), "eyebrow"));
    if (!info.rec) box.append(el("h3", "No school"), el("p", new Date(selected + "T12:00:00Z").getUTCDay() % 6 === 0 ? "Weekend." : "Not a scheduled school day.", "muted"));
    else {
      box.append(el("h3", `Module ${info.rec.module} · Week ${info.rec.week}`));
    }
    const as = L.assessOn(ctx, selected);
    if (as) box.append(el("p", `${L.assessLabel(as)} today`, "lms-strong"));
    for (const e of info.events) {
      const p = el("div", "", "cal-event");
      p.append(el("strong", `${e.type}: ${e.title}`));
      if (e.note) p.append(el("p", e.note, "muted lms-small"));
      box.append(p);
    }
    if (info.subjects.length) {
      const ul = el("ul", "", "lms-list");
      for (const s of info.subjects) {
        const li = el("li");
        li.append(el("span", `${s.done ? "✓ " : ""}${L.NAMES[s.id] || s.id}: ${s.topic || "Review / project"}`), el("span", s.done ? "Done" : "", "lms-chip"));
        if (!s.done) li.lastChild.hidden = true;
        ul.append(li);
      }
      box.append(ul);
      const actions = el("p", "", "lms-actions");
      const a = el("a", "Open lessons", "lms-btn"); a.href = L.agendaUrl(ctx, selected); actions.append(a);
      if (ctx.me.role === "parent") { const b = el("a", "Guide & printing", "lms-btn lms-btn-2"); b.href = `/daily-print?date=${selected}&grade=${ctx.student.grade}`; actions.append(b); }
      box.append(actions);
    }
  }

  function render() {
    const [y, m] = month;
    $("calTitle").textContent = new Date(Date.UTC(y, m, 1, 12)).toLocaleDateString("en-US", { timeZone: "UTC", month: "long", year: "numeric" });
    const grid = $("calGrid");
    grid.replaceChildren();
    for (const d of ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]) { const h = el("div", d, "cal-dow"); h.setAttribute("role", "columnheader"); grid.append(h); }
    const first = new Date(Date.UTC(y, m, 1, 12)).getUTCDay();
    const days = new Date(Date.UTC(y, m + 1, 0, 12)).getUTCDate();
    for (let i = 0; i < first; i++) grid.append(el("div", "", "cal-cell cal-empty"));
    for (let d = 1; d <= days; d++) {
      const date = ymd(y, m, d);
      const info = dayInfo(date);
      const cell = el("button", "", "cal-cell" + (info.rec ? " has-school" : "") + (date === ctx.today ? " is-today" : "") + (date === selected ? " is-selected" : ""));
      cell.type = "button";
      cell.setAttribute("role", "gridcell");
      cell.setAttribute("aria-label", `${L.day(date)}${info.rec ? ", school day" : ""}${info.events.length ? ", " + info.events.map((e) => e.title).join(", ") : ""}`);
      cell.append(el("span", String(d), "cal-num"));
      if (info.rec) {
        const done = info.subjects.filter((s) => s.done).length;
        if (info.subjects.length) cell.append(el("span", `${done}/${info.subjects.length} done`, "cal-meta"));
      }
      const as = L.assessOn(ctx, date);
      if (as) cell.append(el("span", L.assessLabel(as), "cal-tag cal-test"));
      for (const e of info.events) cell.append(el("span", e.type === "field trip" ? "Field trip" : e.title, "cal-tag cal-trip"));
      cell.onclick = () => { selected = date; render(); };
      grid.append(cell);
    }
    renderDetail();
    const dates = Object.keys(ctx.daily).sort();
    $("calPrev").disabled = ymd(y, m, 1) <= dates[0].slice(0, 8) + "01";
    $("calNext").disabled = ymd(y, m, days) >= dates[dates.length - 1];
  }

  function shift(delta) {
    let [y, m] = month;
    m += delta;
    if (m < 0) { m = 11; y--; } else if (m > 11) { m = 0; y++; }
    month = [y, m];
    render();
  }

  function ics() {
    const esc = (t) => String(t).replace(/([,;\\])/g, "\\$1").replace(/\n/g, "\\n");
    const nextDay = (d) => { const x = new Date(d + "T12:00:00Z"); x.setUTCDate(x.getUTCDate() + 1); return x.toISOString().slice(0, 10).replaceAll("-", ""); };
    const lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//VenvLearning//Calendar//EN", "CALSCALE:GREGORIAN"];
    const add = (date, title, note, id) => lines.push("BEGIN:VEVENT", `UID:${id}@venvlearning`, `DTSTAMP:${ctx.today.replaceAll("-", "")}T000000Z`, `DTSTART;VALUE=DATE:${date.replaceAll("-", "")}`, `DTEND;VALUE=DATE:${nextDay(date)}`, `SUMMARY:${esc(title)}`, ...(note ? [`DESCRIPTION:${esc(note)}`] : []), "END:VEVENT");
    for (const date of Object.keys(ctx.daily).sort()) {
      const rec = ctx.daily[date]?.[ctx.student.grade], as = L.assessOn(ctx, date);
      if (as) add(date, `${ctx.student.display_name}: ${L.assessLabel(as)} (Module ${rec?.module ?? ""})`, "", `${ctx.student.id}-a-${date}`);
    }
    for (const e of ctx.events) if (e.grade === "both" || String(e.grade) === String(ctx.student.grade)) add(e.date, `${e.type}: ${e.title}`, e.note, `e-${e.date}-${e.title.length}`);
    lines.push("END:VCALENDAR");
    const a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([lines.join("\r\n")], { type: "text/calendar" }));
    a.download = `venvlearning-${ctx.student.display_name.replace(/\W+/g, "-")}.ics`;
    a.click();
    URL.revokeObjectURL(a.href);
  }

  (async () => {
    try {
      ctx = await L.load();
      $("status").textContent = "";
      const dates = Object.keys(ctx.daily).sort();
      const start = ctx.today < dates[0] ? dates[0] : ctx.today > dates[dates.length - 1] ? dates[dates.length - 1] : ctx.today;
      month = [Number(start.slice(0, 4)), Number(start.slice(5, 7)) - 1];
      selected = start;
      $("lmsSwitch").append(L.studentSwitcher(ctx, (id) => { const u = new URL(location.href); u.searchParams.set("student", id); location.href = u; }) || "");
      $("calPrev").onclick = () => shift(-1);
      $("calNext").onclick = () => shift(1);
      $("calToday").onclick = () => { month = [Number(start.slice(0, 4)), Number(start.slice(5, 7)) - 1]; selected = start; render(); };
      $("calIcs").onclick = ics;
      render();
    } catch (e) {
      $("status").textContent = e.message;
    }
  })();
})();
