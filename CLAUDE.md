# CLAUDE.md

Hugo site using the Hextra theme (git submodule in `themes/hextra`, pinned to a release tag; never edit it — override files under `layouts/` and `assets/` instead). Overrides: `layouts/_partials/custom/head-end.html` (extra `<head>` tags), `layouts/robots.txt` (adds the sitemap line), `i18n/en.yaml` (footer copyright).

- Config: `hugo.toml`. Content: `content/` (`_index.md` home, `publications.md`, `blog/`). Static files: `static/`. Theme overrides: `layouts/`. Extra CSS: `assets/css/custom.css` (picked up by Hextra automatically; Hextra's `.content img` rules win over single-class selectors, so scope image rules with `.content`).
- `hugo server -D` for local development, `hugo --gc --minify` for a production build into `public/` (build output, not source).
- Posts are page bundles (`content/blog/<slug>/index.md`, assets alongside, referenced by bare file name; create with `hugo new content blog/<slug>`). Post URLs are Hugo's default `/blog/<slug>/` (slug = folder name) and must stay stable: giscus uses Hextra's default `pathname` mapping, so each post's discussion is titled with its path (e.g. `blog/matplotlib-viz/`). Posts keep an `aliases` entry for their old `/blog/YYYY/<slug>/` URL.
- Math is rendered server-side by Hextra (KaTeX via passthrough); delimiters are `\(..\)` (inline) and `$$..$$` (display). `math: true` is not needed.
- CI pins the Hugo version in `.github/workflows/deploy.yml`; bump it deliberately and check the build locally first.
