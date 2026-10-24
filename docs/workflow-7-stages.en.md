# The 7-Stage Vibe Engineering Delivery Workflow

**[🇪🇬 النسخة العربية](workflow-7-stages.ar.md)** · **[⬅ Back to Playbook](../README.md)**

Moving from ad-hoc Vibe Coding to disciplined **Vibe / Agentic Engineering** means enforcing seven sequential stages — with explicit artifacts and pass criteria at every boundary.

---

## Stage Overview

```text
1. Discovery (Grilling)
        │
        ▼
2. Specs & System Design  ──►  AGENTS.md + PRD.md + Edge-Case Matrix
        │
        ▼
3. Environment & Least-Privilege Setup  ──►  Git + .env + Linter + Sandbox
        │
        ▼
4. Plan Mode & Sign-Off  ──►  IMPLEMENTATION_PLAN.md (Human Approved)
        │
        ▼
5. Incremental Scoped Build  ──►  Chained Slices + Diff Review + Atomic Commits
        │
        ▼
6. Adversarial Review & Unhappy-Path QA  ──►  Security · Performance · Maintainability
        │
        ▼
7. Production Gate & Next-Engineer Handoff  ──►  Backups + Monitoring + Runbooks
```

---

## Stage 1 — Discovery & Socratic Requirements (`Grilling`)

- **Objective:** Eliminate hidden assumptions before a single file is created.
- **Actions:**
  1. Instruct the agent **not** to write code and to interview you **one question at a time** (with a reasoned recommendation after each question).
  2. Define the lifecycle class (`PoC`, `Software for One`, or `MVP` / `Production`).
  3. Clarify target users, core workflow, sensitive data classes, roles/permissions, expected concurrency, and explicit v1 non-goals.
- **Exit Criterion:** Every product and scope ambiguity is resolved in writing.

---

## Stage 2 — System Design & Written Specifications (`Specs Before Prompts`)

- **Objective:** Establish repository-resident source-of-truth files so context never evaporates across sessions.
- **Artifacts Created:**
  - `AGENTS.md` / `CLAUDE.md` — Stack rules, coding conventions, max function length (`≤ 30` lines), dependency policy, and security red lines.
  - `PRD.md` — User stories, data model overview, API contracts, and at least **15 explicit edge/unhappy-path scenarios**.
- **Exit Criterion:** An engineer (or fresh agent session) can read `AGENTS.md` + `PRD.md` and understand the exact system boundaries without prior chat history.

---

## Stage 3 — Isolated Setup & Tooling Selection

- **Objective:** Choose the right control tier and enforce safety rails before generation starts.
- **Tooling Control Tiers:**

| Tool Tier | Typical Examples | Control Level | Appropriate Scope |
| :--- | :--- | :--- | :--- |
| **All-in-One Browser Builders** | Prompt-to-app web sandboxes | Partial / opaque | Rapid `PoC` validation & disposable demos |
| **AI-Native Code Editors** | IDE copilots & inline diff editors | High (file-level) | Daily feature engineering & refactoring |
| **CLI / Workspace Coding Agents** | `OpenCode`, `Claude Code`, `Codex CLI` | **Maximum ("Manual Transmission")** | Full-lifecycle `MVP` & `Production` engineering |

- **Setup Actions:**
  1. Initialize clean `git` repository + `.gitignore` + `.env.example`.
  2. Configure formatter, linter, type-checker, and test runner from Commit 0.
  3. Isolate agent permissions from personal host files and live production databases.
- **Exit Criterion:** Clean initial commit with working lint/test harness and zero secrets in tracked files.

---

## Stage 4 — Explicit Plan Mode (`IMPLEMENTATION_PLAN.md`)

- **Objective:** Review and approve architecture and task sequencing **before** code generation.
- **Actions:**
  1. Have the agent read `AGENTS.md` + `PRD.md` and output a phased vertical-slice `IMPLEMENTATION_PLAN.md`.
  2. Verify connection pooling, server-side validation, RBAC checks, pinned dependencies, and mobile/responsive states are explicitly scheduled.
  3. Challenge weak or over-engineered choices before approving.
- **Exit Criterion:** Human-signed-off `IMPLEMENTATION_PLAN.md` committed to the repository.

---

## Stage 5 — Incremental Chained Execution & Checkpoints

- **Objective:** Build the `MVP` one verifiable vertical slice at a time without regressions or AI slop.
- **Actions:**
  1. Prompt **one task at a time**: `Schema → Backend API & Validation → Domain Logic → UI → Tests`.
  2. Read 100% of `git diff` before accepting; verify zero out-of-scope file edits and zero unapproved dependencies.
  3. Inspect browser DevTools Network tab (request count) and DOM layers (`z-index`/responsive breakpoints) on UI tasks.
  4. Commit an atomic `git` checkpoint after every green slice; start fresh chat sessions between major modules.
- **Exit Criterion:** Every `MVP` slice works end-to-end on clean, small commits.

---

## Stage 6 — Independent Critique & Unhappy-Path Verification

- **Objective:** Prove **Security · Performance · Maintainability** independently of the author session.
- **Actions:**
  1. Run **Adversarial Critique Mode** (`vibe-critique`) in a separate session/model against `PRD.md`.
  2. Audit all tests for **Green-Check Test Theater** (`vibe-test-gate`); enforce `Fail-Then-Pass` tests on every bugfix.
  3. Execute unhappy-path tests (malformed payloads, expired auth, unauthorized role access, network timeouts, prompt injection, 1,000+ concurrent requests).
  4. Run SAST and dependency vulnerability scanners.
- **Exit Criterion:** Every `PRD.md` requirement has a genuine, non-tautological passing test and zero unresolved high/critical findings.

---

## Stage 7 — Production Release & Building for the Next Engineer

- **Objective:** Ensure the system survives real-world traffic, 2 AM incidents, and future engineer handoffs.
- **Actions:**
  1. Complete all 16 items of the [Pre-Production Launch Gate](checklists.en.md#gate-3--pre-production-launch--security-gate).
  2. Verify automated backups + **actual restore drill**, monitoring/alerting, and incident response runbooks.
  3. Document setup, architecture decisions, and deployment steps clearly.
- **Exit Criterion:** Another engineer can clone the repository and understand, run, and safely modify the system within **one hour** without asking you.

---

## Core Technical Vocabulary Every Vibe Engineer Must Command

> *If you do not own the concept's name, you cannot prompt for it or verify its absence.*

| Pillar | Essential Concepts |
| :--- | :--- |
| **Structure** | Frontend vs. Backend · REST / GraphQL APIs · Relational/Document Schemas · Search Indexing · Modular Monolith vs. Microservices |
| **Behavior** | Routing · Authentication vs. Authorization (RBAC/RLS) · Rendering (`CSR` / `SSR` / `SSG`) · State Management · Connection Pooling · Concurrency / Thread-Safety |
| **Quality** | Clean Code · Design Patterns · Separation of Concerns · Technical Debt · Edge Cases · Happy vs. Unhappy Paths · Adversarial Code Review · Mutation/Behavioral Testing |
| **Operations** | Git Branching & Checkpoints · Containers / Docker · Serverless vs. Stateful Hosting · SAST & Secret Scanning · Observability / Monitoring · Backup & Restore Drills |

---

## 30-Day Transition Roadmap (Vibe Coder → Vibe Engineer)

| Week | Focus | Concrete Deliverable |
| :--- | :--- | :--- |
| **Week 1** | **Web & Systems Foundations** | Trace and explain end-to-end request flow (`Routing → Auth → Validation → DB Pool → Render`) without AI assistance. |
| **Week 2** | **Specs Before Prompts** | Take one real micro-product idea through Stage 1 (`Grilling`) and Stage 2 (`AGENTS.md` + `PRD.md` + 15+ edge cases). |
| **Week 3** | **Disciplined Chained Build** | Execute Stages 3–5 using Plan Mode, chained single-task prompts, full `git diff` review, and clean atomic commits. |
| **Week 4** | **Adversarial Audit & Launch** | Execute Stages 6–7: unhappy-path tests, SAST scan, network/load check, 16-point Production Gate, and live deployment + post-audit log. |
