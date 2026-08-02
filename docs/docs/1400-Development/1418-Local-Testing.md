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
