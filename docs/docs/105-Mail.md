# 105 — Mail

## Overview
The in-game mail system allows asynchronous item and Aurum transfers between characters, including the primary delivery method for Auction House sales ([103-Auction-House.md](103-Auction-House.md)) and completed trades.

## Core Features
* Send items/Aurum to any character by name, with a small delivery cost for non-auction-related sends (an Aurum sink, see [100-Economy.md](100-Economy.md)).
* Auction House sale proceeds and expired/unsold listings are delivered automatically via mail.
* Mailbox accessible from any city or village, and a limited number of times per session from the field via a consumable/skill (to be finalized during Phase 2).

## Design Rules
* Mail attachments should have a reasonable expiration window (several real-world days) before being returned to sender, to prevent permanent item loss from an inactive mailbox.
* Cross-faction mail is restricted, consistent with trading and party restrictions ([104-Trading.md](104-Trading.md), [081-Parties.md](081-Parties.md)).
