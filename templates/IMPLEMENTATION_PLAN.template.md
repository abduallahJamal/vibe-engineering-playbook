# IMPLEMENTATION_PLAN.md — Phased Vertical-Slice Delivery Plan

> Every phase below must end with passing automated tests, full `git diff` review, and an atomic `git commit` checkpoint before advancing.

## Architecture Summary
- **Module Boundaries:** `[routing/controllers] -> [services/domain] -> [repositories/db-pool]`
- **Approved Dependencies (Pinned):** `[List exact packages & versions; justify each]`
- **Asset Strategy:** `[Self-hosted fonts/icons vs. pinned CDN with fallback]`

---

## Phase 1 — Repository Skeleton, Tooling & Environment
- **Files:** `pyproject.toml` / `package.json`, `.gitignore`, `.env.example`, linter & test config.
- **Verification:** Linter, type-checker, and smoke test run cleanly in CI.
- **Status:** `[ ] Pending`

## Phase 2 — Database Schema, Connection Pool & Migrations
- **Files:** `src/db/pool.*`, `migrations/*`, `tests/test_db_pool.*`
- **Verification:** Connection pool checkout/release, timeout, and exhaustion tests pass.
- **Status:** `[ ] Pending`

## Phase 3 — Authentication, RBAC & Rate Limiting
- **Files:** `src/auth/*`, `tests/test_auth_security.*`
- **Verification:** Login, logout, expired session, rate limit (`429`), and cross-user denial (`403`) pass.
- **Status:** `[ ] Pending`

## Phase 4 — Core Domain & Validated API Endpoints
- **Files:** `src/domain/*`, `src/api/*`, `tests/test_api_slices.*`
- **Verification:** Happy + unhappy schema validation tests pass; zero N+1 queries.
- **Status:** `[ ] Pending`

## Phase 5 — Responsive Frontend Integration & Network Audit
- **Files:** `src/ui/*`
- **Verification:** Desktop + mobile (`320px`/`768px`) verified; DevTools Network tab confirms consolidated requests and zero hidden layer (`z-index`) bugs.
- **Status:** `[ ] Pending`

## Phase 6 — Independent Critique, Test-Theater Audit & Launch Gate
- **Actions:** Run `vibe-critique` + `vibe-test-gate` + SAST scan + backup restore drill.
- **Verification:** All 16 items of Gate 3 (`docs/checklists.en.md`) signed off.
- **Status:** `[ ] Pending`
