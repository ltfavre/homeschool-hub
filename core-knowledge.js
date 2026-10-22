(() => {
  const $ = (id) => document.getElementById(id);
  const SUBJECTS = { math: "Math", ela: "Language arts", history: "History & geography", science: "Science" };
  const ORDER = ["math", "ela", "history", "science"];
  let units = [];

  const el = (tag, text = "", cls = "") => {
    const node = document.createElement(tag);
    if (text) node.textContent = text;
    if (cls) node.className = cls;
    return node;
  };

  function render() {
    const grade = Number($("ckGrade").value);
    const subject = $("ckSubject").value;
    const shown = units
      .filter((u) => u.grade === grade && (subject === "all" || u.subject === subject))
      .sort((a, b) => ORDER.indexOf(a.subject) - ORDER.indexOf(b.subject));

    const root = $("ckUnits");
    root.replaceChildren();
    for (const unit of shown) {
      const card = el("article", "", "card ck-card");
      card.append(el("p", SUBJECTS[unit.subject] || unit.subject, "eyebrow"), el("h3", unit.title));
      const link = el("a", "Open on Core Knowledge", "ck-open");
      link.href = unit.url;
      link.target = "_blank";
      link.rel = "noopener noreferrer";
      link.setAttribute("aria-label", `${unit.title} (opens the Core Knowledge site in a new tab)`);
      card.append(link);
      root.append(card);
    }
    $("status").textContent = shown.length
      ? `${shown.length} unit${shown.length === 1 ? "" : "s"} for Grade ${grade}`
      : "No units match these filters.";
  }

  async function init() {
    try {
      const response = await fetch("/core-knowledge-units.json");
      if (response.status === 401 || response.redirected) {
        location.replace("/login");
        return;
      }
      if (!response.ok) throw new Error(`Request failed (${response.status})`);
      units = (await response.json()).units || [];
      $("ckGrade").onchange = render;
      $("ckSubject").onchange = render;
      render();
    } catch (error) {
      $("status").textContent = `Couldn’t load the unit list: ${error.message}`;
    }
  }

  init();
})();
