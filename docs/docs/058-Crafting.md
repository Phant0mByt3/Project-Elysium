# 58 — Crafting

## Overview
Crafting is the umbrella system connecting the gathering professions ([061-Mining.md](061-Mining.md) through [064-Herbalism.md](064-Herbalism.md)) to the production professions ([065-Alchemy.md](065-Alchemy.md) through [069-Tailoring.md](069-Tailoring.md)). See [060-Professions.md](060-Professions.md) for the overall profession system this belongs to.

## Core Loop
1. Gather raw materials in the open world via a gathering profession.
2. Learn recipes from trainers, quests, or rare drops.
3. Craft items using a production profession, consuming materials and a crafting-specific currency/time cost.
4. Sell or use the result — feeding directly into the player economy ([100-Economy.md](100-Economy.md)) via the Auction House ([103-Auction-House.md](103-Auction-House.md)).

## Design Rules
* Crafted gear should be competitive with dungeon-tier drops, giving crafting professions a genuine progression role rather than being purely cosmetic or gold-focused.
* Recipes should include a mix of vendor-taught (baseline), quest-taught (thematic, one-time), and drop-taught (rare, profitable) sources.
* Crafting should support at least one profession-exclusive item type per profession (e.g. only Blacksmiths can craft plate armor) to keep professions meaningfully differentiated.

## Enchanting
Enchanting is documented as its own related-but-distinct system — see [059-Enchanting.md](059-Enchanting.md).
