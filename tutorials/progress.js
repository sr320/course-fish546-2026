/* Progress bar + persistence for FISH 546 tutorials.
   Each tutorial sets window.TUTORIAL_KEY. Checkbox state is stored in localStorage
   so students don't lose progress between sessions. */
(function () {
  var key = window.TUTORIAL_KEY || "fish546-tutorial";
  var boxes = Array.prototype.slice.call(document.querySelectorAll(".check input[type=checkbox]"));
  var bar = document.querySelector(".bar > i");
  var pct = document.querySelector(".prog-pct");

  function save() {
    var state = boxes.map(function (b) { return b.checked ? 1 : 0; });
    try { localStorage.setItem(key, JSON.stringify(state)); } catch (e) {}
  }
  function render() {
    var done = boxes.filter(function (b) { return b.checked; }).length;
    var frac = boxes.length ? done / boxes.length : 0;
    if (bar) bar.style.width = Math.round(frac * 100) + "%";
    if (pct) pct.textContent = done + "/" + boxes.length;
  }
  function load() {
    try {
      var saved = JSON.parse(localStorage.getItem(key) || "[]");
      boxes.forEach(function (b, i) { if (saved[i]) b.checked = true; });
    } catch (e) {}
  }

  boxes.forEach(function (b) {
    b.addEventListener("change", function () { save(); render(); });
  });
  load();
  render();

  // Scroll-spy: highlight the active section in the sidebar.
  var links = Array.prototype.slice.call(document.querySelectorAll("nav.side a[href^='#']"));
  var sections = links.map(function (l) { return document.querySelector(l.getAttribute("href")); });
  window.addEventListener("scroll", function () {
    var y = window.scrollY + 120, idx = 0;
    sections.forEach(function (s, i) { if (s && s.offsetTop <= y) idx = i; });
    links.forEach(function (l, i) { l.classList.toggle("active", i === idx); });
  });
})();
