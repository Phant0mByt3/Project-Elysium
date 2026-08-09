# 0812 — Voice Communication

**Project:** Elysium MMORPG  
**Category:** Multiplayer  
**Status:** Design Complete — Implementation Pending  
**Related:** [0801-Parties.md](0801-Parties.md) · [0800-Guilds.md](0800-Guilds.md) · [0810-Social-Features.md](0810-Social-Features.md) · [1106-Accessibility.md](../1100-Client/1106-Accessibility.md)

---

## 1. Overview

Voice communication is supported for parties, raids, and guilds so that coordinated content (especially Heroic/Mythic dungeons and raids) can be played without requiring external software. It is optional and never mandatory for casual play.

---

## 2. Scope

- Party and Raid voice channels
- Guild voice channels (with possible officer / community sub-channels)
- Push-to-talk and voice-activation options
- Basic volume and mute controls per player
- Integration with the existing social and group UI

---

## 3. Design Rules

1. Voice is a convenience and coordination tool, not a gate for content access.
2. Privacy and consent matter: players can fully disable voice or restrict who can hear/speak.
3. Accessibility options (text-to-speech / speech-to-text where feasible, clear mute indicators) are considered from the start.
4. Performance and bandwidth impact are budgeted so that voice does not degrade combat experience on minimum-spec hardware.

---

## 4. Technical Notes

Voice is handled by a dedicated service or integrated provider, with authentication tied to the Elysium account and current group membership. The game client only manages channel membership and UI; media routing is offloaded appropriately.
