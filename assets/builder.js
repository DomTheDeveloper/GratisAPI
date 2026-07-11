// GratisAPI Builder — turn a CSV / TSV / JSON / YAML / spreadsheet into a
// complete, documented static API, entirely in the browser. Nothing is
// uploaded anywhere: parsing, generation and zipping all happen locally.
(function () {
  "use strict";

  // ---------- tiny helpers ----------
  function $(id) { return document.getElementById(id); }
  function el(tag, attrs, kids) {
    var n = document.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === "class") n.className = attrs[k];
      else if (k === "text") n.textContent = attrs[k];
      else if (k === "html") n.innerHTML = attrs[k];
      else n.setAttribute(k, attrs[k]);
    });
    (kids || []).forEach(function (c) { n.appendChild(typeof c === "string" ? document.createTextNode(c) : c); });
    return n;
  }
  function slug(s) {
    return String(s).toLowerCase().trim()
      .replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "") || "";
  }
  function coerce(v) {
    if (v == null) return null;
    var s = String(v).trim();
    if (s === "") return "";
    if (s === "true") return true;
    if (s === "false") return false;
    if (s === "null") return null;
    if (/^-?\d+$/.test(s) && s.length < 16) return parseInt(s, 10);
    if (/^-?\d*\.\d+$/.test(s)) return parseFloat(s);
    return String(v);
  }

  // ---------- parsers ----------
  function parseDelimited(text, delim) {
    text = text.replace(/\r\n?/g, "\n");
    var rows = [], row = [], field = "", i = 0, inq = false;
    while (i < text.length) {
      var c = text[i];
      if (inq) {
        if (c === '"') { if (text[i + 1] === '"') { field += '"'; i += 2; continue; } inq = false; i++; continue; }
        field += c; i++; continue;
      }
      if (c === '"') { inq = true; i++; continue; }
      if (c === delim) { row.push(field); field = ""; i++; continue; }
      if (c === "\n") { row.push(field); rows.push(row); row = []; field = ""; i++; continue; }
      field += c; i++;
    }
    if (field.length || row.length) { row.push(field); rows.push(row); }
    return rows.filter(function (r) { return !(r.length === 1 && r[0] === ""); });
  }
  function rowsToObjects(rows) {
    if (!rows.length) return [];
    var header = rows[0].map(function (h, j) { return String(h).trim() || ("column_" + (j + 1)); });
    return rows.slice(1).map(function (r) {
      var o = {};
      header.forEach(function (h, j) { o[h] = coerce(r[j]); });
      return o;
    });
  }
  function normalizeToArray(data) {
    if (Array.isArray(data)) return data;
    if (data && typeof data === "object") {
      // find first array-of-objects property, else wrap the object's entries
      for (var k in data) {
        if (Array.isArray(data[k]) && data[k].length && typeof data[k][0] === "object") return data[k];
      }
      // treat a dict of objects as records keyed by id
      var out = [];
      Object.keys(data).forEach(function (key) {
        var v = data[key];
        if (v && typeof v === "object" && !Array.isArray(v)) out.push(Object.assign({ id: key }, v));
        else out.push({ id: key, value: v });
      });
      return out;
    }
    return [];
  }

  function parseInput(text, fmt, arrayBuffer) {
    if (fmt === "xlsx") {
      if (!window.XLSX) throw new Error("Spreadsheet support is still loading — try again in a second, or export your sheet as CSV.");
      var wb = window.XLSX.read(arrayBuffer, { type: "array" });
      var sheet = wb.Sheets[wb.SheetNames[0]];
      return window.XLSX.utils.sheet_to_json(sheet, { defval: "" });
    }
    if (fmt === "json") return normalizeToArray(JSON.parse(text));
    if (fmt === "yaml") {
      if (!window.jsyaml) throw new Error("YAML support is still loading — try again in a second, or paste JSON.");
      return normalizeToArray(window.jsyaml.load(text));
    }
    if (fmt === "tsv") return rowsToObjects(parseDelimited(text, "\t"));
    // csv (default) — sniff tab vs comma
    var delim = (text.indexOf("\t") >= 0 && text.indexOf(",") < 0) ? "\t" : ",";
    return rowsToObjects(parseDelimited(text, delim));
  }

  // ---------- API generation ----------
  function buildApi(records, opts) {
    var name = opts.slug, base = opts.baseUrl.replace(/\/+$/, "");
    var seen = {}, out = [];
    records.forEach(function (row, i) {
      var raw = (opts.idField && row[opts.idField] != null && String(row[opts.idField]).trim() !== "")
        ? String(row[opts.idField]) : String(i);
      var id = slug(raw) || String(i);
      var b = id, k = 2;
      while (seen[id]) { id = b + "-" + k; k++; }
      seen[id] = 1;
      var rec = {};
      rec.id = id;
      Object.keys(row).forEach(function (key) { if (key !== "id" && key !== "url") rec[key] = row[key]; });
      rec.url = base + "/api/" + name + "/" + id;
      out.push(rec);
    });
    var fields = [];
    var fs = {};
    records.forEach(function (r) { Object.keys(r).forEach(function (k) { if (!fs[k]) { fs[k] = 1; fields.push(k); } }); });
    fields = ["id"].concat(fields.filter(function (f) { return f !== "id"; }));

    var index = {
      api: name, title: opts.title, description: opts.description,
      generated_by: "GratisAPI Builder (https://gratisapi.com/builder/)",
      license: opts.license || "", count: out.length,
      self: base + "/api/" + name + "/index",
      endpoints: { list: base + "/api/" + name + "/index", item: base + "/api/" + name + "/{id}" },
      fields: fields.sort(), results: out,
    };
    var catalog = {
      name: opts.title, base_url: base, api_count: 1, total_records: out.length,
      apis: [{ api: name, title: opts.title, description: opts.description, count: out.length, url: base + "/api/" + name + "/index" }],
    };
    var openapi = {
      openapi: "3.1.0",
      info: { title: opts.title, version: "1.0.0", description: opts.description + "\n\nGenerated by the GratisAPI Builder." },
      servers: [{ url: base || "https://your-domain.example" }],
      paths: {},
    };
    openapi.paths["/api/" + name + "/index"] = { get: { summary: "List all " + opts.title.toLowerCase(), responses: { "200": { description: "All records." } } } };
    openapi.paths["/api/" + name + "/{id}"] = {
      get: {
        summary: "Get one record by id",
        parameters: [{ name: "id", "in": "path", required: true, schema: { type: "string" } }],
        responses: { "200": { description: "The record." }, "404": { description: "Not found." } },
      },
    };
    return { index: index, catalog: catalog, openapi: openapi, records: out, fields: index.fields };
  }

  function buildReadme(o, count) {
    var b = o.baseUrl || "https://your-domain.example";
    return [
      "# " + o.title, "", o.description || "", "",
      "A free, static, documented API generated with the "
      + "[GratisAPI Builder](https://gratisapi.com/builder/). " + count + " records, no server required.",
      "", "## Endpoints", "",
      "| Endpoint | Returns |", "| --- | --- |",
      "| `" + b + "/api/" + o.slug + "/index` | Metadata + all records |",
      "| `" + b + "/api/" + o.slug + "/<id>` | A single record |",
      "", "## Deploy", "",
      "Drop the contents of this folder onto any static host — GitHub Pages,",
      "Cloudflare Pages, Netlify, S3 — and your API is live. The `_headers` file",
      "serves the clean (extension-less) URLs as JSON on Cloudflare Pages.",
      "", "## Usage", "", "```bash", "curl " + b + "/api/" + o.slug + "/index", "```",
      "", "Licensed " + (o.license || "as you wish") + ".", "",
    ].join("\n");
  }

  // ---------- dependency-free ZIP (store, no compression) ----------
  function crc32(buf) {
    var t = crc32._t;
    if (!t) {
      t = crc32._t = new Uint32Array(256);
      for (var n = 0; n < 256; n++) { var c = n; for (var k = 0; k < 8; k++) c = (c & 1) ? (0xEDB88320 ^ (c >>> 1)) : (c >>> 1); t[n] = c >>> 0; }
    }
    var crc = 0 ^ (-1);
    for (var i = 0; i < buf.length; i++) crc = (crc >>> 8) ^ t[(crc ^ buf[i]) & 0xFF];
    return (crc ^ (-1)) >>> 0;
  }
  function u16(n) { return new Uint8Array([n & 255, (n >> 8) & 255]); }
  function u32(n) { n >>>= 0; return new Uint8Array([n & 255, (n >> 8) & 255, (n >> 16) & 255, (n >> 24) & 255]); }
  function zipStore(files) {
    var enc = new TextEncoder(), chunks = [], central = [], offset = 0;
    files.forEach(function (f) {
      var nameB = enc.encode(f.name), data = f.bytes, crc = crc32(data), size = data.length;
      var local = [u32(0x04034b50), u16(20), u16(0), u16(0), u16(0), u16(33),
        u32(crc), u32(size), u32(size), u16(nameB.length), u16(0), nameB, data];
      var localOffset = offset;
      local.forEach(function (p) { chunks.push(p); offset += p.length; });
      central.push([u32(0x02014b50), u16(20), u16(20), u16(0), u16(0), u16(0), u16(33),
        u32(crc), u32(size), u32(size), u16(nameB.length), u16(0), u16(0), u16(0), u16(0),
        u32(0), u32(localOffset), nameB]);
    });
    var cdStart = offset, cd = [];
    central.forEach(function (parts) { parts.forEach(function (p) { cd.push(p); offset += p.length; }); });
    var end = [u32(0x06054b50), u16(0), u16(0), u16(files.length), u16(files.length),
      u32(offset - cdStart), u32(cdStart), u16(0)];
    return new Blob(chunks.concat(cd).concat(end), { type: "application/zip" });
  }

  function apiToFiles(built, opts, count) {
    var enc = new TextEncoder();
    var files = [];
    function add(path, text) { files.push({ name: path, bytes: enc.encode(text) }); }
    function addJson(path, obj) {
      var text = JSON.stringify(obj, null, 2) + "\n";
      add(path, text);            // .json (browser-friendly)
      add(path.replace(/\.json$/, ""), text); // clean, extension-less twin
    }
    var n = opts.slug;
    addJson("api/index.json", built.catalog);
    addJson("api/" + n + "/index.json", built.index);
    built.records.forEach(function (rec) { addJson("api/" + n + "/" + rec.id + ".json", rec); });
    add("openapi.json", JSON.stringify(built.openapi, null, 2) + "\n");
    add("README.md", buildReadme(opts, count));
    add(".nojekyll", "");
    add("_headers", "/api/*\n  Access-Control-Allow-Origin: *\n  Content-Type: application/json; charset=utf-8\n  Cache-Control: public, max-age=3600\n");
    return files;
  }

  // ---------- UI wiring ----------
  var state = { records: null, fmt: "csv", buffer: null };

  function highlight(obj) {
    var j = JSON.stringify(obj, null, 2).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    return j.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g,
      function (m) { var c = "n"; if (/^"/.test(m)) c = /:$/.test(m) ? "k" : "s"; else if (/true|false|null/.test(m)) c = "b"; return '<span class="' + c + '">' + m + "</span>"; });
  }

  function detectFmt(filename, text) {
    var ext = (filename.split(".").pop() || "").toLowerCase();
    if (ext === "xlsx" || ext === "xls") return "xlsx";
    if (ext === "json") return "json";
    if (ext === "yaml" || ext === "yml") return "yaml";
    if (ext === "tsv") return "tsv";
    if (ext === "csv") return "csv";
    var t = (text || "").trim();
    if (t[0] === "{" || t[0] === "[") return "json";
    return "csv";
  }

  function analyze() {
    var msg = $("build-msg");
    try {
      var text = $("build-input").value;
      if (state.fmt !== "xlsx" && !text.trim()) { msg.textContent = ""; return; }
      var recs = parseInput(text, state.fmt, state.buffer);
      if (!recs.length) throw new Error("No records found. Need at least one row/object.");
      recs = recs.filter(function (r) { return r && typeof r === "object"; });
      state.records = recs;
      // populate id-field select
      var sel = $("build-idfield");
      var keys = [];
      var ks = {};
      recs.slice(0, 50).forEach(function (r) { Object.keys(r).forEach(function (k) { if (!ks[k]) { ks[k] = 1; keys.push(k); } }); });
      sel.innerHTML = "";
      sel.appendChild(el("option", { value: "" }, ["(auto — row number)"]));
      keys.forEach(function (k) { sel.appendChild(el("option", { value: k }, [k])); });
      // guess id field
      var guess = keys.filter(function (k) { return /^(id|slug|code|key|name)$/i.test(k); })[0];
      if (guess) sel.value = guess;
      if (!$("build-name").value) $("build-name").value = "my-api";
      msg.innerHTML = '<span style="color:var(--accent)">✓ Parsed ' + recs.length + " records, " + keys.length + " fields.</span>";
      preview();
    } catch (e) {
      state.records = null;
      msg.innerHTML = '<span style="color:#ff7b72">' + e.message + "</span>";
    }
  }

  function currentOpts() {
    var name = slug($("build-name").value) || "my-api";
    return {
      slug: name,
      title: $("build-title").value.trim() || (name.replace(/-/g, " ").replace(/\b\w/g, function (c) { return c.toUpperCase(); })),
      description: $("build-desc").value.trim() || ("A static API generated from " + state.records.length + " records."),
      idField: $("build-idfield").value,
      baseUrl: $("build-base").value.trim(),
      license: $("build-license").value.trim(),
    };
  }

  function preview() {
    if (!state.records) return;
    var built = buildApi(state.records, currentOpts());
    var idx = Object.assign({}, built.index);
    if (idx.results.length > 3) { idx = Object.assign({}, built.index); idx.results = built.index.results.slice(0, 3); idx["…"] = "(" + (built.index.count - 3) + " more)"; }
    $("preview-index").innerHTML = highlight(idx);
    $("preview-record").innerHTML = highlight(built.records[0]);
    $("preview-endpoints").innerHTML = "";
    var b = currentOpts().baseUrl || "";
    [["GET", "/api/" + built.index.api + "/index", "list all " + built.index.count + " records"],
    ["GET", "/api/" + built.index.api + "/" + built.records[0].id, "one record"],
    ["GET", "/openapi.json", "OpenAPI 3.1 spec"]].forEach(function (r) {
      $("preview-endpoints").appendChild(el("div", { class: "ep-row" }, [
        el("span", { class: "ep-method", text: r[0] }),
        el("code", { class: "ep-path", text: b + r[1] }),
        el("span", { class: "ep-desc", text: r[2] }),
      ]));
    });
    $("build-download").disabled = false;
    $("build-stats").textContent = built.index.count + " records · " + built.fields.length + " fields · 1 API";
  }

  function download() {
    if (!state.records) return;
    var opts = currentOpts();
    var built = buildApi(state.records, opts);
    var files = apiToFiles(built, opts, built.index.count);
    var blob = zipStore(files);
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = opts.slug + "-api.zip";
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(a.href); }, 4000);
  }

  var SAMPLE = "name,role,city,founded\nAda Lovelace,Mathematician,London,1815\nAlan Turing,Computer Scientist,London,1912\nGrace Hopper,Rear Admiral,New York,1906\nKatherine Johnson,Mathematician,White Sulphur Springs,1918";

  function boot() {
    var input = $("build-input");
    ["build-name", "build-title", "build-desc", "build-idfield", "build-base", "build-license"].forEach(function (id) {
      $(id).addEventListener("input", function () { if (state.records) preview(); });
    });
    input.addEventListener("input", function () { state.fmt = detectFmt("", input.value); state.buffer = null; analyze(); });
    $("build-download").addEventListener("click", download);
    $("build-sample").addEventListener("click", function () { input.value = SAMPLE; state.fmt = "csv"; state.buffer = null; analyze(); });

    var file = $("build-file");
    function handleFile(f) {
      state.fmt = detectFmt(f.name, "");
      if (state.fmt === "xlsx") {
        var r = new FileReader();
        r.onload = function () { state.buffer = new Uint8Array(r.result); input.value = "[binary spreadsheet: " + f.name + "]"; analyze(); };
        r.readAsArrayBuffer(f);
      } else {
        var r2 = new FileReader();
        r2.onload = function () { input.value = r2.result; state.buffer = null; if (state.fmt === "csv") state.fmt = detectFmt(f.name, r2.result); analyze(); };
        r2.readAsText(f);
      }
    }
    file.addEventListener("change", function () { if (file.files[0]) handleFile(file.files[0]); });
    var drop = $("build-drop");
    ["dragover", "dragenter"].forEach(function (e) { drop.addEventListener(e, function (ev) { ev.preventDefault(); drop.classList.add("drag"); }); });
    ["dragleave", "drop"].forEach(function (e) { drop.addEventListener(e, function (ev) { ev.preventDefault(); drop.classList.remove("drag"); }); });
    drop.addEventListener("drop", function (ev) { if (ev.dataTransfer.files[0]) handleFile(ev.dataTransfer.files[0]); });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
