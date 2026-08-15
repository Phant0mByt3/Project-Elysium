# 0311 — Character Customisation

**Project:** Elysium MMORPG
**Category:** Characters
**Status:** Design Complete — Implementation Pending
**Related:** 0310-Character-Creation.md · [0204-Races.md](../0200-Lore/0204-Races.md) · [0903-Cosmetics.md](../0900-Player-Systems/0903-Cosmetics.md) · [1306-Models.md](../1300-Art/1306-Models.md)

---

## 1. Overview

Character customisation allows players to create a character that feels visually distinct while remaining recognisable as their chosen race and class.

Customisation is divided into two systems:

* **Creation Customisation** — appearance options selected during character creation.
* **Ongoing Customisation** — appearance changes and cosmetic items unlocked after creation.

The system is designed around three priorities:

1. Preserve racial identity.
2. Keep characters readable during gameplay.
3. Give players enough visual freedom to make their character feel personal.

Character customisation affects appearance only. It does not change combat statistics, class abilities, racial traits, or faction allegiance.

---

# 2. Creation-Time Customisation

Character creation provides the player's initial appearance.

Available options depend on the selected race.

| Category                | Scope                    | Notes                                                   |
| ----------------------- | ------------------------ | ------------------------------------------------------- |
| Body type / proportions | Limited presets per race | Preserves racial and gameplay silhouettes               |
| Face shape              | Extensive                | Race-specific facial structure                          |
| Eyes                    | Extensive                | Shape, size, colour, and related features               |
| Brows                   | Extensive                | Race-appropriate styles                                 |
| Mouth / jaw             | Extensive                | Subject to racial anatomy                               |
| Skin / scale / fur      | Race-specific            | Colour ranges appropriate to each race                  |
| Hair                    | Extensive                | Styles and colours vary by race                         |
| Facial hair             | Race-dependent           | Expanded options for races where culturally appropriate |
| Markings                | Race-dependent           | Scars, tattoos, paint, and cultural markings            |
| Racial features         | Race-specific            | Ears, horns, tusks, fur patterns, etc.                  |
| Starting outfit         | Class-dependent          | Colour accents may be customised within limits          |

---

# 3. Racial Identity

Race establishes the fundamental physical characteristics of a character.

Customisation cannot remove or replace defining racial features.

Examples:

* Humans retain human anatomy.
* High Elves retain their distinctive elven features.
* Dwarves retain their characteristic build and facial structure.
* Orcs retain their tusks and racial proportions.
* Beastkin retain their animalistic features.
* Revenants retain the visual signs associated with their altered state.

Players have significant freedom within those boundaries.

The goal is not to make every member of a race look identical. The goal is to make different characters recognisable as members of the same people.

---

# 4. Class Readability

Character customisation must not interfere with class readability.

A Warrior, Paladin, Rogue, Ranger, Mage, Necromancer, Cleric, or Druid should remain visually understandable during normal gameplay.

This is primarily achieved through:

* Armour silhouettes.
* Weapons.
* Class effects.
* Ability visuals.
* Equipment shapes.
* Animation sets.

Customisation should complement these systems rather than overpower them.

A player wearing unusual cosmetics should still be recognisable in combat.

---

# 5. Faction Expression

Faction identity can be expressed visually through:

* Starting equipment.
* Colour accents.
* Faction insignia.
* Cosmetic armour.
* Cloaks.
* Banners.
* Mount cosmetics.
* Titles.

Faction cosmetics should communicate allegiance without permanently altering the character's underlying appearance.

A character's race and faction remain separate concepts.

For example, two Orc characters may belong to opposing factions while retaining the same underlying racial appearance.

---

# 6. Appearance Categories

## 6.1 Face

Face customisation includes:

* Face shape.
* Jaw shape.
* Cheek structure.
* Nose.
* Eyes.
* Eyebrows.
* Mouth.
* Ears where applicable.

Facial sliders should have controlled limits rather than allowing extreme deformation.

This keeps character models visually consistent and reduces animation and clipping problems.

---

## 6.2 Hair

Hair includes:

* Hairstyles.
* Hair length.
* Hair colour.
* Facial hair where applicable.

Certain hairstyles may be culturally associated with particular races or factions.

Race-locked styles are allowed when they reinforce cultural identity.

New hairstyles can be added through future content updates.

---

## 6.3 Skin, Fur, and Markings

Players can select appropriate colour variations for their race.

Possible options include:

* Skin tone.
* Fur colour.
* Scale colour.
* Eye colour.
* Tattoos.
* Scars.
* War paint.
* Cultural markings.

Some markings may be unlocked through gameplay rather than being available immediately during character creation.

---

# 7. Racial Features

Certain races possess features that are fundamental to their appearance.

Examples may include:

* High Elf ears.
* Orc tusks.
* Beastkin ears, tails, horns, fur, or other animal characteristics.
* Revenant physical alterations.
* Dwarven facial and body characteristics.

These features can have limited customisation options but cannot be removed entirely.

Racial features should remain visible enough that players can identify a character's race without relying on UI labels.

---

# 8. Starting Equipment Appearance

Starting equipment is partially determined by class.

For example:

* Warriors begin with practical martial equipment.
* Paladins begin with recognisable protective and holy equipment.
* Rogues begin with lightweight equipment.
* Rangers begin with ranged weapons and wilderness equipment.
* Mages begin with robes or light magical equipment.
* Necromancers begin with death-magic themed equipment.
* Clerics begin with religious or restorative equipment.
* Druids begin with natural and ritualistic equipment.

Players may customise limited colour accents during creation.

Full equipment appearance customisation is handled later through the transmog system.

See [0513-Transmog-System.md](../0500-Items/0513-Transmog-System.md).

---

# 9. Ongoing Customisation

Character appearance can continue to evolve after creation.

Players can change or expand their appearance through:

### Barber Services

Available in major settlements.

Possible services include:

* Hairstyle changes.
* Hair colour changes.
* Facial hair changes.
* Marking changes.
* Certain facial appearance changes.

Services normally require a modest Aurum cost.

### Cosmetic Unlocks

Players can acquire cosmetic items through:

* Quests.
* Achievements.
* Events.
* Factions.
* Exploration.
* Dungeons.
* Raids.
* World bosses.
* Seasonal content.
* The Archivarium.
* Other special activities.

Cosmetics may include:

* Outfits.
* Armour appearances.
* Cloaks.
* Mount appearances.
* Pets.
* Accessories.
* Titles.

The broader cosmetic economy is documented in [0903-Cosmetics.md](../0900-Player-Systems/0903-Cosmetics.md).

---

# 10. Character Appearance vs. Equipment

Character customisation and equipment appearance are separate systems.

```text
Character Appearance
        │
        ├── Face
        ├── Hair
        ├── Body
        ├── Skin / Fur
        └── Markings

Equipment Appearance
        │
        ├── Weapons
        ├── Armour
        ├── Cloaks
        └── Accessories

Cosmetics
        │
        ├── Mounts
        ├── Pets
        ├── Outfits
        └── Special Effects
```

This separation allows players to change their equipment appearance without changing their underlying character.

---

# 11. Silhouette and Readability

Silhouette is a core visual requirement.

Character models should remain identifiable in:

* Open-world combat.
* Dungeons.
* Raids.
* PvP.
* Large player gatherings.
* Dark environments.
* Long-distance views.

Customisation should therefore avoid extreme body proportions that interfere with:

* Animation.
* Hitboxes.
* Equipment fitting.
* Character recognition.
* Gameplay readability.

Gameplay hitboxes are never determined by cosmetic body adjustments.

---

# 12. Performance

Character customisation should use shared assets wherever possible.

The system should prefer:

* Shared base meshes.
* Modular body components.
* Texture atlases.
* Reusable hair assets.
* Reusable material instances.
* Level-of-detail models.

This keeps character rendering manageable when many players are visible simultaneously.

See [1306-Models.md](../1300-Art/1306-Models.md).

---

# 13. Data Storage

Character appearance should be stored as compact data rather than as complete model information.

Example:

```text
appearance:
    body_type: 02
    face: 14
    eyes: 07
    eye_colour: 03
    hair: 21
    hair_colour: 08
    markings: 04
    marking_colour: 02
```

The server stores the appearance selections.

The client loads the corresponding assets from the game's content data.

The server does not need to store complete meshes or textures for individual characters.

---

# 14. Server Authority

Appearance data is validated by the server.

The server must verify that:

* The selected appearance exists.
* The appearance is valid for the selected race.
* The player owns any required cosmetic unlock.
* The requested change is permitted.
* The character's appearance data is valid.

The client is responsible for rendering the appearance but cannot grant itself restricted cosmetics.

---

# 15. Future Expansion

The customisation system should support new options without requiring existing characters to be recreated.

Future content may add:

* New hairstyles.
* New markings.
* New facial features.
* New racial variants.
* New cosmetic equipment.
* New faction cosmetics.
* New event cosmetics.
* New expansion-specific appearance options.

Expansion races should define their own customisation rules when introduced.

New appearance assets should be added through content updates while preserving existing appearance IDs so that old characters remain visually valid.

---

# 16. Design Rules

1. Customisation changes appearance, not gameplay statistics.
2. Racial identity must always remain visually recognisable.
3. Class identity must remain readable during combat.
4. Cosmetic body changes must never alter gameplay hitboxes.
5. Character creation provides the initial appearance.
6. Barber and cosmetic systems provide ongoing appearance changes.
7. Equipment appearance is handled separately through transmog.
8. The server remains authoritative over appearance data and cosmetic ownership.
9. Appearance data should remain compact and data-driven.
10. New cosmetic content must not invalidate existing characters.
11. Cosmetic systems should reward exploration, achievements, factions, events, and difficult content without making core progression dependent on them.
12. Appearance customisation should support personal expression without breaking the visual identity of Elysium's races and classes.
