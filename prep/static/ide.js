(function () {
  "use strict";

  var CSRF = (document.querySelector('meta[name="csrf-token"]') || {}).content || "";

  var VERDICTS = {
    AC: "Accepted — Správne / Принято",
    WA: "Wrong Answer — Nesprávny výstup / Неверный ответ",
    CE: "Compilation Error — Chyba kompilácie / Ошибка компиляции",
    TLE: "Time Limit — Prekročený čas / Превышено время",
    RE: "Runtime Error — Chyba za behu / Ошибка выполнения",
    IE: "Internal Error — Skúste neskôr / Попробуйте позже"
  };

  function store(op, k, v) {
    try {
      if (op === "get") return localStorage.getItem(k);
      if (op === "set") localStorage.setItem(k, v);
      if (op === "del") localStorage.removeItem(k);
    } catch (e) { /* storage unavailable: drafts just won't persist */ }
    return null;
  }

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function pre(label, text) {
    return "<div><h4>" + label + "</h4><pre>" + esc(text === "" ? "(prázdne / пусто)" : text) + "</pre></div>";
  }

  function ms(t) { return t != null ? Math.round(t) + " ms" : "—"; }

  function init(root) {
    var key = root.dataset.key;
    var compact = root.classList.contains("compact");
    var draftKey = "draft:" + key;
    var template = root.querySelector(".js-template").value;
    var resultEl = root.querySelector(".js-result");
    var stdinEl = root.querySelector(".js-stdin");
    var buttons = root.querySelectorAll(".js-run, .js-submit");

    var editor = CodeMirror.fromTextArea(root.querySelector(".js-source"), {
      mode: "text/x-csrc",
      lineNumbers: true,
      matchBrackets: true,
      autoCloseBrackets: true,
      indentUnit: 4,
      tabSize: 4,
      viewportMargin: compact ? Infinity : 10,
      extraKeys: { "Ctrl-Enter": submit, "Cmd-Enter": submit }
    });
    var draft = store("get", draftKey);
    if (draft) editor.setValue(draft);
    editor.on("change", function () { store("set", draftKey, editor.getValue()); });

    root.querySelector(".js-reset").addEventListener("click", function () {
      if (confirm("Vrátiť pôvodnú šablónu? / Вернуть исходный шаблон?")) {
        editor.setValue(template);
        store("del", draftKey);
      }
    });
    var runBtn = root.querySelector(".js-run");
    if (runBtn) runBtn.addEventListener("click", runCode);
    root.querySelector(".js-submit").addEventListener("click", submit);

    function needLogin() {
      if (root.dataset.loggedIn === "1") return false;
      resultEl.innerHTML = '<div class="verdict INFO">Na spúšťanie kódu sa prihláste. / Войдите, чтобы запускать код.' +
        ' <a class="btn primary sm" href="' + esc(root.dataset.loginUrl) + '">Prihlásiť</a></div>';
      return true;
    }

    function busy(on) {
      buttons.forEach(function (b) { b.disabled = on; });
      if (on) resultEl.innerHTML = '<p class="pending"><span class="spinner"></span>Prebieha… / Выполняется…</p>';
    }

    function post(url, body) {
      busy(true);
      return fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json", "X-CSRF-Token": CSRF },
        body: JSON.stringify(body)
      }).then(function (r) {
        return r.json().catch(function () { return {}; }).then(function (data) {
          if (!r.ok) throw new Error(data.error || ("HTTP " + r.status));
          return data;
        });
      }).catch(function (err) {
        resultEl.innerHTML = '<div class="verdict IE">' + esc(err.message) + "</div>";
        throw err;
      }).finally(function () { busy(false); });
    }

    function runCode() {
      if (needLogin()) return;
      post(root.dataset.runUrl, { source: editor.getValue(), stdin: stdinEl ? stdinEl.value : "" }).then(function (d) {
        var ok = d.status === "ok";
        var label = { ok: "Program skončil / Программа завершилась", compile_error: VERDICTS.CE,
                      timeout: VERDICTS.TLE, runtime_error: VERDICTS.RE, internal_error: VERDICTS.IE }[d.status] || d.status;
        var html = '<div class="verdict ' + (ok ? "AC" : "WA") + '"><span>' + esc(label) + '</span><span class="score">' + ms(d.time_ms) + "</span></div>";
        if (d.compile_output) html += pre("Kompilátor / Компилятор", d.compile_output);
        if (d.status !== "compile_error") html += pre("stdout", d.stdout);
        if (d.stderr) html += pre("stderr", d.stderr);
        if (d.message) html += '<p class="meta">' + esc(d.message) + "</p>";
        resultEl.innerHTML = html;
      }, function () {});
    }

    function submit() {
      if (needLogin()) return;
      post(root.dataset.submitUrl, { source: editor.getValue() }).then(function (d) {
        var html = '<div class="verdict ' + d.verdict + '"><span>' + esc(VERDICTS[d.verdict] || d.verdict) +
          '</span><span class="score">' + d.passed + " / " + d.total + "</span></div>";
        if (d.compile_output) html += pre("Kompilátor / Компилятор", d.compile_output);
        if (d.message) html += '<p class="meta">' + esc(d.message) + "</p>";
        if (d.tests && d.tests.length && !(compact && d.verdict === "AC")) {
          html += '<table class="tests"><tr><th>Test</th><th>Verdikt</th><th>Čas</th></tr>';
          d.tests.forEach(function (t) {
            html += "<tr><td>#" + esc(t.name) + '</td><td class="v ' + t.verdict + '">' + t.verdict +
              (t.message ? ' <span class="meta">' + esc(t.message) + "</span>" : "") + "</td><td>" + ms(t.time_ms) + "</td></tr>";
            if (t.input != null && t.verdict !== "AC") {
              html += '<tr><td colspan="3">' + (t.input ? pre("Vstup / Ввод", t.input) : "") +
                '<div class="diff">' + pre("Očakávané / Ожидалось", t.expected) + pre("Váš výstup / Ваш вывод", t.actual) + "</div></td></tr>";
            }
          });
          html += "</table>";
          if (d.tests.length < d.total && d.verdict !== "AC") {
            html += '<p class="meta">Ďalšie testy sa nespúšťali. / Остальные тесты не запускались.</p>';
          }
        }
        resultEl.innerHTML = html;
        if (d.verdict === "AC") {
          var drill = root.closest(".drill");
          if (drill) drill.classList.add("solved");
        }
      }, function () {});
    }
  }

  document.querySelectorAll(".code-widget").forEach(init);
})();
