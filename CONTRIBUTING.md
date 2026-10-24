# Contributing to `vibe-engineering-playbook`

Contributions that sharpen engineering checklists, prompt blueprints, or multi-agent skill instructions are welcome!

## Guidelines

1. **Edit Canonical Skills Only:** Update skills under `.opencode/skills/<name>/SKILL.md`, then run `./scripts/sync-platforms.sh` to propagate identical copies to `.claude/skills/` and `.agents/skills/`.
2. **Maintain Bilingual Parity:** Update both English (`*.en.md` / `README.md`) and Arabic (`*.ar.md` / `README.ar.md`) documents together.
3. **Keep It Pure Instructions:** Do not add heavy framework dependencies or application boilerplate — this repository is a lightweight, universal instructions & skills suite.
4. **Validate Before Submitting:**

```bash
bash -n install.sh scripts/*.sh
./scripts/sync-platforms.sh --check
python3 scripts/validate.py
```
