(function () {
    const storageKey = "pulse-polls-language";
    const button = document.getElementById("lang-toggle");

    function applyLanguage(language) {
        document.documentElement.lang = language === "en" ? "en" : "zh-CN";
        document.querySelectorAll("[data-i18n-zh]").forEach((node) => {
            node.textContent = language === "en" ? node.dataset.i18nEn || node.dataset.i18nZh : node.dataset.i18nZh;
        });

        document.querySelectorAll("[data-submit-zh]").forEach((node) => {
            node.value = language === "en" ? node.dataset.submitEn || node.dataset.submitZh : node.dataset.submitZh;
        });
    }

    const current = localStorage.getItem(storageKey) || "zh";
    applyLanguage(current);

    if (button) {
        button.addEventListener("click", () => {
            const next = (localStorage.getItem(storageKey) || "zh") === "zh" ? "en" : "zh";
            localStorage.setItem(storageKey, next);
            applyLanguage(next);
        });
    }
})();
