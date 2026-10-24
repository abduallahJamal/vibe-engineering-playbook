# AGENTS.md — Repository Maintainer Instructions

`vibe-engineering-playbook` is an **instructions-only** repository providing bilingual (English + Arabic RTL) engineering handbooks, drop-in project templates, and 6 pure-instruction Agent Skills.

## Source-of-Truth Rules

1. **Canonical Skills Directory:** `.opencode/skills/` is the single source of truth for all 6 skills (`vibe`, `vibe-grill`, `vibe-spec-plan`, `vibe-scoped-build`, `vibe-critique`, `vibe-test-gate`). Never edit `.claude/skills/` or `.agents/skills/` manually — regenerate them via `./scripts/sync-platforms.sh`.
2. **Instructions Only:** Keep skills and handbooks free of runtime application bloat; every skill must remain a clear, self-contained `SKILL.md` with valid YAML frontmatter (`name`, `description`, `license`, `compatibility`, `metadata`).
3. **Bilingual Parity:** Any rule, blueprint, or checklist updated in an `.en.md` handbook must be updated identically in its paired `.ar.md` handbook (using `<div align="right" dir="rtl">` for GitHub RTL rendering).
4. **Neutral Professional Tone:** Keep all documentation formal, neutral, and vendor/channel-agnostic — zero colloquial transcript chatter or external channel names.
5. **Pre-Commit Verification:** Always run `./scripts/sync-platforms.sh --check` and `python3 scripts/validate.py` before committing.
