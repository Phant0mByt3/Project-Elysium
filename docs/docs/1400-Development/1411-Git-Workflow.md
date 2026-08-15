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


---

## Additional Detail: Commit Standards

Commit messages follow a consistent format (a short imperative summary line, optional detailed body) referencing the relevant `docs/` file or ticket where applicable, keeping the project history genuinely useful for future contributors trying to understand why a change was made.

## Large File Handling

Binary art and audio assets are managed through appropriate large-file handling tooling rather than committed directly to the primary code repository, keeping repository size and clone times manageable as the content pack grows over years of development.
