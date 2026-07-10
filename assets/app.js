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
  function loadRecord(api, url, label) {
    var codeEl = document.getElementById("explorer-code");
    var urlEl = document.getElementById("explorer-url");
    urlEl.textContent = "GET " + pathOf(url);
    codeEl.innerHTML = "Loading…";
    fetch(rel(url)).then(function (r) { return r.json(); }).then(function (data) {
      if (data.results && data.results.length > 6) {
        var clone = Object.assign({}, data);
        clone.results = data.results.slice(0, 3);
        clone["…"] = "(" + (data.count - 3) + " more records — open the endpoint to see them all)";
        data = clone;
      }
      codeEl.innerHTML = highlight(data);
    }).catch(function () { codeEl.textContent = "Could not load " + url; });
    Array.prototype.forEach.call(
      document.querySelectorAll("#explorer-list button"),
      function (b) { b.classList.toggle("active", b.dataset.label === label); }
    );
  }

  function selectApi(api, scroll) {
    state.current = api;
    var list = document.getElementById("explorer-list");
    list.innerHTML = "";
    var idxBtn = el("button", { "data-label": "index" }, ["GET /api/" + api.api]);
    idxBtn.onclick = function () { loadRecord(api, api.url, "index"); };
    list.appendChild(idxBtn);
    fetch(rel(api.url)).then(function (r) { return r.json(); }).then(function (data) {
      (data.results || []).slice(0, 25).forEach(function (rec) {
        var lbl = String(rec.id);
        var b = el("button", { "data-label": lbl }, [lbl]);
        b.onclick = function () { loadRecord(api, rec.url, lbl); };
        list.appendChild(b);
      });
    });
    loadRecord(api, api.url, "index");
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

  function renderCards() {
    var grid = document.getElementById("api-grid");
    var more = document.getElementById("api-more");
    var box = document.getElementById("api-search");
    var q = box ? box.value.trim().toLowerCase() : "";
    var list = !q ? state.apis : state.apis.filter(function (a) {
      return (a.title + " " + a.api + " " + a.description).toLowerCase().indexOf(q) >= 0;
    });
    var shown = (q || state.showAll) ? list : list.slice(0, FEATURED);
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
        var less = el("button", { class: "btn ghost", text: "Show less" });
        less.onclick = function () { state.showAll = false; renderCards(); document.getElementById("apis").scrollIntoView({ behavior: "smooth" }); };
        more.appendChild(less);
      }
    }
  }

  function wireSearch() {
    var box = document.getElementById("api-search");
    if (box) box.addEventListener("input", renderCards);
  }

  // ---------- Hero "Surprise me" ----------
  function surprise() {
    var out = document.getElementById("surprise-out");
    if (!out || !state.apis.length) return;
    var api = state.apis[Math.floor(Math.random() * state.apis.length)];
    out.innerHTML = '<span class="surprise-loading">rolling the dice…</span>';
    fetch(rel(api.url)).then(function (r) { return r.json(); }).then(function (d) {
      var recs = d.results || [];
      if (!recs.length) return;
      var rec = recs[Math.floor(Math.random() * recs.length)];
      var title = rec.name || rec.common_name || rec.title || rec.quote || rec.character || String(rec.id);
      var pretty = {};
      Object.keys(rec).forEach(function (k) {
        if (k === "url" || k === "body") return;
        pretty[k] = rec[k];
      });
      out.innerHTML = "";
      out.appendChild(el("div", { class: "surprise-card" }, [
        el("div", { class: "surprise-top" }, [
          el("span", { class: "surprise-emoji", text: api.emoji || "🎁" }),
          el("div", {}, [
            el("div", { class: "surprise-api", text: api.title }),
            el("code", { class: "surprise-url", text: "GET " + pathOf(rec.url || api.url) }),
          ]),
        ]),
        el("div", { class: "surprise-title", text: String(title).slice(0, 120) }),
        el("pre", { class: "surprise-json", html: highlight(pretty) }),
        el("div", { class: "surprise-actions" }, [
          (function () { var b = el("button", { class: "btn primary", text: "🎲 Again" }); b.onclick = surprise; return b; })(),
          (function () { var b = el("button", { class: "btn ghost", text: "Open in explorer →" }); b.onclick = function () { selectApi(api, true); }; return b; })(),
        ]),
      ]));
    }).catch(function () { out.innerHTML = '<span class="surprise-loading">Hmm, try again.</span>'; });
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
