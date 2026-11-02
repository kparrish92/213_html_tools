# SPN 213 — Lección 4: Minimal HTML practice (7 activities)

The original five practice pages have been preserved. Two new standalone pages have been added:

- `por_para_practice.html` — **Por y para**, built from original contextualized prompts covering textbook uses and expressions (Facetas 6e, pp. 144–145): 90 main examples + 36 review examples.
- `combined_review.html` — **Combined grammar review**, randomized and balanced across commands, por/para, subjunctive, and original integrated prompts: 200 main examples + 128 review examples.

Both pages replicate the original `subjunctive_teaching.html` visual layout: centered blue English prompt, red answer, quiet bottom navigation, 10/20/30/all subsets, audio and optional two-item follow-up review for forms clicked on the answer slide. They open on a randomized 20-item set by default. They run offline / on GitHub Pages with NO external libraries or data requests.

### Editing JSON

Edit `source/por_para_lesson.json` and run `python build_por_para_lesson.py` (Python 3). Edit `source/combined_review_lesson.json` and run `python build_combined_review_lesson.py`. HTML files EMBED a snapshot of the data. Editing JSON by itself does not change the published HTML.

### Original pages and files

- `subjunctive_teaching.html` — unchanged
- `commands_practice.html` — unchanged
- `irregular_subjunctive_practice.html` — unchanged
- `vocabulary_isolated.html` — unchanged
- `vocabulary_contextualized.html` — unchanged

`index.html` and `index.Rmd` now include links to both new activities.

### Source attribution

The **grammar categories** for por/para follow the user's screenshot of Facetas 6e pp.144–145. All new por/para sentence prompts are instructor-generated. The combined review samples from the existing original lesson JSON and these new prompts, with additional custom integrated prompts combining two or more constructions.
