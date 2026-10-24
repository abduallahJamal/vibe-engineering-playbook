# The 3 Mandatory Engineering Gate Checklists & Glossary

**[🇪🇬 النسخة العربية](checklists.ar.md)** · **[⬅ Back to Playbook](../README.md)**

Use these three checklists as hard stop-gates before starting a project, before accepting any task diff, and before releasing to real users.

---

## Gate 1 — Before You Start (Pre-Project Readiness)

- [ ] **1. One-Page Clarity:** Can I explain the core user problem and workflow on a single page without hand-waving?
- [ ] **2. Lifecycle Classification:** Have I explicitly classified this repository as a disposable `PoC` / `Software for One` vs. a real-user `MVP` / `Production` system?
- [ ] **3. Specs Committed First:** Have `AGENTS.md` (or `CLAUDE.md`) and `PRD.md` been written **before** issuing the first coding prompt?
- [ ] **4. Manual Edge-Case Pass:** Have I personally listed at least 15 failure/edge scenarios rather than outsourcing architectural thinking completely?
- [ ] **5. Core Vocabulary Readiness:** Do I understand the routing, auth, database pooling, rendering (`CSR`/`SSR`/`SSG`), and deployment model I am asking for?
- [ ] **6. Control-First Tooling:** Have I selected a workspace/CLI agent or IDE editor with full diff visibility rather than an opaque one-click black box?
- [ ] **7. Token & Cloud Budget:** Have I set a clear monthly API/subscription ceiling and model-tier strategy?
- [ ] **8. Clean Git Baseline:** Is `git` initialized with `.gitignore`, `.env.example`, formatter, linter, and test runner before any generated code lands?

---

## Gate 2 — During Build (Per-Task Diff Acceptance)

- [ ] **1. Bounded Specification:** Did the prompt define stack, scope, acceptance criteria, **and explicit negative constraints** (what *not* to touch)?
- [ ] **2. Single Slice Only:** Is this task a single vertical slice or architectural layer (not a monolithic mega-prompt)?
- [ ] **3. Full Diff Read:** Have I read **every line** of `git diff` prior to accepting?
- [ ] **4. 100% Comprehension:** Can I explain what every accepted line does — and did I require explanations for unfamiliar lines?
- [ ] **5. Supply-Chain Check:** Were zero unnecessary third-party libraries added for trivial tasks (~20 lines of native code)?
- [ ] **6. Secret Hygiene:** Are zero API keys, tokens, credentials, or internal URLs hardcoded in source or committed files?
- [ ] **7. Dual Validation:** Are all inputs validated on both client (UX) and **server (security)**?
- [ ] **8. Atomic Checkpoint:** Did I create a clean `git commit` checkpoint immediately after verifying this unit?
- [ ] **9. Zero Regressions:** Was the full existing test suite executed and confirmed green?
- [ ] **10. Zero AI Slop:** Are functions concise (`≤ 30` lines), well-named, free of duplicated markup, and free of noisy comments?
- [ ] **11. Anti-Test-Theater Check:** Did I read each new test's assertions to confirm it fails when production logic breaks?
- [ ] **12. Runtime Evidence:** Did I verify logs, database state, and browser DevTools Network/DOM layers instead of trusting `"Done"` claims?

---

## Gate 3 — Before Launch (16-Point Production & Security Gate)

- [ ] **1. Static & Dependency Security:** SAST scan and dependency CVE audit executed with zero unresolved critical/high issues.
- [ ] **2. End-to-End Auth & RBAC:** Signup, login, password reset, session expiration, rate limiting, and cross-tenant/role denial verified.
- [ ] **3. Unhappy-Path Suite:** Malformed inputs, missing permissions, network timeouts, and duplicate submissions tested.
- [ ] **4. Concurrency & Load Test:** Verified under `1,000–2,000` concurrent requests with database **Connection Pooling** active.
- [ ] **5. Prompt-Injection Defense:** Any LLM/chat or free-text surface tested against instruction-override and data-exfiltration payloads.
- [ ] **6. Cross-Device & Browser Matrix:** Tested on real mobile viewports, Safari, Firefox, and Chrome (not `localhost` desktop alone).
- [ ] **7. Backups & Destructive Guards:** Automated backups scheduled, **restore drill verified**, and `DROP`/`DELETE` operations gated by manual confirmation.
- [ ] **8. Observability & 2 AM Runbook:** Error tracking, latency/auth alerts, and an incident response checklist documented.
- [ ] **9. Zero Placeholders:** All `Lorem ipsum`, mock arrays, dummy images, and dead links replaced and verified.
- [ ] **10. Pinned Supply Chain & Assets:** Package lockfiles pinned; critical fonts/icons self-hosted or backed by fallbacks.
- [ ] **11. Network Efficiency Audit:** Browser Network tab checked on every key screen — zero N+1 or 5× redundant client requests.
- [ ] **12. Independent Security Review:** Final review conducted by a human engineer or independent model (never the authoring session or an online badge widget).
- [ ] **13. Clean-Room Access Policies:** Every IAM/RBAC/RLS rule written from scratch with least privilege — never copy-pasted across prompts/tools.
- [ ] **14. Legal, Privacy & Accessibility:** Privacy policy, terms, keyboard/screen-reader accessibility, and UI design originality verified.
- [ ] **15. Next-Engineer Onboarding:** `README`, architecture decisions, and local/prod run instructions clear enough for a new engineer to onboard in `< 1 hour`.
- [ ] **16. Blast-Radius Sign-Off:** Explicit human owner accountable if user data or uptime fails in production.

---

## Glossary of Agentic Engineering Terms

| Term | Operational Definition |
| :--- | :--- |
| **Vibe Coding** | Prompting natural-language wishes while ignoring the underlying code. Ideal for disposable `PoC`s and personal utilities; unsafe for real-user production. |
| **Vibe / Agentic Engineering** | Driving coding agents with written specifications, bounded slices, full diff review, adversarial critique, unhappy-path testing, and production gates. |
| **AI Slop** | Verbose, disorganized, repetitive generated code and restatement comments that appear functional initially but destroy maintainability. |
| **Complexity Ceiling** | The threshold of domain coupling and architectural novelty beyond which unconstrained LLM generation degrades into regressions. |
| **Truncation Patching** | Stacking extra wrapper/fallback code over a root defect instead of diagnosing and removing the underlying cause. |
| **Sycophancy** | The default RLHF tendency of models to agree with and reassure the user rather than expose flaws — countered via explicit Critique Mode. |
| **Grounding** | Anchoring model claims in retrieved official documentation, source files, or runtime outputs rather than unverified token prediction. |
| **Test Theater (Fake Tests)** | Tautological or over-mocked AI tests written solely to produce green CI checkmarks without proving external behavior. |
| **Chained Prompting** | Executing one architectural layer or vertical slice per prompt, verifying and committing before advancing. |
| **`AGENTS.md` / `CLAUDE.md`** | Repository-resident project constitution read at session start to enforce architecture, style, and security invariants. |
| **`PRD.md`** | Product Requirements Document translating user goals into testable functional specs, non-goals, and edge cases. |
| **Software for One** | Small personal tools built for a single user (`blast radius = 1`) — the safest high-leverage zone for pure Vibe Coding. |
