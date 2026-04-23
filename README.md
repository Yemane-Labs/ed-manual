# Equitable Dinners Platform Manual

A growing reference for managing the ED platform day-to-day. Written for OOH staff — no code knowledge required.

**📖 Read online:** https://yemane-labs.github.io/ed-manual/

## Structure

- `src/<category>/*.md` — editable source markdown files
- `build.py` — generates `index.html` from `src/`
- `index.html` — rendered output (what GitHub Pages serves)

## Adding new content

1. Create a new category folder under `src/` (e.g. `src/topics/`)
2. Drop numbered markdown files into it (e.g. `01-creating-a-topic.md`)
3. Register the category in `build.py` (uncomment a line in `CATEGORIES`)
4. Run: `python3 build.py`
5. Commit & push — GitHub Pages rebuilds automatically

## Requesting changes (for OOH staff)

Create a task in Asana (Inclusivv Platform Transition & Maintenance project) and assign it to the devs.

## Maintained by

Aki & Dino (Yemane Labs).
