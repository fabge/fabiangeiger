from __future__ import annotations

import html
import json
import re
import shutil
from pathlib import Path
from urllib.parse import quote

import markdown

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
PAGES = CONTENT / "pages"
PHOTOS = CONTENT / "photos"
PHOTO_METADATA = CONTENT / "photo-metadata.json"
STATIC = ROOT / "static"
PUBLIC = ROOT / "public"

SITE_NAME = "fabiangeiger"
SITE_DESCRIPTION = "Personal website of Fabian Geiger"

SUPPORTED_PHOTO_TYPES = {".avif", ".jpeg", ".jpg", ".png", ".webp"}
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?(.*)\Z", re.DOTALL)


def parse_markdown_page(path: Path) -> tuple[dict[str, str], str]:
    source = path.read_text(encoding="utf-8")
    match = FRONTMATTER.match(source)
    if not match:
        return {}, source

    metadata: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, separator, value = line.partition(":")
        if separator:
            metadata[key.strip()] = value.strip().strip('"\'')
    return metadata, match.group(2)


def page_template(title: str, body: str, description: str = SITE_DESCRIPTION) -> str:
    safe_title = html.escape(title)
    safe_description = html.escape(description)
    document_title = safe_title if title == SITE_NAME else f"{safe_title} · {SITE_NAME}"
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="{safe_description}">
    <title>{document_title}</title>
    <link rel="stylesheet" href="/css/site.css">
    <link rel="icon" href="/favicons/favicon.ico">
    <link rel="apple-touch-icon" href="/favicons/apple-touch-icon.png">
  </head>
  <body>
    <header class="site-header">
      <nav class="site-nav" aria-label="Main navigation">
        <a class="site-mark" href="/">FG</a>
        <div class="nav-links">
          <a href="/photos/">photos</a>
          <a href="https://tools.fabiangeiger.com/" target="_blank" rel="noopener">tools</a>
          <a href="https://til.fabiangeiger.com" target="_blank" rel="noopener">til</a>
        </div>
      </nav>
    </header>
    <main class="site-main">
      {body}
    </main>
    <footer class="site-footer">
      <div class="footer-inner">© Fabian Geiger <script>document.write(new Date().getFullYear())</script></div>
    </footer>
  </body>
</html>
"""


def photo_files() -> list[Path]:
    return sorted(
        (path for path in PHOTOS.rglob("*") if path.is_file() and path.suffix.lower() in SUPPORTED_PHOTO_TYPES),
        key=lambda path: path.relative_to(PHOTOS).as_posix(),
        reverse=True,
    )


def photo_url(path: Path) -> str:
    relative = path.relative_to(PHOTOS)
    return "/photos/" + "/".join(quote(part) for part in relative.parts)


def photo_metadata() -> dict[str, str]:
    if not PHOTO_METADATA.exists():
        return {}
    metadata = json.loads(PHOTO_METADATA.read_text(encoding="utf-8"))
    if not isinstance(metadata, dict) or not all(isinstance(key, str) and isinstance(value, str) for key, value in metadata.items()):
        raise ValueError("photo-metadata.json must contain a filename-to-alt-text object")
    return metadata


def photo_alt(path: Path, metadata: dict[str, str]) -> str:
    relative_path = path.relative_to(PHOTOS).as_posix()
    return metadata.get(relative_path, metadata.get(path.name, "Photograph"))


def render_gallery() -> str:
    metadata = photo_metadata()
    items = []
    for path in photo_files():
        url = photo_url(path)
        alt = html.escape(photo_alt(path, metadata), quote=True)
        items.append(
            f'''<a class="photo-link" href="{url}">
  <img src="{url}" loading="lazy" decoding="async" alt="{alt}">
</a>''',
        )
    gallery = "\n".join(items) or '<p class="muted">No photos yet.</p>'
    return f"""<div class="page-layout">
  <div class="page-sidebar">
    <h1 class="section-title">Photos</h1>
    <hr>
  </div>
  <div class="photo-list">
    {gallery}
  </div>
</div>"""


def render_markdown_pages() -> None:
    for source in sorted(PAGES.rglob("*.md")):
        metadata, body = parse_markdown_page(source)
        slug = metadata.get("slug", source.stem)
        title = metadata.get("title", source.stem.replace("-", " ").title())
        description = metadata.get("description", SITE_DESCRIPTION)
        rendered = markdown.markdown(body, extensions=["extra", "sane_lists"])
        destination = PUBLIC / slug / "index.html"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            page_template(title, f'<article class="prose">{rendered}</article>', description),
            encoding="utf-8",
        )


def copy_static_files() -> None:
    if STATIC.exists():
        shutil.copytree(STATIC, PUBLIC, dirs_exist_ok=True)
    if PHOTOS.exists():
        shutil.copytree(PHOTOS, PUBLIC / "photos", dirs_exist_ok=True)


def build() -> None:
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir()

    homepage = (CONTENT / "index.html").read_text(encoding="utf-8")
    (PUBLIC / "index.html").write_text(
        page_template(SITE_NAME, homepage),
        encoding="utf-8",
    )

    gallery_page = page_template("photos", render_gallery())
    gallery_destination = PUBLIC / "photos" / "index.html"
    gallery_destination.parent.mkdir(parents=True, exist_ok=True)
    gallery_destination.write_text(gallery_page, encoding="utf-8")

    render_markdown_pages()
    copy_static_files()


if __name__ == "__main__":
    build()
