# www.steven-braun.com

Personal homepage of Steven Braun, built with [Hugo](https://gohugo.io) and the [Hextra](https://github.com/imfing/hextra) theme.

## Development

```bash
git clone --recurse-submodules git@github.com:braun-steven/braun-steven.github.io.git
hugo server -D        # http://localhost:1313 (-D also renders drafts)
hugo --gc --minify    # production build into public/
```

If the repo was cloned without submodules: `git submodule update --init`. To update the theme: `git -C themes/hextra fetch --tags && git -C themes/hextra checkout <tag>`, then build locally.

## Layout

- `hugo.toml` — site config (menu, math delimiters, giscus, Hextra params)
- `content/_index.md` — home page (about text, selected publications)
- `content/publications.md` — publication list (hand-maintained HTML/Markdown)
- `content/blog/` — posts; URLs are `/blog/<slug>/` (old `/blog/YYYY/<slug>/` URLs redirect via `aliases`)
- `static/` — served as-is (`CNAME`, `assets/pdf`, images, `papers.bib`)
- `layouts/` — theme overrides: `_partials/custom/head-end.html` (extra head tags), `robots.txt`
- `i18n/en.yaml` — footer copyright
- `assets/css/custom.css` — extra styles

## Writing

- **New post:** `hugo new content blog/<slug>` creates a page bundle `content/blog/<slug>/index.md` from `archetypes/blog/`; fill in `title`, `description`, put images next to `index.md` and reference them by file name (`<img src="header.png">`, `images: [header.png]`). Remove `draft: true` to publish.
- **Math:** use `\( … \)` inline and `\[ … \]` for display math (rendered at build time with KaTeX).
- **Comments:** giscus is on for every post (cascade in `content/blog/_index.md`); disable with `comments: false`. Threads are matched by URL path, so don't rename a published post's file or slug.
- **Authors:** `authors: [Steven Braun]` shows the byline.
- **New publication:** copy an existing `<div class="pub">` block in `content/publications.md` (and add to the home page list if selected). Add the BibTeX to `static/assets/bibliography/papers.bib`.

## Deployment

Pushing to `master` runs `.github/workflows/deploy.yml`, which builds with Hugo and publishes `public/` to the `gh-pages` branch (GitHub Pages source: `gh-pages`).

## License

- Code (Hugo config, layouts, CSS, workflows): [MIT](LICENSE)
- Blog posts and their images: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- Papers, posters, slides and third-party files (e.g. the AAAI style files in `content/blog/matplotlib-viz/`) keep their original copyright.
