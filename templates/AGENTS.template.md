# AGENTS.md — Project Engineering Constitution

> Copy this file to the root of your repository as `AGENTS.md` (and/or `CLAUDE.md`) and fill in the bracketed fields before issuing your first implementation prompt.

## 1. Project Overview & Lifecycle Class
- **Project Name:** `[PROJECT_NAME]`
- **Lifecycle Tier:** `[MVP / Production]` *(All production safety, testing, and diff gates apply)*
- **Core Purpose:** `[ONE-SENTENCE PROBLEM & TARGET USER]`

## 2. Approved Tech Stack
- **Frontend:** `[e.g., Next.js 15 / Vanilla HTML+CSS+JS / WPF XAML]`
- **Backend / API:** `[e.g., Python 3.12 + FastAPI / Django / .NET 8]`
- **Database & Pooling:** `[e.g., PostgreSQL 16 via bounded connection pool]`
- **Validation & Auth:** `[e.g., Pydantic / Zod + RBAC session/token auth]`

## 3. Mandatory Agent Operating Rules
1. **Plan Before Code:** Read `AGENTS.md`, `PRD.md`, and `IMPLEMENTATION_PLAN.md` at session start. Present your plan and wait for approval before editing code.
2. **Strict Task Scope:** Modify ONLY files required for the active approved task. Never refactor or touch unrelated modules.
3. **Code Quality Limits:**
   - Target **<= 30 lines** per function with clear, domain-specific naming.
   - Zero duplicated UI blocks or business rules; extract shared components/utilities.
   - Concise docstrings on public interfaces; **zero noisy AI-slop comments**.
4. **Supply-Chain Discipline:** Do NOT add any new package/CDN dependency without explicit approval and justification over ~20 lines of native code. Pin all versions.
5. **Security Red Lines:**
   - Enforce **server-side validation** on every input/endpoint.
   - Store all secrets strictly in `.env` (never hardcode keys, tokens, or credentials).
   - Never run destructive DB commands (`DROP`, `TRUNCATE`, unscoped `DELETE`) without manual confirmation.
6. **Testing & Bugfix Integrity:**
   - Every feature requires behavioral tests covering both happy and **unhappy/edge paths**.
   - Every bugfix requires a **Root-Cause Diagnosis** + a **Fail-Then-Pass (`Red -> Green`)** test.
   - Stop after **2 failed attempts** on the same bug and report diagnostics.

## 4. Verification Commands
```bash
# Lint & typecheck
[e.g., ruff check . && mypy .]

# Test suite
[e.g., pytest -v]
```
