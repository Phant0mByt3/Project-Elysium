# 0810 — Social Features

**Project:** Elysium MMORPG  
**Category:** Multiplayer  
**Status:** Design Complete — Implementation Pending  
**Related:** [0809-Friend-System.md](0809-Friend-System.md) · [0800-Guilds.md](0800-Guilds.md) · [0801-Parties.md](0801-Parties.md) · [0904-Emotes.md](../0900-Player-Systems/0904-Emotes.md)

---

## 1. Overview

Social Features cover the broader set of tools that let players communicate, express themselves, and form relationships beyond the core party and guild systems. They support both organised play and spontaneous community.

---

## 2. Feature Set

| Feature | Description |
|---------|-------------|
| **Chat Channels** | Say, Yell, Party, Guild, Whisper, Region, Trade, LookingForGroup, etc. |
| **Emotes & Roleplay** | Text and animated emotes ([0904-Emotes.md](../0900-Player-Systems/0904-Emotes.md)) |
| **Player Inspection** | View another player’s equipment, titles, and selected profile info |
| **Ignore / Block / Report** | Safety and moderation tools |
| **Group Finder integration** | Seamless movement from social UI into parties and raids |
| **Notifications** | Friend login, guild events, party invites, etc. |

---

## 3. Design Rules

1. Communication tools default to useful and readable; advanced filtering is available for power users.
2. Toxicity countermeasures (mutes, reports, automatic filters) are first-class, not afterthoughts.
3. Roleplay and immersive play are supported without forcing them on players who prefer pure gameplay chat.
4. Cross-faction communication is restricted where it would break faction identity, with clear exceptions for neutral systems (e.g. cross-faction LFG where designed).

---

## 4. Technical Notes

Chat and social events route through the network and synchronisation layers. Rate limiting and moderation hooks are applied server-side. See [1202-Network.md](../1200-Technical/1202-Network.md) and [1206-Security.md](../1200-Technical/1206-Security.md).


## 5. Chat Moderation Tools

Automated chat filters catch common abusive language patterns before they reach other players, backed by the reporting pipeline described in [2003-Moderation.md](../2000-Operations/2003-Moderation.md), while remaining permissive enough not to interfere with normal in-character roleplay dialogue.

## 6. Roleplay Support

Dedicated roleplay-flagged servers or channels (final structure to be confirmed during Phase 5) give the rolewriting community a space with community-specific norms, without forcing roleplay conventions onto players who aren't interested.
