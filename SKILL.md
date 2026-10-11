---
name: de-ai-writing
description: Revise writing to remove formulaic AI-like patterns using the project's Signs of AI Writing field guide. Use when asked to de-AI, humanise, make text sound less robotic, polish AI-assisted drafts, or check writing for these patterns before publication.
---

# De-AI writing

Revise text so it reads like the work of a knowledgeable person. Use `references/signs.md` as the source of truth for the signs covered by this skill. Read it before the first rewrite in a session.

The guide treats signs as symptoms. Language models often smooth specific facts into generic, important-sounding statements. Replacing a flagged word with a synonym can hide the symptom without fixing the sentence. Fix what the sentence is doing: inflating significance, hedging without reason, correcting a misconception nobody raised, repeating itself, or adding interpretation without evidence.

## Workflow

### 1. Get the source text

Work from the supplied text, file, folder, or website. For a codebase or website, locate the source content (such as data files, CMS exports, or templates) and edit that source rather than generated output.

### 2. Scan

If Python is available, run:

```bash
python3 scripts/check_ai_signs.py <file(s)>
python3 scripts/check_ai_signs.py <file> --summary
```

The scanner accepts `.txt`, `.md`, and `.html` files; use `-` to read standard input. It reports pattern matches, not authorship. It only covers patterns that can reasonably be matched in code. Check the judgement-based signs manually against `references/signs.md`.

### 3. Rewrite carefully

- Preserve every fact, number, name, date, link, and claim. Change how a point is expressed, never what is being claimed.
- Keep the author's voice and conventions, including first or third person, UK or US spelling, tone, formatting system, and any word or character limits.
- Never alter quotations from real people or sources, titles of works, or legal text.
- If a sentence is padding, remove it. If it carries a fact, keep the fact.
- Replace vague praise with a specific, supported fact, or remove the praise. Never invent details to make the writing vivid.
- Prefer ordinary verbs such as “is”, “are”, “has”, “wrote”, “moved”, “used”, and “tried” when they express the meaning accurately.
- Rewrite overused em dashes with commas, colons, parentheses, or full stops. Do not simply substitute another dash. One or two em dashes in a long piece may be fine.
- State the positive claim directly unless a contrast is needed to correct a real likely misunderstanding.
- Do not over-correct. Perfect grammar, formal prose, a single transition, or an unsourced claim by itself is not a reason to rewrite.
- Do not flatten the author's personality or make every sentence short. Keep natural variation and useful detail.

### 4. Re-scan and reread

Run the scanner again, then read the full piece for meaning, evidence, flow, and the signs that cannot be detected with simple patterns. Aim to resolve accidental matches. A match may remain when it is a quotation, proper noun, literal use, or otherwise justified; record this briefly.

### 5. Report the work

Return the revised text or confirm which files were edited. Add a short note with:
- scanner counts before and after, if the scanner was available;
- two or three representative before-and-after examples;
- any remaining matches that were kept deliberately.

Keep the report concise. The rewritten text is the main deliverable.

## Do not

- invent facts, examples, sources, dates, links, or evidence;
- change the author's position to make prose smoother;
- replace every flagged word mechanically;
- describe the scanner as an AI detector or claim that zero matches proves human authorship;
- rewrite quotations or legal wording;
- add generic opening or closing filler such as “Certainly”, “I hope this helps”, or “Let me know if you need anything else”.

## Reference

Read [the full signs catalogue](references/signs.md) before applying this skill. The optional scanner is at [scripts/check_ai_signs.py](scripts/check_ai_signs.py).
