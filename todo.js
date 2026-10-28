// Daily to-do list: a simplified checklist of today's lessons, pages, and activities for each girl.
// Students check tasks off (saved as they go) and press "Turn in to Mom"; parents see both girls' lists and turn-in status.
(() => {
  const $ = (id) => document.getElementById(id);
  const node = (tag, text, cls) => { const e = document.createElement(tag); if (text != null) e.textContent = text; if (cls) e.className = cls; return e; };
  const pad = (n) => String(n).padStart(2, "0");
  const localDate = (d = new Date()) => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
  const longDate = (iso) => new Intl.DateTimeFormat("en-US", {weekday: "long", month: "long", day: "numeric"}).format(new Date(iso + "T12:00:00"));
  const time = (epoch) => new Intl.DateTimeFormat("en-US", {hour: "numeric", minute: "2-digit"}).format(new Date(epoch * 1000));
  const api = async (path, body) => {
    const r = await fetch(path, body ? {method: "POST", headers: {"content-type": "application/json"}, body: JSON.stringify(body)} : {cache: "no-store"});
    const data = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(data.error || "Something went wrong. Try again.");
    return data;
  };
  const params = new URLSearchParams(location.search);
  let me = null, students = [], view = null;

  function firstName(s) { return (s?.display_name || "").split(" ")[0] || "My"; }

  function render() {
    const {groups, checked, turned_in, student, date, school_day} = view;
    const done = new Set(checked);
    const total = groups.reduce((n, g) => n + g.tasks.length, 0);
    $("sheetDate").textContent = longDate(date).toUpperCase();
    $("sheetTitle").textContent = `${firstName(student)}'s To-Do List`;
    document.title = `${firstName(student)}'s To-Do · ${longDate(date)}`;
    const box = $("groups"); box.replaceChildren();
    if (!school_day || !groups.length) box.append(node("p", "No school work is scheduled for this day.", "muted"));
    for (const g of groups) {
      const sec = node("section", null, `todo-group subj-${g.subject}`);
      const meta = node("div", null, "todo-meta");
      meta.append(node("span", g.name, "todo-subject"));
      if (g.unit) meta.append(node("span", g.unit, "todo-unit"));
      sec.append(meta, node("h3", g.title || g.name));
      const ul = node("ul", null, "todo-tasks");
      for (const t of g.tasks) {
        const li = node("li", null, "todo-task" + (done.has(t.key) ? " done" : ""));
        const id = "t-" + btoa(unescape(encodeURIComponent(t.key))).replace(/[^a-z0-9]/gi, "");
        const cb = node("input"); cb.type = "checkbox"; cb.id = id; cb.checked = done.has(t.key);
        const label = node("label", t.text); label.htmlFor = id;
        cb.onchange = async () => {
          cb.disabled = true;
          try {
            await api("/api/family/todo", {date, student_id: student.id, key: t.key, checked: cb.checked});
            cb.checked ? done.add(t.key) : done.delete(t.key);
            view.checked = [...done]; li.classList.toggle("done", cb.checked); progress();
          } catch (e) { cb.checked = !cb.checked; $("status").textContent = e.message; }
          cb.disabled = false;
        };
        li.append(cb, label);
        if (t.link) { const a = node("a", "Open ↗"); a.href = t.link; a.target = "_blank"; a.rel = "noopener"; li.append(a); }
        ul.append(li);
      }
      sec.append(ul); box.append(sec);
    }
    const progress = () => {
      const n = groups.reduce((c, g) => c + g.tasks.filter((t) => done.has(t.key)).length, 0);
      $("doneCount").textContent = n; $("doneLabel").textContent = `of ${total} done`;
      $("turnIn").textContent = turned_in ? "Turn in again" : (n === total && total ? "Turn in to Mom ✓" : "Turn in to Mom");
    };
    progress();
    $("turnIn").hidden = !total;
    $("turnStatus").textContent = turned_in ? `Turned in at ${time(turned_in.turned_in_at)} · ${turned_in.done} of ${turned_in.total} done` : "";
    $("sheet").hidden = false; $("status").textContent = "";
  }

  async function overview() {
    if (me.role !== "parent") return;
    const date = $("date").value, box = $("overview"); box.hidden = false; box.replaceChildren();
    for (const s of students) {
      const v = await api(`/api/family/todo?date=${date}&student=${encodeURIComponent(s.id)}`).catch(() => null);
      const total = v ? v.groups.reduce((n, g) => n + g.tasks.length, 0) : 0;
      const chip = node("button", null, "todo-chip"); chip.type = "button"; chip.setAttribute("aria-pressed", String(s.id === $("student").value));
      const left = node("div"); left.append(node("strong", s.display_name), node("br"), node("small", v ? `${v.checked.length} of ${total} checked` : "—"));
      chip.append(left, v?.turned_in ? node("span", `Turned in ${time(v.turned_in.turned_in_at)}`, "in") : node("small", total ? "Not turned in yet" : "No school"));
      chip.onclick = () => { $("student").value = s.id; load(); };
      box.append(chip);
    }
  }

  async function load() {
    const date = $("date").value; $("status").textContent = "Loading…";
    const sid = me.role === "parent" ? `&student=${encodeURIComponent($("student").value)}` : "";
    history.replaceState(null, "", `?date=${date}${me.role === "parent" ? "&student=" + $("student").value : ""}`);
    try { view = await api(`/api/family/todo?date=${date}${sid}`); render(); }
    catch (e) { $("sheet").hidden = true; $("status").textContent = e.message; }
    overview();
  }

  $("turnIn").onclick = async () => {
    $("turnIn").disabled = true;
    try {
      const r = await api("/api/family/todo/turn-in", {date: view.date, student_id: view.student.id});
      view.turned_in = {turned_in_at: Math.floor(Date.now() / 1000), done: r.done, total: r.total};
      render(); overview();
    } catch (e) { $("status").textContent = e.message; }
    $("turnIn").disabled = false;
  };
  $("print").onclick = () => window.print();
  $("today").onclick = () => { $("date").value = localDate(); load(); };
  $("date").onchange = load;
  $("student").onchange = load;

  (async () => {
    try {
      ({user: me} = await api("/api/family/me"));
      $("date").value = params.get("date") || localDate();
      if (me.role === "parent") {
        const u = await api("/api/family/users");
        students = (u.users || u).filter((x) => x.role === "student");
        for (const s of students) { const o = node("option", s.display_name); o.value = s.id; $("student").append(o); }
        if (params.get("student")) $("student").value = params.get("student");
        $("studentLabel").hidden = false; $("print").textContent = "Print this list";
        document.querySelector(".topbar h1").textContent = "Daily To-Do Lists";
      }
      await load();
    } catch (e) { $("status").textContent = e.message; }
  })();
})();
