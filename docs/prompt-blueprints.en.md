# 12 Weak-vs-Strong Prompt Blueprints

**[🇪🇬 النسخة العربية](prompt-blueprints.ar.md)** · **[⬅ Back to Playbook](../README.md)**

Every blueprint contrasts an **unconstrained Vibe-Coder prompt** against a **production-grade Vibe-Engineer specification** with explicit stack rules, security invariants, negative constraints, and verification gates.

---

## `P01` — Secure Authentication & Rate-Limited Login

**❌ Weak Prompt:**
```text
Build me a login page.
```

**✅ Strong Engineering Prompt:**
```text
Act as a Senior Application Security & Full-Stack Engineer.
Implement the login flow using [Next.js + NextAuth / Django Auth] strictly within these constraints:
1. Enforce brute-force rate limiting on login attempts (IP + account lockout backoff).
2. Validate all inputs on BOTH client and server using [Zod / Pydantic] schemas.
3. Follow the existing design tokens in `styles/design-system.ts` (desktop + mobile breakpoints).
4. Load all secrets/keys strictly from environment variables (`.env`) — zero hardcoded values.
5. Do NOT touch any files outside `src/auth/` and its corresponding test file.
Before writing code, list the files you will touch and the failure cases you will test.
```

---

## `P02` — Pooled, Scalable, Thread-Safe Database Layer

**❌ Weak Prompt:**
```text
Frontend is JS and backend is Python. Connect the backend to MySQL.
```

**✅ Strong Engineering Prompt:**
```text
Implement the MySQL database access module in `src/db/pool.py` meeting these production requirements:
1. Use a bounded Connection Pool — never open a raw connection per HTTP request.
2. Read encrypted/TLS connection credentials strictly from environment variables; fail fast on missing vars.
3. Design for thread/async safety under 1,000 concurrent requests/sec with explicit connection/query timeouts.
4. Expose parameterized query helpers only (strict SQL-injection prevention).
5. Write automated tests covering: successful checkout/release, connection failure, query timeout, and pool exhaustion.
Present the pool configuration parameters and edge cases for approval before writing code.
```

---

## `P03` — Scoped Frontend Validation (With Negative Constraints)

**❌ Weak Prompt:**
```text
Add validation to the contact form at the bottom.
```

**✅ Strong Engineering Prompt:**
```text
Add client-side validation ONLY to the existing contact form in `src/components/contact-form.js` using pure vanilla JavaScript:
- Validate three fields: `full_name` (non-empty, >= 2 chars), `email` (RFC-compliant format), and `message` (10–2000 chars).
- Render accessible inline error messages (`aria-live="polite"`) directly beneath each invalid field.
- STRICT NON-GOALS: Do NOT create backend endpoints, do NOT install external validation libraries, and do NOT modify page layout CSS outside error-message classes.
```

---

## `P04` — Responsive Mobile Navigation Specification

**❌ Weak Prompt:**
```text
Make the navbar work on mobile.
```

**✅ Strong Engineering Prompt:**
```text
Implement a responsive mobile navigation menu for `src/components/header.*`:
- Breakpoint: collapse desktop links into an accessible hamburger toggle (`aria-expanded`, `aria-controls`, Escape-key close) below `768px`.
- Prevent background body scroll while open and ensure tap targets are >= 44x44px.
- Verify zero horizontal overflow (`scrollWidth <= clientWidth`) at `320px`, `375px`, `768px`, and `1280px`.
- Do NOT introduce external JS/CSS UI frameworks.
```

---

## `P05` — Zero-Dependency Interactive Component (Supply-Chain Guard)

**❌ Weak Prompt:**
```text
Add an FAQ accordion section.
```

**✅ Strong Engineering Prompt:**
```text
Implement the FAQ accordion component in `src/components/faq.*` using semantic HTML, CSS transitions, and vanilla JavaScript ONLY:
- Zero third-party npm/CDN libraries allowed.
- Required behavior: opening one accordion item automatically closes all other open items; keyboard accessible (`Enter` / `Space` / `Tab`).
- Keep each JS function <= 25 lines with clear naming.
```

---

## `P06` — Existing-Repository Session Bootstrap

**✅ Copy-Paste Session Starter:**
```text
Before proposing or editing anything, read `AGENTS.md` (or `CLAUDE.md`), `PRD.md`, and `IMPLEMENTATION_PLAN.md` in full.
Then:
1. Summarize your understanding of the system architecture, security invariants, and coding rules in 5 bullet points so I can correct any misunderstanding first.
2. Do NOT write or modify code until you present your execution plan for Task `[TASK_ID]` and receive my explicit approval.
3. Scope hard-limit: work strictly on `[TASK_ID]` — touch zero unrelated files.
```

---

## `P07` — Evidence-Based Spec & Security Diff Review

**❌ Weak Prompt:**
```text
Review the code you wrote and make sure there are no bugs or security issues.
```

**✅ Strong Engineering Prompt:**
```text
Audit the current `git diff` against `PRD.md` Section `[X]`. Answer ONLY the five questions below, citing exact `file:line` evidence for every answer (no generic reassurance):
1. Which PRD requirements are fully implemented, and which are partial, mocked, or missing?
2. Which endpoints or handlers accept external input without server-side schema validation?
3. Are any secrets, tokens, URLs, or credentials hardcoded or logged anywhere?
4. Were any new dependencies or external CDN links added? Justify each or flag for removal.
5. Which existing modules/tests could regress due to these changes, and what test proves they did not?
```

---

## `P08` — Root-Cause Scoped Bugfix (Anti-Regression Guard)

**❌ Weak Prompt:**
```text
[Paste raw error traceback] — fix this!
```

**✅ Strong Engineering Prompt:**
```text
Here is the observed failure:
[PASTE ERROR + REPRODUCTION STEPS]

Follow this strict sequence:
1. Diagnose and explain the ROOT CAUSE (data flow / state / CSS layer / query) — do NOT stack a workaround or try/catch suppressor.
2. Write or identify a test that FAILS right now because of this bug.
3. Fix the root cause strictly inside `[TARGET_FILE]` without adding new dependencies, deleting unrelated functions, or touching other modules.
4. Run the full test suite and report exact output. If two attempts fail, STOP immediately and report findings.
```

---

## `P09` — Pre-Code Socratic Discovery (`Grilling`)

**✅ Copy-Paste Discovery Prompt:**
```text
I have a product idea: `[DESCRIBE IDEA IN 2-3 SENTENCES]`.
Do NOT write any code. Interview me systematically — asking ONE focused question at a time — until every engineering decision is clear across:
1) Lifecycle class (PoC vs. Production), 2) Core user workflow, 3) Data sensitivity,
4) Auth & permissions, 5) Concurrency/scale target, 6) Stack & hosting, 7) Explicit non-goals, and 8) Edge/unhappy cases.
At the end of EVERY question, give your recommended engineering choice and why.
Once all questions are answered, generate `AGENTS.md` and `PRD.md` capturing every decision.
```

---

## `P10` — Behavior-Preserving Anti-Slop Refactor

**✅ Copy-Paste Refactor Prompt:**
```text
Refactor `[TARGET_FILE_OR_MODULE]` with ZERO change to external behavior or public signatures:
1. Split any function exceeding 30 lines into cohesive, single-responsibility helpers.
2. Rename vague identifiers (`data`, `res2`, `temp`, `handleStuff`) to domain-accurate names.
3. Delete dead code, duplicated blocks, and redundant AI-slop comments that restate syntax.
4. Add concise docstrings to public functions/classes only.
First list your planned structural edits for approval; after editing, run the full test suite and linter to prove 100% behavioral parity.
```

---

## `P11` — Anti-Sycophancy Adversarial Critique Mode

**✅ Copy-Paste Critique Prompt:**
```text
Disable polite agreement — I know your default bias is to validate my assumptions.
Evaluate `[PLAN / ARCHITECTURE / PR DIFF]` as an external Principal Engineer & Security Auditor hired to find flaws:
1. Identify the 3 worst architectural or security decisions here and explain why each is dangerous.
2. For every technical claim in this design, assign a confidence score (0-100) and state whether it is grounded in official docs/code or unverified inference.
3. Describe the exact production conditions (load, malicious input, 2 AM partial outage) under which this system will break first.
4. If you had to issue a hard REJECT on this work today, state the exact blocking reason.
Zero flattery, filler, or reassuring language allowed.
```

---

## `P12` — Test-Theater Audit & Fail-Then-Pass Enforcement

**✅ Copy-Paste Test Audit Prompt:**
```text
Audit every test added or modified in this branch and output a Markdown table with 4 columns:
1. Test Name & `file:line`
2. Observable External Behavior Proven (in plain human language — not function names)
3. Sabotage Check: Would this test STILL PASS if I commented out or broke the core logic of the function under test? Be brutally honest — flag any "Yes" as FAKE TEST.
4. Edge/Unhappy Path Covered (or "Happy-path only")

Then propose one concrete Failing Test (`Red`) that reproduces Bug/Edge-Case `[X]`. Do NOT touch implementation code until I see that test fail first.
```
