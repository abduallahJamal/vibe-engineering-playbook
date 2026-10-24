# Changelog

All notable changes to **`vibe-engineering-playbook`** are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-10-24

### Added
- Bilingual English + Arabic (`RTL`) Vibe Engineering Playbook covering:
  - **33 Anti-Patterns Catalog** across 7 risk families (`docs/anti-patterns.{en,ar}.md`).
  - **7-Stage Production Delivery Workflow** + **30-Day Transition Plan** + **Technical Vocabulary Matrix** (`docs/workflow-7-stages.{en,ar}.md`).
  - **12 Weak-vs-Strong Prompt Blueprints** (`docs/prompt-blueprints.{en,ar}.md`).
  - **3 Mandatory Engineering Gate Checklists** (Pre-Start, Per-Task, 16-Point Production Launch) + **Glossary** (`docs/checklists.{en,ar}.md`).
- Drop-in project templates (`templates/AGENTS.template.md`, `templates/AGENTS.template.ar.md`, `templates/PRD.template.md`, `templates/IMPLEMENTATION_PLAN.template.md`).
- Six pure-instruction Agent Skills (`vibe`, `vibe-grill`, `vibe-spec-plan`, `vibe-scoped-build`, `vibe-critique`, `vibe-test-gate`) + `/vibe` command synced across **OpenCode**, **Claude Code**, and **Codex CLI**.
- Multi-agent installer (`install.sh`), SHA-256 platform sync script (`scripts/sync-platforms.sh`), and Python CI validator (`scripts/validate.py` + `.github/workflows/validate.yml`).
