# 1418 — Local Testing

**Project:** Elysium MMORPG  
**Category:** Development  
**Status:** Design Complete — Implementation Pending  
**Related:** [1406-Testing.md](1406-Testing.md) · [1410-Developer-Environment.md](1410-Developer-Environment.md) · [1419-Staging-Environment.md](1419-Staging-Environment.md)

---

## 1. Overview

Local Testing is what every engineer runs before pushing: unit tests, smoke starts of the dev server, and basic feature verification.

---

## 2. Rules

- Critical paths have automated tests  
- A minimal “boot and login” smoke path is documented  
- Local test data never points at production  


---

## Additional Detail: Fast Iteration Loops

Local testing setups prioritize fast iteration — quick server restart times, hot-reloadable content where feasible ([1200-Plugin-Architecture.md](../1200-Technical/1200-Plugin-Architecture.md)) — recognizing that developer iteration speed directly affects how much testing actually happens before a change reaches shared environments.

## Isolated Test Data

Local environments use seeded, isolated test data (test characters, test items) separate from any shared staging data, letting individual contributors test freely without risk of corrupting shared testing state for the rest of the team.
