const $ = (s) => document.querySelector(s);
const today = new Date();
const pad = (n) => String(n).padStart(2, "0");
// Local calendar date (toISOString() is UTC and flips to "tomorrow" in the evening in US time zones).
const iso = (d) => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
const fmt = (d, opts={weekday:"long", month:"long", day:"numeric"}) =>
  new Intl.DateTimeFormat("en-US", opts).format(d);
const esc = (value) => String(value ?? "").replace(/[&<>"']/g, (c) => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const safeUrl = (url) => (/^https?:\/\//i.test(String(url || "")) ? url : "");

let bootstrap = {students:[], subjects:[]};

$("#todayLabel").textContent = fmt(today).toUpperCase();

async function api(path, options={}) {
  const res = await fetch(path, {
    headers: {"content-type":"application/json", ...(options.headers||{})},
    ...options
  });
  if (!res.ok) {
    let message = `Request failed: ${res.status}`;
    try { message = (await res.json()).error || message; } catch {}
    throw new Error(message);
  }
  return res.json();
}

function itemMarkup(x, dateKey) {
  const url = safeUrl(x.resource_url);
  const link = url ? `<a href="${esc(url)}" target="_blank" rel="noopener noreferrer">Resource</a>` : "";
  return `<div class="item">
    <div class="item-top"><strong>${esc(x.title)}</strong><span class="pill">${esc(x.subject_name)}</span></div>
    <div class="meta">${esc(x.student_name)} · ${esc(x[dateKey])} ${link ? "· " + link : ""}</div>
  </div>`;
}

async function load() {
  const button = $("#refreshBtn");
  button.disabled = true;
  button.textContent = "Refreshing…";
  try {
    const start = new Date(today); start.setDate(start.getDate()-1);
    const end = new Date(today); end.setDate(end.getDate()+7);

    bootstrap = await api("/api/bootstrap");
    const [lessons, assignments] = await Promise.all([
      api(`/api/lessons?start=${iso(start)}&end=${iso(end)}`),
      api(`/api/assignments?start=${iso(start)}&end=${iso(end)}`)
    ]);

    const todaysLessons = lessons.filter(x => x.lesson_date === iso(today));
    const todaysAssignments = assignments.filter(x => x.due_date === iso(today));
    $("#lessonCount").textContent = todaysLessons.length;
    $("#assignmentCount").textContent = todaysAssignments.length;

    $("#lessons").innerHTML = todaysLessons.length
      ? todaysLessons.map(x => itemMarkup(x,"lesson_date")).join("")
      : `<div class="empty">No lessons scheduled for today. Use “+ Add lesson” to plan one.</div>`;

    $("#assignments").innerHTML = todaysAssignments.length
      ? todaysAssignments.map(x => itemMarkup(x,"due_date")).join("")
      : `<div class="empty">Nothing due today.</div>`;

    $("#student").innerHTML = bootstrap.students.map(x => `<option value="${esc(x.id)}">${esc(x.name)} — Grade ${esc(x.grade)}</option>`).join("");
    $("#subject").innerHTML = bootstrap.subjects.map(x => `<option value="${esc(x.id)}">${esc(x.name)}</option>`).join("");

    $("#week").innerHTML = Array.from({length:7}, (_,i) => {
      const d = new Date(today); d.setDate(d.getDate()+i);
      const key = iso(d);
      const dayLessons = lessons.filter(x=>x.lesson_date===key);
      const dayAssignments = assignments.filter(x=>x.due_date===key);
      const items = dayLessons.map(x=>`<span class="dot">${esc(x.student_name)}: ${esc(x.title)}</span>`).join("")
        + dayAssignments.map(x=>`<span class="dot due">Due: ${esc(x.title)}</span>`).join("");
      return `<div class="day${i === 0 ? " is-today" : ""}"${i === 0 ? ' aria-current="date"' : ""}>
        <strong>${esc(fmt(d,{weekday:"short",month:"numeric",day:"numeric"}))}${i === 0 ? " · Today" : ""}</strong>
        ${items || `<span class="day-empty">Nothing planned</span>`}
      </div>`;
    }).join("");
  } finally {
    button.disabled = false;
    button.textContent = "Refresh";
  }
}

function openDialog(type) {
  $("#entryType").value = type;
  $("#dialogTitle").textContent = type === "lesson" ? "Add lesson" : "Add assignment";
  $("#date").value = iso(today);
  $("#title").value = "";
  $("#instructions").value = "";
  $("#resourceUrl").value = "";
  $("#formError").textContent = "";
  $("#entryDialog").showModal();
  $("#title").focus();
}

$("#addLessonBtn").onclick = () => openDialog("lesson");
$("#addAssignmentBtn").onclick = () => openDialog("assignment");
$("#refreshBtn").onclick = () => load().catch(showLoadError);

$("#entryForm").addEventListener("submit", async (e) => {
  const submitter = e.submitter;
  if (submitter?.value === "cancel") return;
  e.preventDefault();

  const saveBtn = $("#saveBtn");
  const type = $("#entryType").value;
  const payload = {
    student_id: Number($("#student").value),
    subject_id: Number($("#subject").value),
    title: $("#title").value,
    instructions: $("#instructions").value || null,
    resource_url: $("#resourceUrl").value || null
  };

  if (type === "lesson") payload.lesson_date = $("#date").value;
  else payload.due_date = $("#date").value;

  saveBtn.disabled = true;
  saveBtn.textContent = "Saving…";
  $("#formError").textContent = "";
  try {
    await api(`/api/${type === "lesson" ? "lessons" : "assignments"}`, {
      method:"POST",
      body:JSON.stringify(payload)
    });
    $("#entryDialog").close();
    await load();
  } catch (err) {
    // Keep the dialog open so nothing typed is lost, and say what went wrong.
    $("#formError").textContent = `Couldn’t save: ${err.message}`;
  } finally {
    saveBtn.disabled = false;
    saveBtn.textContent = "Save";
  }
});

function showLoadError(err) {
  console.error(err);
  $("#lessons").innerHTML = `<div class="empty">Couldn’t load your hub (${esc(err.message)}). If this is a brand-new setup, run the schema setup from the README.</div>`;
}

load().catch(showLoadError);

// Today's textbook lessons for each student, plus the parent's own Data Science & Psychometrics lesson.
const TB_SUBJECT = {math:"Math", ela:"ELA", science:"Science", social:"Social Studies", spanish:"Spanish", art:"Art", data:"Data Science"};
const TB_KIND = {textbook:"Textbook", workbook:"Workbook", teacher:"Teacher Edition"};
async function loadTextbooks() {
  const box = $("#textbookToday");
  if (!box) return;
  try {
    const res = await fetch("/textbook-schedule.json", {cache:"no-store"});
    if (!res.ok) throw new Error(String(res.status));
    const {grades} = await res.json();
    const todayKey = iso(today);
    // On weekends and breaks, show the next school day that has lessons.
    const dates = [...new Set(Object.values(grades).flatMap((g) => Object.keys(g)))].sort();
    const day = dates.find((d) => d >= todayKey);
    if (!day) { box.textContent = "No textbook lessons are scheduled."; return; }
    const when = new Date(day + "T12:00:00");
    $("#textbookHeading").textContent = day === todayKey ? "Today in the books" : `Next up · ${fmt(when, {weekday:"long", month:"short", day:"numeric"})}`;
    const cols = [["4", "Grade 4"], ["7", "Grade 7"], ["parent", "You · Professional learning"]].map(([g, label]) => {
      // A column with nothing on this day shows its own next scheduled day (the parent course starts later).
      const own = grades[g]?.[day] ? day : Object.keys(grades[g] || {}).sort().find((d) => d >= todayKey);
      const subjects = (own && grades[g][own]) || {};
      const note = own && own !== day ? `<p class="muted">Starts ${fmt(new Date(own + "T12:00:00"), {weekday:"long", month:"short", day:"numeric"})}</p>` : "";
      const rows = Object.entries(subjects).flatMap(([subject, items]) => items.map((it) => {
        const name = it.kind === "lesson" ? `Lesson ${esc(it.num)}: ${esc(it.title)}` : esc(it.title);
        const links = Object.entries(it.links || {}).map(([k, href]) => {
          const p = it.pages?.[k]; const pages = p ? (p[0] === p[1] ? ` p. ${p[0]}` : ` pp. ${p[0]}–${p[1]}`) : "";
          return `<a href="${esc(href)}" target="_blank" rel="noopener">${TB_KIND[k] || k}${pages}</a>`;
        }).join(" · ");
        return `<div class="item"><div class="item-top"><strong>${name}</strong><span class="pill">${TB_SUBJECT[subject] || esc(subject)}</span></div><div class="meta">${links}</div></div>`;
      })).join("");
      return `<div class="textbook-col"><h4>${label}</h4>${note}${rows || '<p class="muted">Nothing scheduled.</p>'}</div>`;
    }).join("");
    box.classList.remove("empty");
    box.innerHTML = cols;
  } catch {
    box.textContent = "The textbook schedule could not be loaded.";
  }
}
loadTextbooks();
