// GratisAPI — articles list + reader. One script serves both pages; it detects
// which one it is on by the elements present. All fetches use clean API URLs.
(function () {
  "use strict";

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === "class") node.className = attrs[k];
      else if (k === "text") node.textContent = attrs[k];
      else if (k === "html") node.innerHTML = attrs[k];
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

  function highlight(obj) {
    var json = JSON.stringify(obj, null, 2);
    json = json.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    return json.replace(
      /("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g,
      function (m) {
        var cls = "n";
        if (/^"/.test(m)) cls = /:$/.test(m) ? "k" : "s";
        else if (/true|false|null/.test(m)) cls = "b";
        return '<span class="' + cls + '">' + m + "</span>";
      }
    );
  }

  // ---------- "Try it" API panel (bottom of every article) ----------
  function buildTryIt(apiSlug) {
    var wrap = el("div", { class: "tryit" });
    wrap.appendChild(el("div", { class: "tryit-head" }, [
      el("span", { class: "tryit-badge", text: "Try it" }),
      el("span", { class: "tryit-lead", text: "This is a live, free API — no key needed. Run it right now:" }),
    ]));
    var bar = el("div", { class: "tryit-bar" }, [
      el("span", { class: "dot r" }), el("span", { class: "dot y" }), el("span", { class: "dot g" }),
      el("code", { class: "tryit-url", text: "GET /api/" + apiSlug }),
    ]);
    var pre = el("pre", { class: "tryit-json", text: "loading…" });
    var actions = el("div", { class: "tryit-actions" });
    wrap.appendChild(bar);
    wrap.appendChild(pre);
    wrap.appendChild(actions);

    function show(rec) {
      var pretty = {};
      Object.keys(rec).forEach(function (k) { if (k !== "url" && k !== "body") pretty[k] = rec[k]; });
      bar.querySelector(".tryit-url").textContent = "GET " + (rec.url ? rec.url.replace(/^https?:\/\/[^/]+/, "") : "/api/" + apiSlug);
      pre.innerHTML = highlight(pretty);
    }

    fetch("../api/" + apiSlug + "/index").then(function (r) { return r.json(); }).then(function (d) {
      var recs = d.results || [];
      if (!recs.length) { pre.textContent = "No data."; return; }
      var pick = function () { show(recs[Math.floor(Math.random() * recs.length)]); };
      pick();
      var again = el("button", { class: "btn ghost", text: "🎲 Another record" });
      again.onclick = pick;
      var explore = el("a", { class: "btn ghost", href: "../#apis", text: "Explore all APIs →" });
      var docs = el("a", { class: "btn ghost", href: "../docs/", text: "API docs →" });
      actions.appendChild(again); actions.appendChild(explore); actions.appendChild(docs);
    }).catch(function () {
      pre.textContent = "Could not reach /api/" + apiSlug + " right now.";
    });
    return wrap;
  }

  // ---------- Reader page ----------
  var view = document.getElementById("article-view");
  if (view) {
    var id = new URLSearchParams(location.search).get("id") || "";
    if (!/^[A-Za-z0-9._-]+$/.test(id)) { view.innerHTML = ""; view.appendChild(el("p", { text: "Unknown article." })); return; }
    fetch("../api/articles/" + id).then(function (r) { if (!r.ok) throw 0; return r.json(); }).then(function (a) {
      document.title = a.title + " — GratisAPI";
      view.innerHTML = "";
      view.appendChild(el("div", { class: "eyebrow", text: a.category || "Article" }));
      view.appendChild(el("h1", { text: a.title }));
      view.appendChild(el("div", { class: "article-meta-line" }, [
        el("span", { text: a.author || "GratisAPI" }),
        el("span", { text: fmtDate(a.date) }),
        el("span", { text: (a.reading_time_min || 1) + " min read" }),
      ]));
      String(a.body || "").split(/\n\n+/).forEach(function (p) {
        if (p.trim()) view.appendChild(el("p", { text: p.trim() }));
      });
      if (a.tags && a.tags.length) {
        var tags = el("p", { style: "margin-top:26px" });
        a.tags.forEach(function (t) {
          tags.appendChild(el("span", { text: "#" + t, style: "font-size:0.75rem;color:var(--text-dim);background:var(--bg-soft);border:1px solid var(--border-soft);padding:3px 10px;border-radius:999px;margin-right:6px;display:inline-block;margin-bottom:6px" }));
        });
        view.appendChild(tags);
      }
      // Live "Try it" API panel — on every article.
      view.appendChild(buildTryIt(a.try_api || "quotes"));
      view.appendChild(el("p", { style: "margin-top:30px" }, [
        (function () { var b = el("a", { class: "btn ghost", href: "./" }); b.textContent = "← All articles"; return b; })(),
      ]));
    }).catch(function () {
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
      grid.appendChild(el("a", { class: "article-card", href: "article.html?id=" + encodeURIComponent(a.id) }, [
        el("div", { class: "meta" }, [
          el("span", { class: "cat", text: a.category || "Article" }),
          el("span", { text: fmtDate(a.date) }),
          el("span", { text: (a.reading_time_min || 1) + " min" }),
        ]),
        el("h3", { text: a.title }),
        el("p", { text: a.summary || "" }),
        el("div", { class: "tags" }, (a.tags || []).slice(0, 3).map(function (t) { return el("span", { text: "#" + t }); })),
      ]));
    });
  }

  fetch("../api/articles/index").then(function (r) { return r.json(); }).then(function (d) {
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
  }).catch(function () {
    grid.innerHTML = "";
    grid.appendChild(el("p", { text: "Could not load articles. If viewing locally, serve the folder over HTTP." }));
  });
})();
