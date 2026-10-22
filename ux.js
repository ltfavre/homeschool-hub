/* Small, dependency-free usability helpers shared by the interactive pages.
   Everything here is progressive enhancement: pages work without it. */
(() => {
  // 1. Skip link for keyboard and screen-reader users.
  const main = document.querySelector("main");
  if (main) {
    if (!main.id) main.id = "main-content";
    if (!document.querySelector(".skip-link")) {
      const skip = document.createElement("a");
      skip.className = "skip-link";
      skip.href = "#" + main.id;
      skip.textContent = "Skip to main content";
      document.body.prepend(skip);
    }
  }

  // 2. Screen readers announce status text changes (loading, saved, errors).
  for (const el of document.querySelectorAll("#status, #message")) {
    if (!el.hasAttribute("aria-live")) el.setAttribute("aria-live", "polite");
  }

  // 3. Dialogs close when the dark backdrop is clicked.
  for (const dialog of document.querySelectorAll("dialog")) {
    dialog.addEventListener("click", (event) => {
      if (event.target !== dialog) return;
      const r = dialog.getBoundingClientRect();
      const inside = event.clientX >= r.left && event.clientX <= r.right && event.clientY >= r.top && event.clientY <= r.bottom;
      if (!inside) dialog.close();
    });
  }

  // 4. Show/hide password on password fields (helpful for children signing in).
  for (const input of document.querySelectorAll('input[type="password"]')) {
    if (input.dataset.revealReady) continue;
    input.dataset.revealReady = "1";
    const wrap = document.createElement("span");
    wrap.className = "password-field";
    input.parentNode.insertBefore(wrap, input);
    wrap.append(input);
    const toggle = document.createElement("button");
    toggle.type = "button";
    toggle.className = "reveal-toggle";
    toggle.textContent = "Show";
    toggle.setAttribute("aria-label", "Show password");
    toggle.setAttribute("aria-pressed", "false");
    toggle.addEventListener("click", () => {
      const show = input.type === "password";
      input.type = show ? "text" : "password";
      toggle.textContent = show ? "Hide" : "Show";
      toggle.setAttribute("aria-label", show ? "Hide password" : "Show password");
      toggle.setAttribute("aria-pressed", String(show));
    });
    wrap.append(toggle);
  }
})();
