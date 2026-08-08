# 1009 — Inflation Control

**Project:** Elysium MMORPG  
**Category:** Economy  
**Status:** Design Complete — Implementation Pending  
**Related:** [1008-Economic-Balance.md](1008-Economic-Balance.md) · [1010-Currency-Sinks.md](1010-Currency-Sinks.md) · [1011-Currency-Sources.md](1011-Currency-Sources.md) · [1000-Economy.md](1000-Economy.md)

---

## 1. Overview

Inflation Control is the specific set of design and operational measures that prevent the soft currency (Aurum) and key materials from losing value too quickly as players generate wealth through quests, dungeons, raids, and gathering.

---

## 2. Primary Levers

| Lever | Examples |
|-------|----------|
| **Sinks** | Repairs, training, housing upkeep, transmog fees, crafting costs, vendor purchases |
| **Source tuning** | Quest gold, drop rates, vendor buyback limits |
| **Itemisation** | Binding rules that keep powerful gear from flooding the open market |
| **Time gates** | Daily/weekly lockouts and reward caps on the highest-yield content |
| **Material sinks** | Upgrade systems, consumable use, high-end crafting |

---

## 3. Design Rules

1. Sinks should feel like natural costs of playing, not punitive taxes.
2. New content that introduces large new sources of currency must be paired with corresponding sinks or sinks must be adjusted.
3. Monitoring is continuous; sudden spikes in currency supply or key item prices trigger investigation.

---

## 4. Technical Notes

Currency creation and destruction events are logged for analysis. Dashboards track supply, flow rate, and price indices for critical goods.
