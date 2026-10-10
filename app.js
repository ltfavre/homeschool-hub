const $ = (s) => document.querySelector(s);
const today = new Date();
const iso = (d) => d.toISOString().slice(0,10);
const fmt = (d, opts={weekday:"long", month:"long", day:"numeric"}) =>
  new Intl.DateTimeFormat("en-US", opts).format(d);

let bootstrap = {students:[], subjects:[]};

$("#todayLabel").textContent = fmt(today).toUpperCase();

async function api(path, options={}) {
  const res = await fetch(path, {
    headers: {"content-type":"application/json", ...(options.headers||{})},
    ...options
  });
  if (!res.ok) throw new Error((await res.json()).error || `Request failed: ${res.status}`);
  return res.json();
}

function itemMarkup(x, dateKey) {
  const link = x.resource_url ? `<a href="${x.resource_url}" target="_blank" rel="noopener">Resource</a>` : "";
  return `<div class="item">
    <div class="item-top"><strong>${x.title}</strong><span class="pill">${x.subject_name}</span></div>
    <div class="meta">${x.student_name} · ${x[dateKey]} ${link ? "· " + link : ""}</div>
  </div>`;
}

async function load() {
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
    : `<div class="empty">No lessons scheduled for today.</div>`;

  $("#assignments").innerHTML = todaysAssignments.length
    ? todaysAssignments.map(x => itemMarkup(x,"due_date")).join("")
    : `<div class="empty">No assignments due today.</div>`;

  $("#student").innerHTML = bootstrap.students.map(x => `<option value="${x.id}">${x.name} — Grade ${x.grade}</option>`).join("");
  $("#subject").innerHTML = bootstrap.subjects.map(x => `<option value="${x.id}">${x.name}</option>`).join("");

  $("#week").innerHTML = Array.from({length:7}, (_,i) => {
    const d = new Date(today); d.setDate(d.getDate()+i);
    const key = iso(d);
    const dayLessons = lessons.filter(x=>x.lesson_date===key);
    const dayAssignments = assignments.filter(x=>x.due_date===key);
    return `<div class="day">
      <strong>${fmt(d,{weekday:"short",month:"numeric",day:"numeric"})}</strong>
      ${dayLessons.map(x=>`<span class="dot">${x.student_name}: ${x.title}</span>`).join("")}
      ${dayAssignments.map(x=>`<span class="dot">Due: ${x.title}</span>`).join("")}
    </div>`;
  }).join("");
}

function openDialog(type) {
  $("#entryType").value = type;
  $("#dialogTitle").textContent = type === "lesson" ? "Add lesson" : "Add assignment";
  $("#date").value = iso(today);
  $("#title").value = "";
  $("#instructions").value = "";
  $("#resourceUrl").value = "";
  $("#entryDialog").showModal();
}

$("#addLessonBtn").onclick = () => openDialog("lesson");
$("#addAssignmentBtn").onclick = () => openDialog("assignment");
$("#refreshBtn").onclick = load;

$("#entryForm").addEventListener("submit", async (e) => {
  const submitter = e.submitter;
  if (submitter?.value === "cancel") return;
  e.preventDefault();

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

  await api(`/api/${type === "lesson" ? "lessons" : "assignments"}`, {
    method:"POST",
    body:JSON.stringify(payload)
  });
  $("#entryDialog").close();
  await load();
});

load().catch(err => {
  console.error(err);
  $("#lessons").innerHTML = `<div class="empty">Database not initialized yet. Run the schema setup from README.</div>`;
});
