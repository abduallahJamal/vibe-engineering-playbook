---
name: vibe-spec-plan
description: System design and Plan Mode skill — converts PRD.md into an approved phased IMPLEMENTATION_PLAN.md with architectural boundaries, security controls, and dependency rules.
license: MIT
compatibility: opencode, claude-code, codex
metadata:
  category: architecture-planning
  version: "1.0.0"
---

# `vibe-spec-plan` — Architecture & Plan Mode Gate

## Purpose

Eliminate **Mega-Prompt Drift (B1)**, **Supply-Chain Bloat (D5)**, and **Infrastructure Blindness (F3)** by producing a human-approved `IMPLEMENTATION_PLAN.md` before implementation begins.

---

## Mandatory Planning Checklist

Read `PRD.md` and `AGENTS.md` / `CLAUDE.md`, then design the system across four pillars:

### 1. Architecture & State Boundaries
- Module decomposition (clear separation between routing/controllers, domain logic, data access, and UI).
- Rendering and state model (`SSR` / `SSG` / `CSR`), avoiding hidden client-side request storms (N+1 fetches per view).
- Database access strategy: mandatory **Connection Pooling**, thread/async safety, migrations, and zero raw `DROP`/`DELETE` paths exposed to automation.

### 2. Security & Input Controls
- Dual validation: client-side UX validation + **mandatory server-side schema validation**.
- Secret management: `.env` + `.gitignore` + `.env.example` (zero hardcoded keys or credentials).
- Auth/RBAC matrix: explicit role checks per endpoint; rate limiting on authentication and expensive routes.

### 3. Dependency & Asset Policy
- List every external dependency to be installed and **justify why native code (~20 lines) is insufficient**.
- Pin exact package versions; decide explicitly which fonts/icons/scripts are self-hosted vs. external CDN.

### 4. Vertical-Slice Task Breakdown (`IMPLEMENTATION_PLAN.md`)
Break execution into small, sequential checkpoints:
1. Project skeleton, linting/formatting, & environment configuration
2. Data schema, connection pool, & migrations
3. Core domain/API slice + server-side validation + unit tests
4. Authentication, authorization, & rate-limiting slice
5. UI integration (desktop + mobile responsive states + empty/error states)
6. Unhappy-path, security, & network-tab verification

---

## Gate Rule

Present `IMPLEMENTATION_PLAN.md` and **stop for explicit approval** before executing Task 1.
