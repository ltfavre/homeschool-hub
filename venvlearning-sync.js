const TASK_SOURCE = "venvlearning";
const STATUS_MAP = {
  complete: "completed",
  completed: "completed",
  done: "completed",
  inprogress: "in_progress",
  in_progress: "in_progress",
  started: "in_progress",
  active: "in_progress",
  pending: "pending",
  todo: "pending",
  assigned: "pending",
  overdue: "overdue",
  late: "overdue",
  cancelled: "cancelled",
  canceled: "cancelled"
};

function clean(value) {
  if (value === undefined || value === null) return "";
  return String(value).trim();
}

function toDateOnly(input) {
  const value = clean(input);
  if (!value) return null;
  if (/^\d{4}-\d{2}-\d{2}$/.test(value)) return value;
  const parsed = new Date(value);
  if (Number.isNaN(parsed.getTime())) return null;
  return parsed.toISOString().slice(0, 10);
}

function normalizedStatus(value) {
  if (typeof value === "boolean") return value ? "completed" : "pending";
  const key = clean(value).toLowerCase().replace(/\s+/g, "_");
  return STATUS_MAP[key] || "pending";
}

function taskArrayFromPayload(payload) {
  if (Array.isArray(payload)) return payload;
  if (!payload || typeof payload !== "object") return [];
  if (Array.isArray(payload.tasks)) return payload.tasks;
  if (Array.isArray(payload.items)) return payload.items;
  if (payload.data && Array.isArray(payload.data.tasks)) return payload.data.tasks;
  if (Array.isArray(payload.data)) return payload.data;
  return [];
}

function stableExternalId(rawTask) {
  const fallback = JSON.stringify({
    title: clean(rawTask.title || rawTask.name || rawTask.task_title),
    due: clean(rawTask.due_date || rawTask.dueDate || rawTask.date),
    assignee: clean(rawTask.assignee || rawTask.child || rawTask.student || rawTask.student_name)
  });
  let hash = 0;
  for (let i = 0; i < fallback.length; i++) {
    hash = ((hash << 5) - hash + fallback.charCodeAt(i)) | 0;
  }
  return `derived-${Math.abs(hash)}`;
}

function extractAssignee(rawTask) {
  return clean(
    rawTask.assignee ||
    rawTask.child ||
    rawTask.student ||
    rawTask.student_name ||
    rawTask.learner ||
    rawTask.user
  );
}

export function normalizeVenvlearningTask(rawTask) {
  const title = clean(rawTask.title || rawTask.name || rawTask.task_title || rawTask.description);
  const dueDate = toDateOnly(rawTask.due_date || rawTask.dueDate || rawTask.date || rawTask.assigned_for);
  const assignee = extractAssignee(rawTask);
  if (!title || !dueDate || !assignee) {
    return {
      ok: false,
      error: "Task is missing required title, due date, or assignee",
      rawTask
    };
  }

  return {
    ok: true,
    task: {
      source: TASK_SOURCE,
      external_id: clean(rawTask.external_id || rawTask.task_id || rawTask.id || rawTask.uuid) || stableExternalId(rawTask),
      title,
      assignee,
      due_date: dueDate,
      status: normalizedStatus(rawTask.status ?? rawTask.completed),
      payload_json: JSON.stringify(rawTask)
    }
  };
}

export function normalizeVenvlearningPayload(payload) {
  const rawTasks = taskArrayFromPayload(payload);
  const normalized = [];
  const errors = [];
  for (const rawTask of rawTasks) {
    const result = normalizeVenvlearningTask(rawTask || {});
    if (result.ok) normalized.push(result.task);
    else errors.push(result.error);
  }
  return { tasks: normalized, errors, total: rawTasks.length };
}

export function resolveAssigneeUserId(taskAssignee, users, mapping = {}) {
  const explicit = mapping[taskAssignee];
  if (explicit) return String(explicit);

  const normalized = taskAssignee.toLowerCase();
  const byName = users.find((user) =>
    String(user.display_name || "").trim().toLowerCase() === normalized ||
    String(user.username || "").trim().toLowerCase() === normalized
  );
  return byName ? String(byName.id) : null;
}

export function mapTasksToUsers(tasks, users, mapping = {}) {
  const mapped = [];
  const unmapped = [];
  for (const task of tasks) {
    const userId = resolveAssigneeUserId(task.assignee, users, mapping);
    if (!userId) {
      unmapped.push(task);
      continue;
    }
    mapped.push({
      ...task,
      user_id: userId
    });
  }
  return { mapped, unmapped };
}

export const VENVLEARNING_TASK_SOURCE = TASK_SOURCE;
