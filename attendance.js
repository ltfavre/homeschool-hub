(() => {
  const L = window.LMS, { el } = L;
  const $ = (id) => document.getElementById(id);
  let ctx, rows = new Map(), month = "";

  const schoolDays = () => Object.keys(ctx.daily).filter((d) => ctx.daily[d]?.[ctx.student.grade]).sort();
  const post = (entries) => L.json("/api/family/attendance", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify({ student_id: ctx.student.id, entries }) });

  async function reload() {
    const data = await L.json(`/api/family/attendance?student=${encodeURIComponent(ctx.student.id)}`);
    rows = new Map((data.rows || []).map((r) => [r.d, r]));
  }

  function summary() {
    const past = schoolDays().filter((d) => d <= ctx.today);
    const all = [...rows.values()];
    const present = all.filter((r) => r.s === "present" || r.s === "partial").length;
    const absent = all.filter((r) => r.s === "absent").length;
    const hours = all.reduce((n, r) => n + (r.h || 0), 0);
    const unrecorded = past.filter((d) => !rows.has(d)).length;
    const box = $("attSum");
    box.replaceChildren();
    for (const [v, t] of [[present, "Days attended"], [absent, "Days absent"], [unrecorded, "Past days unrecorded"], [L.pct1(hours), "Hours logged"], [schoolDays().length, "Scheduled days this year"]]) {
      const d = el("div"); d.append(el("strong", String(v)), el("span", t, "muted lms-small")); box.append(d);
    }
    const bulk = $("attBulk");
    bulk.replaceChildren();
    if (unrecorded) {
      const b = el("button", `Mark ${unrecorded} unrecorded past day${unrecorded === 1 ? "" : "s"} present`, "secondary"); b.type = "button";
      let armed = false;
      b.onclick = async () => {
        if (!armed) { armed = true; b.textContent = `Tap again to confirm: mark ${unrecorded} days present`; return; }
        b.disabled = true;
        try { await post(past.filter((d) => !rows.has(d)).map((d) => ({ date: d, status: "present" }))); await reload(); render(); } catch (e) { $("status").textContent = e.message; b.disabled = false; }
      };
      bulk.append(b);
    }
  }

  function render() {
    $("attName").textContent = `${ctx.student.display_name} · Grade ${ctx.student.grade}`;
    summary();
    const tbody = $("attRows");
    tbody.replaceChildren();
    const days = schoolDays().filter((d) => d.startsWith(month) && d <= ctx.today).reverse();
    if (!days.length) { const tr = el("tr"); tr.append(el("td", "No school days to record in this month yet.")); tbody.append(tr); }
    for (const d of days) {
      const r = rows.get(d);
      const tr = el("tr");
      tr.append(el("td", L.day(d)));
      const st = el("td"); const btns = el("div", "", "att-btns");
      const save = async (entry) => { $("status").textContent = "Saving…"; try { await post([{ date: d, ...entry }]); await reload(); $("status").textContent = ""; render(); } catch (e) { $("status").textContent = e.message; } };
      for (const [v, t] of [["present", "Present"], ["partial", "Partial"], ["absent", "Absent"]]) {
        const b = el("button", t); b.type = "button"; b.dataset.s = v; b.setAttribute("aria-pressed", String(r?.s === v));
        b.onclick = () => save(r?.s === v ? { clear: true } : { status: v, hours: r?.h ?? null, note: r?.n || "" });
        btns.append(b);
      }
      st.append(btns);
      const hrs = el("td"); const hi = el("input"); hi.type = "number"; hi.min = "0"; hi.max = "24"; hi.step = "0.25"; hi.style.width = "5rem"; hi.value = r?.h ?? ""; hi.disabled = !r; hi.setAttribute("aria-label", `Hours for ${L.day(d)}`);
      hi.onchange = () => save({ status: r.s, hours: hi.value === "" ? null : Number(hi.value), note: r.n || "" });
      hrs.append(hi);
      const nt = el("td"); const ni = el("input"); ni.type = "text"; ni.maxLength = 300; ni.value = r?.n || ""; ni.disabled = !r; ni.setAttribute("aria-label", `Note for ${L.day(d)}`);
      ni.onchange = () => save({ status: r.s, hours: r.h ?? null, note: ni.value.trim() });
      nt.append(ni);
      tr.append(st, hrs, nt);
      tbody.append(tr);
    }
  }

  function csv() {
    const lines = [["Date", "Status", "Hours", "Note"], ...schoolDays().filter((d) => d <= ctx.today).map((d) => { const r = rows.get(d); return [d, r?.s || "unrecorded", r?.h ?? "", r?.n || ""]; })];
    const text = lines.map((r) => r.map((v) => `"${String(v).replaceAll('"', '""')}"`).join(",")).join("\n");
    const a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([text], { type: "text/csv" }));
    a.download = `attendance-${ctx.student.display_name.replace(/\W+/g, "-")}-${ctx.today}.csv`;
    a.click();
    URL.revokeObjectURL(a.href);
  }

  (async () => {
    try {
      ctx = await L.load();
      if (ctx.me.role !== "parent") { location.replace("/courses"); return; }
      await reload();
      $("status").textContent = "";
      $("lmsSwitch").append(L.studentSwitcher(ctx, (id) => { const u = new URL(location.href); u.searchParams.set("student", id); location.href = u; }) || "");
      const months = [...new Set(schoolDays().filter((d) => d <= ctx.today).map((d) => d.slice(0, 7)))];
      month = months[months.length - 1] || ctx.today.slice(0, 7);
      const sel = $("attMonth");
      for (const m of months) { const o = el("option", new Date(m + "-01T12:00:00Z").toLocaleDateString("en-US", { timeZone: "UTC", month: "long", year: "numeric" })); o.value = m; o.selected = m === month; sel.append(o); }
      sel.onchange = () => { month = sel.value; render(); };
      $("attCsv").onclick = csv;
      render();
    } catch (e) {
      $("status").textContent = e.message;
    }
  })();
})();
