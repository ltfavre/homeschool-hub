// Shared file helpers for the Library and Assignments pages.
window.VenvFiles = (() => {
  const MAX = 25 * 1024 * 1024;
  const ACCEPT = ".pdf,.png,.jpg,.jpeg,.gif,.webp,.heic,.txt,.csv,.rtf,.md,.doc,.docx,.xls,.xlsx,.ppt,.pptx,.odt,.ods,.odp,.epub,.mp3,.m4a,.wav,.mp4,.mov,.zip";

  const size = (n) => (n < 1024 ? `${n} B` : n < 1048576 ? `${Math.round(n / 1024)} KB` : `${(n / 1048576).toFixed(1)} MB`);
  const icon = (mime = "") => (mime.includes("pdf") ? "PDF" : mime.startsWith("image/") ? "IMG" : mime.startsWith("audio/") ? "AUD" : mime.startsWith("video/") ? "VID" : /sheet|excel|csv/.test(mime) ? "XLS" : /presentation|powerpoint/.test(mime) ? "PPT" : /word|opendocument.text|rtf/.test(mime) ? "DOC" : "FILE");

  // Upload one file. params become the query string (kind, title, subject, audience, assignment_id).
  async function upload(file, params = {}) {
    if (file.size > MAX) throw new Error(`${file.name} is larger than 25 MB.`);
    const qs = new URLSearchParams(Object.entries(params).filter(([, v]) => v !== undefined && v !== null && v !== ""));
    const r = await fetch("/api/family/files?" + qs, { method: "POST", headers: { "x-venv-upload": "1", "x-file-name": encodeURIComponent(file.name) }, body: file });
    if (r.status === 401) { location.replace("/login"); throw new Error("Please sign in."); }
    const b = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(b.error || `Upload failed (${r.status})`);
    return b.file;
  }

  // A link row for one stored file.
  function link(f, el, extra) {
    const row = el("div", "", "vf-file");
    row.append(el("span", icon(f.mime), "vf-icon"));
    const a = el("a", f.title || f.name);
    a.href = f.url; a.target = "_blank"; a.rel = "noopener";
    const meta = el("span", `${f.name} · ${size(f.size)}`, "muted lms-small");
    const text = el("span", "", "vf-text"); text.append(a, meta);
    row.append(text);
    if (extra) row.append(extra);
    return row;
  }

  // A drop zone + file picker. onFiles receives an array of File objects.
  function picker(el, onFiles, { multiple = true, label = "Choose files or drop them here" } = {}) {
    const zone = el("label", "", "vf-drop");
    const input = el("input"); input.type = "file"; input.multiple = multiple; input.accept = ACCEPT; input.className = "vf-input";
    zone.append(input, el("span", label, "vf-drop-label"), el("span", "PDF, Word, Excel, PowerPoint, images, audio or video · up to 25 MB each", "muted lms-small"));
    input.onchange = () => { if (input.files.length) onFiles([...input.files]); input.value = ""; };
    for (const ev of ["dragenter", "dragover"]) zone.addEventListener(ev, (e) => { e.preventDefault(); zone.classList.add("is-over"); });
    for (const ev of ["dragleave", "drop"]) zone.addEventListener(ev, (e) => { e.preventDefault(); zone.classList.remove("is-over"); });
    zone.addEventListener("drop", (e) => { const files = [...(e.dataTransfer?.files || [])]; if (files.length) onFiles(multiple ? files : files.slice(0, 1)); });
    return zone;
  }

  return { upload, link, picker, size, icon, MAX, ACCEPT };
})();
