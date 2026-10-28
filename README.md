# Lección 4 · Minimal HTML trainers

This folder contains **five** independent HTML practice pages and both `index.html` and editable `index.Rmd` landing pages.

- `subjunctive_teaching.html` — original trainer (unchanged; visual reference).
- `commands_practice.html` — **minimal version**, aligned to the original subjunctive trainer.
- `irregular_subjunctive_practice.html` — **minimal version**, aligned to the original subjunctive trainer.
- `vocabulary_isolated.html` and `vocabulary_contextualized.html` — original vocabulary trainers (unchanged).

## Visual design

The two revised trainers match `subjunctive_teaching.html`: white full-screen slides, centered blue English prompts and red Spanish answers, tiny progress and edge navigation, a small 10/20/30/all selector, audio on/off, and underlined clickable forms. They open directly on the first practice prompt. Small italic-free gray infinitive/person cues appear under English prompts only to disambiguate the intended form. There are no headings, extra help panels, group labels, or large toolbars on practice slides.

### Extra practice

Click the underlined command to request two new prompts from that **command group**; click the underlined subjunctive form to request two new prompts using **that verb**. Review order is shuffled.

### Editing JSON and rebuilding HTML

- Edit `source/commands_lesson.json`; run `python build_commands.py`.
- Edit `source/irregular_subjunctive_lesson.json`; run `python build_irregular_subjunctive.py`.

The HTML files embed the data for simple GitHub Pages hosting and local offline use. Editing JSON alone will not change the site until the associated build script is run. All other original files in the bundle are left unchanged.
