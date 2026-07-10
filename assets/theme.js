// Light/dark theme toggle. The initial theme is applied pre-paint by a tiny
// inline script in each page's <head>; this adds the toggle button and persists
// the user's choice to localStorage.
(function () {
  "use strict";
  var root = document.documentElement;

  function current() {
    return root.getAttribute("data-theme") === "light" ? "light" : "dark";
  }
  function icon() { return current() === "light" ? "🌙" : "☀️"; }

  function apply(theme) {
    root.setAttribute("data-theme", theme);
    try { localStorage.setItem("ga-theme", theme); } catch (e) {}
    if (btn) { btn.textContent = icon(); btn.setAttribute("aria-label", "Switch to " + (theme === "light" ? "dark" : "light") + " mode"); }
  }

  var links = document.querySelector(".nav .links");
  var btn = document.createElement("button");
  btn.className = "theme-toggle";
  btn.type = "button";
  btn.textContent = icon();
  btn.setAttribute("aria-label", "Toggle theme");
  btn.onclick = function () { apply(current() === "light" ? "dark" : "light"); };
  if (links) links.appendChild(btn);
})();
