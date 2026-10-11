#!/usr/bin/env python3
"""Flag selected writing patterns from the De-AI writing field guide.

This is a lightweight editorial aid, not an AI detector. A match does not
establish authorship; a lack of matches does not establish human authorship.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("1.1 significance inflation", re.compile(r"\b(?:stands as|serves as a testament|is a testament to|pivotal role|crucial role|enduring legacy|reflects broader|indelible mark|key turning point|underscores? (?:its )?importance)\b", re.I)),
    ("1.2 media notability", re.compile(r"\b(?:independent coverage|local and national media outlets|trade publications|maintains an active social media presence)\b", re.I)),
    ("1.3 superficial analysis", re.compile(r",\s*(?:highlighting|underscoring|emphasising|emphasizing|ensuring|reflecting|symbolising|symbolizing|showcasing|contributing to)\b", re.I)),
    ("1.4 promotional tone", re.compile(r"\b(?:nestled in|in the heart of|boasts a diverse array|world-class|state-of-the-art|breathtaking|seamless experience|vibrant tapestry)\b", re.I)),
    ("1.5 vague attribution", re.compile(r"\b(?:experts argue|observers note|studies show|widely regarded|some critics argue|industry reports)\b", re.I)),
    ("1.6 challenges formula", re.compile(r"\bdespite these challenges\b", re.I)),
    ("2.1 AI vocabulary", re.compile(r"\b(?:delve into|crucial|pivotal|tapestry|underscore|additionally|intricate interplay|valuable insights)\b", re.I)),
    ("2.2 copula avoidance", re.compile(r"\b(?:serves as|functions as|operates as|features|offers)\b", re.I)),
    ("2.4 negative parallelism", re.compile(r"\bnot only\b.{0,100}\bbut also\b|\bit'?s not just\b.{0,100}\bit'?s\b|\bno \w+, no \w+, just\b", re.I)),
    ("3.1 possible Title Case heading", re.compile(r"(?m)^#{1,6}\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+){2,}\s*$")),
    ("3.4 em dash", re.compile(r"—")),
    ("4.1 chat residue", re.compile(r"\b(?:I hope this helps|Certainly!|Great question|Let me know if|Would you like me to|In this section, we will discuss)\b", re.I)),
    ("4.2 gap disclaimer", re.compile(r"\b(?:as of my last update|not widely documented|based on available information|while specific details are limited)\b", re.I)),
    ("4.3 placeholder", re.compile(r"\[(?:Your Name|Describe the section)\]|\bINSERT_URL\b|\b\d{4}-XX-XX\b", re.I)),
    ("5.1 didactic disclaimer", re.compile(r"\b(?:it'?s important to note|it is worth noting|keep in mind)\b", re.I)),
    ("5.2 summary opener", re.compile(r"\b(?:in conclusion|in summary|overall|ultimately)\b", re.I)),
]

def sentences(text: str) -> list[str]:
    # Deliberately simple segmentation for a lightweight scanner.
    chunks = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [chunk.strip() for chunk in chunks if chunk.strip()]

def scan(text: str) -> list[tuple[str, str, str]]:
    found: list[tuple[str, str, str]] = []
    for sentence in sentences(text):
        for label, pattern in PATTERNS:
            match = pattern.search(sentence)
            if match:
                found.append((label, sentence, match.group(0)))
    return found

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", help="Input .txt, .md, or .html files; use - for stdin")
    parser.add_argument("--summary", action="store_true", help="Print counts by sign instead of matching sentences")
    args = parser.parse_args()
    all_found: list[tuple[str, str, str, str]] = []
    for name in args.files:
        if name == "-":
            content = sys.stdin.read()
        else:
            path = Path(name)
            if path.suffix.lower() not in {".txt", ".md", ".html", ".htm"}:
                print(f"Skipping unsupported file type: {name}", file=sys.stderr)
                continue
            try:
                content = path.read_text(encoding="utf-8")
            except OSError as exc:
                print(f"Cannot read {name}: {exc}", file=sys.stderr)
                continue
        for label, sentence, match in scan(content):
            all_found.append((name, label, sentence, match))
    if args.summary:
        counts: dict[str, int] = {}
        for _, label, _, _ in all_found:
            counts[label] = counts.get(label, 0) + 1
        if not counts:
            print("No configured patterns matched. This is not proof of human authorship.")
        else:
            for label, count in sorted(counts.items()):
                print(f"{count:>3}  {label}")
            print(f"Total matches: {len(all_found)}")
    else:
        for name, label, sentence, match in all_found:
            print(f"{name}: [{label}] matched {match!r}\n  {sentence}\n")
        if not all_found:
            print("No configured patterns matched. This is not proof of human authorship.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
