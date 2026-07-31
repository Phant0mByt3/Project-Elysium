# 104 — Trading

## Overview
Direct trading allows two players to exchange items and Aurum face-to-face, distinct from the open Auction House market ([103-Auction-House.md](103-Auction-House.md)).

## Core Features
* A trade window requiring both parties to confirm twice (lock, then confirm) before the exchange completes, to prevent last-second scam swaps.
* No trade restrictions on Aurum amount; item restrictions mirror Auction House bind rules (bind-on-pickup items cannot be traded once bound, per [054-Loot-Tables.md](054-Loot-Tables.md)).

## Use Cases
* Guild loot distribution outside of formal raid loot rules ([082-Raiding.md](082-Raiding.md)).
* Gifting starter gear or materials to lower-level guildmates.
* Negotiated trades for items not efficiently sold via Auction House (e.g. bulk material swaps).

## Design Rules
Trading should remain single-faction only, consistent with party/guild restrictions elsewhere ([081-Parties.md](081-Parties.md), [080-Guilds.md](080-Guilds.md)), except where explicitly routed through the neutral Wayfarer's Guild systems noted in [103-Auction-House.md](103-Auction-House.md).
