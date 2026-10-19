const $ = (id) => document.getElementById(id);
const node = (tag, text = "", cls = "") => {
  const element = document.createElement(tag);
  element.textContent = text;
  element.className = cls;
  return element;
};

const names = {math:'Math',ela:'ELA',science:'Physical Sciences',social:'Social Studies',spanish:'Spanish',art:'Art',life:'Life Sciences',computer:'Computer Science',skills:'Life Skills',review:'Friday Review / Projects / Catch-up'};

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
  $("status").textContent = `${done} of ${view.subjects.length} subjects complete · Saved to this account`;
}

async function load() {
  try {
    $("status").textContent = "Loading agenda…";
    const date = $("date").value || today;
    const studentQuery = me.role === "parent" ? `&student=${$("student").value}` : "";
    view = await api(`/api/family/agenda?date=${date}${studentQuery}`);

    $("cards").replaceChildren();
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

    $("printPacket").hidden = !view.teaching;
    if (!view.teaching) {
      $("summary").append(node("p", "No teaching activities are scheduled for this date."));
      if (view.next_date) $("summary").append(node("p", `Next teaching day: ${view.next_date}`));
      $("status").textContent = "Weekend, break, or a day outside the teaching calendar.";
      renderDailyTasks();
      return;
    }

    $("printPacket").href = view.print_url;
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

    KhanUI.assessments(view.primary_assessments, $("summary"));if(view.integration)$("summary").append(node("p","Weekly connections: "+view.integration));

    for (const subject of view.subjects) {
      const card = node("article", "", `agenda-card${subject.completed ? " completed" : ""}`);
      card.append(node("p", (names[subject.key]||subject.key).toUpperCase(), "eyebrow"), node("h2", subject.topic));
      KhanUI.priority(subject, card);

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

      const list = node("ul");
      for (const resource of subject.resources) {
        if (!/^https:\/\//.test(resource.url)) continue;
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
      card.append(list);

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
          card.classList.toggle("completed", checkbox.checked);
          updateProgress();
        } catch (error) {
          checkbox.checked = !checkbox.checked;
          $("status").textContent = error.message;
        } finally {
          checkbox.disabled = false;
        }
      };
      card.append(label);
      $("cards").append(card);
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
