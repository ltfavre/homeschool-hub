import test from "node:test";
import assert from "node:assert/strict";
import {
  mapTasksToUsers,
  normalizeVenvlearningPayload,
  normalizeVenvlearningTask
} from "./venvlearning-sync.js";

test("normalizeVenvlearningTask maps required fields", () => {
  const result = normalizeVenvlearningTask({
    id: "task-101",
    title: "Read chapter 2",
    assignee: "4th Grader",
    dueDate: "2026-10-14T08:00:00-05:00",
    status: "in progress"
  });

  assert.equal(result.ok, true);
  assert.equal(result.task.external_id, "task-101");
  assert.equal(result.task.title, "Read chapter 2");
  assert.equal(result.task.assignee, "4th Grader");
  assert.equal(result.task.due_date, "2026-10-14");
  assert.equal(result.task.status, "in_progress");
});

test("normalizeVenvlearningPayload collects invalid records", () => {
  const output = normalizeVenvlearningPayload({
    tasks: [
      { id: "ok-1", title: "Math practice", assignee: "7th Grader", due_date: "2026-10-14" },
      { id: "bad-1", title: "", assignee: "7th Grader", due_date: "2026-10-14" }
    ]
  });

  assert.equal(output.total, 2);
  assert.equal(output.tasks.length, 1);
  assert.equal(output.errors.length, 1);
});

test("mapTasksToUsers respects explicit student map then name matching", () => {
  const users = [
    { id: "student-4", display_name: "4th Grader", username: "grade4" },
    { id: "student-7", display_name: "7th Grader", username: "grade7" }
  ];
  const tasks = [
    { external_id: "a", title: "A", assignee: "Learner One", due_date: "2026-10-14", source: "venvlearning", status: "pending" },
    { external_id: "b", title: "B", assignee: "7th Grader", due_date: "2026-10-14", source: "venvlearning", status: "pending" },
    { external_id: "c", title: "C", assignee: "Unknown", due_date: "2026-10-14", source: "venvlearning", status: "pending" }
  ];

  const mapped = mapTasksToUsers(tasks, users, { "Learner One": "student-4" });
  assert.equal(mapped.mapped.length, 2);
  assert.equal(mapped.unmapped.length, 1);
  assert.equal(mapped.mapped[0].user_id, "student-4");
  assert.equal(mapped.mapped[1].user_id, "student-7");
});
