# -*- coding: utf-8 -*-
"""Add a direct link to the standalone file at the top of each embedded report."""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REPORTS_DIR = Path("reports")
LATEST_REPORT = REPORTS_DIR / "latest_report.md"

START_RE = re.compile(
    r"<!--\s*([A-Z][A-Z0-9_]+)_START\s*-->"
)
H1_RE = re.compile(r"^#\s+(.+?)\s*$", flags=re.MULTILINE)
GENERATED_RE = re.compile(
    r"^\s*(?:Generato|Aggiornato|Ultimo aggiornamento)\s*:",
    flags=re.IGNORECASE,
)

AUTO_MARKER = "<!-- DIRECT_REPORT_LINK -->"
DIRECT_LINE_PREFIX = "Report separato completo:"


@dataclass(frozen=True)
class Candidate:
    path: Path
    title: str
    markers: frozenset[str]


def _read(path: Path) -> str:
    try:
        return path.read_text(
            encoding="utf-8",
            errors="replace",
        )
    except OSError:
        return ""


def _normalise(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    ascii_like = "".join(
        char
        for char in decomposed
        if not unicodedata.combining(char)
    )
    return " ".join(
        re.findall(
            r"[a-z0-9]+",
            ascii_like.lower(),
        )
    )


def _first_title(text: str) -> str:
    match = H1_RE.search(text)
    return match.group(1).strip() if match else ""


def _candidate_files() -> list[Candidate]:
    candidates: list[Candidate] = []
    if not REPORTS_DIR.exists():
        return candidates

    for path in sorted(REPORTS_DIR.glob("*.md")):
        if path == LATEST_REPORT:
            continue
        text = _read(path)
        if not text:
            continue
        markers = frozenset(START_RE.findall(text))
        title = _first_title(text)
        if not markers and not title:
            continue
        candidates.append(
            Candidate(
                path=path,
                title=title,
                markers=markers,
            )
        )
    return candidates


def _rank_candidate(
    marker: str,
    title: str,
    candidate: Candidate,
) -> tuple[int, int, str]:
    stem = candidate.path.stem.lower()
    marker_words = marker.lower().split("_")
    title_key = _normalise(title)
    candidate_title_key = _normalise(candidate.title)

    score = 0
    if marker in candidate.markers:
        score += 1000
    if title_key and candidate_title_key == title_key:
        score += 700
    elif (
        title_key
        and candidate_title_key
        and (
            title_key in candidate_title_key
            or candidate_title_key in title_key
        )
    ):
        score += 250

    if stem == marker.lower():
        score += 180
    if stem == marker.lower() + "_report":
        score += 220
    if all(word in stem for word in marker_words):
        score += 80
    if stem.endswith("_report"):
        score += 20

    return (
        score,
        -len(candidate.path.name),
        candidate.path.name,
    )


def _choose_candidate(
    marker: str,
    block: str,
    candidates: Iterable[Candidate],
) -> Candidate | None:
    title = _first_title(block)
    ranked = sorted(
        (
            (_rank_candidate(marker, title, candidate), candidate)
            for candidate in candidates
        ),
        key=lambda item: item[0],
        reverse=True,
    )
    if not ranked:
        return None

    best_rank, best = ranked[0]
    if best_rank[0] < 250:
        return None
    return best


def _find_blocks(text: str) -> list[tuple[int, int, str]]:
    blocks: list[tuple[int, int, str]] = []
    cursor = 0

    while True:
        start_match = START_RE.search(text, cursor)
        if start_match is None:
            break

        marker = start_match.group(1)
        end_token = f"<!-- {marker}_END -->"
        end_index = text.find(
            end_token,
            start_match.end(),
        )
        if end_index < 0:
            cursor = start_match.end()
            continue

        end_index += len(end_token)
        blocks.append(
            (
                start_match.start(),
                end_index,
                marker,
            )
        )
        cursor = end_index

    return blocks


def _has_direct_link(
    block: str,
    filename: str,
) -> bool:
    lines = block.splitlines()
    top = "\n".join(lines[:30])

    if AUTO_MARKER in top:
        return True
    if DIRECT_LINE_PREFIX.lower() in top.lower():
        return True

    relative_patterns = (
        f"]({filename})",
        f"](./{filename})",
        f"](reports/{filename})",
    )
    return any(pattern in top for pattern in relative_patterns)


def _insert_direct_link(
    block: str,
    filename: str,
) -> tuple[str, bool]:
    if _has_direct_link(block, filename):
        return block, False

    lines = block.splitlines()
    heading_index = next(
        (
            index
            for index, line in enumerate(lines)
            if line.startswith("# ")
        ),
        None,
    )
    if heading_index is None:
        return block, False

    generated_index = None
    upper = min(len(lines), heading_index + 14)
    for index in range(heading_index + 1, upper):
        if GENERATED_RE.match(lines[index]):
            generated_index = index
            break

    anchor = (
        generated_index + 1
        if generated_index is not None
        else heading_index + 1
    )

    while (
        anchor < len(lines)
        and not lines[anchor].strip()
    ):
        anchor += 1

    insertion = [
        "",
        AUTO_MARKER,
        (
            f"{DIRECT_LINE_PREFIX} "
            f"[{filename}]({filename})"
        ),
        "",
    ]
    lines[anchor:anchor] = insertion

    trailing_newline = "\n" if block.endswith("\n") else ""
    return "\n".join(lines) + trailing_newline, True


def process(text: str) -> tuple[str, dict[str, object]]:
    candidates = _candidate_files()
    blocks = _find_blocks(text)

    changed = 0
    linked = 0
    unresolved: list[str] = []
    replacements: list[tuple[int, int, str]] = []

    for start, end, marker in blocks:
        block = text[start:end]
        candidate = _choose_candidate(
            marker,
            block,
            candidates,
        )
        if candidate is None:
            unresolved.append(marker)
            continue

        filename = candidate.path.name
        if _has_direct_link(block, filename):
            linked += 1
            continue

        updated, did_change = _insert_direct_link(
            block,
            filename,
        )
        if did_change:
            replacements.append((start, end, updated))
            changed += 1

    output = text
    for start, end, replacement in reversed(replacements):
        output = output[:start] + replacement + output[end:]

    audit = {
        "blocks": len(blocks),
        "candidates": len(candidates),
        "already_linked": linked,
        "added": changed,
        "unresolved": sorted(set(unresolved)),
    }
    return output, audit


def _missing_resolvable_links(text: str) -> list[str]:
    candidates = _candidate_files()
    missing: list[str] = []

    for start, end, marker in _find_blocks(text):
        block = text[start:end]
        candidate = _choose_candidate(
            marker,
            block,
            candidates,
        )
        if candidate is None:
            continue
        if not _has_direct_link(
            block,
            candidate.path.name,
        ):
            missing.append(marker)

    return sorted(set(missing))


def update_latest_report_links() -> dict[str, object]:
    if not LATEST_REPORT.exists():
        return {
            "blocks": 0,
            "candidates": 0,
            "already_linked": 0,
            "added": 0,
            "unresolved": [],
        }

    original = _read(LATEST_REPORT)
    updated, audit = process(original)
    if updated != original:
        LATEST_REPORT.write_text(
            updated,
            encoding="utf-8",
            newline="\n",
        )
    return audit


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="Verify links without modifying the report.",
    )
    args = parser.parse_args()

    if not LATEST_REPORT.exists():
        print(
            f"Report non trovato: {LATEST_REPORT}",
            file=sys.stderr,
        )
        return 1

    if args.check:
        missing = _missing_resolvable_links(
            _read(LATEST_REPORT)
        )
        if missing:
            print(
                "Sezioni con report separato ma senza link: "
                + ", ".join(missing),
                file=sys.stderr,
            )
            return 1
        print(
            "Controllo link report superato: "
            "tutte le sezioni risolvibili hanno il link."
        )
        return 0

    audit = update_latest_report_links()
    print(
        "Link report: "
        f"{audit['added']} aggiunti, "
        f"{audit['already_linked']} già presenti, "
        f"{len(audit['unresolved'])} sezioni senza "
        "file separato riconoscibile."
    )
    if audit["unresolved"]:
        print(
            "Senza file separato: "
            + ", ".join(audit["unresolved"])
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
