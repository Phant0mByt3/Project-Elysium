# 0513 — Transmog System

**Project:** Elysium MMORPG  
**Category:** Items  
**Status:** Design Complete — Implementation Pending  
**Related:** [0501-Armour.md](0501-Armour.md) · [0903-Cosmetics.md](../0900-Player-Systems/0903-Cosmetics.md) · [0311-Character-Customisation.md](../0300-Characters/0311-Character-Customisation.md) · [1300-Art-Style.md](../1300-Art/1300-Art-Style.md)

---

## 1. Overview

Transmog (transmogrification) lets players separate an item’s appearance from its stats. Once a player has collected or unlocked an appearance, they may apply it to compatible gear of the same slot and armour type.

---

## 2. Core Rules

- Appearances are unlocked account-wide or character-wide (decision to be finalised; default leaning account-wide for collection satisfaction).
- Only appearances the player has actually obtained can be applied.
- Armour type restrictions remain (cloth cannot look like plate, etc.) to preserve class silhouette readability.
- Weapons have type restrictions (swords onto swords, staves onto staves, etc.) with limited exceptions for fantasy reasons.
- Transmog is purely cosmetic; it never changes stats, set bonuses, or item level.

---

## 3. Design Goals

- Let players express identity without sacrificing power.
- Make collecting gear feel rewarding even after the stats are obsolete.
- Keep combat readability intact — silhouette and major colour language should still communicate role and class at a glance.

---

## 4. UI & Cost

A dedicated Transmog interface (accessible from major cities or the character sheet) shows unlocked appearances and currently applied looks. Applying a transmog may cost a small amount of Aurum as a light sink.

---

## 5. Technical Notes

Appearance unlocks are stored on the account or character record. The client renders the chosen model and textures; the server only validates that the appearance is owned and legal for the slot.


---

## 6. Faction and Regional Appearances

Certain appearances are tied to faction reputation or regional achievements rather than raw drop chance, giving the Dawnbound Concord and Duskward Pact each a recognizable visual identity players can collect toward deliberately.

## 7. Collection Progress Tracking

The Collections UI ([0907-Collections.md](../0900-Player-Systems/0907-Collections.md)) tracks overall transmog completion percentage, giving completionist players a long-term account-wide goal independent of current character power.
