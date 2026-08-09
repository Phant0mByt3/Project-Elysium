# 1411 — Git Workflow

**Project:** Elysium MMORPG  
**Category:** Development  
**Status:** Design Complete — Implementation Pending  
**Related:** [1415-Version-Control.md](1415-Version-Control.md) · [1416-Branch-Strategy.md](1416-Branch-Strategy.md) · [1412-Code-Review.md](1412-Code-Review.md)

---

## 1. Overview

Git Workflow defines how contributors branch, commit, review, and merge. Consistency keeps history readable and CI reliable.

---

## 2. Practices

- Small, focused commits with clear messages  
- Feature branches from the agreed base branch  
- Pull/merge requests required for shared branches  
- CI must pass before merge  
- No force-push to protected branches  

---

## 3. Rules

Workflow details live alongside Branch Strategy. Exceptions for hotfixes are documented in the Release Process.
