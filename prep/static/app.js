(function () {
  "use strict";

  // Theme toggle: explicit choice is stored, otherwise follow the OS.
  var btn = document.getElementById("theme-toggle");
  if (btn) {
    btn.addEventListener("click", function () {
      var root = document.documentElement;
      var dark = root.dataset.theme
        ? root.dataset.theme === "dark"
        : window.matchMedia("(prefers-color-scheme: dark)").matches;
      root.dataset.theme = dark ? "light" : "dark";
      try { localStorage.setItem("theme", root.dataset.theme); } catch (e) {}
    });
    if (!document.documentElement.dataset.theme && window.matchMedia("(prefers-color-scheme: dark)").matches) {
      document.documentElement.dataset.theme = "dark";
    }
  }

  // Quizzes: one click reveals right/wrong and the explanation.
  document.querySelectorAll("[data-quiz]").forEach(function (quiz) {
    var options = quiz.querySelectorAll(".quiz-opt");
    options.forEach(function (opt) {
      opt.addEventListener("click", function () {
        options.forEach(function (o) {
          o.disabled = true;
          if (o.dataset.ok === "1") o.classList.add("right");
        });
        if (opt.dataset.ok !== "1") opt.classList.add("wrong");
        var expl = quiz.querySelector(".quiz-expl");
        if (expl) expl.hidden = false;
      });
    });
  });
})();
