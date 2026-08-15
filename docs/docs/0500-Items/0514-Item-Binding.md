# 0514 — Item Binding

**Project:** Elysium MMORPG  
**Category:** Items  
**Status:** Design Complete — Implementation Pending  
**Related:** [0503-Loot.md](0503-Loot.md) · [1003-Auction-House.md](../1000-Economy/1003-Auction-House.md) · [1004-Trading.md](../1000-Economy/1004-Trading.md) · [0801-Parties.md](../0800-Multiplayer/0801-Parties.md)

---

## 1. Overview

Item binding controls whether an item can be traded, sold on the Auction House, or mailed after it has been obtained. Binding exists to preserve the value of personal progression and to limit the most extreme forms of gold-selling and boosting markets.

---

## 2. Binding Types

| Type | Behaviour |
|------|-----------|
| **Bind on Pickup (BoP)** | Becomes soulbound as soon as it enters the player’s inventory. Typical for most dungeon and raid gear. |
| **Bind on Equip (BoE)** | Remains tradeable until the player equips it. Common for world drops and some crafted items. |
| **Bind on Use** | Becomes soulbound when the item’s active effect is first used (certain consumables or trinkets). |
| **Account Bound** | Can be mailed or transferred between characters on the same account but not to other players. |
| **Unbound** | Fully tradeable (vendor trash, basic materials, some cosmetics). |

---

## 3. Design Rules

1. The majority of meaningful power upgrades from group content are BoP so that the player who earned them keeps them.
2. A healthy BoE and crafted market still exists for players who prefer to buy power or appearance.
3. Binding status is always visible on the tooltip before the player loots or purchases the item.
4. Special “trade within group for a limited time” windows after a boss kill may be supported for BoP items to allow fair loot distribution without opening full trading.

---

## 4. Technical Notes

Binding state is an immutable property of the item instance once set. All trade, mail, and Auction House operations validate binding rules server-side before completing the transfer.


---

## 5. Trade Windows

BoP raid drops support a limited "trade within group" window (typically 2 hours) after a boss kill, allowing groups to correct accidental loot assignment or defer a decision without opening full unrestricted trading — a common quality-of-life feature in modern MMORPGs that this system deliberately preserves.

## 6. Interaction with the Economy

Binding rules directly shape which items are meaningful to the Auction House economy — see [1003-Auction-House.md](../1000-Economy/1003-Auction-House.md) for how BoE and unbound items form the backbone of the tradeable gear market.
