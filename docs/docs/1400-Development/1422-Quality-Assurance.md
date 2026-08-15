# 1422 — Quality Assurance

**Project:** Elysium MMORPG  
**Category:** Development  
**Status:** Design Complete — Implementation Pending  
**Related:** [1406-Testing.md](1406-Testing.md) · [1407-Bug-Tracking.md](1407-Bug-Tracking.md) · [1400-Development-Standards.md](1400-Development-Standards.md)

---

## 1. Overview

QA is the discipline of finding issues before players do: test plans, regression suites, exploratory play, and release certification.

---

## 2. Rules

- Critical and major bugs block release  
- Regression coverage grows with the game  
- QA is involved early on large features, not only at the end  


---

## Additional Detail: QA Team Structure

Dedicated QA contributors work alongside designers and engineers throughout each phase rather than only at the end of the pipeline, catching issues earlier when they're cheaper to fix, and building deep familiarity with each system's intended behavior over time.

## Exploratory vs Scripted Testing

QA passes combine scripted test cases (verifying known expected behavior) with exploratory testing (deliberately trying to break systems in unexpected ways), since scripted tests alone tend to miss the creative edge cases real players will inevitably find.
