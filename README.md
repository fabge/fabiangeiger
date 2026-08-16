# Personal website

The site is a small static website built with Python and Markdown and deployed to GitHub Pages.

Install the dependency and build locally:

```sh
python3 -m pip install -r requirements.txt
python3 build.py
```

The generated site is written to `public/`. To preview it locally:

```sh
python3 -m http.server --directory public
```

Markdown pages live in `content/pages/` and use simple frontmatter:

```markdown
---
title: About
description: A short description for search engines.
---
```

Photos placed in `content/photos/` are automatically included in the gallery. The homepage photo selection is intentionally maintained by hand in `content/index.html`.

Photo alt text is kept in `content/photo-metadata.json`. Photos without an entry use `Photograph` as a fallback.
