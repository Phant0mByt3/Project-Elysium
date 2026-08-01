# 47 — Status Effects

## Categories

**Buffs** — positive effects applied to allies (damage boosts, shields, haste). Typically class-generated, some from consumables ([0507-Consumables.md](../0500-Items/0507-Consumables.md)).

**Debuffs** — negative effects applied to enemies (damage-over-time, armor reduction, weakened healing).

**Crowd Control (CC)** — effects that limit enemy action: stuns, roots, silences, fears, polymorph-style disables. Central to dungeon/raid mechanics ([0106-Dungeons.md](../0100-World/0106-Dungeons.md), [0107-Raids.md](../0100-World/0107-Raids.md)) and PvP ([0804-PvP.md](../0800-Multiplayer/0804-PvP.md)).

**Elemental Conditions** — status effects tied directly to the elemental damage types in [0307-Elements.md](0307-Elements.md) (burning, frozen, shocked, etc.), each with a distinct secondary effect beyond raw damage.

## Diminishing Returns
Crowd control effects use a diminishing-returns system in PvP to prevent chain-stun lockouts — repeated CC of the same category on the same target within a short window has reduced duration, resetting after a cooldown. PvE bosses are generally immune or highly resistant to hard CC, per raid design standards in [0107-Raids.md](../0100-World/0107-Raids.md).

## Design Rules
* Every CC effect must have a clear visual tell so it reads instantly in group content.
* DoT/HoT effects should tick on a consistent, predictable interval to support add-on/UI clarity.
* Status effect interactions with elements (e.g. Frozen + Fire damage) are defined in [0307-Elements.md](0307-Elements.md) rather than duplicated here.
