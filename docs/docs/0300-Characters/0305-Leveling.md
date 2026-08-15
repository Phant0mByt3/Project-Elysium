# 0305 — Leveling

## Overview

Character leveling is the primary progression system in Elysium.

The launch level cap is **50**.

The leveling experience is intentionally split into two phases:

**Early progression** teaches the player's class and gradually introduces its core skills.

**Later progression** focuses more heavily on specialization, talents, equipment and build customization.

The goal is for players to understand their character before being given a large number of customization options.

---

# Level Range

### Levels 1–9 — Class Foundation

Players learn the fundamentals of their chosen class.

Progression focuses on:

* Core Skills
* Basic combat mechanics
* Class resources
* Utility abilities
* Early equipment
* World exploration

Players should gain new abilities frequently during this stage.

---

### Level 10 — Specialization

At level 10, the player chooses one of their class's two specializations.

See [0301-Specializations.md](0301-Specializations.md).

The specialization unlocks:

* Specialization Skills
* Specialization Talent Tree
* Specialization-specific mechanics
* New combat options
* A defined group role

The player can later change between their two specializations outside of combat.

---

### Levels 10–50 — Specialization Progression

After specialization, progression gradually shifts away from constantly receiving new abilities.

Players instead gain:

* Talent Points
* Improved equipment
* New specialization skills
* Stronger class mechanics
* New content access
* More build customization

Talent Points become a major part of character progression.

See [0303-Talent-Trees.md](0303-Talent-Trees.md).

---

# Experience Sources

Experience can be earned through several activities.

## Quests

Questing is the primary source of experience, particularly during the early game.

Regional questlines are designed to naturally guide players through the world without requiring repetitive grinding.

See [0102-Regions.md](../0100-World/0102-Regions.md).

---

## Dungeons

Dungeon completion provides meaningful experience alongside equipment and other rewards.

See [0106-Dungeons.md](../0100-World/0106-Dungeons.md).

Dungeons should provide an alternative progression path for players who prefer group content.

---

## Exploration

Exploration rewards players for discovering the world.

Experience can be granted for:

* Discovering landmarks
* Entering unexplored areas
* Finding hidden locations
* Discovering secret areas
* Completing exploration objectives

See [0105-Landmarks.md](../0100-World/0105-Landmarks.md).

---

## Enemy Defeats

Defeating enemies provides a small amount of experience.

Enemy kills are intentionally a secondary source of progression.

Players should not need to repeatedly kill enemies for hours to reach the next level.

This supports Pillar 5 in [0002-Core-Pillars.md](../0000-Project/0002-Core-Pillars.md).

---

# Progression Philosophy

Elysium's leveling system should encourage players to experience the world rather than optimize a single repetitive activity.

A player should be able to reach the level cap primarily through normal gameplay.

The main progression paths are:

```text
Questing
   │
   ├── Experience
   ├── Equipment
   └── Story progression

Dungeons
   │
   ├── Experience
   ├── Equipment
   └── Group progression

Exploration
   │
   ├── Experience
   ├── Discoveries
   └── Lore

Combat
   │
   └── Secondary experience
```

---

# Leveling Curve

The experience curve should be tuned against the level ranges of individual regions.

Completing the intended quest content within a region should naturally bring the player to the appropriate level for the next region.

Players should not be forced to grind simply because they completed all available quests.

The intended progression is:

```text
Region
   ↓
Questlines
   ↓
Level increases
   ↓
New region becomes available
   ↓
New questlines
```

Players who explore more heavily or complete dungeons may progress slightly faster.

The world should still provide suitable content for them without making the main questline obsolete.

---

# Level Milestones

## Level 10 — Specialization

The player chooses one of their class's two specializations.

The specialization's Talent Tree becomes available.

See [0301-Specializations.md](0301-Specializations.md).

---

## Level 15 — First Mount

Players unlock access to their first mount.

See [0901-Mounts.md](../0900-Player-Systems/0901-Mounts.md).

Mount progression should significantly improve world traversal without removing the importance of exploration.

---

## Level 25 — Cross-Continent Travel

Players unlock regular travel between Aurelia and Vethmoor.

This corresponds with the conclusion of Act I of the main story.

See [0207-Main-Story.md](../0200-Lore/0207-Main-Story.md).

The unlocking of cross-continent travel represents a major transition in the player's journey.

---

## Level 50 — Level Cap

Level 50 is the launch level cap.

Reaching level 50 unlocks the full endgame progression system, including:

* Endgame dungeons
* Heroic dungeon difficulty
* Raid content
* Endgame reputation
* High-level equipment
* Advanced Talent Tree builds
* Endgame PvP progression

See [0707-Factions-Reputation.md](../0700-Quests/0707-Factions-Reputation.md).

---

# Level-Up Rewards

Leveling should provide more than an increase to character statistics.

Depending on the level, players may receive:

* Skills
* Talent Points
* Equipment
* Stat increases
* Mount access
* New content
* Quest access
* Dungeon access
* System unlocks

A level-up should always feel like meaningful progression, even when the player does not receive a major new ability.

---

# Level-Up Structure

A simplified progression model:

```text
Level 1
│
├── Class selected
├── Core abilities
└── Basic equipment
│
├── Levels 2–9
│   ├── Core Skills
│   ├── Utility Skills
│   └── Class mechanics
│
Level 10
│
├── Specialization
├── Specialization Skills
└── Talent Tree
│
├── Levels 11–14
│   ├── Talents
│   └── Advanced skills
│
Level 15
│
└── Mount
│
├── Levels 16–24
│   ├── Talents
│   ├── Equipment
│   └── New content
│
Level 25
│
└── Cross-continent travel
│
├── Levels 26–49
│   ├── Advanced talents
│   ├── Specialization mechanics
│   ├── Endgame preparation
│   └── Equipment progression
│
Level 50
│
└── Endgame
```

---

# Level Scaling

Character statistics and skill effectiveness scale with level.

The scaling system should remain compatible with the formulas defined in [0304-Stats.md](0304-Stats.md).

Equipment should also scale appropriately so that newly acquired gear remains relevant throughout the leveling experience.

---

# Level Sync

Future systems may allow players to temporarily scale down to the level of lower-level content.

This could allow:

* Friends to quest together
* Older dungeons to remain useful
* Previous regions to remain populated
* Players to revisit earlier content without completely overwhelming it

Level Sync should preserve appropriate rewards while preventing it from becoming an unintended optimal leveling method.

The final system will be documented separately if implemented.

---

# Death and Leveling

Death should not remove earned experience or levels.

Players retain their progression after death.

Any death penalties should instead be handled through the combat and durability systems.

---

# Expansion Progression

Future expansions may increase the level cap.

Each expansion should document:

* New maximum level
* New leveling zones
* New progression systems
* New equipment tiers
* New class progression
* New Talent Tree interactions

The launch level cap of 50 should remain the baseline for the original Elysium experience.

Future expansions are documented separately, beginning with [1500-Expansion-01.md](../1500-Expansions/1500-Expansion-01.md).

---

# Design Rules

1. The launch level cap is 50.
2. Early levels focus on teaching the class.
3. Level 10 unlocks specialization.
4. Level 10 also begins Talent Tree progression.
5. Skills should unlock frequently during the early game.
6. Skill unlock frequency should decrease later in progression.
7. Questing is the primary leveling path.
8. Dungeons and exploration provide meaningful alternatives.
9. Enemy grinding should never be required for normal progression.
10. Regional content should naturally provide enough experience for progression.
11. Level milestones should unlock meaningful systems.
12. Leveling should introduce systems gradually rather than overwhelming new players.
13. Reaching level 50 should transition naturally into endgame progression.
14. Future expansions may increase the level cap.
15. Leveling balance should be tested against all major progression paths.
