---
trigger: always_on
---

# ⚡ Superpowers Rules (Always-On)

These rules apply to ALL work unless the user explicitly opts out.

---

# 0) Core Principle

This system enforces **strict Test-Driven Development (TDD)**.

🚫 Writing production code before tests is **NOT allowed**  
✅ Tests define behavior — code satisfies tests  

---

# 1) Plan Gate (Mandatory for non-trivial work)

If the task is anything beyond a tiny change, you MUST NOT edit code immediately.

## Required steps:
1) Brainstorm:
   - Goal
   - Constraints
   - Risks
   - Acceptance criteria

2) Create a step-by-step plan:
   - Implementation steps
   - Verification steps
   - Risks & mitigations

3) Define test strategy:
   - Test types (unit / integration / e2e)
   - Edge cases
   - Failure scenarios

4) Map requirements → tests

5) Ask user for approval

🚫 DO NOT implement before approval

---

# 1.5) Test Plan Gate (Mandatory)

Before execution, you MUST:

- Convert acceptance criteria into concrete test cases
- Define:
  - Inputs
  - Expected outputs
  - Edge cases
- Specify test structure and scope

Then ask for approval.

🚫 Implementation is NOT allowed before test plan approval

---

# 1.6) Execute Plan Gate

After approval:

🚫 DO NOT start implementation automatically

You MUST instruct the user to run:
`/superpowers-execute-plan`

Only proceed after this command is invoked  
(unless user explicitly overrides)

---

# 2) Test Execution Gate (STRICT TDD)

After `/superpowers-execute-plan`:

## REQUIRED FLOW (NO EXCEPTIONS):

### 1. Write tests FIRST
- Provide full test code

### 2. Run tests (or simulate)
- Show exact commands

### 3. Confirm tests FAIL (RED)
- Must fail for correct reason

🚫 STOP if tests do NOT fail

---

# 3) Implementation Phase (TDD ENFORCED)

Only after RED phase is confirmed:

### 4. Implement minimal code (GREEN)
- Only what is needed to pass tests

### 5. Run tests again
- Confirm they PASS

### 6. Refactor (optional)
- Without breaking tests

---

# 3.1) Anti-Cheating Rules

The agent MUST NOT:

- Write implementation before tests
- Modify tests just to make them pass
- Skip the failing (RED) phase
- Write weak or meaningless tests

Tests MUST:

- Assert real behavior
- Fail without implementation
- Cover edge cases

---

# 3.2) Minimal Implementation Rule

- Write ONLY the minimum code required to pass tests
- No speculative features
- No premature optimization

---

# 3.3) Coverage Requirement

- New/changed code MUST have ≥ 80% coverage (if applicable)
- Otherwise: explicit justification required

---

# 3.4) Regression Protection

For every bug fix:

- Add a failing regression test FIRST
- Prove it fails before fix
- Then fix and verify it passes

---

# 4) Verification is Mandatory

After implementation, you MUST provide:

- Exact commands to:
  - run tests
  - run lint
  - run application (if relevant)

- Evidence that:
  - tests failed before implementation
  - tests now pass

If execution is not possible:
- Provide exact expected outputs

---

# 5) Review Pass (Required)

Before final response, perform a review:

## Categorize issues:
- 🔴 Blocker
- 🟠 Major
- 🟡 Minor
- ⚪ Nit

Include:
- Code quality issues
- Edge cases not covered
- Performance concerns
- Security risks

---

# 6) Safety Rules

- NEVER log secrets
- ALWAYS use:
  - timeouts
  - retries
  - idempotency (for external calls)

- FAIL SAFE:
  - No silent data loss
  - Explicit error handling required

---

# 7) Artifact Persistence (Mandatory)

All outputs MUST be persisted to:

`artifacts/superpowers/`

Includes:
- Brainstorm
- Plan
- Test plan
- Review

---

# 7.1) Persistence Enforcement

You MUST ensure files exist on disk.

Preferred:
```bash
python .agent/skills/superpowers-workflow/scripts/write_artifact.py --path <path>