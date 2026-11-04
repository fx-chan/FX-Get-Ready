(function () {
  "use strict";

  var CSRF = (document.querySelector('meta[name="csrf-token"]') || {}).content || "";

  function store(op, k, v) {
    try {
      if (op === "get") return localStorage.getItem(k);
      if (op === "set") localStorage.setItem(k, v);
    } catch (e) { /* storage unavailable: drafts just won't persist */ }
    return null;
  }

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  // TeX written in lessons and statements ($...$ placeholders rendered by the server as .math).
  function renderMath(root) {
    if (!window.katex) return;
    (root || document).querySelectorAll(".math:not([data-done])").forEach(function (el) {
      try {
        katex.render(el.textContent, el, { displayMode: el.dataset.display === "1", throwOnError: false });
      } catch (e) { /* leave the raw TeX visible */ }
      el.dataset.done = "1";
    });
  }

  // Live preview of a typed matrix / vector, so the student sees how the input is read.
  function toTex(cell) {
    return cell.replace(/sqrt\(([^()]*)\)/g, "\\sqrt{$1}").replace(/√(\w+)/g, "\\sqrt{$1}")
      .replace(/\bpi\b/g, "\\pi").replace(/\*/g, "\\cdot ");
  }

  function previewRows(text) {
    var blocks = text.trim().split(/\n\s*\n/);
    return blocks.map(function (block) {
      var rows = block.split(/[;\n]/).map(function (line) {
        line = line.trim().replace(/^[\[(|]+|[\])|]+$/g, "");
        if (!line) return null;
        var cells = line.indexOf(",") >= 0 ? line.split(",") : line.split(/\s+/);
        return cells.map(function (c) { return toTex(c.trim()); }).join(" & ");
      }).filter(Boolean);
      return rows.length ? "\\begin{bmatrix}" + rows.join(" \\\\ ") + "\\end{bmatrix}" : "";
    }).join("\\quad ");
  }

  function updatePreview(part) {
    var box = part.querySelector(".ans-preview");
    var input = part.querySelector(".js-value");
    if (!box || !input || !window.katex) return;
    var tex = input.value.trim() ? previewRows(input.value) : "";
    if (!tex) { box.innerHTML = ""; return; }
    try { katex.render(tex, box, { throwOnError: false, displayMode: false }); } catch (e) { box.textContent = ""; }
  }

  function collect(root) {
    var answers = {};
    root.querySelectorAll(".ans-part").forEach(function (part) {
      var kind = part.dataset.kind;
      var item = {};
      if (kind === "choice") {
        var picked = part.querySelector("input[type=radio]:checked");
        item.value = picked ? picked.value : null;
      } else if (kind === "multi") {
        item.value = Array.prototype.map.call(part.querySelectorAll(".ans-options input:checked"), function (i) { return i.value; });
      } else {
        item.value = part.querySelector(".js-value").value;
      }
      var none = part.querySelector(".js-none");
      item.none = !!(none && none.checked);
      answers[part.dataset.id] = item;
    });
    return answers;
  }

  function restore(root, saved) {
    Object.keys(saved || {}).forEach(function (id) {
      var part = root.querySelector('.ans-part[data-id="' + id + '"]');
      if (!part) return;
      var item = saved[id] || {};
      var input = part.querySelector(".js-value");
      if (input && typeof item.value === "string" && !input.value) input.value = item.value;
      if (part.dataset.kind === "choice" && item.value != null) {
        var r = part.querySelector('input[type=radio][value="' + item.value + '"]');
        if (r && !part.querySelector("input[type=radio]:checked")) r.checked = true;
      }
      if (part.dataset.kind === "multi" && Array.isArray(item.value) && !part.querySelector(".ans-options input:checked")) {
        item.value.forEach(function (v) {
          var c = part.querySelector('.ans-options input[value="' + v + '"]');
          if (c) c.checked = true;
        });
      }
      var none = part.querySelector(".js-none");
      if (none && item.none) none.checked = true;
      syncNone(part);
    });
  }

  function syncNone(part) {
    var none = part.querySelector(".js-none");
    var input = part.querySelector(".js-value");
    if (none && input) input.disabled = none.checked;
  }

  function init(root) {
    var draftKey = "answers:" + root.dataset.key;
    var resultEl = root.querySelector(".js-result");
    var button = root.querySelector(".js-check");

    try { restore(root, JSON.parse(store("get", draftKey) || "{}")); } catch (e) { /* bad draft */ }

    root.querySelectorAll(".ans-part").forEach(function (part) {
      updatePreview(part);
      part.addEventListener("input", function () {
        updatePreview(part);
        part.classList.remove("ok", "wrong", "invalid");
        store("set", draftKey, JSON.stringify(collect(root)));
      });
      part.addEventListener("change", function () {
        syncNone(part);
        store("set", draftKey, JSON.stringify(collect(root)));
      });
      syncNone(part);
    });

    button.addEventListener("click", function () {
      if (root.dataset.loggedIn !== "1") {
        resultEl.innerHTML = '<div class="verdict INFO">Na kontrolu odpovedí sa prihláste. / Войдите, чтобы проверять ответы.' +
          ' <a class="btn primary sm" href="' + esc(root.dataset.loginUrl) + '">Prihlásiť</a></div>';
        return;
      }
      button.disabled = true;
      resultEl.innerHTML = '<p class="pending"><span class="spinner"></span>Kontrolujem… / Проверяю…</p>';
      fetch(root.dataset.checkUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json", "X-CSRF-Token": CSRF },
        body: JSON.stringify({ answers: collect(root) })
      }).then(function (r) {
        return r.json().then(function (data) { return { ok: r.ok, data: data }; });
      }).then(function (res) {
        if (!res.ok) throw new Error(res.data.error || "Chyba");
        show(res.data);
      }).catch(function (err) {
        resultEl.innerHTML = '<div class="verdict IE">' + esc(err.message) + "</div>";
      }).then(function () { button.disabled = false; });
    });

    function show(data) {
      Object.keys(data.parts).forEach(function (id) {
        var part = root.querySelector('.ans-part[data-id="' + id + '"]');
        if (!part) return;
        var res = data.parts[id];
        part.classList.remove("ok", "wrong", "invalid");
        part.classList.add(res.status);
        part.querySelector(".ans-msg").textContent = res.message || "";
      });
      var ac = data.verdict === "AC";
      resultEl.innerHTML = '<div class="verdict ' + (ac ? "AC" : "WA") + '">' +
        (ac ? "✓ Všetko správne! / Всё верно!" : "Správne " + data.passed + " z " + data.total +
          ". Opravte červené časti. / Верно " + data.passed + " из " + data.total + ".") + "</div>";
      if (ac) {
        var drill = root.closest(".drill");
        if (drill) drill.classList.add("solved");
      }
    }
  }

  renderMath(document);
  document.querySelectorAll(".answer-widget").forEach(init);
})();
