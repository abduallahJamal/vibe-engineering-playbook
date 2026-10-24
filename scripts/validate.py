#!/usr/bin/env python3
"""
CI validator for vibe-engineering-playbook.

Verifies:
1. All 6 canonical skills exist across .opencode/skills, .claude/skills, and .agents/skills
   with byte-for-byte SHA-256 parity and valid YAML frontmatter.
2. .opencode/commands/vibe.md has valid frontmatter and non-empty body.
3. All bilingual handbooks (EN + AR), templates, and root governance docs exist and have
   zero broken relative Markdown links.
4. assets/banner.svg is valid XML and contains zero Arabic <text> glyphs (preventing headless bidi fallback).
5. Zero leftover channel/transcript references from raw research notes.
6. Zero runtime code bloat inside skill directories (pure-instruction SKILL.md enforcement).
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXPECTED_SKILLS = [
    "vibe",
    "vibe-grill",
    "vibe-spec-plan",
    "vibe-scoped-build",
    "vibe-critique",
    "vibe-test-gate",
]

SKILL_TREES = [
    ROOT / ".opencode/skills",
    ROOT / ".claude/skills",
    ROOT / ".agents/skills",
]

REQUIRED_DOCS = [
    "README.md",
    "README.ar.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "docs/anti-patterns.en.md",
    "docs/anti-patterns.ar.md",
    "docs/workflow-7-stages.en.md",
    "docs/workflow-7-stages.ar.md",
    "docs/prompt-blueprints.en.md",
    "docs/prompt-blueprints.ar.md",
    "docs/checklists.en.md",
    "docs/checklists.ar.md",
    "templates/AGENTS.template.md",
    "templates/AGENTS.template.ar.md",
    "templates/PRD.template.md",
    "templates/IMPLEMENTATION_PLAN.template.md",
]

# Ensure all docs remain neutral, formal, and free of raw video-channel attributions
FORBIDDEN_TERMS = [
    "Elzero",
    "الزيرو",
    "Codezilla",
    "Koura bytes",
    "غريب الشيخ",
    "بشمهندس مازن",
    "فتحي وأبوسريع",
    "اتعلم ببساطة",
    "code zetta",
    "SEO Equation",
]

MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
ARABIC_RE = re.compile(r"[\u0600-\u06FF]")


def sha256_bytes(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("Missing opening YAML frontmatter delimiter '---'")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("Missing closing YAML frontmatter delimiter '---'")
    raw_fm = text[4:end]
    body = text[end + 5 :].strip()
    meta: dict[str, str] = {}
    for line in raw_fm.splitlines():
        if not line.strip() or line.startswith("  ") or line.strip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {line!r}")
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, body


def strip_fenced_code(md: str) -> str:
    return re.sub(r"```.*?```", "", md, flags=re.DOTALL)


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate vibe-engineering-playbook repository.")
    ap.add_argument("--github-annotations", action="store_true", help="Emit GitHub Actions error annotations")
    args = ap.parse_args()

    errors: list[tuple[str, str]] = []

    def fail(rel_path: str, msg: str) -> None:
        errors.append((rel_path, msg))
        if args.github_annotations:
            print(f"::error file={rel_path}::{msg}")
        else:
            print(f"[ERROR] {rel_path}: {msg}", file=sys.stderr)

    # 1. Validate command file
    cmd_path = ROOT / ".opencode/commands/vibe.md"
    if not cmd_path.exists():
        fail(".opencode/commands/vibe.md", "Missing /vibe slash command file")
    else:
        try:
            fm, body = parse_frontmatter(cmd_path.read_text(encoding="utf-8"))
            if not fm.get("description"):
                fail(".opencode/commands/vibe.md", "Missing 'description' in frontmatter")
            if len(body) < 40:
                fail(".opencode/commands/vibe.md", "Command body is too short")
        except ValueError as exc:
            fail(".opencode/commands/vibe.md", str(exc))

    # 2. Validate skills & pure-instruction rule + SHA-256 sync
    skill_md_count = 0
    for skill_name in EXPECTED_SKILLS:
        canonical = ROOT / ".opencode/skills" / skill_name / "SKILL.md"
        if not canonical.exists():
            fail(f".opencode/skills/{skill_name}/SKILL.md", "Missing canonical SKILL.md")
            continue

        # Enforce instructions-only inside skill folders (only SKILL.md allowed)
        extra_files = [
            p for p in (ROOT / ".opencode/skills" / skill_name).rglob("*") if p.is_file() and p.name != "SKILL.md"
        ]
        if extra_files:
            fail(
                f".opencode/skills/{skill_name}",
                f"Instructions-only violation — unexpected file(s): {[p.name for p in extra_files]}",
            )

        canonical_digest = sha256_bytes(canonical)
        for tree in SKILL_TREES:
            s_file = tree / skill_name / "SKILL.md"
            rel = str(s_file.relative_to(ROOT))
            if not s_file.exists():
                fail(rel, "Missing mirrored SKILL.md")
                continue
            skill_md_count += 1
            try:
                fm, body = parse_frontmatter(s_file.read_text(encoding="utf-8"))
                if fm.get("name") != skill_name:
                    fail(rel, f"Frontmatter name {fm.get('name')!r} != directory {skill_name!r}")
                for req_key in ("description", "license", "compatibility"):
                    if not fm.get(req_key):
                        fail(rel, f"Missing required frontmatter key {req_key!r}")
                if len(body) < 200:
                    fail(rel, "SKILL.md instruction body is unexpectedly short")
            except ValueError as exc:
                fail(rel, str(exc))

            if sha256_bytes(s_file) != canonical_digest:
                fail(rel, "SHA-256 mismatch against canonical .opencode/skills copy")

    # 3. Validate SVG banner
    banner = ROOT / "assets/banner.svg"
    if not banner.exists():
        fail("assets/banner.svg", "Missing banner SVG")
    else:
        try:
            tree = ET.fromstring(banner.read_text(encoding="utf-8"))
            for elem in tree.iter():
                if elem.tag.endswith("text"):
                    txt = "".join(elem.itertext())
                    if ARABIC_RE.search(txt):
                        fail("assets/banner.svg", f"Arabic glyphs inside SVG <text> cause bidi fallback bugs: {txt!r}")
        except ET.ParseError as exc:
            fail("assets/banner.svg", f"Invalid SVG XML: {exc}")

    # 4. Validate required docs, relative links & neutrality
    for rel_doc in REQUIRED_DOCS:
        p = ROOT / rel_doc
        if not p.exists():
            fail(rel_doc, "Missing required documentation/template file")
            continue
        raw = p.read_text(encoding="utf-8")
        if len(raw.strip()) < 100:
            fail(rel_doc, "File content is unexpectedly short")

        for term in FORBIDDEN_TERMS:
            if term.lower() in raw.lower():
                fail(rel_doc, f"Contains non-neutral source attribution term: {term!r}")

        cleaned = strip_fenced_code(raw)
        for m in MD_LINK_RE.finditer(cleaned):
            target = m.group(1).strip().split()[0]
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            resolved = (p.parent / path_part).resolve()
            if not resolved.exists():
                fail(rel_doc, f"Broken relative link -> {target}")

    if errors:
        print(f"\nValidation FAILED with {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(
        f"Validation PASSED: {skill_md_count} SKILL.md files (instructions-only, SHA-256 synced), "
        f"{len(REQUIRED_DOCS)} bilingual docs & templates, valid SVG banner, and zero broken links."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
