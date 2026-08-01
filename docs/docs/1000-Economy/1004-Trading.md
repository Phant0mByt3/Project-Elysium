# 104 — Trading

## Overview
Direct trading allows two players to exchange items and Aurum face-to-face, distinct from the open Auction House market ([1003-Auction-House.md](1003-Auction-House.md)).

## Core Features
* A trade window requiring both parties to confirm twice (lock, then confirm) before the exchange completes, to prevent last-second scam swaps.
* No trade restrictions on Aurum amount; item restrictions mirror Auction House bind rules (bind-on-pickup items cannot be traded once bound, per [0504-Loot-Tables.md](../0500-Items/0504-Loot-Tables.md)).

## Use Cases
* Guild loot distribution outside of formal raid loot rules ([0802-Raiding.md](../0800-Multiplayer/0802-Raiding.md)).
* Gifting starter gear or materials to lower-level guildmates.
* Negotiated trades for items not efficiently sold via Auction House (e.g. bulk material swaps).

## Design Rules
Trading should remain single-faction only, consistent with party/guild restrictions elsewhere ([0801-Parties.md](../0800-Multiplayer/0801-Parties.md), [0800-Guilds.md](../0800-Multiplayer/0800-Guilds.md)), except where explicitly routed through the neutral Wayfarer's Guild systems noted in [1003-Auction-House.md](1003-Auction-House.md).
