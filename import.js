const $ = (s) => document.querySelector(s);

let records = [];
let rawDefaults = {};
let currentFileName = "";

const escapeHtml = (v) =>
  String(v ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");

function parseCSV(text) {
  const rows = [];
  let row = [];
  let cell = "";
  let quoted = false;

  for (let i = 0; i < text.length; i++) {
    const ch = text[i];
    const next = text[i + 1];

    if (ch === '"') {
      if (quoted && next === '"') {
        cell += '"';
        i++;
      } else {
        quoted = !quoted;
      }
      continue;
    }

    if (ch === "," && !quoted) {
      row.push(cell);
      cell = "";
      continue;
    }

    if ((ch === "\n" || ch === "\r") && !quoted) {
      if (ch === "\r" && next === "\n") i++;
      row.push(cell);
      cell = "";
      if (row.some((v) => String(v).trim() !== "")) rows.push(row);
      row = [];
      continue;
    }

    cell += ch;
  }

  if (cell.length || row.length) {
    row.push(cell);
    if (row.some((v) => String(v).trim() !== "")) rows.push(row);
  }

  if (!rows.length) return [];

  const headers = rows[0].map((h) => h.trim());
  return rows.slice(1).map((values) => {
    const out = {};
    headers.forEach((header, idx) => {
      const value = values[idx] ?? "";
      out[header] = value.trim();
    });
    return out;
  });
}

function normalizeRecord(r) {
  const out = { ...r };

  // Convert empty strings to null-like omissions.
  Object.keys(out).forEach((k) => {
    if (typeof out[k] === "string" && out[k].trim() === "") delete out[k];
  });

  // CSV-friendly aliases.
  if (!out.lesson_date && !out.due_date && out.date) {
    const type = String(out.record_type || out.type || "lesson").toLowerCase();
    if (type === "assignment") out.due_date = out.date;
    else out.lesson_date = out.date;
  }

  ["segment", "week", "estimated_minutes", "points_possible", "student_id", "subject_id", "lesson_id"]
    .forEach((k) => {
      if (out[k] !== undefined && out[k] !== "") {
        const n = Number(out[k]);
        if (Number.isFinite(n)) out[k] = n;
      }
    });

  return out;
}

function parseJSON(text) {
  const parsed = JSON.parse(text);

  if (Array.isArray(parsed)) {
    return { records: parsed, defaults: {} };
  }

  if (!parsed || !Array.isArray(parsed.records)) {
    throw new Error("JSON must be an array or an object with a records array.");
  }

  return {
    records: parsed.records,
    defaults: parsed.defaults || {}
  };
}

function setFileMeta(file) {
  $("#fileMeta").classList.remove("hidden");
  $("#fileMeta").innerHTML = `
    <strong>${escapeHtml(file.name)}</strong>
    <span>${Math.max(1, Math.round(file.size / 1024))} KB · ${records.length} record${records.length === 1 ? "" : "s"}</span>
  `;
}

function dateFor(r) {
  return r.lesson_date || r.due_date || r.date || "";
}

function studentFor(r) {
  if (r.student_name) return r.student_name;
  if (r.grade) return `Grade ${r.grade}`;
  if (r.student_id) return `Student #${r.student_id}`;
  return "—";
}

function renderPreview() {
  const lessons = records.filter((r) =>
    String(r.record_type || r.type || "lesson").toLowerCase() === "lesson"
  ).length;
  const assignments = records.length - lessons;

  $("#summaryCards").innerHTML = `
    <div><strong>${records.length}</strong><span>Total records</span></div>
    <div><strong>${lessons}</strong><span>Lessons</span></div>
    <div><strong>${assignments}</strong><span>Assignments</span></div>
  `;

  if (!records.length) {
    $("#previewBody").innerHTML =
      `<tr><td colspan="7" class="empty-cell">No records found.</td></tr>`;
    $("#validateBtn").disabled = true;
    $("#importBtn").disabled = true;
    return;
  }

  $("#previewBody").innerHTML = records.slice(0, 200).map((r, idx) => {
    const type = String(r.record_type || r.type || "lesson").toLowerCase();
    return `
      <tr>
        <td>${idx + 1}</td>
        <td><span class="pill">${escapeHtml(type)}</span></td>
        <td>${escapeHtml(studentFor(r))}</td>
        <td>${escapeHtml(r.subject || r.subject_id || "—")}</td>
        <td>${escapeHtml(r.title || "—")}</td>
        <td>${escapeHtml(dateFor(r) || "—")}</td>
        <td class="mono">${escapeHtml(r.external_id || "—")}</td>
      </tr>
    `;
  }).join("");

  if (records.length > 200) {
    $("#previewBody").insertAdjacentHTML(
      "beforeend",
      `<tr><td colspan="7" class="empty-cell">Showing first 200 of ${records.length} records.</td></tr>`
    );
  }

  $("#validateBtn").disabled = false;
  $("#importBtn").disabled = false;
}

async function loadFile(file) {
  if (!file) return;

  currentFileName = file.name;
  const text = await file.text();
  const lower = file.name.toLowerCase();

  if (lower.endsWith(".json")) {
    const parsed = parseJSON(text);
    records = parsed.records.map(normalizeRecord);
    rawDefaults = parsed.defaults || {};
    if (rawDefaults.source_name && !$("#sourceInput").value) {
      $("#sourceInput").value = rawDefaults.source_name;
    }
  } else if (lower.endsWith(".csv")) {
    records = parseCSV(text).map(normalizeRecord);
    rawDefaults = {};
  } else {
    throw new Error("Choose a .csv or .json file.");
  }

  setFileMeta(file);
  renderPreview();
  hideResult();
}

function token() {
  return $("#tokenInput").value.trim();
}

function makePayload(dryRun) {
  const defaults = { ...rawDefaults };
  const source = $("#sourceInput").value.trim();
  if (source) defaults.source_name = source;

  return {
    dry_run: dryRun,
    defaults,
    records
  };
}

async function sendImport(dryRun) {
  if (!records.length) throw new Error("Choose a file first.");
  if (!token()) throw new Error("Paste your IMPORT_TOKEN.");

  const button = dryRun ? $("#validateBtn") : $("#importBtn");
  const original = button.textContent;
  button.disabled = true;
  button.textContent = dryRun ? "Validating…" : "Importing…";

  try {
    const response = await fetch("/api/import", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        "authorization": `Bearer ${token()}`
      },
      body: JSON.stringify(makePayload(dryRun))
    });

    const data = await response.json().catch(() => ({}));

    if (!response.ok && !data.summary) {
      throw new Error(data.error || `Request failed with ${response.status}`);
    }

    showResult(data, dryRun);

    if (!dryRun && data.summary?.failed === 0) {
      $("#importBtn").textContent = "Imported ✓";
    }
  } finally {
    button.disabled = false;
    if (button.textContent !== "Imported ✓") button.textContent = original;
  }
}

function showResult(data, dryRun) {
  const card = $("#resultCard");
  card.classList.remove("hidden");

  const s = data.summary || {
    total: records.length,
    inserted: 0,
    updated: 0,
    failed: 0
  };

  $("#resultTitle").textContent = dryRun
    ? (s.failed ? "Validation found problems" : "Validation passed")
    : (s.failed ? "Import completed with errors" : "Import complete");

  $("#resultSubtitle").textContent = dryRun
    ? "No database records were changed."
    : `${currentFileName || "File"} was processed by Homeschool Hub.`;

  $("#resultSummary").innerHTML = `
    <div><strong>${s.total ?? 0}</strong><span>Processed</span></div>
    <div><strong>${s.inserted ?? 0}</strong><span>Inserted</span></div>
    <div><strong>${s.updated ?? 0}</strong><span>Updated</span></div>
    <div><strong>${s.failed ?? 0}</strong><span>Failed</span></div>
  `;

  const failures = (data.results || []).filter((r) => r.action === "failed");
  $("#resultErrors").innerHTML = failures.length
    ? `<div class="error-list">
         <h4>Rows needing attention</h4>
         ${failures.map((r) =>
           `<div><strong>Row ${r.row}</strong> · ${escapeHtml(r.error || "Unknown error")}</div>`
         ).join("")}
       </div>`
    : `<div class="success-box">${dryRun
        ? "Everything is valid. You can import these records."
        : "All records were imported successfully."}</div>`;

  card.scrollIntoView({ behavior: "smooth", block: "start" });
}

function hideResult() {
  $("#resultCard").classList.add("hidden");
}

function handleError(err) {
  alert(err.message || String(err));
}

const drop = $("#dropZone");
const input = $("#fileInput");

drop.addEventListener("click", () => input.click());
drop.addEventListener("keydown", (e) => {
  if (e.key === "Enter" || e.key === " ") input.click();
});
drop.addEventListener("dragover", (e) => {
  e.preventDefault();
  drop.classList.add("dragging");
});
drop.addEventListener("dragleave", () => drop.classList.remove("dragging"));
drop.addEventListener("drop", (e) => {
  e.preventDefault();
  drop.classList.remove("dragging");
  loadFile(e.dataTransfer.files?.[0]).catch(handleError);
});

input.addEventListener("change", () => {
  loadFile(input.files?.[0]).catch(handleError);
});

$("#rememberToken").addEventListener("change", (e) => {
  if (e.target.checked && token()) sessionStorage.setItem("hhImportToken", token());
  if (!e.target.checked) sessionStorage.removeItem("hhImportToken");
});

$("#tokenInput").addEventListener("input", () => {
  if ($("#rememberToken").checked) {
    sessionStorage.setItem("hhImportToken", token());
  }
});

$("#validateBtn").addEventListener("click", () => {
  sendImport(true).catch(handleError);
});

$("#importBtn").addEventListener("click", async () => {
  const confirmed = confirm(
    `Import ${records.length} record${records.length === 1 ? "" : "s"} into Homeschool Hub?`
  );
  if (!confirmed) return;

  sendImport(false).catch(handleError);
});

const saved = sessionStorage.getItem("hhImportToken");
if (saved) {
  $("#tokenInput").value = saved;
  $("#rememberToken").checked = true;
}

renderPreview();
