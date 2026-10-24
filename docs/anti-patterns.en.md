# Catalog of 33 Vibe-Coding Anti-Patterns (7 Risk Families)

**[🇪🇬 النسخة العربية](anti-patterns.ar.md)** · **[⬅ Back to Playbook](../README.md)**

Every failure mode below originates from treating a probabilistic code generator as an autonomous software engineer. Each item documents **what goes wrong**, **why it hurts in production**, and the **mandatory engineering rule** that eliminates it.

---

## Summary Index

| Family | Focus Area | Rule IDs | Count |
| :--- | :--- | :--- | :---: |
| **Family A** | Mindset, Ownership & Cognitive Discipline | `A1` – `A6` | 6 |
| **Family B** | Prompting, Scope & Specification Discipline | `B1` – `B4` | 4 |
| **Family C** | Code Quality, AI Slop & Technical Debt | `C1` – `C5` | 5 |
| **Family D** | Security, Access Control & Supply Chain | `D1` – `D7` | 7 |
| **Family E** | Context Decay, Hallucinations & Regressions | `E1` – `E3` | 3 |
| **Family F** | Testing, Infrastructure & Green-Check Theater | `F1` – `F4` | 4 |
| **Family G** | Product Viability, Economics & Team Health | `G1` – `G4` | 4 |

---

## Family A — Mindset, Ownership & Cognitive Discipline

### `A1` — Blind "Accept" Without Diff Inspection *(The Root Failure)*
- **Pattern:** Accepting multi-file generated edits because the visible UI appeared to work on a quick click.
- **Impact:** Unnecessary code, incompatible imports, silent state mutations, and broken neighbor features enter `main` undetected.
- **Engineering Rule:** **Zero blind accepts.** Read every line of `git diff` against written specifications as a Tech Lead reviewing a junior engineer's Pull Request. If you cannot explain a line, require the agent to explain it before merging.

### `A2` — Magical Thinking & Author Self-Certification
- **Pattern:** Treating the model as an infallible oracle and asking the same session `"Is everything secure and complete?"`
- **Impact:** You cannot spot omissions in domains you did not specify (*unknown unknowns*), and an author model naturally validates its own assumptions.
- **Engineering Rule:** Treat the agent as a fast junior implementer requiring explicit constraints. Separate code authorship from code/security verification.

### `A3` — Cognitive Atrophy (Outsourcing Problem Decomposition)
- **Pattern:** Delegating architecture, debugging, and decomposition entirely to the model until your own diagnostic instincts atrophy.
- **Impact:** When the project hits the model's complexity ceiling or a subtle production incident occurs, you are paralyzed.
- **Engineering Rule:** Reserve **manual architectural ownership** for system boundaries, data modeling, and failure analysis. Modify, break, and trace critical code paths yourself.

### `A4` — The One-Shot Product Illusion & Complexity Ceiling
- **Pattern:** Expecting a single natural-language sentence to produce a complex, stateful, multi-role production platform.
- **Impact:** Models excel at common boilerplate patterns but degrade sharply on novel domain invariants and complex distributed state.
- **Engineering Rule:** Decompose systems into small, verifiable vertical slices executed inside an iterative **Specify → Implement → Review → Test** loop.

### `A5` — Loss of Production Reverence (2 AM Blast-Radius Blindness)
- **Pattern:** Shipping software to real users with the casual mindset of a disposable weekend prototype because generation felt effortless.
- **Impact:** Real customer data loss, night-time outages with no runbook, regulatory liability, and permanent reputational damage.
- **Engineering Rule:** Explicitly classify every repository on Day 1: **Disposable Prototype (`PoC`)** vs. **Production System**. Production requires monitoring, backups, incident ownership, and staged release gates.

### `A6` — Falling for Model Sycophancy (Agreeable Over Accurate)
- **Pattern:** Assuming default model responses are neutral and objective when evaluating your ideas or code.
- **Impact:** RLHF-trained models default to agreeable, reassuring answers — praising weak architectures and underreporting risk.
- **Engineering Rule:** Explicitly invoke **Adversarial Critique Mode** (see [Prompt Blueprint P11](prompt-blueprints.en.md#p11--anti-sycophancy-adversarial-critique-mode)) and challenge conclusions on high-stakes decisions.

---

## Family B — Prompting, Scope & Specification Discipline

### `B1` — Monolithic Mega-Prompts
- **Pattern:** Requesting database schema, backend APIs, authentication, state management, and responsive UI in one giant prompt.
- **Impact:** Context dilution causes skipped endpoints, mocked/stubbed wiring disguised as working UI, and unreviewable 2,000-line diffs.
- **Engineering Rule:** Use **Chained Layer Prompting**: `Project Skeleton → Data Schema → API & Validation → Domain Logic → UI → Styling → Tests`, closing and committing each layer before starting the next.

### `B2` — Vague, Unscoped Prompts Without Negative Constraints
- **Pattern:** Asking `"Build a login page"` or `"Add form validation"` without specifying stack, validation library, design tokens, or what **not** to build.
- **Impact:** The model invents unrequested backend routes, installs arbitrary packages, and ignores security controls.
- **Engineering Rule:** Specify **Role + Exact Stack + Security/Validation Rules + Design Reference + Explicit Non-Goals** (what files/layers must *not* be touched).

### `B3` — Raw Error-Pasting Doom Loops
- **Pattern:** Pasting raw stack traces with `"Fix this"` repeatedly without reading or diagnosing the failure.
- **Impact:** Fixing Error A introduces Error B, which breaks Feature C — spiraling into corrupted state and wasted tokens.
- **Engineering Rule:** Diagnose first, checkpoint with `git commit` before attempting fixes, constrain the fix to the responsible module, and enforce a **Two-Strike Stop Rule** (if two attempts fail, halt and re-diagnose root cause).

### `B4` — Prompting Before Written Specifications
- **Pattern:** Jumping straight into code generation without spending 30 minutes documenting requirements and edge cases.
- **Impact:** Every edge case you failed to think through is guaranteed to be absent from the generated system.
- **Engineering Rule:** **Specs Before Prompts.** Commit `AGENTS.md` / `CLAUDE.md`, `PRD.md`, and `IMPLEMENTATION_PLAN.md` in the repository before Task 1.

---

## Family C — Code Quality, AI Slop & Technical Debt

### `C1` — Bloated Functions, Weak Naming & Public-Repo Training Bias
- **Pattern:** Accepting 200-line functions, vague variable names (`data2`, `tempRes`), and missing docstrings because tests appear to pass.
- **Impact:** Models trained heavily on uncurated public repositories reproduce amateur patterns unless constrained by explicit standards.
- **Engineering Rule:** Enforce automated linters/formatters, a **≤ 30-line function target**, domain-accurate naming, and concise public docstrings inside `AGENTS.md`.

### `C2` — AI Slop & Unmaintainable Boilerplate
- **Pattern:** Verbose, repetitive markup, dead branches, and noisy comments restating obvious syntax across every file.
- **Impact:** High cognitive load slows future feature work until rewriting from scratch becomes cheaper than editing.
- **Engineering Rule:** Make maintainability an explicit acceptance criterion; extract shared components/templates and run dedicated behavior-preserving refactor passes.

### `C3` — Unbounded Technical Debt Accumulation
- **Pattern:** Stacking feature upon feature in parallel without closing, cleaning, or testing previous increments.
- **Impact:** Structural fragility where every small change triggers cascading regressions across unrelated modules.
- **Engineering Rule:** Never start Feature `N+1` until Feature `N` is tested, linted, refactored, and committed. Track deferred debt explicitly in the repository.

### `C4` — Truncation Patching (Workarounds Over Root Causes)
- **Pattern:** When two libraries or state flows conflict, the agent wraps extra adapter/fallback layers on top instead of removing the root conflict.
- **Impact:** Ever-growing layers of dead/conflicting workarounds that obscure runtime behavior.
- **Engineering Rule:** Require a written root-cause explanation before any bugfix diff. If workarounds accumulate, `git reset` to the last clean checkpoint and fix cleanly.

### `C5` — AI-Signature UI Layer Bugs & Invisible Network Storms
- **Pattern:** Broken interactions caused by invisible CSS `z-index`/`visibility` overlays, or pages firing 5+ sequential client HTTP requests where 1 bulk request belongs.
- **Impact:** Developers waste hours debugging backend logic for a CSS layer bug, while silent N+1 client requests crush server latency and cloud bills.
- **Engineering Rule:** Inspect browser **DevTools Network & DOM Layers** on every UI review: audit request count per screen and verify overlay/stacking behavior explicitly.

---

## Family D — Security, Access Control & Supply Chain

### `D1` — Shipping Unaudited Code to Real Users
- **Pattern:** Deploying generated applications directly to production assuming the builder platform handled security automatically.
- **Impact:** Exposed user tables, missing authorization checks (IDOR/broken RLS), and public data leaks.
- **Engineering Rule:** Run SAST, dependency vulnerability scans, and manual auth/authorization path audits prior to every production release.

### `D2` — Asking the Author Model (or Online Score Widgets) to Certify Security
- **Pattern:** Asking the same AI session that wrote the app — or a superficial online grading badge — to certify security readiness.
- **Impact:** False confidence masking critical business-logic, authorization, and supply-chain vulnerabilities.
- **Engineering Rule:** Enforce **separation of duties**: audit with an independent model using explicit security criteria, static analysis tools, and human penetration testing for sensitive data.

### `D3` — Missing Server-Side Validation & Hardcoded Secrets
- **Pattern:** Relying on client-side form checks alone, embedding API keys in frontend/source files, or storing credentials unsafely.
- **Impact:** Trivial request tampering bypasses client checks; leaked keys in bundles or git history lead to immediate compromise.
- **Engineering Rule:** Enforce strict **server-side schema validation** on every endpoint, keep all secrets in `.env` (excluded via `.gitignore`), and scan git commits for secrets.

### `D4` — Over-Privileged Host Execution & Production Data Access
- **Pattern:** Running autonomous CLI/IDE agents in unrestricted YOLO mode with access to personal directories, SSH keys, or live production credentials.
- **Impact:** Accidental exfiltration, destructive shell commands, or corruption of real customer environments.
- **Engineering Rule:** Run agents inside isolated workspaces/containers under **least privilege**, strictly separated from production credentials and live databases.

### `D5` — Trivial-Dependency Supply-Chain Bloat
- **Pattern:** Allowing the agent to install unfamiliar third-party packages for trivial 15-line tasks (string formatting, simple Markdown helpers).
- **Impact:** Every unnecessary package expands your CVE and supply-chain compromise surface.
- **Engineering Rule:** Challenge every new dependency: if it can be written cleanly in ~20 lines of standard library code, write it natively. Audit maintainer health and pin versions for required packages.

### `D6` — Unprotected `DROP`/`DELETE` Operations & Untested Backups
- **Pattern:** Giving an agent migration or database execution rights against live data without destructive-command guards or verified backups.
- **Impact:** Single hallucinated migration or cleanup command wipes production tables permanently.
- **Engineering Rule:** Block automated `DROP`/`TRUNCATE`/`DELETE` without manual human confirmation, isolate dev/staging DBs from prod, and **test backup restoration** regularly.

### `D7` — Copy-Pasting Permission Prompts Across Tools
- **Pattern:** Copying prompts containing role names, access tokens, or security-rule snippets from one AI chat into another tool without rewriting access boundaries from scratch.
- **Impact:** Misaligned RBAC/RLS rules silently expose private customer records to public read access for weeks without triggering errors.
- **Engineering Rule:** Write every IAM/RBAC/RLS policy from first principles (default-deny), test cross-user access negative cases, and alert on permission policy changes.

---

## Family E — Context Decay, Hallucinations & Regressions

### `E1` — Regression Whack-a-Mole (Breaking Working Features During Fixes)
- **Pattern:** Asking for a localized fix in a growing project and discovering previously working flows were altered or deleted.
- **Impact:** Endless regression cycles without a safety net.
- **Engineering Rule:** Lock down working slices with automated unit + integration/E2E tests, work in feature branches with atomic commits, and forbid touching out-of-scope files.

### `E2` — Plausible Hallucinations, Mocked Wiring & Unoriginal Templates
- **Pattern:** Polished UI screens backed by hardcoded mock arrays, nonexistent API methods, or designs copied verbatim from public templates.
- **Impact:** Demo looks complete while core backend integrations do not exist or expose IP/copyright risk.
- **Engineering Rule:** Verify real database writes, live network payloads, and library docs via grounded search; audit visual originality before commercial launch.

### `E3` — Context Window Decay in Growing Repositories
- **Pattern:** Keeping a single marathon chat open across dozens of features until the model forgets architectural invariants and mixes old and new tasks.
- **Engineering Rule:** Persist institutional memory in **repository files** (`AGENTS.md`, `PRD.md`, `IMPLEMENTATION_PLAN.md`), keep modules small, and start a fresh context session per bounded task.

---

## Family F — Testing, Infrastructure & Green-Check Theater

### `F1` — Happy-Path-Only Verification
- **Pattern:** Testing with one ideal user on `localhost` Chrome desktop and declaring the product ready.
- **Impact:** Immediate failures on mobile viewports, Safari/Firefox, slow networks, expired sessions, or malformed inputs.
- **Engineering Rule:** Mandate explicit **Unhappy-Path Testing**: invalid payloads, unauthorized roles, network drops, concurrency races, mobile viewports, and prompt-injection inputs.

### `F2` — Unplanned External CDNs & Unreplaced Placeholders
- **Pattern:** Shipping generated links to unpinned third-party CDNs, placeholder copy, broken footer links, or stock watermarked assets.
- **Impact:** Broken production styling when an external URL changes, licensing issues, and amateur brand trust loss.
- **Engineering Rule:** Pin and self-host critical fonts/icons where appropriate, replace 100% of placeholder content, and run an automated link/asset checker pre-launch.

### `F3` — Ignoring Infrastructure, Pooling & Scalability
- **Pattern:** Opening a new database connection per request, storing session state in local process memory, and never load-testing concurrency.
- **Impact:** Viral launch traffic immediately exhausts connections and brings the service down at peak demand.
- **Engineering Rule:** Require **Connection Pooling**, stateless/thread-safe request handling, caching strategy, and load testing (`1,000+` concurrent requests) before launch.

### `F4` — Green-Check Test Theater *(Fake AI Unit Tests)*
- **Pattern:** Celebrating `"450 tests passing"` when the agent wrote tautological or mock-only tests simply to satisfy the prompt and turn CI green.
- **Impact:** Broken business logic auto-deploys to production behind a wall of meaningless green checkmarks.
- **Engineering Rule:** Audit every test's assertions (see [Prompt Blueprint P12](prompt-blueprints.en.md#p12--test-theater-audit--fail-then-pass-enforcement)): verify each test fails when the production logic is disabled (`Fail-Then-Pass`) and test observable behavior independently.

---

## Family G — Product Viability, Economics & Team Health

### `G1` — Confusing Code Generation With Distribution & Revenue
- **Pattern:** Believing that generating an app effortlessly equals a viable business without distribution, audience, or operational reliability.
- **Engineering Rule:** Use rapid prototyping strictly to validate `PoC` demand cheaply; invest engineering rigor and distribution effort simultaneously once moving to `MVP`.

### `G2` — Arbitraging Client Ignorance With Raw AI Output
- **Pattern:** Selling raw, unreviewed one-prompt websites/outputs that clients could generate themselves with a $20 subscription.
- **Engineering Rule:** Deliver **defensible engineering value** tools cannot self-provide: custom architecture, security hardening, complex integrations, reliability, and long-term maintainability.

### `G3` — Ignoring Token Economics, Legal Compliance & Accessibility
- **Pattern:** Burning数百/thousands of dollars in unfocused chat loops, or ignoring data-privacy, accessibility, and licensing obligations.
- **Engineering Rule:** Set strict monthly token/API budgets, use concise spec-driven prompts (and lighter models for routine test runs), and verify accessibility/privacy compliance pre-release.

### `G4` — Knowledge-Transfer Erosion & Abandoning Engineering Hygiene
- **Pattern:** Senior engineers bypassing junior mentorship (`"faster to prompt it myself"`), keeping architectural context trapped in private AI chats, or skipping Git/code review for speed.
- **Engineering Rule:** Keep **Git, Pull Request reviews, automated tests, and written ADRs** non-negotiable red lines; document decisions in the repo and protect team code-review mentorship.
