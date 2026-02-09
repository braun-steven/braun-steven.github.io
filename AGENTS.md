# Repository Guidelines

## Project Structure & Module Organization
This repository is a Jekyll site customized from `al-folio`.
- Core config lives in `_config.yml`.
- Content lives in `_pages/`, `_posts/`, `_news/`, `_projects/`, and `_bibliography/`.
- Rendering and reusable UI live in `_layouts/`, `_includes/`, and `_sass/`.
- Custom Ruby extensions are in `_plugins/`.
- Static files (CSS, JS, images, PDFs, post assets) are in `assets/`.
- Generated output is written to `_site/`; treat it as build output, not hand-edited source.

## Build, Test, and Development Commands
- `bundle install`: install Ruby dependencies from `Gemfile`.
- `bundle exec jekyll serve --lsi`: run local development server.
- `bundle exec jekyll build --lsi`: production-style build to `_site/`.
- `docker compose up`: run the containerized dev environment on port `8080`.
- `bin/cibuild`: quick CI-equivalent build helper.
- `pre-commit run --all-files`: run configured checks (`trailing-whitespace`, `end-of-file-fixer`, YAML validation, large-file check).

## Coding Style & Naming Conventions
- Use 2-space indentation in YAML and SCSS.
- Keep Markdown content in files with front matter (`---` blocks).
- Blog posts should use `_posts/YYYY-MM-DD-topic.md`.
- Post-specific assets should live in `assets/posts/YYYY-MM-DD-topic/`.
- Keep page/content files focused on content; move shared logic/markup to `_includes/` and layout structure to `_layouts/`.

## Testing Guidelines
There is no separate unit-test suite in this repository. Validation is build-based:
- Run `bundle exec jekyll build --lsi` before opening a PR.
- For UI/content-heavy changes, also run `bundle exec jekyll serve --lsi` and verify affected pages in a browser.
- Run pre-commit hooks before pushing changes.

## Commit & Pull Request Guidelines
- Follow the existing commit style: short, imperative subjects such as `Add ...`, `Fix ...`, `Update ...`.
- Keep commits scoped to one logical change.
- PRs should include a concise description, changed paths, linked issue (if relevant), and screenshots for visual updates.
- For new features or bug fixes, reference an issue first, consistent with `CONTRIBUTING.md`.

## Security & Configuration Tips
- Do not commit credentials, tokens, or private keys to the repo.
- Re-check `_config.yml` values (`url`, `baseurl`, social/user IDs) before deployment.
