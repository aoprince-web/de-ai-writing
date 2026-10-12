# De-AI writing

A reusable writing standard for revising text that sounds generic, formulaic, or machine-written. It is based on the September 2026 edition of Wikipedia's *Signs of AI writing* guide (WikiProject AI Cleanup), as supplied in the project's source PDF.

The goal is to make writing clearer and more specific while preserving the author's meaning and voice. This is an editing guide, not an AI detector. A flagged phrase does not prove that a person or a model wrote the text.

## Repository contents

- `SKILL.md`: instructions for an AI assistant or editor applying the de-AI writing standard.
- `skills/phase-plan/SKILL.md`: a separate, imported project-planning skill from [BCYAYAY14/phase-plan](https://github.com/BCYAYAY14/phase-plan). It is designed primarily for Claude Code; see its [local notes](skills/phase-plan/README.md) for compatibility details.
- `references/signs.md`: the catalogue of signs, explanations, and suggested fixes.
- `scripts/check_ai_signs.py`: a lightweight pattern scanner for plain-text, Markdown, and HTML files.
- `examples/before-after.md`: a short example of the editing approach.

## Quick start

Read `SKILL.md` first. Before editing, read `references/signs.md` as the source of truth for the signs covered by this project.

Run the optional scanner with Python 3:

```bash
python3 scripts/check_ai_signs.py path/to/file.md
python3 scripts/check_ai_signs.py path/to/file.md --summary
cat draft.txt | python3 scripts/check_ai_signs.py -
```

The scanner only catches a subset of wording patterns. It cannot reliably judge puffed-up structure, rule-of-three phrasing, elegant variation, or whether a sentence adds evidence. Always read the complete piece before and after editing.

## Non-negotiable editing rules

1. Preserve facts, numbers, names, dates, links, claims, quotations, titles, legal text, spelling convention, voice, tone, formatting requirements, and length limits.
2. Do not invent details to make a rewrite sound more vivid or human.
3. Remove the underlying padding or faulty sentence structure. Do not merely swap a flagged word for a synonym.
4. Keep clean sentences. Do not rewrite text just to make it different.
5. Leave quotations and source titles unchanged.
6. Report briefly what changed, what pattern counts changed where the scanner was used, and any deliberate remaining matches.

## Separate project-planning skill

The repository also includes an imported copy of the `phase-plan` skill in `skills/phase-plan/`. It is separate from the de-AI writing workflow and does not change the root `SKILL.md`. The original skill targets Claude Code and may need adaptation before use with other assistants.

## Use with other assistants

This repository can be used as a reference when configuring Claude Code, other coding assistants, or a general-purpose AI assistant. Copy or point the assistant to `SKILL.md` and ensure it can read `references/signs.md`. Exact installation steps depend on the assistant and its skill-loading conventions.

## Source and scope

The source PDF provided for this project identifies its basis as Wikipedia's *Signs of AI writing* (WikiProject AI Cleanup), September 2026 edition. The repository adapts that material into a practical editing workflow. Check the source page and its licensing terms before redistributing material beyond what the applicable licence permits.

## Important limitation

This project does not determine authorship and cannot prove that text was written by AI. It helps an editor notice and revise stylistic patterns. Human writing can contain these patterns, and AI-assisted writing can avoid them.
