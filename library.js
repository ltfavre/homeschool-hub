(() => {
  const F = window.VenvFiles, el = window.LMS.el, NAMES = window.LMS.NAMES;
  const $ = (id) => document.getElementById(id);
  let me, today, list, books, files = [], tab = "reading";
  const AUD = { private: "Only me", both: "Both students", 4: "Grade 4", 7: "Grade 7" };
  const post = (path, body) => window.LMS.json(path, { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(body) });
  const parent = () => me.role === "parent";
  const grade = () => (parent() ? $("libGrade").value : String(me.grade));
  const q = () => $("libSearch").value.trim().toLowerCase();
  const match = (...parts) => !q() || parts.join(" ").toLowerCase().includes(q());
  const safe = (u) => (/^(https?:\/\/|\/)/i.test(u || "") ? u : "");

  function linkBtn(l, cls = "lms-btn") {
    const a = el("a", l.label, cls);
    a.href = safe(l.url); a.target = "_blank"; a.rel = "noopener noreferrer";
    return a;
  }

  function bookCard(b) {
    const c = el("article", "", "lib-book" + (b.role === "companion" ? " is-companion" : ""));
    c.append(el("span", b.role === "companion" ? "Companion" : "Core book", "lms-chip"));
    c.append(el("h4", b.title), el("p", `${b.author} · ${b.year}${b.length ? " · " + b.length : ""}`, "muted lms-small"));
    c.append(el("p", b.why));
    const ties = el("p", "", "lib-ties"); ties.append(el("strong", "Connects to: "), document.createTextNode(b.ties)); c.append(ties);
    if (b.note) { const n = el("p", "", "lib-note"); n.append(el("strong", "Note for parents: "), document.createTextNode(b.note)); c.append(n); }
    const d = el("details", "", "lms-details"); d.append(el("summary", "Discussion and writing prompts"));
    const ul = el("ul"); for (const p of b.prompts) ul.append(el("li", p)); d.append(ul); c.append(d);
    const act = el("div", "", "lms-actions"); b.links.forEach((l, i) => act.append(linkBtn(l, i ? "lms-btn lms-btn-2" : "lms-btn"))); c.append(act);
    c.append(el("p", b.access, "muted lms-small"));
    return c;
  }

  function reading(root) {
    const g = list.grades[grade()];
    root.append(el("p", `${list.about} ${g.pace}`, "muted lib-lead"));
    for (const [m, info] of Object.entries(list.modules)) {
      const items = g.books.filter((b) => String(b.module) === m && match(b.title, b.author, b.why, b.ties));
      if (!items.length) continue;
      const now = today >= info.start && today <= info.end, past = today > info.end;
      const sec = el("section", "", "lib-module" + (now ? " is-current" : "") + (past ? " is-past" : ""));
      const h = el("div", "", "lib-module-head");
      h.append(el("h3", info.label), el("span", info.dates, "muted"));
      if (now) h.append(el("span", "Reading now", "lms-chip lms-chip-now"));
      sec.append(h);
      const grid = el("div", "", "lib-grid"); for (const b of items) grid.append(bookCard(b)); sec.append(grid);
      root.append(sec);
    }
    const libs = g.library.filter((b) => match(b.title, b.author, b.why));
    if (libs.length) {
      const sec = el("section", "", "lib-section");
      sec.append(el("h3", "Free with a library card"), el("p", "Modern favorites to borrow in print or as e-books and audiobooks through your public library's Libby or Hoopla apps. The link searches libraries near you.", "muted"));
      const grid = el("div", "", "lib-grid lib-grid-tight");
      for (const b of libs) {
        const c = el("article", "", "lib-book is-borrow");
        c.append(el("span", `Modules ${b.modules.join(", ")}`, "lms-chip"), el("h4", b.title), el("p", b.author, "muted lms-small"), el("p", b.why));
        if (b.note) { const n = el("p", "", "lib-note"); n.append(el("strong", "Note: "), document.createTextNode(b.note)); c.append(n); }
        const act = el("div", "", "lms-actions"); for (const l of b.links) act.append(linkBtn(l, "lms-btn lms-btn-2")); c.append(act);
        grid.append(c);
      }
      sec.append(grid); root.append(sec);
    }
    const plats = list.platforms.filter((p) => match(p.title, p.what));
    if (plats.length) {
      const sec = el("section", "", "lib-section");
      sec.append(el("h3", "Free reading platforms"));
      const grid = el("div", "", "lib-grid lib-grid-tight");
      for (const p of plats) {
        const c = el("article", "", "lib-book is-platform");
        const a = el("a", p.title); a.href = safe(p.url); a.target = "_blank"; a.rel = "noopener noreferrer";
        const h = el("h4"); h.append(a);
        c.append(el("span", `Grades ${p.grades}`, "lms-chip"), h, el("p", p.what), el("p", p.access, "muted lms-small"));
        grid.append(c);
      }
      sec.append(grid); root.append(sec);
    }
  }

  function curriculumBooks(root) {
    const g = Number(grade());
    const shown = books.items.filter((b) => b.grade === g && (parent() || !b.teacher) && match(b.title, b.provider, b.kind));
    root.append(el("p", "Every reader, workbook and textbook linked in the lesson plans. The number shows how many weeks use each one.", "muted lib-lead"));
    for (const [key, name] of Object.entries(books.subjects)) {
      const group = shown.filter((b) => b.subject === key);
      if (!group.length) continue;
      const sec = el("section", "", "lib-section");
      sec.append(el("h3", `${name} (${group.length})`));
      const grid = el("div", "", "lib-grid lib-grid-tight");
      for (const b of group) {
        const c = el("article", "", "lib-book is-curriculum");
        c.append(el("p", b.provider || "", "eyebrow"), el("h4", b.title), el("p", `${b.kind}${b.access ? " · " + b.access : ""} · used in ${b.weeks} week${b.weeks === 1 ? "" : "s"}`, "muted lms-small"));
        if (b.teacher) c.append(el("span", "Teacher copy", "lms-chip"));
        const url = safe(b.url);
        if (url) { const act = el("div", "", "lms-actions"); act.append(linkBtn({ label: "Open", url }, "lms-btn lms-btn-2")); c.append(act); }
        grid.append(c);
      }
      sec.append(grid); root.append(sec);
    }
    if (!shown.length) root.append(el("p", "No books match.", "muted"));
  }

  function uploader() {
    const box = el("section", "", "card lib-upload");
    box.append(el("h3", "Add documents"), el("p", "Upload worksheets, handouts, scanned pages, rubrics or records. Choose who can see each file; “Only me” keeps it private to parent accounts.", "muted"));
    const row = el("div", "", "lib-upload-row");
    const aud = el("select"); aud.setAttribute("aria-label", "Who can see it");
    for (const [v, n] of Object.entries(AUD)) aud.append(new Option(n, v));
    aud.value = "both";
    const subj = el("select"); subj.setAttribute("aria-label", "Subject"); subj.append(new Option("Any subject", ""));
    for (const [k, n] of Object.entries(NAMES)) subj.append(new Option(n, k));
    const title = el("input"); title.placeholder = "Title (optional, one file)"; title.maxLength = 160; title.setAttribute("aria-label", "Title");
    const lab = (t, i) => { const l = el("label", "", "as-field"); l.append(el("span", t), i); return l; };
    row.append(lab("Who can see it", aud), lab("Subject", subj), lab("Title", title));
    const msg = el("p", "", "lms-small"); msg.setAttribute("role", "status");
    box.append(row, F.picker(el, async (picked) => {
      let done = 0;
      for (const file of picked) {
        msg.textContent = `Uploading ${file.name} (${done + 1} of ${picked.length})…`;
        try { await F.upload(file, { kind: "document", audience: aud.value, subject: subj.value, title: picked.length === 1 ? title.value : "" }); done++; } catch (e) { msg.textContent = e.message; break; }
      }
      if (done) { title.value = ""; msg.textContent = `Uploaded ${done} file${done === 1 ? "" : "s"}.`; await loadFiles(); render(); }
    }), msg);
    return box;
  }

  function docs(root) {
    if (parent()) root.append(uploader());
    const shown = files.filter((f) => match(f.title, f.name, NAMES[f.subject] || "", AUD[f.audience] || ""));
    const sec = el("section", "", "lib-section");
    sec.append(el("h3", parent() ? `All documents (${shown.length})` : `Shared with you (${shown.length})`));
    if (!shown.length) sec.append(el("p", parent() ? "Nothing uploaded yet." : "Your teacher hasn't shared any documents yet.", "muted"));
    const listEl = el("div", "", "vf-list lib-docs");
    for (const f of shown) {
      const extra = el("div", "", "lib-doc-meta");
      if (f.subject) extra.append(el("span", NAMES[f.subject] || f.subject, "lms-chip"));
      extra.append(el("span", new Date(f.created_at * 1000).toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" }), "muted lms-small"));
      if (parent()) {
        if (f.kind === "attachment") extra.append(el("span", "Assignment attachment", "lms-chip"));
        else {
          const sel = el("select"); sel.setAttribute("aria-label", `Who can see ${f.title}`);
          for (const [v, n] of Object.entries(AUD)) sel.append(new Option(n, v));
          sel.value = f.audience;
          sel.onchange = async () => { sel.disabled = true; try { await post(`/api/family/files/${f.id}`, { audience: sel.value }); f.audience = sel.value; } catch (e) { $("status").textContent = e.message; } sel.disabled = false; render(); };
          extra.append(sel);
        }
        const del = el("button", "Delete", "secondary lms-small"); del.type = "button";
        del.onclick = async () => { if (!confirm(`Delete “${f.title}”? Assignments that attach it will lose the file.`)) return; del.disabled = true; try { await post(`/api/family/files/${f.id}`, { delete: true }); await loadFiles(); render(); } catch (e) { $("status").textContent = e.message; del.disabled = false; } };
        extra.append(del);
      }
      listEl.append(F.link(f, el, extra));
    }
    sec.append(listEl); root.append(sec);
  }

  async function loadFiles() { try { files = (await window.LMS.json("/api/family/files")).files || []; } catch (e) { files = []; $("status").textContent = `Documents unavailable: ${e.message}`; } }

  function render() {
    for (const b of document.querySelectorAll("[data-tab]")) b.setAttribute("aria-pressed", String(b.dataset.tab === tab));
    $("libPrint").hidden = tab !== "reading";
    $("libGradeWrap").hidden = !parent() || tab === "docs";
    const root = $("view"); root.replaceChildren();
    ({ reading, books: curriculumBooks, docs })[tab](root);
    if (location.hash.slice(1) !== tab) history.replaceState(null, "", `#${tab}`);
  }

  (async () => {
    try {
      const meRes = await window.LMS.json("/api/family/me");
      me = meRes.user; today = meRes.today;
      [list, books] = await Promise.all([window.LMS.json("/reading-list.json"), window.LMS.json("/books-library.json")]);
      await loadFiles();
      if (parent()) { const want = new URLSearchParams(location.search).get("grade"); if (want === "4" || want === "7") $("libGrade").value = want; }
      else { $("libGradeWrap").hidden = true; $("libIntro").textContent = `Your Grade ${me.grade} reading list, the books in your lessons, and documents your teacher shared with you.`; }
      const h = location.hash.slice(1); if (["reading", "books", "docs"].includes(h)) tab = h;
      for (const b of document.querySelectorAll("[data-tab]")) b.onclick = () => { tab = b.dataset.tab; render(); };
      $("libGrade").onchange = render; $("libSearch").oninput = render; $("libPrint").onclick = () => window.print();
      $("status").textContent = "";
      render();
    } catch (e) { $("status").textContent = `Couldn’t load the library: ${e.message}`; }
  })();
})();
