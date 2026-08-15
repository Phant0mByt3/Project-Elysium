# 1115 — Character Select

**Project:** Elysium MMORPG  
**Category:** Client  
**Status:** Design Complete — Implementation Pending  
**Related:** [0310-Character-Creation.md](../0300-Characters/0310-Character-Creation.md) · [1114-Main-Menu.md](1114-Main-Menu.md) · [1204-Authentication.md](../1200-Technical/1204-Authentication.md) · [1301-UI-Style.md](../1300-Art/1301-UI-Style.md)

---

## 1. Overview

Character Select displays the player’s existing characters and provides entry into character creation or the game world. It is the last screen before the player is fully in-world.

---

## 2. Features

- List or carousel of characters with name, level, class, race, and location
- 3D or illustrated preview of the selected character
- Create new character
- Delete character (with confirmation)
- Enter world / Play
- Account and realm/server information as needed

---

## 3. Design Rules

1. Character identity (appearance, class fantasy) should be immediately readable.
2. Creation and deletion flows are clear and protected against accidents.
3. The screen respects the same art and UI language as the rest of the client.
4. Performance remains solid even with the maximum number of characters displayed.


---

## Additional Detail: Character Preview

Each character slot displays a fully rendered, idle-animated preview of the character in their current gear, letting players confirm which character they're selecting at a glance rather than relying on text labels alone.

## Character Slot Expansion

Base account character slots are generous enough to support one character per class for players who want to try every class, with additional slot purchases available for players who want further alts beyond that baseline.
