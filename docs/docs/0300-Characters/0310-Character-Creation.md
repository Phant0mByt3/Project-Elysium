# 0310 — Character Creation

**Project:** Elysium MMORPG
**Category:** Characters
**Status:** Design Complete — Implementation Pending
**Related:** 0300-Classes.md · [0204-Races.md](../0200-Lore/0204-Races.md) · [0203-Factions.md](../0200-Lore/0203-Factions.md) · 0311-Character-Customisation.md · [1100-Launcher.md](../1100-Client/1100-Launcher.md)

---

## 1. Overview

Character creation is the player's first direct interaction with Elysium.

The system should establish the character's identity, cultural background, faction allegiance, and combat role without overwhelming the player with systems that are not yet relevant.

Character creation is intentionally simple:

**Race → Faction → Class → Appearance → Name → Confirmation**

Race establishes the character's cultural identity. Faction establishes their political and ideological allegiance. Class establishes their combat identity.

These choices are presented separately so that players are not forced into predetermined race/class/faction combinations.

---

# 2. Creation Flow

## 2.1 Race Selection

The player first selects their race.

Launch playable races are:

* Human
* High Elf
* Dwarf
* Orc
* Beastkin
* Revenant

Each race selection displays:

* Race name.
* Short lore description.
* Cultural background.
* Common regions of origin.
* Racial passive traits.
* Typical faction alignment.
* Available appearance options.

Race affects:

* Character appearance.
* Starting racial passive traits.
* Cultural dialogue.
* Some NPC reactions.
* Starting location or introduction where appropriate.

Race does not restrict class selection.

A player should be able to create combinations such as:

* Orc Mage.
* Dwarf Rogue.
* High Elf Warrior.
* Human Necromancer.
* Revenant Paladin.
* Beastkin Cleric.

Racial faction tendencies are defaults rather than restrictions.

---

## 2.2 Faction Selection

After choosing a race, the player chooses their faction.

Faction is an ideological and political decision rather than a racial requirement.

The character may join any faction available during character creation regardless of their race.

Faction selection affects:

* Starting narrative framing.
* Faction reputation.
* Political relationships.
* Faction-specific dialogue.
* Certain quests.
* PvP allegiance where applicable.
* Access to faction-specific activities and locations.

Faction selection should never prevent a player from choosing a class.

The character's race and faction can therefore represent different perspectives within Elysium.

For example, an Orc character may reject the traditional politics of their people and join a rival faction.

This is intentional.

---

## 2.3 Class Selection

The player then chooses their base class.

The launch classes are:

| Class       | Primary Identity                 |
| ----------- | -------------------------------- |
| Warrior     | Frontline weapon specialist      |
| Paladin     | Holy warrior and protector       |
| Rogue       | Stealth and precision combatant  |
| Ranger      | Ranged and wilderness combatant  |
| Mage        | Arcane and elemental spellcaster |
| Necromancer | Death magic and summoned minions |
| Cleric      | Dedicated healer and holy caster |
| Druid       | Nature magic and shapeshifting   |

Each class selection displays:

* Class fantasy.
* Primary combat role.
* Available roles.
* Core resources.
* Starting abilities.
* Combat difficulty.
* Specialisations available later.

Specialisation is not selected during character creation.

Players begin as their base class and later choose a specialisation as part of class progression.

See:

* [0300-Classes.md](0300-Classes.md)
* [0301-Specializations.md](0301-Specializations.md)
* [0308-Class-Progression.md](0308-Class-Progression.md)

---

# 3. Appearance

After selecting race, faction, and class, the player customises their character.

Appearance options are defined in:

[0311-Character-Customisation.md](0311-Character-Customisation.md)

Customisation may include:

* Face.
* Skin or complexion.
* Hair.
* Hair colour.
* Eyes.
* Facial features.
* Body features.
* Markings.
* Scars.
* Racial features.
* Starting outfit appearance.

Appearance options are restricted where necessary by race.

Starting equipment should visually communicate the chosen class while remaining culturally appropriate for the character's race.

---

# 4. Name

The player chooses a character name.

Names are validated server-side.

Validation includes:

* Minimum and maximum length.
* Character restrictions.
* Forbidden terms.
* Duplicate-name rules.
* Reserved names.
* Exploit prevention.

Players do not select titles during character creation.

Titles are earned through gameplay.

Names should not be required to follow strict racial naming conventions, but NPCs and lore should still establish recognisable naming traditions for each culture.

---

# 5. Character Preview

The creation screen should provide a full character preview.

The preview updates immediately when the player changes:

* Race.
* Appearance.
* Class.
* Starting equipment.
* Faction.

Faction selection may alter the displayed starting equipment or visual presentation without changing the player's race or class.

The player should be able to rotate and inspect the character before confirming creation.

---

# 6. Character Summary

Before final confirmation, the player receives a complete summary.

Example:

```text
─────────────────────────────────
          CHARACTER
─────────────────────────────────

Name:
Aren Valen

Race:
Human

Faction:
[Selected Faction]

Class:
Mage

Starting Region:
Aurelia

─────────────────────────────────

Your character cannot change race
after creation.

Faction and class changes follow
the rules defined by their respective
systems.
─────────────────────────────────

        [ Back ]     [ Create ]
─────────────────────────────────
```

The summary exists to prevent accidental creation with an incorrect race, faction, class, or appearance.

---

# 7. Confirmation

Character creation is only committed after the player confirms.

Before confirmation, all selected values remain local to the creation interface.

After confirmation:

1. The client sends the character creation payload.
2. The server validates the payload.
3. The server verifies that the selected race, faction, and class are valid.
4. The character is created in the account database.
5. Starting equipment and abilities are assigned.
6. The character is placed into the appropriate starting experience.
7. The player enters the game.

Invalid or interrupted creation attempts do not create partial characters.

---

# 8. Starting Experience

The starting experience is determined primarily by faction and race.

The opening should introduce the player to:

* Their chosen faction.
* Their race and culture.
* Basic combat.
* Class abilities.
* The local region.
* The current state of Elysium.
* The wider conflict surrounding the player.

The tutorial should not attempt to explain the entire history of Elysium.

Major lore concepts such as the Sundering, the gods, ancient civilisations, and the Archivarium should be introduced gradually through gameplay.

---

# 9. Race, Faction, and Class Independence

Elysium deliberately separates the three major identity choices.

```text
                CHARACTER
                    │
        ┌───────────┼───────────┐
        │           │           │
      RACE       FACTION      CLASS
        │           │           │
    Culture     Allegiance    Combat
        │           │           │
        └───────────┼───────────┘
                    │
              CHARACTER IDENTITY
```

Race answers:

> Where does my character come from?

Faction answers:

> What does my character believe or support?

Class answers:

> How does my character fight?

These systems should not unnecessarily dictate one another.

A player's character should be able to tell a unique story through the combination of these choices.

---

# 10. Permanent and Changeable Choices

Character creation establishes several long-term choices.

| Choice         | Change After Creation                          |
| -------------- | ---------------------------------------------- |
| Race           | No                                             |
| Appearance     | Yes, through applicable customisation systems  |
| Name           | Yes, through applicable name-change systems    |
| Faction        | Subject to faction-change rules                |
| Class          | No                                             |
| Specialisation | Yes                                            |
| Talents        | Yes                                            |
| Skills         | Yes, where supported by the progression system |

Race and base class define the permanent foundation of the character.

Specialisation, talents, and skills provide the majority of build flexibility later.

See [0308-Class-Progression.md](0308-Class-Progression.md).

---

# 11. Technical Requirements

Character creation should be primarily client-driven until final confirmation.

The client may temporarily store:

```text
race
faction
class
appearance
name
```

The server remains authoritative.

The server must validate:

* Race availability.
* Faction availability.
* Class availability.
* Name validity.
* Appearance options.
* Starting equipment.
* Starting abilities.
* Character limits.
* Account permissions.

The client must never be trusted to grant invalid abilities, items, currencies, or progression.

---

# 12. Rejoining Character Creation

If the player exits character creation before confirmation, no character is created.

The incomplete state may be discarded.

The player can start again when returning to the character creation screen.

No database character record should exist until final confirmation succeeds.

---

# 13. Design Rules

1. Race, faction, and class must remain separate choices.
2. Race must never restrict class selection.
3. Faction must never restrict class selection.
4. Specialisation is selected later through class progression.
5. Character creation should not require knowledge of advanced game systems.
6. The UI should explain important choices without overwhelming the player.
7. The server must validate every creation parameter.
8. No partially created characters should exist in the main character database.
9. The starting experience should introduce the player's identity before introducing larger world conflicts.
10. Character creation should establish the player's place in Elysium without determining their entire story.

---

# 14. Future Expansion Compatibility

New races can be added without changing the existing creation flow.

New factions can be added through the faction-selection stage.

New classes can be added through the class-selection stage.

Expansion-specific starting experiences can be added without changing the fundamental creation pipeline.

The character creation system should therefore treat race, faction, class, and starting experience as data-driven systems rather than hardcoded combinations.

This allows future content to introduce new cultures, factions, classes, and continents without requiring a complete rewrite of character creation.
