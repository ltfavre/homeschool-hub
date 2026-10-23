(() => {
  const L = window.LMS, F = window.VenvFiles, { el } = L;
  const $ = (id) => document.getElementById(id);
  let ctx, filter = null, library = [];
  const drafts = new Map(); // unsaved student answers survive re-renders
  const openPanels = new Set(); // grading panels the parent has open
  const post = (path, body) => L.json(path, { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(body) });
  const parent = () => ctx.me.role === "parent";
  const SUBJECTS = Object.keys(L.NAMES);
  const status = (t) => { $("status").textContent = t; };

  async function refresh() {
    await Promise.all([L.loadAssignments(ctx), L.loadGrades(ctx)]);
    render();
  }

  const FILTERS = {
    parent: [["needs", "Needs grading", (a, s) => s.code === "submitted"], ["upcoming", "Upcoming", (a, s) => a.due_date >= ctx.today && s.code !== "graded"], ["past", "Past due", (a, s) => a.due_date < ctx.today && s.code !== "graded"], ["graded", "Graded", (a, s) => s.code === "graded"], ["all", "All", () => true]],
    student: [["todo", "To do", (a, s) => ["open", "today", "late"].includes(s.code)], ["done", "Turned in", (a, s) => s.code === "submitted"], ["graded", "Graded", (a, s) => s.code === "graded"], ["all", "All", () => true]],
  };

  function stateChip(s) { return el("span", s.label, `lms-chip as-state as-${s.code}`); }

  function scoreLine(a) {
    const g = ctx.grades.get(a.key);
    if (!g) return null;
    const box = el("div", "", "as-score");
    box.append(el("strong", `Score: ${g.p} / ${g.m}`), el("span", ` (${L.pct1((g.p / g.m) * 100)}%, ${L.letter(ctx, (g.p / g.m) * 100)})`, "muted"));
    if (g.n) box.append(el("p", g.n, "as-comment"));
    return box;
  }

  function workView(sub, files) {
    const box = el("div", "", "as-work");
    if (sub?.body) box.append(el("p", sub.body, "as-body"));
    for (const f of files || []) box.append(F.link(f, el));
    if (!sub?.body && !(files || []).length) box.append(el("p", "Nothing turned in yet.", "muted"));
    return box;
  }

  // Student: write an answer, attach files, turn it in.
  function studentPanel(a, s) {
    const sub = a.submissions[0], files = sub ? sub.files : a.pending_files;
    const box = el("section", "", "as-panel");
    box.append(el("h4", "Your work"));
    if (s.code === "graded" || sub?.status === "returned") {
      box.append(workView(sub, files));
      if (sub?.feedback) { const fb = el("div", "", "as-feedback"); fb.append(el("strong", "Feedback"), el("p", sub.feedback)); box.append(fb); }
      return box;
    }
    if (!a.allow_submission) { box.append(el("p", "Hand this one in on paper, or show your work to your teacher.", "muted")); return box; }
    if (sub?.status === "submitted") {
      box.append(el("p", `Turned in ${new Date(sub.submitted_at * 1000).toLocaleString("en-US", { month: "short", day: "numeric", hour: "numeric", minute: "2-digit" })}.`, "as-ok"), workView(sub, files));
      const undo = el("button", "Unsubmit to make changes", "secondary"); undo.type = "button";
      undo.onclick = async () => { undo.disabled = true; try { await post("/api/family/submissions", { assignment_id: a.id, unsubmit: true }); await refresh(); } catch (e) { status(e.message); undo.disabled = false; } };
      box.append(undo);
      return box;
    }
    const area = el("textarea"); area.rows = 6; area.maxLength = 20000; area.placeholder = "Type your answer here (optional if you attach a file)";
    area.setAttribute("aria-label", `Your answer for ${a.title}`);
    area.value = drafts.has(a.id) ? drafts.get(a.id) : sub?.body || "";
    area.oninput = () => drafts.set(a.id, area.value);
    box.append(area);
    const list = el("div", "", "vf-list");
    for (const f of files || []) {
      const rm = el("button", "Remove", "secondary lms-small"); rm.type = "button";
      rm.onclick = async () => { rm.disabled = true; try { await post("/api/family/submissions", { assignment_id: a.id, remove_files: [f.id], unsubmit: true }); await refresh(); } catch (e) { status(e.message); } };
      list.append(F.link(f, el, rm));
    }
    box.append(list);
    const msg = el("p", "", "lms-small"); msg.setAttribute("role", "status");
    box.append(F.picker(el, async (picked) => {
      drafts.set(a.id, area.value);
      for (const file of picked) {
        msg.textContent = `Uploading ${file.name}…`;
        try { await F.upload(file, { kind: "submission", assignment_id: a.id }); } catch (e) { msg.textContent = e.message; return; }
      }
      await refresh();
    }, { label: "Attach a photo or file of your work" }), msg);
    const go = el("button", "Turn in"); go.type = "button";
    go.onclick = async () => {
      go.disabled = true; msg.textContent = "Turning in…";
      try { await post("/api/family/submissions", { assignment_id: a.id, body: area.value }); drafts.delete(a.id); await refresh(); } catch (e) { msg.textContent = /400/.test(e.message) ? "Write an answer or attach a file first." : e.message; go.disabled = false; }
    };
    const actions = el("div", "", "lms-actions"); actions.append(go); box.append(actions);
    return box;
  }

  // Parent: see the work, score it, return it with feedback.
  function gradePanel(a, s) {
    const sub = a.submissions[0];
    const d = el("details", "", "as-grade");
    d.open = openPanels.has(a.id) || s.code === "submitted" || location.hash === `#a${a.id}`;
    if (d.open) openPanels.add(a.id);
    d.ontoggle = () => (d.open ? openPanels.add(a.id) : openPanels.delete(a.id));
    d.append(el("summary", s.code === "submitted" ? "Grade turned-in work" : s.code === "graded" ? "Edit grade" : "Grade"));
    if (a.allow_submission) { d.append(el("h4", `${ctx.student.display_name}'s work`)); d.append(workView(sub, sub?.files)); }
    d.append(el("h4", "Score"), L.gradeEditor(ctx, L.assignmentItem(a), refresh));
    const fbf = el("form", "", "as-fb-form");
    const fb = el("textarea"); fb.rows = 3; fb.maxLength = 2000; fb.placeholder = "Feedback for the student (shown with the grade)"; fb.value = sub?.feedback || ""; fb.setAttribute("aria-label", "Feedback");
    const ret = el("button", sub?.status === "returned" ? "Update feedback" : "Return to student"); ret.type = "submit";
    const re = el("button", "Reopen for changes", "secondary"); re.type = "button";
    const msg = el("span", "", "lms-small muted"); msg.setAttribute("role", "status");
    fbf.onsubmit = async (e) => { e.preventDefault(); ret.disabled = true; try { await post("/api/family/submissions", { assignment_id: a.id, student_id: ctx.student.id, status: "returned", feedback: fb.value }); await refresh(); } catch (err) { msg.textContent = err.message; ret.disabled = false; } };
    re.onclick = async () => { re.disabled = true; try { await post("/api/family/submissions", { assignment_id: a.id, student_id: ctx.student.id, status: "reopen", feedback: fb.value }); await refresh(); } catch (err) { msg.textContent = err.message; re.disabled = false; } };
    const row = el("div", "", "lms-actions"); row.append(ret);
    if (sub && a.allow_submission) row.append(re);
    row.append(msg);
    fbf.append(fb, row);
    d.append(el("h4", "Feedback"), fbf);
    return d;
  }

  function card(a) {
    const s = L.assignmentState(ctx, a);
    const c = el("article", "", "card as-card");
    c.id = `a${a.id}`; c.dataset.subject = a.subject;
    const head = el("div", "", "as-head");
    const left = el("div");
    left.append(el("p", `${L.NAMES[a.subject] || a.subject} · ${L.CATEGORY_NAMES[a.category] || a.category} · ${a.points} pts`, "eyebrow"), el("h3", a.title));
    const due = el("p", "", "as-due"); due.append(el("span", `Due ${L.day(a.due_date)}`), stateChip(s));
    if (parent() && !a.published) due.append(el("span", "Hidden from student", "lms-chip as-hidden"));
    if (!a.allow_submission) due.append(el("span", "On paper", "lms-chip"));
    left.append(due);
    head.append(left);
    if (parent()) {
      const tools = el("div", "", "as-tools");
      const edit = el("button", "Edit", "secondary"); edit.type = "button"; edit.onclick = () => openEditor(a);
      const del = el("button", "Delete", "secondary"); del.type = "button";
      del.onclick = async () => { if (!confirm(`Delete “${a.title}”? This also removes its grade and any turned-in work.`)) return; del.disabled = true; try { await post("/api/family/assignments", { delete_id: a.id }); await refresh(); } catch (e) { status(e.message); del.disabled = false; } };
      tools.append(edit, del);
      head.append(tools);
    }
    c.append(head);
    if (a.instructions) c.append(el("p", a.instructions, "as-body"));
    if (a.attachments.length) { const att = el("div", "", "vf-list"); for (const f of a.attachments) att.append(F.link(f, el)); c.append(att); }
    const score = scoreLine(a); if (score) c.append(score);
    c.append(parent() ? gradePanel(a, s) : studentPanel(a, s));
    return c;
  }

  // Parent: create or edit an assignment.
  function openEditor(a = null) {
    const box = $("asNew");
    box.replaceChildren();
    const f = el("form", "", "card as-editor");
    f.append(el("h3", a ? "Edit assignment" : "New assignment"));
    const field = (label, input, cls = "") => { const l = el("label", "", "as-field " + cls); l.append(el("span", label), input); return l; };
    const title = el("input"); title.required = true; title.maxLength = 160; title.value = a?.title || "";
    const grade = el("select"); for (const s of ctx.students) { const o = el("option", `Grade ${s.grade} · ${s.display_name}`); o.value = s.grade; o.selected = String(a?.grade || ctx.student.grade) === String(s.grade); grade.append(o); }
    const subject = el("select"); for (const k of SUBJECTS) { const o = el("option", L.NAMES[k]); o.value = k; o.selected = (a?.subject || "ela") === k; subject.append(o); }
    const cat = el("select"); for (const [k, n] of Object.entries(L.CATEGORY_NAMES)) { const o = el("option", n); o.value = k; o.selected = (a?.category || "work") === k; cat.append(o); }
    const due = el("input"); due.type = "date"; due.required = true; due.value = a?.due_date || ctx.today;
    const pts = el("input"); pts.type = "number"; pts.min = "1"; pts.max = "1000"; pts.step = "any"; pts.required = true; pts.value = a?.points || ctx.config.defaultPossible?.[cat.value] || 10;
    cat.onchange = () => { if (!a) pts.value = ctx.config.defaultPossible?.[cat.value] || pts.value; };
    const ins = el("textarea"); ins.rows = 5; ins.maxLength = 5000; ins.value = a?.instructions || ""; ins.placeholder = "What should the student do? Include page numbers, length, and how it will be graded.";
    const online = el("input"); online.type = "checkbox"; online.checked = a ? a.allow_submission : true;
    const pub = el("input"); pub.type = "checkbox"; pub.checked = a ? a.published : true;
    const grid = el("div", "", "as-grid");
    grid.append(field("Title", title, "as-wide"), field("Grade", grade), field("Subject", subject), field("Type", cat), field("Due date", due), field("Points", pts), field("Instructions", ins, "as-wide"));
    const checks = el("div", "", "as-checks");
    const c1 = el("label"); c1.append(online, el("span", " Student turns in work online (text or files)"));
    const c2 = el("label"); c2.append(pub, el("span", " Visible to the student now"));
    checks.append(c1, c2);
    f.append(grid, checks);
    // Attachments: upload new files or reuse documents from the Library.
    const chosen = new Map((a?.attachments || []).map((x) => [x.id, x]));
    const list = el("div", "", "vf-list");
    const drawList = () => {
      list.replaceChildren();
      for (const x of chosen.values()) { const rm = el("button", "Remove", "secondary lms-small"); rm.type = "button"; rm.onclick = () => { chosen.delete(x.id); drawList(); }; list.append(F.link(x, el, rm)); }
      if (!chosen.size) list.append(el("p", "No attachments.", "muted lms-small"));
    };
    drawList();
    const umsg = el("p", "", "lms-small"); umsg.setAttribute("role", "status");
    const reuse = el("select"); reuse.setAttribute("aria-label", "Attach a document from the Library");
    reuse.append(new Option("Attach a document from the Library…", ""));
    for (const d of library) reuse.append(new Option(`${d.title} (${d.name})`, d.id));
    reuse.onchange = () => { const d = library.find((x) => x.id === reuse.value); if (d) { chosen.set(d.id, d); drawList(); } reuse.value = ""; };
    f.append(el("h4", "Attachments (worksheets, rubrics, readings)"), list, F.picker(el, async (files) => {
      for (const file of files) {
        umsg.textContent = `Uploading ${file.name}…`;
        try { const up = await F.upload(file, { kind: "attachment", subject: subject.value }); chosen.set(up.id, up); library.push(up); drawList(); } catch (e) { umsg.textContent = e.message; return; }
      }
      umsg.textContent = "Uploaded.";
    }, { label: "Upload files to attach" }), umsg);
    if (library.length) f.append(reuse);
    const save = el("button", a ? "Save changes" : "Create assignment"); save.type = "submit";
    const cancel = el("button", "Cancel", "secondary"); cancel.type = "button"; cancel.onclick = () => box.replaceChildren(newButton());
    const msg = el("span", "", "lms-small muted"); msg.setAttribute("role", "status");
    const row = el("div", "", "lms-actions"); row.append(save, cancel, msg); f.append(row);
    f.onsubmit = async (e) => {
      e.preventDefault(); save.disabled = true; msg.textContent = "Saving…";
      try {
        await post("/api/family/assignments", { id: a?.id, title: title.value, grade: grade.value, subject: subject.value, category: cat.value, due_date: due.value, points: Number(pts.value), instructions: ins.value, allow_submission: online.checked, published: pub.checked, attachments: [...chosen.keys()] });
        box.replaceChildren(newButton());
        if (grade.value !== String(ctx.student.grade)) { const s = ctx.students.find((x) => String(x.grade) === grade.value); if (s) { const u = new URL(location.href); u.searchParams.set("student", s.id); location.href = u; return; } }
        filter = "upcoming"; await refresh();
      } catch (err) { msg.textContent = err.message; save.disabled = false; }
    };
    box.append(f);
    title.focus();
    box.scrollIntoView({ behavior: "smooth", block: "start" });
  }

  function newButton() {
    const b = el("button", "+ New assignment"); b.type = "button"; b.onclick = () => openEditor();
    const wrap = el("div", "", "as-new"); wrap.append(b, el("span", "Create work, quizzes or projects with attachments. They appear on the student's dashboard and in the gradebook.", "muted lms-small"));
    return wrap;
  }

  function render() {
    const sets = FILTERS[parent() ? "parent" : "student"];
    const states = new Map(ctx.assignments.map((a) => [a.id, L.assignmentState(ctx, a)]));
    if (!filter) { filter = sets[0][0]; if (!ctx.assignments.some((a) => sets[0][2](a, states.get(a.id)))) filter = parent() ? "upcoming" : "all"; }
    const tabs = $("asTabs"); tabs.replaceChildren();
    for (const [k, name, test] of sets) {
      const n = ctx.assignments.filter((a) => test(a, states.get(a.id))).length;
      const b = el("button", `${name} (${n})`); b.type = "button"; b.setAttribute("aria-pressed", String(filter === k));
      b.onclick = () => { filter = k; openPanels.clear(); render(); };
      tabs.append(b);
    }
    const test = sets.find(([k]) => k === filter)[2];
    // Keep a card on screen while its grading panel is open, even after it changes category.
    const shown = ctx.assignments.filter((a) => test(a, states.get(a.id)) || (parent() && openPanels.has(a.id)));
    if (filter === "graded" || filter === "past") shown.reverse();
    const root = $("view"); root.replaceChildren();
    if (!shown.length) root.append(el("p", ctx.assignments.length ? "Nothing here right now." : parent() ? "No assignments yet. Use “New assignment” to create one." : "No assignments yet.", "muted as-empty"));
    for (const a of shown) root.append(card(a));
    status("");
    if (location.hash.startsWith("#a")) { const t = document.getElementById(location.hash.slice(1)); if (t) t.scrollIntoView({ block: "start" }); }
  }

  (async () => {
    try {
      ctx = await L.load();
      $("asHello").textContent = parent() ? `${ctx.student.display_name}'s assignments` : "My assignments";
      $("asSub").textContent = `Grade ${ctx.student.grade} · ${L.fmt(ctx.today, { weekday: "long", month: "long", day: "numeric" })}`;
      if (parent()) {
        $("lmsSwitch").append(L.studentSwitcher(ctx, (id) => { const u = new URL(location.href); u.searchParams.set("student", id); u.hash = ""; location.href = u; }) || "");
        $("asNew").append(newButton());
        try { library = (await L.json("/api/family/files")).files || []; } catch { library = []; }
        if (location.hash.startsWith("#a")) filter = "all";
      }
      render();
    } catch (e) { status(e.message); }
  })();
})();
