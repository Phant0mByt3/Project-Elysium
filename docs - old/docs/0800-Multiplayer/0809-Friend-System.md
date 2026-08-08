# 0809 — Friend System

**Project:** Elysium MMORPG  
**Category:** Multiplayer  
**Status:** Design Complete — Implementation Pending  
**Related:** [0810-Social-Features.md](0810-Social-Features.md) · [0801-Parties.md](0801-Parties.md) · [0800-Guilds.md](0800-Guilds.md) · [1100-Client/](../1100-Client/)

---

## 1. Overview

The Friend System lets players maintain a persistent list of other players they want to stay connected with across sessions and characters. It is a foundational social layer for parties, guilds, and informal play.

---

## 2. Core Features

- Send / accept / decline friend requests
- Friend list with online status, current character, and location (where privacy settings allow)
- Notes and optional nicknames
- Quick invite to party or whisper
- Cross-character visibility on the same account (friends see the account’s online presence, not every alt by default)

---

## 3. Design Rules

1. Privacy controls are clear: players can limit who sees their location or online status.
2. Friend lists have a generous but finite cap to prevent abuse and performance issues.
3. Blocking and reporting tools are immediately available from the same social UI.
4. The system works across the proxy and instance architecture so friends remain visible regardless of which continent or instance they are in.

---

## 4. Technical Notes

Friend relationships are stored at the account level. Presence and location updates are published through the synchronisation and social services so that the client always has a consistent view.
