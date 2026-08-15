# 1014 — NPC Economy

**Project:** Elysium MMORPG  
**Category:** Economy  
**Status:** Design Complete — Implementation Pending  
**Related:** [1013-Merchant-System.md](1013-Merchant-System.md) · [0906-Simulated-Civilisation.md](../0900-Player-Systems/0906-Simulated-Civilisation.md) · [1000-Economy.md](1000-Economy.md) · [0209-NPCs.md](../0200-Lore/0209-NPCs.md)

---

## 1. Overview

NPC Economy describes how non-player characters participate in the economic life of Elysium: merchants buying and selling, caravans moving goods, and the simulation of a living marketplace that exists whether or not players are watching.

---

## 2. Elements

- Static and rotating vendor inventories
- Buyback and sell prices that create natural sinks and sources
- Flavour caravans and trade routes that can be interacted with or defended (world events)
- Reputation-gated stock that reflects faction and organisational standing
- Optional future simulation of supply/demand flavour without full dynamic pricing complexity at launch

---

## 3. Design Rules

1. NPC economy supports immersion and convenience; it does not attempt to fully simulate a real-world market.
2. Player-driven prices on the Auction House remain the primary discovery mechanism for true market value.
3. NPC interactions should reinforce the sense that cities and roads are alive ([0906-Simulated-Civilisation.md](../0900-Player-Systems/0906-Simulated-Civilisation.md)).


---

## Additional Detail: Simulated Economic Activity

Background NPC economic activity (documented more fully in [0906-Simulated-Civilisation.md](../0900-Player-Systems/0906-Simulated-Civilisation.md)) includes simulated trade caravans between cities and villages, contributing to the sense of a living economy that exists independent of direct player participation.

## Player Impact on NPC Markets

Certain player actions (completing a supply-chain quest chain, defending a caravan) can measurably affect simulated NPC vendor stock or pricing in that region for a limited time, giving quest completion a light, satisfying economic ripple effect.
