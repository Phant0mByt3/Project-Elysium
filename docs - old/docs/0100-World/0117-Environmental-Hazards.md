# 0117 — Environmental Hazards

**Project:** Elysium MMORPG  
**Category:** World  
**Status:** Design Complete — Implementation Pending  
**Related:** [0113-Biomes.md](0113-Biomes.md) · [0114-Weather-System.md](0114-Weather-System.md) · [0306-Status-Effects.md](../0300-Characters/0306-Status-Effects.md) · [0307-Elements.md](../0300-Characters/0307-Elements.md) · [0401-Combat.md](../0400-Gameplay/0401-Combat.md)

---

## 1. Overview

Environmental hazards are persistent or temporary dangers built into the terrain and weather of a region. They exist to make exploration feel consequential, to reward preparation (gear, consumables, class abilities), and to reinforce biome identity.

Hazards are never pure “gotchas”; they are readable, telegraphed, and usually avoidable or mitigable.

---

## 2. Hazard Categories

| Hazard | Typical Biomes | Effect | Mitigation |
|--------|----------------|--------|------------|
| **Lava / Magma Pools** | Volcanic | Instant or ticking fire damage | Fire resistance, careful pathing |
| **Toxic Marsh Gas** | Wetland | Poison DoT + reduced healing | Nature resistance, anti-toxin potions |
| **Unstable Sundered Ground** | Corrupted / Shattered | Periodic knockback or minor damage + temporary slow | Movement abilities, awareness |
| **Blizzard Wind** | Tundra | Movement speed reduction + frost application | Frost resistance, shelter |
| **Ash Cloud** | Volcanic | Reduced visibility + mild fire DoT | Fire resistance, masks/consumables |
| **Deep Water / Undertow** | Coastal, certain rivers | Drown risk or strong current | Swimming skill, water-breathing effects |
| **Falling Ash / Embers** | Near active volcanoes | Random small fire damage | Fire resistance |

---

## 3. Design Rules

1. Every hazard must have a clear visual and/or audio tell.
2. Hazards should be denser in higher-level or endgame regions and lighter in starter zones.
3. No hazard should soft-lock a quest path; an alternative route or temporary mitigation must exist.
4. Class abilities, consumables, and gear should provide meaningful counterplay (see [0507-Consumables.md](../0500-Items/0507-Consumables.md) and resistance stats in [0304-Stats.md](../0300-Characters/0304-Stats.md)).

---

## 4. Interaction with Other Systems

- Weather can intensify or create temporary hazards (e.g. heavy rain turns certain slopes into mud slides).
- Some world events deliberately raise hazard levels in a region for the duration of the event.
- Status effects applied by hazards use the same framework as combat status effects ([0306-Status-Effects.md](../0300-Characters/0306-Status-Effects.md)) so that cleansing and immunity tools remain consistent.

---

## 5. Technical Notes

Hazards are implemented as server-authoritative volume triggers or periodic region-wide checks. Client-side particle and sound effects are cosmetic only; damage and status application always come from the server.
