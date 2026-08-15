# 1417 — Development Tools

**Project:** Elysium MMORPG  
**Category:** Development  
**Status:** Design Complete — Implementation Pending  
**Related:** [1410-Developer-Environment.md](1410-Developer-Environment.md) · [1215-Developer-Tools.md](../1200-Technical/1215-Developer-Tools.md) · [1401-Coding-Standards.md](1401-Coding-Standards.md)

---

## 1. Overview

Development Tools are the IDEs, linters, profilers, and internal utilities that support daily engineering work.

---

## 2. Rules

- Preferred tools are documented for onboarding  
- Formatters and static analysis run in CI  
- Profiling tools are available for performance work  


---

## Additional Detail: Internal Tool Investment

Given the multi-year scope of the project, the team invests deliberately in internal tooling quality (editor plugins, debug overlays, content validation tools) rather than treating tooling as a one-off afterthought, since tooling quality compounds in value across the entire remaining development timeline.

## Tool Feedback Loop

Internal tools are iterated on based on direct feedback from the designers, builders, and writers using them daily, treating internal tool users as a first-class "customer" whose workflow friction is worth actively reducing.
