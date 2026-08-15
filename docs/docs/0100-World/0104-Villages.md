# 0104 — Villages

**Category:** World
**Status:** Living Document
**Related:** [0103-Cities.md](0103-Cities.md) · [0102-Regions.md](0102-Regions.md)

---

## 1. Purpose

Villages are smaller, lower-stakes settlements scattered through regions — rest stops, local quest hubs, and flavor locations that make the world feel lived-in outside of the capital cities. Where cities ([0103-Cities.md](0103-Cities.md)) serve major hub functions, villages exist to:

* Anchor a region's local questline and NPCs.
* Provide a lightweight vendor and rest point without full city services.
* Give each region a distinct sense of community and culture.

## 2. Design Requirements

* 5–15 buildings, populated with named NPCs relevant to the local story.
* At least one quest hub tied to the region's "local conflict" (see the region template in [0102-Regions.md](0102-Regions.md)).
* Should feel handcrafted and distinct — no copy-pasted village kits between regions.
* A minor vendor (general goods) and a rest/recall point, but not full trainer or auction house access.

## 3. Aurelia Villages

**Millhaven** — Southern Shires starting village where new Concord-aligned characters begin their journey; home to the tutorial questline ([0409-Tutorial-System.md](../0400-Gameplay/0409-Tutorial-System.md)). Built around a working watermill, reinforcing the farmland theme of the Shires.

**Fenwick Crossing** — a waterlogged trading post in the Greywater Fens, central to the undead-incursion questline in that region. Built on stilts above the marsh, with narrow boardwalks connecting its buildings.

**Sunspire Vale** — a farming village beneath the Sunspire Hills, frequently referenced in Solmere's supply-chain quests. Represents the everyday economic life the Concord capital depends on.

## 4. Vethmoor Villages

**Frostgate Watch** — a small garrison-village at the Frostgate Approach, half military outpost, half trading stop for travelers crossing between Dawnbound and Duskward territory.

**Cinderhearth** — a mining settlement on the edge of the Ember Deeps, home to independent dwarven prospectors not directly aligned with Ironpeak Hold's official operations.

## 5. Village vs. City: Functional Differences

| Feature | City | Village |
| --- | --- | --- |
| Bank | Yes | No |
| Auction House | Yes | No |
| Class Trainers | Yes | No |
| Fast Travel Point | Yes | Sometimes |
| General Vendor | Yes | Yes |
| Rest/Recall Point | Yes | Yes |
| NPC Population | Large, mixed | Small, tightly themed |

## 6. Writing Standard

Village NPCs should reference the local conflict directly and specifically — not generic filler dialogue. A villager in Fenwick Crossing should talk about the undead rising from the fens, not deliver a line that could apply to any swamp in any game. See [1404-NPC-Writing-Guide.md](../1400-Development/1404-NPC-Writing-Guide.md) for the full standard.

Villages are cross-referenced from their parent region entries in [0102-Regions.md](0102-Regions.md) and should never duplicate content covered by nearby landmarks ([0105-Landmarks.md](0105-Landmarks.md)).
