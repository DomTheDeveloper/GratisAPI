// GratisAPI homepage — live API index, explorer, card search and the hero
// "Surprise me" toy. Every fetch uses the clean, extension-less API URLs.
(function () {
  "use strict";

  var API_INDEX = "api/index";

  // Records carry absolute production URLs; fetch them relative to wherever the
  // site is actually hosted so the page works on forks and locally too.
  function rel(url) {
    var i = url.indexOf("/api/");
    return i >= 0 ? url.slice(i + 1) : url;
  }
  function pathOf(url) { return url.replace(/^https?:\/\/[^/]+/, ""); }

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === "class") node.className = attrs[k];
      else if (k === "html") node.innerHTML = attrs[k];
      else if (k === "text") node.textContent = attrs[k];
      else node.setAttribute(k, attrs[k]);
    });
    (children || []).forEach(function (c) {
      node.appendChild(typeof c === "string" ? document.createTextNode(c) : c);
    });
    return node;
  }

  // Minimal, safe JSON pretty-printer with syntax highlighting.
  function highlight(obj) {
    var json = JSON.stringify(obj, null, 2);
    json = json.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    return json.replace(
      /("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g,
      function (match) {
        var cls = "n";
        if (/^"/.test(match)) cls = /:$/.test(match) ? "k" : "s";
        else if (/true|false|null/.test(match)) cls = "b";
        return '<span class="' + cls + '">' + match + "</span>";
      }
    );
  }

  function fmt(n) { return n.toLocaleString("en-US"); }
  // Round DOWN to the leading digit and add "+": 116 -> "100+", 3890 -> "3,000+".
  function roundy(n) {
    if (n < 10) return String(n);
    var mag = Math.pow(10, Math.floor(Math.log10(n)));
    return fmt(Math.floor(n / mag) * mag) + "+";
  }

  var state = { apis: [], current: null };

  // ---------- Explorer ----------
  function setActive(label) {
    Array.prototype.forEach.call(
      document.querySelectorAll("#explorer-list button"),
      function (b) { b.classList.toggle("active", b.dataset.label === label); }
    );
  }

  // Render an object we already have (a record, or the index) — no fetch needed,
  // which is important for list-only APIs that have no per-record files.
  function showObject(url, obj, label) {
    var codeEl = document.getElementById("explorer-code");
    document.getElementById("explorer-url").textContent = "GET " + pathOf(url);
    var data = obj;
    if (data && data.results && data.results.length > 6) {
      data = Object.assign({}, obj);
      data.results = obj.results.slice(0, 3);
      data["…"] = "(" + (obj.count - 3) + " more records — fetch the endpoint to see them all)";
    }
    codeEl.innerHTML = highlight(data);
    setActive(label);
  }

  function loadIndex(api) {
    var codeEl = document.getElementById("explorer-code");
    document.getElementById("explorer-url").textContent = "GET " + pathOf(api.url);
    codeEl.innerHTML = "Loading…";
    fetch(rel(api.url)).then(function (r) { return r.json(); })
      .then(function (data) { showObject(api.url, data, "index"); })
      .catch(function () { codeEl.textContent = "Could not load " + api.url; });
    setActive("index");
  }

  function selectApi(api, scroll) {
    state.current = api;
    var list = document.getElementById("explorer-list");
    list.innerHTML = "";
    var idxBtn = el("button", { "data-label": "index" }, ["GET /api/" + api.api]);
    idxBtn.onclick = function () { loadIndex(api); };
    list.appendChild(idxBtn);
    fetch(rel(api.url)).then(function (r) { return r.json(); }).then(function (data) {
      (data.results || []).slice(0, 25).forEach(function (rec) {
        var lbl = String(rec.id);
        var b = el("button", { "data-label": lbl }, [lbl]);
        b.onclick = function () { showObject(rec.url || api.url, rec, lbl); };
        list.appendChild(b);
      });
    });
    loadIndex(api);
    // Only scroll when the user explicitly picks an API — never on initial load.
    if (scroll) {
      var exp = document.querySelector(".explorer");
      if (exp) exp.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  }

  // ---------- API cards + search ----------
  var FEATURED = 12;
  state.showAll = false;

  function cardFor(api) {
    var card = el("a", { class: "card", href: api.url }, [
      el("div", { class: "emoji" }, [api.emoji || "📦"]),
      el("h3", null, [api.title]),
      el("p", null, [api.description]),
      el("span", { class: "count" }, [fmt(api.count) + " records"]),
    ]);
    card.onclick = function (e) { e.preventDefault(); selectApi(api, true); };
    return card;
  }

  var MAX_RENDER = 240;  // never paint more than this many cards at once
  function renderCards() {
    var grid = document.getElementById("api-grid");
    var more = document.getElementById("api-more");
    var box = document.getElementById("api-search");
    var q = box ? box.value.trim().toLowerCase() : "";
    var list = !q ? state.apis : state.apis.filter(function (a) {
      return (a.title + " " + a.api + " " + a.description).toLowerCase().indexOf(q) >= 0;
    });
    var full = (q || state.showAll) ? list : list.slice(0, FEATURED);
    var shown = full.slice(0, MAX_RENDER);
    grid.innerHTML = "";
    if (!shown.length) { grid.appendChild(el("p", { text: "No APIs match your search." })); }
    shown.forEach(function (api) { grid.appendChild(cardFor(api)); });
    if (more) {
      more.innerHTML = "";
      if (!q && !state.showAll && list.length > FEATURED) {
        var btn = el("button", { class: "btn ghost", text: "＋ Show all " + roundy(list.length) + " APIs" });
        btn.onclick = function () { state.showAll = true; renderCards(); };
        more.appendChild(btn);
      } else if (!q && state.showAll) {
        if (full.length > MAX_RENDER) {
          more.appendChild(el("p", { class: "more-note", text: "Showing " + MAX_RENDER + " of " + fmt(list.length) + " APIs — use search to find any of them." }));
        }
        var less = el("button", { class: "btn ghost", text: "Show less" });
        less.onclick = function () { state.showAll = false; renderCards(); document.getElementById("apis").scrollIntoView({ behavior: "smooth" }); };
        more.appendChild(less);
      } else if (q && list.length > MAX_RENDER) {
        more.appendChild(el("p", { class: "more-note", text: "Showing first " + MAX_RENDER + " of " + fmt(list.length) + " matches — refine your search." }));
      }
    }
  }

  function wireSearch() {
    var box = document.getElementById("api-search");
    if (box) box.addEventListener("input", renderCards);
  }

  // ---------- Hero "Surprise me" ----------
  // The card shell is built once; each roll only swaps the result content
  // inside it (no full rebuild, so no flash or layout jump).
  var sref = null;

  function buildSurpriseShell() {
    var out = document.getElementById("surprise-out");
    if (!out) return;
    sref = {
      emoji: el("span", { class: "surprise-emoji", text: "🎁" }),
      api: el("div", { class: "surprise-api", text: "…" }),
      url: el("code", { class: "surprise-url", text: "GET /api/…" }),
      title: el("div", { class: "surprise-title", text: "Rolling the dice…" }),
      json: el("pre", { class: "surprise-json" }),
      again: el("button", { class: "btn primary", text: "🎲 Again" }),
      open: el("button", { class: "btn ghost", text: "Open in explorer →" }),
    };
    sref.again.onclick = roll;
    out.innerHTML = "";
    out.appendChild(el("div", { class: "surprise-card" }, [
      el("div", { class: "surprise-top" }, [sref.emoji, el("div", {}, [sref.api, sref.url])]),
      sref.title, sref.json,
      el("div", { class: "surprise-actions" }, [sref.again, sref.open]),
    ]));
  }

  function roll() {
    if (!sref || !state.apis.length) return;
    var api = state.apis[Math.floor(Math.random() * state.apis.length)];
    fetch(rel(api.url)).then(function (r) { return r.json(); }).then(function (d) {
      var recs = d.results || [];
      if (!recs.length) return;
      var rec = recs[Math.floor(Math.random() * recs.length)];
      var title = rec.name || rec.common_name || rec.title || rec.quote || rec.character || String(rec.id);
      var pretty = {};
      Object.keys(rec).forEach(function (k) { if (k !== "url" && k !== "body") pretty[k] = rec[k]; });
      // Update only the result nodes in place.
      sref.emoji.textContent = api.emoji || "🎁";
      sref.api.textContent = api.title;
      sref.url.textContent = "GET " + pathOf(rec.url || api.url);
      sref.title.textContent = String(title).slice(0, 120);
      sref.json.innerHTML = highlight(pretty);
      sref.open.onclick = function () { selectApi(api, true); };
      // brief flash to signal the change without rebuilding anything
      sref.json.classList.remove("flash"); void sref.json.offsetWidth; sref.json.classList.add("flash");
    }).catch(function () { if (sref) sref.title.textContent = "Hmm, try again."; });
  }

  function surprise() {
    if (!sref) buildSurpriseShell();
    roll();
  }

  // ---------- Boot ----------
  fetch(API_INDEX).then(function (r) { return r.json(); }).then(function (root) {
    state.apis = root.apis;
    var sa = document.getElementById("stat-apis");
    var sr = document.getElementById("stat-records");
    var sart = document.getElementById("stat-articles");
    if (sa) sa.textContent = roundy(root.api_count);
    if (sr) sr.textContent = roundy(root.total_records);
    if (sart) {
      var art = root.apis.filter(function (a) { return a.api === "articles"; })[0];
      sart.textContent = art ? roundy(art.count) : "100+";
    }
    renderCards();
    wireSearch();
    var btn = document.getElementById("surprise-btn");
    if (btn) btn.onclick = surprise;
    surprise();
    if (state.apis.length) selectApi(state.apis[0]);
  }).catch(function () {
    var g = document.getElementById("api-grid");
    if (g) g.innerHTML = '<p style="color:var(--text-dim)">Could not load the API index. If you are viewing this locally, serve the folder over HTTP.</p>';
  });
})();
