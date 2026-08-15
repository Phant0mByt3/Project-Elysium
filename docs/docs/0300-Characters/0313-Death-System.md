# 0313 — Death System

**Project:** Elysium MMORPG
**Category:** Characters
**Status:** Design Complete — Implementation Pending
**Related:** 0305-Leveling.md · 0312-Character-Animations.md · [0401-Combat.md](../0400-Gameplay/0401-Combat.md) · [0111-Fast-Travel.md](../0100-World/0111-Fast-Travel.md) · [0103-Cities.md](../0100-World/0103-Cities.md) · [0515-Item-Durability.md](../0500-Items/0515-Item-Durability.md)

---

## 1. Overview

Death in Elysium is a temporary setback rather than a punishment loop.

The system should make dangerous content feel meaningful without forcing players through long corpse runs, permanent progression loss, or excessive downtime. Players should be able to recover from death quickly while still having meaningful reasons to avoid dying repeatedly.

Death is fully server-authoritative. The client presents the player's spirit state, available resurrection options, recovery penalties, and respawn locations.

---

## 2. Death State

When a player's health reaches zero, the character enters the **Dead** state.

The player:

* Becomes a spirit at the location of death.
* Cannot use normal combat abilities or interact with most world objects.
* Can move within a limited area around their death location.
* Can view nearby players, enemies, and available resurrection options.
* Can choose to remain at the death location or release.

The spirit state exists primarily to allow player resurrection and provide a short recovery period without requiring a traditional corpse-run system.

### 2.1 Spirit Interaction

While dead, the player may:

* Wait for a player resurrection.
* Accept a resurrection from an eligible NPC or system checkpoint where available.
* Release to an available recovery location.
* Use permitted spirit-only interactions, such as viewing nearby objectives or identifying the location of their death.

Dead players cannot permanently block objectives, loot, dungeon progression, or other required content.

---

## 3. Resurrection

Resurrection is divided into two forms.

### Player Resurrection

Classes with resurrection abilities can restore fallen allies without requiring them to release.

The exact abilities and restrictions are defined by the relevant class and specialization documents.

Player resurrection:

* Returns the character to the world at or near their death location.
* Restores a controlled amount of health and resources.
* Applies a short **Resurrection Sickness** effect.
* Does not restore durability lost from the original death.

Resurrection abilities may have combat restrictions or cooldowns depending on the class.

### Spirit Healer Resurrection

If the player releases, they are restored at the nearest valid recovery location.

Spirit healers may exist in:

* Major cities.
* Inns.
* Graveyards.
* Faction settlements.
* Dungeon and raid recovery areas.

This option is always available where a valid recovery location exists.

---

## 4. Release System

When releasing, the player is presented with the available recovery location.

Priority is generally:

1. Active dungeon or raid checkpoint.
2. Recently unlocked local spirit healer.
3. Bound inn or Hearth location.
4. Nearest appropriate city or settlement.

The system should prefer locations that return the player to relevant gameplay rather than simply selecting the geographically closest location.

For example, a player who dies deep inside a dungeon should normally return to the dungeon's entrance or most recent checkpoint rather than a city several kilometres away.

---

## 5. Recovery by Content Type

| Content                 | Death Behaviour                                                |
| ----------------------- | -------------------------------------------------------------- |
| Open World              | Spirit remains at death location until resurrected or released |
| Dungeon                 | Returns to entrance or latest activated checkpoint             |
| Raid                    | Returns to the current raid recovery checkpoint                |
| World Boss              | Releases to the nearest appropriate spirit healer              |
| PvP                     | Releases to a faction-aligned recovery location                |
| Contested Territory     | Uses the nearest valid faction recovery point                  |
| Instanced Story Content | Uses the instance's designated recovery point                  |

Dungeon and raid encounters should never require players to repeat excessive traversal simply because they died.

---

## 6. Resurrection Sickness

Players resurrected after death receive a short **Resurrection Sickness** debuff.

The effect temporarily reduces combat effectiveness, primarily through reduced damage and healing output.

The effect:

* Has a short duration.
* Fades automatically.
* Does not affect normal movement or exploration.
* Does not permanently reduce character power.
* Can be tuned separately for PvE and PvP.

The purpose is to discourage repeatedly dying and immediately re-entering dangerous combat without creating a major progression penalty.

---

## 7. Death Costs

Death does not remove character progression.

At launch, death causes:

* Modest equipment durability loss.
* No experience debt.
* No level loss.
* No permanent stat loss.
* No loss of learned skills or talents.
* No loss of quest progress.

Durability loss acts primarily as a controlled gold sink rather than a punishment for attempting difficult content.

Repeated deaths should therefore cost resources and time, but should never create a situation where a player becomes permanently weaker because they failed an encounter.

---

## 8. Group Resurrection

Healers and other appropriate classes can make resurrection an important part of group play.

A successful resurrection should:

* Reduce downtime after a wipe or partial party death.
* Reward groups for protecting their healer.
* Give resurrection abilities meaningful utility without making them mandatory.
* Respect encounter-specific resurrection limits where required.

Raid and dungeon encounters may restrict the number or timing of combat resurrections to prevent resurrection mechanics from trivialising encounter failure.

---

## 9. Death During Boss Encounters

Boss encounters determine their own resurrection rules.

Possible behaviours include:

* Normal player resurrection during combat.
* Limited combat resurrection charges.
* Resurrection disabled during specific encounter phases.
* Full party recovery after a wipe.
* Automatic checkpoint restoration.

These rules are encounter-specific and should be documented in the relevant dungeon or raid design rather than hardcoded into the global death system.

---

## 10. PvP Death

PvP death follows the same core system but uses faction-aware recovery locations.

Players should not be trapped in an endless death loop caused by enemy players camping a single resurrection location.

Anti-camping measures may include:

* Temporary protection after resurrection.
* Spirit-only movement away from the death location.
* Protected faction recovery zones.
* Alternative resurrection points.
* Diminishing rewards for repeatedly killing the same player.

PvP death should create meaningful risk without making contested areas effectively inaccessible.

---

## 11. Death and Fast Travel

The Death System works alongside the Hearth / Recall system ([0111-Fast-Travel.md](../0100-World/0111-Fast-Travel.md)).

Death should never invalidate the player's established travel network.

For example:

```text
Player dies
     |
     v
Spirit State
     |
     +--------------------+
     |                    |
     v                    v
Player Resurrection     Release
     |                    |
     v                    v
Death Location       Recovery Location
                          |
                          v
                    Continue Playing
```

The Hearth / Recall system remains a separate travel tool and should not be required to recover from ordinary deaths.

---

## 12. Death Presentation

Death should feel significant without becoming frustrating.

The client should provide:

* Clear death animation.
* Brief transition into spirit form.
* Visible death location.
* Clear resurrection/release interface.
* Available recovery location.
* Remaining Resurrection Sickness duration after recovery.

The spirit form should have a distinct visual identity consistent with the world's lore and the character's race.

Animation requirements are covered by [0312-Character-Animations.md](0312-Character-Animations.md).

---

## 13. Design Goals

The Death System should:

1. Keep players in the world.
2. Make death meaningful without being excessively punitive.
3. Make healer resurrection valuable.
4. Avoid traditional corpse-run frustration.
5. Prevent PvP resurrection camping from becoming oppressive.
6. Preserve all meaningful character progression after death.
7. Keep dungeon and raid recovery fast enough to maintain encounter pacing.
8. Provide enough death cost to discourage reckless play without discouraging experimentation.
9. Remain flexible enough for individual encounter and PvP rules.

---

## 14. Technical Rules

Death is completely server-authoritative.

The server records:

* Character death state.
* Death location.
* Current instance and checkpoint.
* Durability changes.
* Resurrection state.
* Active Resurrection Sickness.
* Available recovery locations.

The client is responsible only for presenting the appropriate state and interface.

A disconnected player who is dead remains dead on the server and can continue from the same recovery state when reconnecting.

---

## 15. System Boundaries

The Death System owns:

* Death state.
* Spirit state.
* Resurrection.
* Release.
* Recovery locations.
* Resurrection Sickness.
* Death-related durability loss.

Other systems own their respective mechanics:

* Combat determines when a character reaches zero health.
* Classes determine resurrection abilities.
* Dungeons and raids determine encounter-specific recovery rules.
* PvP determines PvP-specific death and anti-camping behaviour.
* Item systems determine durability.
* Fast Travel determines Hearth / Recall behaviour.

This separation prevents the Death System from becoming responsible for unrelated character or world mechanics.
