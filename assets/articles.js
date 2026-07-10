// GratisAPI — articles list + reader. One script serves both pages; it detects
// which one it is on by the elements present. All fetches are origin-relative.
(function () {
  "use strict";

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === "class") node.className = attrs[k];
      else if (k === "text") node.textContent = attrs[k];
      else node.setAttribute(k, attrs[k]);
    });
    (children || []).forEach(function (c) {
      node.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
    });
    return node;
  }

  function fmtDate(s) {
    if (!s) return "";
    var d = new Date(s + "T00:00:00Z");
    if (isNaN(d)) return s;
    return d.toLocaleDateString("en-US", { year: "numeric", month: "short", day: "numeric", timeZone: "UTC" });
  }

  // ---------- Reader page ----------
  var view = document.getElementById("article-view");
  if (view) {
    var id = new URLSearchParams(location.search).get("id") || "";
    if (!/^[A-Za-z0-9._-]+$/.test(id)) {
      view.innerHTML = "";
      view.appendChild(el("p", { text: "Unknown article." }));
      return;
    }
    fetch("../api/articles/" + id + ".json")
      .then(function (r) { if (!r.ok) throw new Error("404"); return r.json(); })
      .then(function (a) {
        document.title = a.title + " — GratisAPI";
        view.innerHTML = "";
        view.appendChild(el("div", { class: "eyebrow", text: a.category || "Article" }));
        view.appendChild(el("h1", { text: a.title }));
        var meta = el("div", { class: "article-meta-line" }, [
          el("span", { text: (a.author || "GratisAPI") }),
          el("span", { text: fmtDate(a.date) }),
          el("span", { text: (a.reading_time_min || 1) + " min read" }),
        ]);
        view.appendChild(meta);
        (String(a.body || "").split(/\n\n+/)).forEach(function (para) {
          if (para.trim()) view.appendChild(el("p", { text: para.trim() }));
        });
        if (a.tags && a.tags.length) {
          var tags = el("p", { class: "article-card tags" });
          tags.className = "tags";
          tags.style.marginTop = "28px";
          a.tags.forEach(function (t) {
            tags.appendChild(el("span", { text: "#" + t, style: "font-size:0.75rem;color:var(--text-dim);background:var(--bg-soft);border:1px solid var(--border-soft);padding:3px 10px;border-radius:999px;margin-right:6px" }));
          });
          view.appendChild(tags);
        }
        view.appendChild(el("p", { style: "margin-top:36px" }, [
          (function () { var a2 = el("a", { class: "btn ghost", href: "./" }); a2.textContent = "← Back to all articles"; return a2; })(),
        ]));
      })
      .catch(function () {
        view.innerHTML = "";
        view.appendChild(el("h1", { text: "Article not found" }));
        view.appendChild(el("p", { text: "We couldn't find that article. It may have been renamed." }));
        var back = el("a", { class: "btn primary", href: "./" }); back.textContent = "Browse all articles";
        view.appendChild(back);
      });
    return;
  }

  // ---------- List page ----------
  var grid = document.getElementById("article-grid");
  if (!grid) return;
  var filtersEl = document.getElementById("filters");
  var searchEl = document.getElementById("search");
  var countEl = document.getElementById("count");
  var state = { all: [], category: "All", query: "" };

  function render() {
    var q = state.query.trim().toLowerCase();
    var items = state.all.filter(function (a) {
      if (state.category !== "All" && a.category !== state.category) return false;
      if (!q) return true;
      return (a.title + " " + (a.summary || "") + " " + (a.tags || []).join(" ")).toLowerCase().indexOf(q) >= 0;
    });
    countEl.textContent = items.length + " article" + (items.length === 1 ? "" : "s");
    grid.innerHTML = "";
    if (!items.length) { grid.appendChild(el("p", { text: "No articles match your search." })); return; }
    items.forEach(function (a) {
      var card = el("a", { class: "article-card", href: "article.html?id=" + encodeURIComponent(a.id) }, [
        el("div", { class: "meta" }, [
          el("span", { class: "cat", text: a.category || "Article" }),
          el("span", { text: fmtDate(a.date) }),
          el("span", { text: (a.reading_time_min || 1) + " min" }),
        ]),
        el("h3", { text: a.title }),
        el("p", { text: a.summary || "" }),
        el("div", { class: "tags" }, (a.tags || []).slice(0, 3).map(function (t) { return el("span", { text: "#" + t }); })),
      ]);
      grid.appendChild(card);
    });
  }

  fetch("../api/articles/index.json")
    .then(function (r) { return r.json(); })
    .then(function (d) {
      state.all = d.results || [];
      var cats = ["All"].concat(Object.keys(state.all.reduce(function (m, a) { if (a.category) m[a.category] = 1; return m; }, {})).sort());
      cats.forEach(function (c) {
        var chip = el("button", { class: "chip" + (c === "All" ? " active" : ""), text: c });
        chip.onclick = function () {
          state.category = c;
          Array.prototype.forEach.call(filtersEl.children, function (b) { b.classList.toggle("active", b.textContent === c); });
          render();
        };
        filtersEl.appendChild(chip);
      });
      if (searchEl) searchEl.addEventListener("input", function () { state.query = searchEl.value; render(); });
      render();
    })
    .catch(function () {
      grid.innerHTML = "";
      grid.appendChild(el("p", { text: "Could not load articles. If viewing locally, serve the folder over HTTP." }));
    });
})();
