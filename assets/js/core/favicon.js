// Project override of themes/hextra/assets/js/core/favicon.js.
// Adds ?v=... to the favicon URLs so browsers fetch a replaced icon.
// {{ $faviconDarkExists := fileExists (path.Join "static" "favicon-dark.svg") }}
// {{ $faviconVersion := site.Params.faviconVersion | default "1" }}
(function () {
  const faviconEl = document.getElementById("favicon-svg");
  const faviconDarkExists = "{{ $faviconDarkExists }}" === "true";

  if (faviconEl && faviconDarkExists) {
    const lightFavicon = '{{ "favicon.svg" | relURL }}?v={{ $faviconVersion }}';
    const darkFavicon = '{{ "favicon-dark.svg" | relURL }}?v={{ $faviconVersion }}';

    const darkModeQuery = window.matchMedia("(prefers-color-scheme: dark)");

    function updateFavicon(e) {
      faviconEl.href = e.matches ? darkFavicon : lightFavicon;
    }

    // Set favicon on load
    updateFavicon(darkModeQuery);

    // Listen for system preference changes
    darkModeQuery.addEventListener("change", updateFavicon);
  }
})();
