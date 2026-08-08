# 0311 — Character Customisation

**Project:** Elysium MMORPG  
**Category:** Characters  
**Status:** Design Complete — Implementation Pending  
**Related:** [0310-Character-Creation.md](0310-Character-Creation.md) · [0204-Races.md](../0200-Lore/0204-Races.md) · [0903-Cosmetics.md](../0900-Player-Systems/0903-Cosmetics.md) · [1306-Models.md](../1300-Art/1306-Models.md)

---

## 1. Overview

Character customisation lets players express identity within the visual language of their chosen race while remaining readable in combat and group content. Customisation is split into **Creation-time** options and **Ongoing** cosmetic options (the latter covered primarily in [0903-Cosmetics.md](../0900-Player-Systems/0903-Cosmetics.md)).

---

## 2. Creation-Time Options

| Category | Scope | Notes |
|----------|-------|-------|
| Body type / proportions | Limited presets per race | Maintains silhouette readability |
| Face shape, eyes, brows, mouth | High detail | Racial feature limits enforced |
| Skin / scale / fur tone | Race-appropriate ranges | Revenants have a cooler, desaturated palette |
| Hair style & colour | Extensive | Some styles race-locked for cultural consistency |
| Facial hair / markings | Race-dependent | Dwarves, orcs, and beastkin have richer options |
| Starting outfit colour accents | Limited | Full transmog comes later |

---

## 3. Design Principles

- **Silhouette first** — a player should be identifiable as their class/role at a distance even after heavy cosmetic customisation.
- **Racial identity preserved** — customisation never lets a human look like a high elf or an orc look like a dwarf.
- **Performance** — all customisation uses shared base meshes and texture atlases where possible ([1306-Models.md](../1300-Art/1306-Models.md)).
- **Future-proof** — new hairstyles, markings, and body options can be added via the content pack without requiring a full character re-creation.

---

## 4. Ongoing Customisation

After creation, further visual change comes through:

- Transmog / appearance system ([0513-Transmog-System.md](../0500-Items/0513-Transmog-System.md))
- Cosmetic unlocks (pets, mounts, cloaks, etc.)
- Barber / appearance-change NPCs in major cities (modest Aurum cost)

---

## 5. Technical Notes

Appearance data is stored as a compact set of indices and colour values on the character record. Client-side rendering pulls the correct models and textures from the content pack. Server never needs the full visual mesh data.
