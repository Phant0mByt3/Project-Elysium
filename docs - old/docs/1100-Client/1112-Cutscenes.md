# 1112 — Cutscenes

**Project:** Elysium MMORPG  
**Category:** Client  
**Status:** Design Complete — Implementation Pending  
**Related:** [0712-Cinematics.md](../0700-Quests/0712-Cinematics.md) · [1309-Cinematics.md](../1300-Art/1309-Cinematics.md) · [1111-Animations.md](1111-Animations.md) · [1106-Accessibility.md](1106-Accessibility.md)

---

## 1. Overview

Cutscenes are the client-side playback of scripted cinematic sequences triggered by quests, story moments, or zone transitions. This document covers presentation, skip behaviour, and technical integration.

---

## 2. Behaviour

- Triggered by server or quest script events
- Camera, animation, and dialogue playback under client control once started
- Skip available after first viewing (or always, per accessibility settings)
- Subtitles and accessibility options supported

---

## 3. Design Rules

1. Cutscenes are skippable so that repeat playthroughs and alts are not forced to re-watch.
2. Critical information is never conveyed only in a cutscene.
3. Performance during cutscenes still respects minimum-spec targets.
4. Art and animation direction follow [1309-Cinematics.md](../1300-Art/1309-Cinematics.md).

---

## 4. Technical Notes

Cutscene definitions reference animation, camera, and dialogue assets. The client plays them in a controlled mode that temporarily suppresses normal gameplay input while preserving the ability to skip and to display subtitles.
