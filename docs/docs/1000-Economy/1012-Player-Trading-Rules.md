# 1012 — Player Trading Rules

**Project:** Elysium MMORPG  
**Category:** Economy  
**Status:** Design Complete — Implementation Pending  
**Related:** [1004-Trading.md](1004-Trading.md) · [0514-Item-Binding.md](../0500-Items/0514-Item-Binding.md) · [1003-Auction-House.md](1003-Auction-House.md) · [1207-Anti-Cheat.md](../1200-Technical/1207-Anti-Cheat.md)

---

## 1. Overview

Player Trading Rules define what can be exchanged directly between players, under what conditions, and with what safeguards. They exist to enable legitimate trade while limiting RMT, boosting, and item duplication risks.

---

## 2. Core Rules

- Only unbound or appropriately bound items may be traded.
- Both parties must confirm the trade window contents before completion.
- Trade range and context restrictions (e.g. not while in combat, not across certain instance boundaries) apply.
- Large or unusual trades may be logged for review.
- Cross-faction trade is restricted or routed through neutral systems (Auction House, mail with limitations).

---

## 3. Design Rules

1. Legitimate crafting and material trade should feel frictionless.
2. Powerful BoP gear should not become freely tradable after the intended loot window.
3. The rules are enforced server-side; client UI only reflects what is allowed.

---

## 4. Technical Notes

Trade sessions are transactional. Failure or disconnect mid-trade rolls back cleanly. All completed trades are recorded for economy and security analysis.


---

## Additional Detail: New Account Trade Restrictions

Newly created accounts face a brief trade and mail restriction window before their first trades are permitted, a standard anti-fraud measure reducing the effectiveness of throwaway accounts used for real-money-trading or scamming operations.

## Cross-Faction Trade Exception

The only sanctioned cross-faction economic interaction is through the neutral Auction House system managed by the Wayfarer's Guild ([1003-Auction-House.md](1003-Auction-House.md)); direct trading, mail, and guild bank access all remain strictly single-faction.
