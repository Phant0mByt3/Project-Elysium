# 1412 — Code Review

**Project:** Elysium MMORPG  
**Category:** Development  
**Status:** Design Complete — Implementation Pending  
**Related:** [1401-Coding-Standards.md](1401-Coding-Standards.md) · [1411-Git-Workflow.md](1411-Git-Workflow.md) · [1406-Testing.md](1406-Testing.md)

---

## 1. Overview

Code Review is mandatory for changes that affect shared code. Reviews protect architecture, security, and coding standards.

---

## 2. Focus Areas

- Correctness and edge cases  
- Server authority and anti-cheat implications  
- Performance and data access patterns  
- Readability and documentation  
- Test coverage for critical paths  

---

## 3. Rules

At least one approving review is required for protected branches. Reviewers prioritise risk over style nitpicks when time is limited.


---

## Additional Detail: Review Turnaround Expectations

Reviewers are expected to provide initial feedback within a reasonable turnaround window, keeping the development velocity healthy — a review process that becomes a bottleneck defeats its own purpose of maintaining quality without unduly slowing shipping.

## What Reviewers Check

Beyond functional correctness, reviewers check adherence to [1401-Coding-Standards.md](1401-Coding-Standards.md), appropriate test coverage per [1406-Testing.md](1406-Testing.md), and whether the change requires a corresponding documentation update per the documentation-first principle in [0008-Development-Philosophy.md](../0000-Project/0008-Development-Philosophy.md).
