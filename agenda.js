const $ = (id) => document.getElementById(id);
const node = (tag, text = "", cls = "") => {
  const element = document.createElement(tag);
  element.textContent = text;
  element.className = cls;
  return element;
};

const names = {math:'Math',ela:'ELA',science:'Physical Sciences',social:'Social Studies',spanish:'Spanish',art:'Art',life:'Human Sciences',computer:'Computer Science',skills:'Life Skills',review:'Friday Review / Projects / Catch-up'};

let me;
let today;
let view;

async function api(path, options = {}) {
  const response = await fetch(path, {
    ...options,
    headers: { "content-type": "application/json" }
  });
  const body = await response.json();
  if (response.status === 401) {
    location.replace("/login");
    throw new Error("Please sign in");
  }
  if (!response.ok) throw new Error(body.error);
  return body;
}

function renderDailyTasks() {
  const tasks = Array.isArray(view.daily_tasks) ? view.daily_tasks : [];
  const existing = $("venvTasks");
  if (existing) existing.remove();
  if (!tasks.length) return;

  const section = node("section", "", "agenda-card");
  section.id = "venvTasks";
  section.append(node("p", "VENVLEARNING", "eyebrow"), node("h2", "Daily tasks"));

  const list = node("ul");
  for (const task of tasks) {
    const status = String(task.status || "pending")
      .replaceAll("_", " ")
      .replace(/^\w/, (x) => x.toUpperCase());
    const item = node("li");
    item.append(
      node("p", task.title || "Untitled task"),
      node("p", `${status} · ${task.source || "venvlearning"}`, "muted")
    );
    list.append(item);
  }
  section.append(list);
  $("cards").prepend(section);
}

function updateProgress() {
  const done = view.subjects.filter((subject) => subject.completed).length;
  const total = view.subjects.length;
  $("status").textContent = done === total && total
    ? `All ${total} subjects complete — great work today! · Saved to this account`
    : `${done} of ${total} subjects complete · Saved to this account`;
  let bar = $("dayProgress");
  if (!bar) {
    bar = node("div", "", "day-progress");
    bar.id = "dayProgress";
    bar.setAttribute("role", "progressbar");
    bar.setAttribute("aria-label", "Subjects completed today");
    bar.append(node("span"));
    $("status").after(bar);
  }
  bar.setAttribute("aria-valuemin", "0");
  bar.setAttribute("aria-valuemax", String(total));
  bar.setAttribute("aria-valuenow", String(done));
  bar.firstChild.style.width = total ? `${Math.round((done / total) * 100)}%` : "0%";
  bar.classList.toggle("is-complete", total > 0 && done === total);
}

async function load() {
  try {
    $("status").textContent = "Loading agenda…";
    const date = $("date").value || today;
    const studentQuery = me.role === "parent" ? `&student=${$("student").value}` : "";
    view = await api(`/api/family/agenda?date=${date}${studentQuery}`);

    $("cards").replaceChildren();
    $("dayProgress")?.remove();
    $("summary").replaceChildren(
      node("h2", `${view.student.display_name} · Grade ${view.student.grade}`),
      node(
        "p",
        new Date(`${date}T12:00:00`).toLocaleDateString("en-US", {
          weekday: "long",
          month: "long",
          day: "numeric",
          year: "numeric"
        })
      )
    );

    $("printPacket").hidden = !view.teaching;$("lessonGuide").hidden=!view.teaching;
    if (!view.teaching) {
      $("summary").append(node("p", "No teaching activities are scheduled for this date."));
      if (view.next_date) $("summary").append(node("p", `Next teaching day: ${view.next_date}`));
      $("status").textContent = "Weekend, break, or a day outside the teaching calendar.";
      renderDailyTasks();
      return;
    }

    $("printPacket").href = view.print_url+"&kind=work";$("lessonGuide").href=view.print_url+"&kind=guide";
    $("summary").append(
      node("p", `Module ${view.module} · Week ${view.week}`),
      node("p", "Read the assigned book with your parent, practice together, and use the supporting links when helpful.")
    );

    const dailyPlan = node("details");
    dailyPlan.append(node("summary", "Today’s lesson plan"), node("p", view.tasks));
    $("summary").append(dailyPlan);

    if (view.assessment) {
      const note = node("p", `${view.assessment.title} · Use taught skills for the selected review. Friday can also be used for projects, field trips, independent study, or catch-up. `);
      const anchor = node("a", "Download student assessment PDF");
      anchor.href = view.assessment.student_pdf;
      anchor.download = "";
      note.append(anchor);
      $("summary").append(note);
    }

    KhanUI.assessments(view.primary_assessments, $("summary"));if(view.integration){const connections=node('details','','support-details');connections.append(node('summary','This week’s connections'),node('p',view.integration));$("summary").append(connections);}

    for (const subject of view.subjects) {
      const outer = node("article", "", `agenda-card${subject.completed ? " completed" : ""}`), disclosure=node('details','','lesson-disclosure'),heading=node('summary'),title=node('div'),card=node('div','','lesson-body');
      title.append(node('span',names[subject.key]||subject.key,'subject-tag'),node('h2',subject.topic),node('span','Open lesson & reading','summary-hint'));heading.append(title);disclosure.append(heading,card);outer.append(disclosure);

      const taskPrefix = {
        math: "Math:",
        ela: "ELA:",
        science: "Sci:",
        social: "SS:",
        spanish: "Sp:", art:"Art:",life:"Life:",computer:"CS:",skills:"Skills:",review:"Friday:"
      }[subject.key];
      const task = subject.task || view.tasks
        .split(/\s+(?=Math:|ELA:|Sci:|SS:|Art:|Life:|CS:|Skills:|Sp:|Friday:)/)
        .find((entry) => entry.startsWith(taskPrefix));

      card.append(
        node(
          "p",
          task
            ? task.slice(taskPrefix.length).trim()
            : view.assessment
              ? "Complete this subject in your printed assessment, then review corrections."
              : "Follow today’s lesson plan."
        )
      );

      PageReadings.append({readings:subject.readings||[]},{resources:Object.fromEntries((subject.readings||[]).map(r=>[r.resource_id,r]))},card);
      const list = node("ul");
      for (const resource of subject.resources) {
        if (!/^https:\/\//.test(resource.url)||(subject.readings||[]).some(r=>r.url.split('#')[0]===resource.url.split('#')[0])) continue;
        const item = node("li");
        const anchor = node("a", resource.title);
        anchor.href = resource.url;
        anchor.target = "_blank";
        anchor.rel = "noopener noreferrer";
        item.append(
          node("p", resource.kind === "Primary course" ? "OPTIONAL KHAN SUPPORT" : "BOOK / SUPPORTING PRACTICE", "curriculum-label"),
          anchor,
          node("p", `${resource.provider} · ${resource.kind} · ${resource.access}`, "muted")
        );
        if (/collection|downloads/i.test(resource.kind)) {
          item.append(node("p", `Choose the activity for: ${subject.topic}.`, "muted"));
        }
        if (resource.note) item.append(node("p", resource.note, "muted"));
        list.append(item);
      }
      if(list.children.length){const support=node('details','','support-details');support.append(node('summary','Optional books & practice'),list);card.append(support);}

      const label = node("label", "", "done");
      const checkbox = node("input");
      checkbox.type = "checkbox";
      checkbox.checked = subject.completed;
      label.append(checkbox, node("span", `I finished today’s ${names[subject.key]} activities`));
      checkbox.onchange = async () => {
        checkbox.disabled = true;
        try {
          await api("/api/family/completion", {
            method: "POST",
            body: JSON.stringify({
              date: view.date,
              subject: subject.key,
              completed: checkbox.checked,
              student_id: view.student.id
            })
          });
          subject.completed = checkbox.checked;
          outer.classList.toggle("completed", checkbox.checked);
          updateProgress();
        } catch (error) {
          checkbox.checked = !checkbox.checked;
          $("status").textContent = error.message;
        } finally {
          checkbox.disabled = false;
        }
      };
      outer.append(label);
      $("cards").append(outer);
    }

    renderDailyTasks();
    updateProgress();
  } catch (error) {
    $("status").textContent = error.message;
  }
}

(async () => {
  try {
    const bootstrap = await api("/api/family/me");
    me = bootstrap.user;
    today = bootstrap.today;
    $("date").value = today;

    if (me.role === "parent") {
      $("studentLabel").hidden = false;
      const users = await api("/api/family/users");
      for (const user of users.users.filter((entry) => entry.role === "student")) {
        const option = node("option", `${user.display_name} · Grade ${user.grade}`);
        option.value = user.id;
        $("student").append(option);
      }
    }

    const q = new URLSearchParams(location.search);
    if (/^\d{4}-\d{2}-\d{2}$/.test(q.get("date") || "")) $("date").value = q.get("date");
    if (me.role === "parent" && q.get("student")) $("student").value = q.get("student");
    $("date").onchange = load;
    $("student").onchange = load;
    $("today").onclick = () => {
      $("date").value = today;
      load();
    };

    await load();
  } catch (error) {
    $("status").textContent = error.message;
  }
})();
