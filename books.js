(() => {
  const $ = (id) => document.getElementById(id);
  let data = { subjects: {}, items: [] };
  const el = (tag, text = "", cls = "") => {
    const n = document.createElement(tag);
    if (text) n.textContent = text;
    if (cls) n.className = cls;
    return n;
  };
  const safe = (u) => (/^(https?:\/\/|\/)/i.test(u || "") ? u : "");

  function render() {
    const grade = Number($("bkGrade").value);
    const subject = $("bkSubject").value;
    const q = $("bkSearch").value.trim().toLowerCase();
    const shown = data.items.filter((b) => b.grade === grade && (subject === "all" || b.subject === subject) &&
      (!q || `${b.title} ${b.provider}`.toLowerCase().includes(q)));
    const root = $("bkList");
    root.replaceChildren();
    for (const key of Object.keys(data.subjects)) {
      const group = shown.filter((b) => b.subject === key);
      if (!group.length) continue;
      const section = el("section", "", "bk-group");
      section.append(el("h3", `${data.subjects[key]} (${group.length})`));
      const grid = el("div", "", "ck-grid");
      for (const b of group) {
        const card = el("article", "", "card ck-card");
        card.append(el("p", b.provider || "", "eyebrow"), el("h4", b.title));
        card.append(el("p", `${b.kind}${b.access ? " · " + b.access : ""} · used in ${b.weeks} week${b.weeks === 1 ? "" : "s"}`, "muted"));
        const url = safe(b.url);
        if (url) {
          const a = el("a", "Open book", "ck-open");
          a.href = url;
          if (/^https?:/i.test(url)) { a.target = "_blank"; a.rel = "noopener noreferrer"; }
          a.setAttribute("aria-label", `Open ${b.title}`);
          card.append(a);
        }
        grid.append(card);
      }
      section.append(grid);
      root.append(section);
    }
    $("status").textContent = shown.length ? `${shown.length} book${shown.length === 1 ? "" : "s"} for Grade ${grade}` : "No books match these filters.";
  }

  async function init() {
    try {
      const r = await fetch("/books-library.json");
      if (r.status === 401 || r.redirected) { location.replace("/login"); return; }
      if (!r.ok) throw new Error(`Request failed (${r.status})`);
      data = await r.json();
      for (const [k, v] of Object.entries(data.subjects)) $("bkSubject").append(new Option(v, k));
      for (const id of ["bkGrade", "bkSubject"]) $(id).onchange = render;
      $("bkSearch").oninput = render;
      render();
    } catch (e) {
      $("status").textContent = `Couldn’t load the book list: ${e.message}`;
    }
  }
  init();
})();
