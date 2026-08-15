# 1415 — Version Control

**Project:** Elysium MMORPG  
**Category:** Development  
**Status:** Design Complete — Implementation Pending  
**Related:** [1411-Git-Workflow.md](1411-Git-Workflow.md) · [1416-Branch-Strategy.md](1416-Branch-Strategy.md) · [0004-Version-History.md](../0000-Project/0004-Version-History.md)

---

## 1. Overview

Version Control is the single source of truth for code, config, and documentation history. Git is the standard.

---

## 2. Rules

- All production-bound changes are committed  
- Secrets never enter the repository  
- Large binary policy is explicit  
- Tags and releases align with Version History and the launcher  


---

## Additional Detail: Repository Structure

The codebase is organized to mirror the plugin architecture described in [1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md), with each plugin module maintained as a clearly bounded directory, keeping the relationship between code organization and runtime architecture intuitive for contributors.

## Tagging and Release Snapshots

Every production release is tagged in version control, providing a precise, reproducible snapshot corresponding to each entry in [0004-Version-History.md](../0000-Project/0004-Version-History.md).
