<div align="center">

<img src="assets/banner.svg" alt="vibe-engineering-playbook — From Vibe Coding to Production Engineering" width="100%"/>

<br/>

**Bilingual operational playbook + 6 pure-instruction [Agent Skills](https://agentskills.io) (`/vibe`) for shipping production-grade software with AI coding agents — replacing blind "Accept" loops with specs-first governance, adversarial critique, and real verification gates.**

[![CI](https://github.com/abduallahJamal/vibe-engineering-playbook/actions/workflows/validate.yml/badge.svg?label=CI)](https://github.com/abduallahJamal/vibe-engineering-playbook/actions/workflows/validate.yml)
[![Skills](https://img.shields.io/badge/Skills-6%20%2B%20%2Fvibe-38BDF8)](#the-six-agent-skills)
[![Anti-Patterns](https://img.shields.io/badge/Anti--Patterns-33%20Rules-818CF8)](docs/anti-patterns.en.md)
[![Prompt Blueprints](https://img.shields.io/badge/Prompts-12%20Blueprints-A78BFA)](docs/prompt-blueprints.en.md)
[![OpenCode](https://img.shields.io/badge/OpenCode-ready-111827)](#installation)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-ready-D97757)](#installation)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-ready-10A37F)](#installation)
[![License: MIT](https://img.shields.io/badge/License-MIT-22C55E.svg)](LICENSE)
[![Arabic Docs](https://img.shields.io/badge/%D8%A7%D9%84%D8%AA%D9%88%D8%AB%D9%8A%D9%82-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9-1E293B)](README.ar.md)

**🇬🇧 English** · **[🇪🇬 العربية](README.ar.md)**

</div>

---

## 📌 Core Premise: Vibe Coding ≠ Vibe Engineering

**Vibe Coding** — prompting natural-language wishes while ignoring the underlying code — is an exceptional accelerator for **disposable prototypes (`PoC`)** and **single-user personal tools (`Software for One`)**. Applied directly to products with real users, sensitive data, and real traffic, it becomes a predictable source of **security breaches, AI slop, fake green tests, and compounding technical debt**.

The difference is not the model or IDE — **it is who sits in the driver's seat:**

| Dimension | Unconstrained Vibe Coder | Disciplined Vibe / Agentic Engineer |
| :--- | :--- | :--- |
| **Who drives?** | Model drives; human relays wishes & stack traces | **Engineer drives**; agent executes bounded specs |
| **Starting point** | Immediate mega-prompt | Written specs (`AGENTS.md` + `PRD.md` + `Plan`) first |
| **When an error occurs** | Pastes raw error: *"Fix this"* | Diagnoses root cause; enforces `Fail-Then-Pass` scoped fix |
| **Code review** | Clicks UI once; hits *"Accept All"* | Reviews 100% of `git diff` & logic against `PRD.md` |
| **Testing posture** | Happy path on `localhost` + green-check theater | Unhappy paths, `1,000+` req load, SAST & mutation checks |
| **Security verification** | Asks the author model *"Is this secure?"* | Independent adversarial audit (`reviewer ≠ author`) |
| **Definition of done** | *"The button works right now"* | **Secure · Performant · Maintainable** for the next engineer |

---

## 📊 Why Governance Matters (Documented Industry Benchmarks)

| Metric | Operational Reality |
| :--- | :--- |
| **`45%`** | Share of AI-generated code snippets containing security flaws in benchmark studies (Veracode 2025). |
| **`3×`** | Higher security vulnerability density observed in unreviewed generated code vs. human-authored baselines. |
| **`1.7×`** | Increase in major structural defects across repositories dominated by unreviewed agent commits. |
| **`19%` slower** | Net slowdown measured when developers get trapped in `prompt → review → re-prompt → manual patch` loops. |
| **`80 / 20` cliff** | Prompting reaches an `80%` demo rapidly; the final `20%` (auth, pooling, edge cases, ops) breaks production. |

---

## 📚 Bilingual Playbook Handbooks (`docs/`)

Every handbook is pure, actionable engineering guidance — available side-by-side in **English** and **Arabic (`RTL`)**:

| Handbook | What It Covers | English | العربية |
| :--- | :--- | :---: | :---: |
| **1. 33 Anti-Patterns Catalog** | All **33 failure patterns** organized into **7 families** (Mindset, Prompting, Code Quality & AI Slop, Security & Supply Chain, Context & Hallucinations, Testing Theater, Viability & Teams) — each with concrete mitigation rules. | **[Read EN →](docs/anti-patterns.en.md)** | **[اقرأ بالعربية ←](docs/anti-patterns.ar.md)** |
| **2. 7-Stage Delivery Workflow** | Step-by-step lifecycle from **Discovery (`Grilling`)** and **Specs Before Prompts** through **Plan Mode**, **Chained Increments**, **Adversarial Review**, and **Production Handoff** + **30-Day Transition Plan**. | **[Read EN →](docs/workflow-7-stages.en.md)** | **[اقرأ بالعربية ←](docs/workflow-7-stages.ar.md)** |
| **3. 12 Prompt Blueprints** | Copy-paste **Weak vs. Strong** engineering prompts: Auth, DB Connection Pools, Scoped Frontend, Session Bootstrap, `file:line` Diff Audit, Root-Cause Bugfix, Grilling, Anti-Slop Refactor, Anti-Sycophancy Critique & Fake-Test Audit. | **[Read EN →](docs/prompt-blueprints.en.md)** | **[اقرأ بالعربية ←](docs/prompt-blueprints.ar.md)** |
| **4. 3 Gate Checklists & Glossary** | Hard stop-gates: **Pre-Project (8 checks)**, **Per-Task Diff Acceptance (12 checks)**, and **Pre-Launch Production Gate (16 checks)** + operational glossary. | **[Read EN →](docs/checklists.en.md)** | **[اقرأ بالعربية ←](docs/checklists.ar.md)** |

---

## 🗂️ Drop-In Project Templates (`templates/`)

Copy these templates straight into the root of any new or existing repository before prompting your agent:

- **[`templates/AGENTS.template.md`](templates/AGENTS.template.md)** — Universal `AGENTS.md` / `CLAUDE.md` engineering constitution (English).
- **[`templates/AGENTS.template.ar.md`](templates/AGENTS.template.ar.md)** — النسخة العربية من دستور المشروع `AGENTS.md` / `CLAUDE.md`.
- **[`templates/PRD.template.md`](templates/PRD.template.md)** — Product Requirements Document + mandatory 15-row Edge & Unhappy-Path Matrix.
- **[`templates/IMPLEMENTATION_PLAN.template.md`](templates/IMPLEMENTATION_PLAN.template.md)** — 6-phase vertical-slice implementation plan with checkpoint gates.

---

## 🧩 The Six Agent Skills + `/vibe` Command

In addition to human-readable handbooks, this repository packages **6 zero-code instruction skills** that enforce the playbook directly inside **OpenCode**, **Claude Code**, and **Codex CLI**:

| Skill | Role in the 7-Stage Pipeline |
| :--- | :--- |
| **`vibe` (`/vibe`)** | **Master Orchestrator** — classifies `PoC` vs. `Production`, enforces specs-before-prompts, and routes across all stages. |
| **`vibe-grill`** | **Stage 1 Discovery** — interviews you **one question at a time** with recommendations, then writes `AGENTS.md` & `PRD.md`. |
| **`vibe-spec-plan`** | **Stages 2–4 Planning** — designs pooling, validation, RBAC, and pinned dependencies into an approved `IMPLEMENTATION_PLAN.md`. |
| **`vibe-scoped-build`** | **Stage 5 Execution** — enforces single-slice diffs, `≤ 30`-line clean functions, root-cause bugfixes, and Two-Strike stops. |
| **`vibe-critique`** | **Stage 6A Adversarial Review** — disables model sycophancy; surfaces top 3 risks with `0–100` confidence & `file:line` proof. |
| **`vibe-test-gate`** | **Stages 6B–7 Verification** — catches fake green tests (`Test Theater`), enforces `Fail-Then-Pass`, and runs the 16-point Launch Gate. |

---

## 🔌 One Standard, Three Agents (`install.sh`)

| Agent | Project Path | Global Path | Invocation |
| :--- | :--- | :--- | :--- |
| **OpenCode** | `.opencode/skills/` + `.opencode/commands/` | `~/.config/opencode/` | `/vibe` or skill `vibe-critique` |
| **Claude Code** | `.claude/skills/` | `~/.claude/skills/` | `/vibe`, `/vibe-grill`, `/vibe-test-gate`… |
| **Codex CLI** | `.agents/skills/` | `~/.agents/skills/` | `$vibe` or `/skills` |

### Installation

```bash
git clone https://github.com/abduallahJamal/vibe-engineering-playbook.git
cd vibe-engineering-playbook

# Install globally for OpenCode + Claude Code + Codex CLI
./install.sh --all --global

# Or install into a specific project workspace
./install.sh --all --project /path/to/your-project
```

### Usage Example

```text
/vibe
I want to build a multi-tenant invoice portal. Start with Stage 1 (vibe-grill) —
interview me one question at a time and generate AGENTS.md + PRD.md before any code.
```

---

## 📁 Repository Structure

```text
vibe-engineering-playbook/
├── .opencode/
│   ├── commands/vibe.md                 # /vibe master slash command
│   └── skills/                          # Canonical source of truth (6 pure-instruction skills)
│       ├── vibe/SKILL.md
│       ├── vibe-grill/SKILL.md
│       ├── vibe-spec-plan/SKILL.md
│       ├── vibe-scoped-build/SKILL.md
│       ├── vibe-critique/SKILL.md
│       └── vibe-test-gate/SKILL.md
├── .claude/skills/                      # Synced Claude Code skills
├── .agents/skills/                      # Synced Codex CLI / Cursor skills
├── docs/                                # Bilingual engineering handbooks (EN + AR)
│   ├── anti-patterns.{en,ar}.md         # 33 anti-patterns across 7 risk families
│   ├── workflow-7-stages.{en,ar}.md     # 7-stage lifecycle + 30-day transition plan
│   ├── prompt-blueprints.{en,ar}.md     # 12 weak-vs-strong prompt blueprints
│   └── checklists.{en,ar}.md            # 3 gate checklists + glossary
├── templates/                           # Drop-in project templates
│   ├── AGENTS.template.{md,ar.md}
│   ├── PRD.template.md
│   └── IMPLEMENTATION_PLAN.template.md
├── scripts/
│   ├── sync-platforms.sh                # SHA-256 multi-agent sync script
│   ├── validate.py                      # CI validator (frontmatter, sync, links, SVG)
│   └── publish.sh                       # Validation + release helper
├── assets/banner.svg                    # Repository header banner
├── install.sh                           # Multi-agent installer
├── README.md                            # English overview (this file)
├── README.ar.md                         # التوثيق الكامل بالعربية
└── LICENSE                              # MIT License
```

---

## 🤝 Contributing & Validation

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Before opening a pull request, run:

```bash
./scripts/sync-platforms.sh --check
python3 scripts/validate.py
```

---

## 📄 License

Released under the [MIT License](LICENSE) © 2026 Abduallah Jamal.
