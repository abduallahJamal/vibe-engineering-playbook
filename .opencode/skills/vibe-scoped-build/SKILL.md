---
name: vibe-scoped-build
description: Disciplined incremental implementation skill — enforces single-task diffs, clean 30-line functions, root-cause bugfixes, zero AI slop, and Git checkpoint hygiene.
license: MIT
compatibility: opencode, claude-code, codex
metadata:
  category: incremental-execution
  version: "1.0.0"
---

# `vibe-scoped-build` — Scoped Incremental Execution & Anti-Slop Build

## Purpose

Prevent **Blind-Accept Regressions (A1, E1)**, **AI Slop (C1, C2)**, and **Truncation Patching (C4)** during active coding tasks.

---

## Execution Rules (Every Task)

1. **Strict File & Feature Scope:**
   - Implement **only** the current approved task from `IMPLEMENTATION_PLAN.md`.
   - Do **not** touch unrelated files, reformat untouched modules, or sneak in unrequested features.
   - Respect negative constraints (e.g., if asked for client-side validation only, do not invent backend endpoints).

2. **Code Quality & Maintainability ("Build for the Next Engineer"):**
   - Keep functions focused (target **≤ 30 lines** per function) with descriptive, domain-accurate identifiers.
   - Extract shared UI layouts/components instead of duplicating markup across pages.
   - Add concise docstrings for public interfaces; **ban noisy AI-slop comments** that restate obvious syntax.
   - Run the project linter/formatter and type-checker before presenting work.

3. **Network & UI Layer Sanity:**
   - Consolidate data fetching (bulk endpoints over 5 sequential client requests for one screen).
   - Verify CSS layering (`z-index`, `overflow`, `visibility`, mobile breakpoints) rather than stacking `!important` hacks.

4. **Root-Cause Bug Fixing Protocol (Anti-Doom-Loop):**
   - When given an error, **diagnose and explain the root cause first** — never stack wrapper/fallback patches (`Truncation Patching`) around broken logic.
   - Write or identify a **failing test first** (`Fail-Then-Pass`), fix only the responsible module, and verify the full test suite still passes.
   - **Two-Strike Rule:** If two fix attempts on the same bug fail, **stop immediately**, summarize what failed, and propose an alternative diagnostic path instead of looping blindly.

5. **Checkpoint Handoff:**
   - End every completed task with:
     - Files modified & why (`file:line`),
     - Dependencies added (`none` by default),
     - Test & linter command outputs,
     - A suggested atomic `git commit` message so the human engineer can checkpoint cleanly.
