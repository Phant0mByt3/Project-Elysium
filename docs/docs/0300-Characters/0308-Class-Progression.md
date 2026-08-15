# 0308 — Class Progression

**Project:** Elysium MMORPG
**Category:** Characters
**Status:** Design Complete — Implementation Pending
**Related Systems:** 0300-Classes.md · 0301-Specializations.md · 0302-Skills.md · 0303-Talent-Trees.md · 0304-Stats.md · 0305-Leveling.md · 0309-Balance.md · ../0400-Gameplay/0400-Game-Mechanics.md · ../0400-Gameplay/0401-Combat.md

---

## 1. Overview

Class Progression defines how a character develops from their first level into a complete endgame build.

The system connects:

* Class selection
* Skill unlocks
* Specialisation
* Talent Trees
* Stat progression
* Class resources
* Endgame abilities

The goal is to introduce a class's identity quickly while giving players increasingly more control over how they build it.

Elysium does not use a separate class tier system at launch. A character chooses one of the eight base classes at character creation and develops that class through skills, specialisation, and talents.

---

# 2. Progression Structure

Class progression has three major stages.

```text
LEVEL 1–9
Foundation
    │
    ├── Core abilities
    ├── Class resource
    ├── Basic passives
    └── Class movement ability
            │
            ▼
LEVEL 10
Specialisation
    │
    ├── Choose one of two specialisations
    ├── Unlock specialisation abilities
    └── Unlock full Talent Tree
            │
            ▼
LEVEL 10–49
Development
    │
    ├── Skill progression
    ├── Talent choices
    ├── Stat growth
    └── Build specialisation
            │
            ▼
LEVEL 50
Mastery
    │
    ├── Signature ability
    ├── Endgame builds
    ├── Heroic dungeons
    ├── Raids
    └── Advanced talent investment
```

The system is intentionally straightforward during the early game and increasingly customizable as the player approaches the level cap.

---

# 3. Base Classes

Players choose one base class during character creation.

| Class           | Primary Identity                        | Role(s)         |
| --------------- | --------------------------------------- | --------------- |
| **Warrior**     | Weapon mastery and frontline combat     | Tank / Damage   |
| **Paladin**     | Holy protection and martial combat      | Tank / Healer   |
| **Rogue**       | Stealth, precision, and deception       | Damage          |
| **Ranger**      | Ranged combat, mobility, and companions | Damage          |
| **Mage**        | Arcane and elemental spellcasting       | Damage          |
| **Necromancer** | Death magic and summoned forces         | Damage          |
| **Cleric**      | Divine healing and battlefield support  | Healer          |
| **Druid**       | Nature magic and shapeshifting          | Healer / Damage |

Class choice is permanent for the character.

Race does not restrict class selection. Any playable race can choose any class, as defined in [0204-Races.md](../0200-Lore/0204-Races.md).

---

# 4. Levels 1–9 — Class Foundation

The first nine levels introduce the player's class without overwhelming them with build decisions.

The player receives a fixed sequence of core abilities.

| Level  | Progression                                   |
| ------ | --------------------------------------------- |
| **1**  | Class selected, starting weapon, basic attack |
| **2**  | First active ability                          |
| **3**  | First passive ability                         |
| **4**  | Second active ability                         |
| **5**  | First talent point earned                     |
| **6**  | Third active ability                          |
| **7**  | Full class resource system unlocked           |
| **8**  | Fourth active ability                         |
| **9**  | Class movement or mobility ability            |
| **10** | Specialisation and Talent Tree unlocked       |

The exact ability differs by class.

For example, a Mage may receive an elemental projectile early, while a Rogue may receive a stealth or positioning ability.

The goal is that a player can understand the basic fantasy of their class before reaching level 10.

---

# 5. Level 10 — Specialisation

At level 10, the player chooses one of two specialisations.

Specialisations determine the character's primary playstyle and significantly modify their Talent Tree.

| Class       | Specialisation A | Specialisation B |
| ----------- | ---------------- | ---------------- |
| Warrior     | Vanguard         | Berserker        |
| Paladin     | Sentinel         | Lightbringer     |
| Rogue       | Shadowblade      | Trickster        |
| Ranger      | Marksman         | Beastmaster      |
| Mage        | Frostweaver      | Pyromancer       |
| Necromancer | Reaper           | Plaguebringer    |
| Cleric      | Warden           | Zealot           |
| Druid       | Wildshaper       | Grovekeeper      |

See [0301-Specializations.md](0301-Specializations.md) for the complete specialisation design.

Specialisation selection unlocks:

* Specialisation abilities
* Specialisation passives
* Specialisation Talent Tree
* Specialisation Mastery effects
* New visual and mechanical class identity

Specialisation can be changed outside combat.

---

# 6. Skills

Skills are the active and passive abilities used by the player.

See [0302-Skills.md](0302-Skills.md).

Skills are divided into four categories:

### Core Skills

Available to every player of the class.

These establish the basic combat rotation.

### Specialisation Skills

Unlocked after choosing a specialisation.

These provide the majority of a specialisation's unique gameplay.

### Utility Skills

Movement, crowd control, defensive abilities, buffs, and other non-damage tools.

### Ultimate Skills

Powerful abilities with long cooldowns.

Each specialisation receives an ultimate ability as part of its endgame progression.

---

# 7. Skill Progression

Core skills are unlocked primarily through character level.

Players should receive new abilities regularly during the early leveling experience.

After level 10, new abilities become less frequent and Talent Trees become increasingly important.

Skill progression follows three principles:

1. Core abilities arrive automatically.
2. Specialisation abilities arrive after level 10.
3. Talent choices modify and expand existing abilities.

This prevents the player from needing to manually purchase every basic ability just to make their class functional.

---

# 8. Talent Progression

Talent Trees are the primary build customization system.

See [0303-Talent-Trees.md](0303-Talent-Trees.md).

Each specialisation has one Talent Tree containing three major paths.

```text
                 Specialisation
                       │
              ┌────────┼────────┐
              │        │        │
           Path A   Path B   Path C
              │        │        │
           Talents   Talents   Talents
              │        │        │
              └────────┼────────┘
                       │
                   Capstones
```

Players can invest in different paths to create different versions of the same specialisation.

For example, two Berserker Warriors could focus on:

* sustained damage
* burst damage
* self-sustain

Neither build is intended to be universally superior.

---

# 9. Talent Point Progression

Talent Points become available from level 10 onward.

They are primarily used to unlock nodes within the player's specialisation tree.

Talent progression should provide meaningful decisions rather than simply increasing every damage number.

Talent nodes may provide:

* New abilities
* Ability modifications
* Passive bonuses
* Resource changes
* Defensive effects
* Mobility improvements
* Utility effects
* Changes to existing rotations

Capstone talents should significantly change the player's build.

---

# 10. Stat Progression

Character stats increase naturally with level.

See [0304-Stats.md](0304-Stats.md).

Primary stats are:

* Strength
* Intellect
* Agility
* Stamina

Secondary stats include:

* Critical Strike Chance
* Haste
* Mastery
* Versatility
* Armor
* Resistance

Gear becomes increasingly important as players approach level 50.

Class progression should not depend on a specific item set.

A player's class remains functional regardless of their equipment, while better equipment improves performance.

---

# 11. Class Resources

Each class has a resource system that supports its combat identity.

Examples may include:

| Class       | Resource Concept      |
| ----------- | --------------------- |
| Warrior     | Rage                  |
| Paladin     | Holy Power            |
| Rogue       | Combo Points / Energy |
| Ranger      | Focus                 |
| Mage        | Mana                  |
| Necromancer | Essence               |
| Cleric      | Faith                 |
| Druid       | Nature / Spirit       |

The exact resource mechanics are documented within the combat system and individual class designs.

Resources should reinforce class identity rather than exist purely as another bar to manage.

---

# 12. Class Milestones

Certain levels provide major progression moments.

| Level  | Milestone                                        |
| ------ | ------------------------------------------------ |
| **1**  | Class selection and starting abilities           |
| **5**  | First talent point earned                        |
| **10** | Specialisation and Talent Tree unlocked          |
| **15** | First mount                                      |
| **25** | Cross-continent travel unlocked                  |
| **30** | Major talent progression milestone               |
| **40** | Advanced specialization talents become available |
| **50** | Level cap and endgame class progression          |

These milestones align with the broader character progression system defined in [0305-Leveling.md](0305-Leveling.md).

---

# 13. Level 50 — Endgame Class Progression

Level 50 is the launch level cap.

Reaching level 50 does not mean that class development stops.

Instead, progression shifts from basic character advancement toward build optimization.

Endgame class development comes primarily from:

* Talent optimization
* Gear
* Legendary items
* Relics
* Specialisation mastery
* High-level content rewards

Players should gain new ways to refine their build without simply receiving unlimited raw statistical power.

---

# 14. Signature Abilities

Every specialisation receives a signature ability associated with its identity.

Signature abilities are powerful abilities designed to define the specialisation at endgame.

Examples:

### Vanguard Warrior

A defensive ability that converts successful blocks into a temporary offensive counterattack.

### Pyromancer Mage

A high-impact fire ability that rewards maintaining Burning effects on multiple enemies.

### Grovekeeper Druid

A powerful healing ability that creates a temporary area of living nature around the caster.

The final abilities and names are documented in the relevant class and specialisation files.

---

# 15. Specialisation Mastery

At high levels, players gain access to Mastery progression tied to their chosen specialisation.

Mastery should strengthen the defining mechanic of a specialisation rather than simply increase every statistic.

Examples:

* Vanguard Mastery improves defensive resource generation.
* Berserker Mastery improves Rage-based damage windows.
* Frostweaver Mastery improves control and Frozen interactions.
* Beastmaster Mastery improves companion coordination.
* Grovekeeper Mastery improves healing through Nature effects.

Mastery effects are subject to the balance rules in [0309-Balance.md](0309-Balance.md).

---

# 16. Respecialisation

Players should be encouraged to experiment with their builds.

Players can change:

* Talent allocations
* Talent paths
* Specialisation

outside combat.

Respecialisation should have a modest Aurum cost where appropriate, as defined in [0303-Talent-Trees.md](0303-Talent-Trees.md).

Changing a specialisation should not reset:

* Character level
* Gear
* Quest progress
* Reputation
* Achievements
* Mounts
* Cosmetics

Only class-specific build choices are affected.

---

# 17. Class Identity

Class progression should preserve a strong distinction between the eight classes.

A player should be able to identify a class through:

* Weapon choice
* Ability effects
* Animation
* Resource system
* Combat rhythm
* Armor style
* Specialisation
* Talent choices

Two classes may share a role without feeling interchangeable.

For example, a Paladin and Cleric can both provide healing, but they should approach healing differently.

The Paladin should combine healing with frontline protection and holy combat.

The Cleric should focus more heavily on direct restoration, support, and divine spellcasting.

---

# 18. Progression Philosophy

Elysium follows several core progression rules.

### Early Identity

Players should understand their class within the first few levels.

### Meaningful Choices

Major build decisions begin after level 10.

### No Dead Levels

Every level should provide meaningful progression, whether through abilities, talents, stats, gear, quests, or other character systems.

### No Mandatory Builds

No single talent path should be required to play a class effectively.

### Horizontal Endgame

Once players reach level 50, progression should focus increasingly on build refinement rather than endless level increases.

### Expansion Compatibility

Future expansions can raise the level cap and add new class content without invalidating existing classes or specialisations.

---

# 19. Relationship With Other Systems

Class Progression connects the following systems:

```text
0300 Classes
      │
      ▼
0305 Leveling
      │
      ├──────────────┐
      ▼              ▼
0302 Skills      0301 Specialisations
      │              │
      └──────┬───────┘
             ▼
       0303 Talent Trees
             │
             ▼
          0304 Stats
             │
             ▼
       0309 Balance
```

Each document has a separate responsibility:

* **0300 Classes** — defines the eight base classes.
* **0301 Specialisations** — defines the two specialisations for each class.
* **0302 Skills** — defines class abilities.
* **0303 Talent Trees** — defines build customization.
* **0304 Stats** — defines character statistics.
* **0305 Leveling** — defines character level progression.
* **0308 Class Progression** — connects these systems together.
* **0309 Balance** — ensures the systems remain balanced.

---

# 20. Expansion Compatibility

Future expansions may introduce:

* Additional specialisations
* New talent branches
* New class abilities
* New signature abilities
* New mastery options
* Additional endgame systems

New systems should extend the existing class structure instead of replacing it without a strong design reason.

Existing classes should remain recognizable even after multiple expansions.

A future expansion may also introduce entirely new classes if the lore and gameplay justify them.

New classes must receive their own entries in:

* 0300-Classes.md
* 0301-Specializations.md
* 0302-Skills.md
* 0303-Talent-Trees.md
* 0308-Class-Progression.md

---

# 21. System Rules Summary

1. Players choose one of eight base classes at character creation.
2. Race does not restrict class selection.
3. Core class abilities unlock automatically through leveling.
4. Specialisation becomes available at level 10.
5. Each class has two specialisations.
6. Each specialisation has its own Talent Tree.
7. Talent Trees provide the primary source of build customization.
8. Players can respecialise outside combat.
9. Level 50 is the launch level cap.
10. Endgame progression focuses on build refinement rather than unlimited vertical power.
11. Class resources should reinforce class identity.
12. Every class must remain viable for its intended role.
13. No specialisation should be a mandatory choice.
14. Future expansions should extend existing progression rather than invalidate it.
15. Class progression must remain consistent with 0300–0309 as those documents are updated.

---

## 22. Open Design Questions

The following systems remain subject to further class-design passes:

* Exact resource mechanics for each class.
* Exact skill unlock levels after level 10.
* Signature ability designs.
* Specialisation Mastery implementation.
* Talent Tree capstone structure.
* Legendary item interactions with class abilities.
* Whether future expansions should add new specialisations or new classes.
* Exact endgame progression beyond level 50.
