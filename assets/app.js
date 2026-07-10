// GratisAPI homepage — loads the live API index and renders cards + explorer.
(function () {
  "use strict";

  var API_INDEX = "api/index.json";

  // Records carry absolute production URLs; fetch them relative to wherever the
  // site is actually hosted so the page works on forks and locally too.
  function rel(url) {
    var i = url.indexOf("/api/");
    return i >= 0 ? url.slice(i + 1) : url;
  }

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === "class") node.className = attrs[k];
      else if (k === "html") node.innerHTML = attrs[k];
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

  var state = { apis: [], current: null };

  function loadRecord(api, url, label) {
    var codeEl = document.getElementById("explorer-code");
    var urlEl = document.getElementById("explorer-url");
    var path = url.replace(/^https?:\/\/[^/]+/, "");
    urlEl.textContent = "GET " + path;
    codeEl.innerHTML = "Loading…";
    fetch(rel(url)).then(function (r) { return r.json(); }).then(function (data) {
      // For the index view, trim results so the sample stays readable.
      if (data.results && data.results.length > 6) {
        var clone = Object.assign({}, data);
        clone.results = data.results.slice(0, 3);
        clone["…"] = "(" + (data.count - 3) + " more records — open the endpoint to see them all)";
        data = clone;
      }
      codeEl.innerHTML = highlight(data);
    }).catch(function () {
      codeEl.textContent = "Could not load " + url;
    });
    Array.prototype.forEach.call(
      document.querySelectorAll("#explorer-list button"),
      function (b) { b.classList.toggle("active", b.dataset.label === label); }
    );
  }

  function selectApi(api) {
    state.current = api;
    var list = document.getElementById("explorer-list");
    list.innerHTML = "";
    var idxBtn = el("button", { "data-label": "index" }, ["GET " + api.api + "/"]);
    idxBtn.onclick = function () { loadRecord(api, api.url, "index"); };
    list.appendChild(idxBtn);
    // Fetch the index to list a few individual record endpoints too.
    fetch(rel(api.url)).then(function (r) { return r.json(); }).then(function (data) {
      (data.results || []).slice(0, 25).forEach(function (rec) {
        var lbl = String(rec.id);
        var b = el("button", { "data-label": lbl }, [lbl]);
        b.onclick = function () { loadRecord(api, rec.url, lbl); };
        list.appendChild(b);
      });
    });
    loadRecord(api, api.url, "index");
    document.querySelector(".explorer").scrollIntoView({ behavior: "smooth", block: "center" });
  }

  function renderCards(root) {
    var grid = document.getElementById("api-grid");
    grid.innerHTML = "";
    root.apis.forEach(function (api) {
      var card = el("a", { class: "card", href: api.url }, [
        el("div", { class: "emoji" }, [api.emoji || "📦"]),
        el("h3", null, [api.title]),
        el("p", null, [api.description]),
        el("span", { class: "count" }, [fmt(api.count) + " records"]),
      ]);
      card.onclick = function (e) { e.preventDefault(); selectApi(api); };
      grid.appendChild(card);
    });
  }

  fetch(API_INDEX).then(function (r) { return r.json(); }).then(function (root) {
    state.apis = root.apis;
    document.getElementById("stat-apis").textContent = fmt(root.api_count);
    document.getElementById("stat-records").textContent = fmt(root.total_records);
    renderCards(root);
    if (root.apis.length) selectApi(root.apis[0]);
  }).catch(function () {
    document.getElementById("api-grid").innerHTML =
      '<p style="color:var(--text-dim)">Could not load the API index. If you are viewing this locally, serve the folder over HTTP.</p>';
  });
})();
