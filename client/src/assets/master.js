if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.documentElement.className = "dark-theme";
} else {
    document.documentElement.className = "light-theme";
}
