# 1416 — Branch Strategy

**Project:** Elysium MMORPG  
**Category:** Development  
**Status:** Design Complete — Implementation Pending  
**Related:** [1411-Git-Workflow.md](1411-Git-Workflow.md) · [1408-Release-Process.md](1408-Release-Process.md) · [1415-Version-Control.md](1415-Version-Control.md)

---

## 1. Overview

Branch Strategy defines long-lived vs short-lived branches, release branches, and hotfix flow.

---

## 2. Typical Model

- `main` / `trunk` — stable, releasable  
- Short-lived feature branches  
- Optional release branches for stabilisation  
- Hotfix branches cut from the live tag when needed  

Exact names are team-agreed; the principle is predictability and protected stable lines.


---

## Additional Detail: Long-Lived Feature Branches

Large systems requiring extended development (a new expansion's world content) may use a longer-lived integration branch, periodically synced with the main development branch to avoid painful merge conflicts at final integration time.

## Hotfix Branching

Critical production hotfixes ([1408-Release-Process.md](1408-Release-Process.md)) branch directly from the current production release tag rather than the main development branch, ensuring the hotfix doesn't accidentally include unrelated in-progress work.
