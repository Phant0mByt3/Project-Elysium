# 1011 — Currency Sources

**Project:** Elysium MMORPG  
**Category:** Economy  
**Status:** Design Complete — Implementation Pending  
**Related:** [1001-Currency.md](1001-Currency.md) · [1009-Inflation-Control.md](1009-Inflation-Control.md) · [0700-Quests.md](../0700-Quests/0700-Quests.md) · [0106-Dungeons.md](../0100-World/0106-Dungeons.md)

---

## 1. Overview

Currency Sources are the systems that inject Aurum and other currencies into the player economy. They are tuned so that players feel rewarded for play without flooding the market.

---

## 2. Primary Sources

| Source | Notes |
|--------|-------|
| **Quest rewards** | Steady income while leveling and for dailies/weeklies |
| **Mob & boss drops** | Small amounts from trash, larger from bosses |
| **Vendor sell** | Vendor trash and excess materials |
| **Auction House sales** | Player-to-player transfer (not net new currency, but redistributes) |
| **Event & seasonal rewards** | Time-limited boosts |
| **Achievement / milestone grants** | Occasional one-time sums |

---

## 3. Design Rules

1. Sources are front-loaded during leveling so new characters can afford training and repairs, then moderated at max level.
2. The highest-yield sources are usually time-gated (lockouts, daily/weekly caps).
3. Sources and sinks are reviewed together; increasing one without the other risks imbalance.
