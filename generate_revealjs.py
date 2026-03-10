"""
Markdown presenter-deck to Reveal.js HTML converter.

Usage:
    python generate_revealjs.py

Reads all presenter-deck.md files from materials/*/slides/ and produces
self-contained HTML slide decks in html-slides/.

No npm or local install required -- uses Reveal.js from CDN.
"""

import re
import os
import glob
import html as html_lib
from pathlib import Path


# ---------------------------------------------------------------------------
# Markdown parser (handles both deck patterns)
# ---------------------------------------------------------------------------

def parse_presenter_deck(md_path):
    """Parse a presenter-deck.md into (deck_title, [slide_dicts])."""
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()

    deck_title = ""
    h1 = re.match(r"^#\s+(.+)", text, re.MULTILINE)
    if h1:
        deck_title = h1.group(1).strip()
        deck_title = re.sub(r"^Presenter Deck:\s*", "", deck_title)

    slide_blocks = re.split(r"\n(?=## )", text)
    slides = []

    for block in slide_blocks:
        h2 = re.match(r"^##\s+Slide\s+\d+[.:]\s*(.+)", block)
        if not h2:
            continue
        title = h2.group(1).strip()
        body = block[h2.end():].strip()

        content = []
        notes = []
        section = None

        for line in body.split("\n"):
            s = line.strip()
            low = s.lower()
            if low.startswith("on-screen content:") or low.startswith("key points:"):
                section = "content"
                continue
            elif low.startswith("presenter note"):
                section = "notes"
                continue
            if s.startswith("- "):
                item = s[2:].strip()
                if section == "content":
                    content.append(item)
                elif section == "notes":
                    notes.append(item)
                else:
                    content.append(item)

        slides.append({"title": title, "content": content, "notes": notes})

    return deck_title, slides


# ---------------------------------------------------------------------------
# Slide categorization for accent colors
# ---------------------------------------------------------------------------

CATEGORY_COLORS = {
    "title":      ("#0078D4", "#001f3f"),   # accent, bg gradient end
    "objectives": ("#0078D4", "#0a1628"),
    "example":    ("#2ecc71", "#0a1628"),
    "lab":        ("#2ecc71", "#0f2b1a"),
    "validation": ("#e74c3c", "#0a1628"),
    "reflection": ("#9b59b6", "#1a0a28"),
    "references": ("#95a5a6", "#0a1628"),
    "default":    ("#0078D4", "#0a1628"),
}


def categorize(title_lower):
    for key, words in [
        ("title", ["title", "module purpose"]),
        ("objectives", ["objective", "learning"]),
        ("example", ["example", "bi example", "ds example", "de example", "scenario"]),
        ("lab", ["lab", "hands-on", "exercise"]),
        ("validation", ["validation", "checklist"]),
        ("reflection", ["reflection", "wrap"]),
        ("references", ["reference", "resource"]),
    ]:
        if any(w in title_lower for w in words):
            return key
    return "default"


# ---------------------------------------------------------------------------
# HTML generation
# ---------------------------------------------------------------------------

def esc(text):
    return html_lib.escape(text)


def slide_html(slide_data, index, total, deck_title):
    """Generate HTML for one Reveal.js slide section."""
    title = slide_data["title"]
    content = slide_data["content"]
    notes = slide_data["notes"]
    cat = categorize(title.lower())
    accent, _ = CATEGORY_COLORS.get(cat, CATEGORY_COLORS["default"])

    # Build bullet list
    bullets = ""
    if content:
        items = "\n".join(
            f'                        <li class="fragment fade-in-then-semi-out">{esc(c)}</li>'
            for c in content
        )
        bullets = f"""
                    <ul class="content-list">
{items}
                    </ul>"""

    # Notes
    notes_html = ""
    if notes:
        notes_text = "<br>".join(esc(n) for n in notes)
        notes_html = f"""
                    <aside class="notes">
                        {notes_text}
                    </aside>"""

    # Category badge
    cat_label = cat.upper() if cat != "default" else ""
    badge = f'<span class="slide-badge" style="background:{accent}">{cat_label}</span>' if cat_label else ""

    return f"""
                <section data-background-color="#0f1729" data-transition="slide">
                    <div class="slide-header">
                        <div class="accent-line" style="background:{accent}"></div>
                        <div class="slide-meta">
                            {badge}
                            <span class="slide-num">{index}/{total}</span>
                        </div>
                    </div>
                    <h2 style="border-left: 4px solid {accent}; padding-left: 0.5em;">{esc(title)}</h2>
{bullets}
{notes_html}
                </section>"""


def title_slide_html(deck_title, subtitle):
    return f"""
                <section data-background-gradient="radial-gradient(circle at 30% 50%, #0078D4 0%, #001a33 70%)" data-transition="zoom">
                    <div class="title-slide">
                        <div class="title-decoration"></div>
                        <h1>{esc(deck_title)}</h1>
                        <p class="subtitle">{esc(subtitle)}</p>
                        <div class="title-divider"></div>
                        <p class="branding">AI Coding Agent Training &nbsp;|&nbsp; GitHub Copilot in VS Code</p>
                    </div>
                </section>"""


def section_divider_html(heading, sub=""):
    sub_html = f'<p class="section-sub">{esc(sub)}</p>' if sub else ""
    return f"""
                <section data-background-gradient="linear-gradient(135deg, #0078D4 0%, #00b4d8 100%)" data-transition="zoom">
                    <div class="section-divider">
                        <h1>{esc(heading)}</h1>
                        {sub_html}
                    </div>
                </section>"""


def end_slide_html(deck_title):
    return f"""
                <section data-background-gradient="radial-gradient(circle at 70% 50%, #0078D4 0%, #001a33 70%)" data-transition="zoom">
                    <div class="end-slide">
                        <h1>Thank You</h1>
                        <div class="end-divider"></div>
                        <p class="end-title">{esc(deck_title)}</p>
                        <p class="end-cta">Questions &amp; Discussion</p>
                    </div>
                </section>"""


def full_html(deck_title, slides):
    total = len(slides)
    subtitle = f"{total} slides  |  BI, Data Science, Data Engineering"

    sections = [title_slide_html(deck_title, subtitle)]

    for i, sd in enumerate(slides, 1):
        cat = categorize(sd["title"].lower())
        if cat == "lab":
            sections.append(section_divider_html("Hands-On Lab", "Time to practice"))
        elif cat == "reflection":
            sections.append(section_divider_html("Reflection", "What did you learn?"))
        sections.append(slide_html(sd, i, total, deck_title))

    sections.append(end_slide_html(deck_title))
    all_sections = "\n".join(sections)

    return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{esc(deck_title)}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/theme/black.css">
    <style>
        /* ---- Custom theme overrides ---- */
        :root {{
            --r-background-color: #0f1729;
            --r-heading-color: #ffffff;
            --r-main-color: #e0e6ed;
            --r-link-color: #00b4d8;
            --accent-blue: #0078D4;
            --accent-green: #2ecc71;
            --accent-red: #e74c3c;
        }}

        .reveal {{
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        }}

        .reveal h1, .reveal h2, .reveal h3 {{
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            font-weight: 600;
            text-transform: none;
            letter-spacing: -0.02em;
        }}

        .reveal h1 {{ font-size: 2.4em; }}
        .reveal h2 {{ font-size: 1.6em; color: #ffffff; }}

        /* Title slide */
        .title-slide {{
            text-align: left;
            padding-left: 2em;
        }}
        .title-slide h1 {{
            font-size: 2.6em;
            line-height: 1.15;
            margin-bottom: 0.3em;
            text-shadow: 0 2px 20px rgba(0,0,0,0.4);
        }}
        .title-slide .subtitle {{
            font-size: 1.1em;
            color: #8ecae6;
            margin-bottom: 1em;
        }}
        .title-decoration {{
            width: 80px;
            height: 4px;
            background: var(--accent-green);
            margin-bottom: 1.5em;
            border-radius: 2px;
        }}
        .title-divider {{
            width: 120px;
            height: 3px;
            background: linear-gradient(90deg, var(--accent-blue), var(--accent-green));
            margin: 0.8em 0;
            border-radius: 2px;
        }}
        .title-slide .branding {{
            font-size: 0.75em;
            color: #5d6d7e;
            margin-top: 1.5em;
        }}

        /* Slide header bar */
        .slide-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.8em;
        }}
        .accent-line {{
            height: 3px;
            flex-grow: 1;
            border-radius: 2px;
            margin-right: 1em;
        }}
        .slide-meta {{
            display: flex;
            align-items: center;
            gap: 0.6em;
            flex-shrink: 0;
        }}
        .slide-badge {{
            font-size: 0.55em;
            padding: 0.15em 0.6em;
            border-radius: 20px;
            color: white;
            font-weight: 600;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }}
        .slide-num {{
            font-size: 0.6em;
            color: #5d6d7e;
            font-variant-numeric: tabular-nums;
        }}

        /* Content bullets */
        .content-list {{
            list-style: none;
            text-align: left;
            padding-left: 0;
            margin-top: 0.6em;
        }}
        .content-list li {{
            position: relative;
            padding-left: 1.6em;
            margin-bottom: 0.55em;
            font-size: 0.85em;
            line-height: 1.5;
            color: #c8d6e5;
        }}
        .content-list li::before {{
            content: '';
            position: absolute;
            left: 0;
            top: 0.55em;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--accent-blue);
        }}

        /* Fragment animation */
        .content-list li.fragment.fade-in-then-semi-out.visible {{
            opacity: 1;
            color: #ffffff;
        }}
        .content-list li.fragment.fade-in-then-semi-out.visible.current-fragment {{
            color: #ffffff;
        }}

        /* Section divider */
        .section-divider {{
            text-align: center;
        }}
        .section-divider h1 {{
            font-size: 3em;
            margin-bottom: 0.2em;
            text-shadow: 0 4px 30px rgba(0,0,0,0.3);
        }}
        .section-sub {{
            font-size: 1.2em;
            color: rgba(255,255,255,0.7);
            font-style: italic;
        }}

        /* End slide */
        .end-slide {{
            text-align: center;
        }}
        .end-slide h1 {{
            font-size: 3.2em;
            margin-bottom: 0.1em;
        }}
        .end-divider {{
            width: 140px;
            height: 3px;
            background: linear-gradient(90deg, var(--accent-green), var(--accent-blue));
            margin: 0.6em auto;
            border-radius: 2px;
        }}
        .end-title {{
            font-size: 1em;
            color: #8ecae6;
        }}
        .end-cta {{
            font-size: 0.85em;
            color: #5d6d7e;
            margin-top: 1em;
        }}

        /* Speaker notes are handled natively by Reveal.js --
           press S while presenting to see them */

        /* Progress bar styling */
        .reveal .progress {{
            color: var(--accent-blue);
            height: 4px;
        }}

        /* Slide number */
        .reveal .slide-number {{
            font-size: 0.6em;
            color: #5d6d7e;
        }}
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
{all_sections}
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/plugin/notes/notes.js"></script>
    <script>
        Reveal.initialize({{
            hash: true,
            slideNumber: 'c/t',
            showSlideNumber: 'all',
            transition: 'slide',
            transitionSpeed: 'default',
            backgroundTransition: 'fade',
            center: true,
            progress: true,
            controls: true,
            controlsTutorial: true,
            plugins: [RevealNotes],
            width: 1920,
            height: 1080,
        }});
    </script>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    base = Path(__file__).parent
    output_dir = base / "html-slides"
    output_dir.mkdir(exist_ok=True)

    md_files = sorted(glob.glob(
        str(base / "materials" / "*" / "slides" / "presenter-deck.md")
    ))

    if not md_files:
        print("No presenter-deck.md files found.")
        return

    print(f"Found {len(md_files)} presenter decks. Generating Reveal.js HTML...\n")

    for md_path in md_files:
        module_name = Path(md_path).parts[-3]
        out_path = output_dir / f"{module_name}.html"

        deck_title, slides = parse_presenter_deck(md_path)
        if not slides:
            print(f"  SKIP (no slides): {module_name}")
            continue

        html_content = full_html(deck_title, slides)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html_content)

        size_kb = os.path.getsize(out_path) / 1024
        print(f"  OK  {module_name}.html ({size_kb:.1f} KB, {len(slides)} content slides)")

    print(f"\nDone. Open any HTML file from: {output_dir}")
    print("Press S during presentation to open speaker notes view.")


if __name__ == "__main__":
    main()
