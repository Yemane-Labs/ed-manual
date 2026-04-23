#!/usr/bin/env python3
"""
Build script for the ED Platform Manual.

Reads markdown files from src/<category>/*.md and generates a single-page
index.html with a categorized sidebar.

Adding new content:
  1. Create a new category folder under src/ (e.g., `src/topics/`)
  2. Drop numbered markdown files into it (e.g., `01-creating-a-topic.md`)
  3. Register the category in CATEGORIES below
  4. Run: python3 build.py
  5. Commit & push — GitHub Pages rebuilds automatically

File naming conventions:
  - `NN-kebab-case-slug.md` — prefix NN controls sort order in the sidebar
  - The first-line `# Heading` becomes the sidebar label (falls back to filename)
"""

import json
import re
from pathlib import Path

# Order matters — this is the order sections appear in the sidebar
CATEGORIES = [
    ("overview", "Overview", ""),
    ("emails",   "Emails",   "📧"),
    # Future (uncomment + add folder + docs to enable):
    # ("admin-navigation", "Admin Navigation", "🧭"),
    # ("topics",           "Topics",           "🏷️"),
    # ("conversations",    "Conversations",    "🗓️"),
    # ("partner-pages",    "Partner Pages",    "👥"),
    # ("users-and-roles",  "Users & Roles",    "👤"),
    # ("reports",          "Reports & Exports","📊"),
]

HERE = Path(__file__).parent
SRC = HERE / "src"

def extract_title(md_text: str, fallback: str) -> str:
    """Pull the first `# ` heading for the sidebar label."""
    for line in md_text.splitlines():
        m = re.match(r"^#\s+(.+?)\s*$", line)
        if m:
            return m.group(1).strip()
    return fallback

def slugify_filename(stem: str) -> str:
    """Strip leading NN- numeric prefix and return kebab-case slug."""
    return re.sub(r"^\d+-", "", stem)

def collect_docs():
    """Walk categories, return {doc_key: {title, markdown, category}}, plus sidebar tree."""
    docs = {}
    sidebar = []  # list of (category_label, emoji, [(doc_key, title), ...])

    for folder, label, emoji in CATEGORIES:
        cat_dir = SRC / folder
        entries = []
        if cat_dir.exists():
            for md_path in sorted(cat_dir.glob("*.md")):
                slug = slugify_filename(md_path.stem)
                doc_key = f"{folder}/{slug}"
                text = md_path.read_text()
                title = extract_title(text, slug)
                docs[doc_key] = text
                entries.append((doc_key, title))
        sidebar.append((folder, label, emoji, entries))
    return docs, sidebar

def render_html(docs, sidebar) -> str:
    sidebar_html = []
    first_doc = None
    for folder, label, emoji, entries in sidebar:
        if not entries:
            continue
        if folder == "overview":
            # Render overview entries as ungrouped top links
            for key, title in entries:
                if first_doc is None:
                    first_doc = key
                sidebar_html.append(
                    f'    <a data-doc="{key}">{title}</a>'
                )
        else:
            header = f"{emoji + ' ' if emoji else ''}{label}".strip()
            sidebar_html.append(f'    <div class="sec">{header}</div>')
            for key, title in entries:
                if first_doc is None:
                    first_doc = key
                # Strip category prefix from display
                display = title
                sidebar_html.append(
                    f'    <a data-doc="{key}">{display}</a>'
                )

    nav_html = "\n".join(sidebar_html)
    docs_json = json.dumps(docs)
    first_doc = first_doc or "overview/overview"

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>ED Platform — Manual</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
  body {{ font: 16px/1.65 -apple-system, BlinkMacSystemFont, sans-serif; margin: 0; background: #f7f7f5; color: #222; }}
  .layout {{ display: grid; grid-template-columns: 280px 1fr; min-height: 100vh; }}
  aside {{ background: #AE4C5F; color: #fff; padding: 0; position: sticky; top: 0; height: 100vh; overflow-y: auto; }}
  aside .brand {{ padding: 20px 22px; border-bottom: 1px solid rgba(255,255,255,0.15); }}
  aside .brand h1 {{ margin: 0; font-size: 17px; font-weight: 600; }}
  aside nav {{ padding: 12px 0 40px; }}
  aside nav a {{ display: block; padding: 9px 22px; color: #fff; text-decoration: none; border-left: 3px solid transparent; font-size: 14px; cursor: pointer; }}
  aside nav a:hover {{ background: rgba(255,255,255,0.08); }}
  aside nav a.active {{ background: rgba(255,255,255,0.14); border-left-color: #FCB44C; font-weight: 600; }}
  aside nav .sec {{ font-size: 11px; text-transform: uppercase; letter-spacing: 1px; opacity: 0.6; padding: 18px 22px 6px; }}
  main {{ padding: 40px 56px 80px; max-width: 820px; }}
  h1 {{ border-bottom: 3px solid #FCB44C; padding-bottom: 10px; font-size: 28px; }}
  h2 {{ margin-top: 44px; color: #AE4C5F; font-size: 22px; }}
  h3 {{ margin-top: 34px; color: #444; font-size: 17px; }}
  h4 {{ color: #555; font-size: 15px; margin-top: 24px; }}
  table {{ border-collapse: collapse; width: 100%; margin: 16px 0; background: #fff; font-size: 14px; border-radius: 6px; overflow: hidden; box-shadow: 0 1px 3px rgba(0,0,0,0.04); }}
  th, td {{ padding: 10px 14px; border-bottom: 1px solid #eee; text-align: left; vertical-align: top; }}
  th {{ background: #FCB44C; color: #333; font-weight: 600; border-bottom: none; }}
  tr:last-child td {{ border-bottom: none; }}
  tr:nth-child(even) {{ background: #fafafa; }}
  code {{ background: #fff0e8; padding: 1px 6px; border-radius: 3px; font-size: 0.9em; color: #AE4C5F; font-family: 'SF Mono', Menlo, monospace; }}
  blockquote {{ border-left: 3px solid #FCB44C; margin: 20px 0; padding: 12px 18px; color: #555; background: #fff8ea; border-radius: 0 6px 6px 0; }}
  hr {{ border: 0; border-top: 2px dashed #ddd; margin: 36px 0; }}
  a {{ color: #AE4C5F; }}
  strong {{ color: #333; }}
  ul, ol {{ padding-left: 22px; }}
  li {{ margin: 4px 0; }}
  .footer-note {{ margin-top: 60px; padding: 20px; background: #fff; border-radius: 8px; color: #888; font-size: 13px; text-align: center; }}
  .dim {{ opacity: 0.45; transition: opacity 0.15s; }}
  .dim:hover {{ opacity: 0.75; }}
</style>
</head><body>
<div class="layout">
<aside>
  <div class="brand"><h1>ED Platform Manual</h1></div>
  <nav>
{nav_html}
  </nav>
</aside>
<main>
  <div id="doc"></div>
  <div class="footer-note">Maintained by the devs · built from <a href="https://github.com/Yemane-Labs/ed-manual" style="color:#AE4C5F;">Yemane-Labs/ed-manual</a></div>
</main>
</div>
<script>
const DOCS = {docs_json};
function render(key) {{
  document.querySelectorAll('aside nav a').forEach(a => a.classList.toggle('active', a.dataset.doc === key));
  const md = DOCS[key] || '# Not found\\n\\nThat section does not exist yet.';
  document.getElementById('doc').innerHTML = marked.parse(md);
  // Dim any section whose heading says "(coming soon)"
  document.querySelectorAll('#doc h1, #doc h2, #doc h3, #doc h4').forEach(h => {{
    if (/coming soon/i.test(h.textContent)) {{
      h.classList.add('dim');
      let sib = h.nextElementSibling;
      while (sib && !/^H[1-4]$/.test(sib.tagName)) {{
        sib.classList.add('dim');
        sib = sib.nextElementSibling;
      }}
    }}
  }});
  window.scrollTo(0, 0);
  history.replaceState(null, '', '#' + key.replace(/\\//g, '-'));
}}
document.querySelectorAll('aside nav a').forEach(a => a.addEventListener('click', () => render(a.dataset.doc)));
const initialHash = location.hash.slice(1).replace('-', '/');
render((initialHash && DOCS[initialHash]) ? initialHash : '{first_doc}');
</script>
</body></html>"""

def main():
    docs, sidebar = collect_docs()
    html = render_html(docs, sidebar)
    (HERE / "index.html").write_text(html)
    total = sum(len(v) for v in docs.values())
    print(f"✓ Built index.html ({total:,} bytes of markdown across {len(docs)} docs)")
    for folder, label, emoji, entries in sidebar:
        if entries:
            print(f"  {emoji} {label}: {len(entries)} doc(s)")

if __name__ == "__main__":
    main()
