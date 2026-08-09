# 0915 — Player Rewards

**Project:** Elysium MMORPG  
**Category:** Player Systems  
**Status:** Design Complete — Implementation Pending  
**Related:** [0701-Quest-Rewards.md](../0700-Quests/0711-Quest-Rewards.md) · [0807-Seasons.md](../0800-Multiplayer/0807-Seasons.md) · [0907-Collections.md](0907-Collections.md) · [1001-Currency.md](../1000-Economy/1001-Currency.md)

---

## 1. Overview

Player Rewards is the umbrella concept for all the ways the game gives players tangible or cosmetic benefits: quest payouts, dungeon and raid loot, seasonal tracks, achievement grants, login or event rewards, and more. This document focuses on the cross-cutting design principles rather than any single source.

---

## 2. Principles

1. **Clarity** — Players should understand what they earned and why.
2. **Variety** — Rewards mix power, currency, cosmetics, and convenience.
3. **Fairness** — Core progression rewards are available through normal play; exclusive prestige rewards exist but do not gate essential power.
4. **Pacing** — Reward frequency and size support the leveling and endgame curves without constant dopamine spikes or long droughts.
5. **Account value** — Where appropriate, rewards unlock account-wide collection progress.

---

## 3. Delivery

Rewards are granted through the relevant systems (quest turn-in, loot distribution, seasonal claim UI, mail, etc.). A unified “recent rewards” or notification stream helps players notice what they received.
