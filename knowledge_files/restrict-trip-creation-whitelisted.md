---
feature_name: Restrict Trip Creation to Whitelisted Corporates
feature_id: restrict-trip-creation-whitelisted
category: Bookings & Duplicate Bookings
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-06-06
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - trip-management-service
  - corporate-entitlement-service
  - sales-service
technical_keys:
  - whitelist.company.for.restrict.trip.creation
tags:
  - trip creation
  - whitelist
  - restricted accounts
  - controlled rollout
  - create trip
  - corporate whitelist
  - access control
  - feature gating
  - restrict booking
  - allowed companies
---

# Restrict Trip Creation to Whitelisted Corporates

## Summary
This feature limits who can create new trips on the platform so that only specific, whitelisted corporates are allowed to do so. It is typically used for controlled rollouts of new functionality or for restricted accounts where trip creation needs to be tightly gated until a company is ready.

## What this feature does
When trip-creation restriction is active, the system checks whether the booking company appears on an approved whitelist before allowing a new trip to be created:

- **Whitelisted company** – trip creation proceeds as normal.
- **Non-whitelisted company** – trip creation is blocked for that company.

This lets the platform enable new trip flows for a small set of customers first (a phased rollout) and expand the list over time, or keep certain restricted accounts from creating trips at all.

## Customer experience
- Bookers at whitelisted companies create trips with no change to their flow.
- Bookers at companies not on the whitelist are prevented from creating new trips.
- The restriction is invisible to end users beyond the ability (or inability) to start a new trip.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Whitelisting** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — companies are added to the whitelist key by ID |

## Which team to connect with
**👉 Tech Team**

Because this is controlled by a **whitelisting key in Secret Manager**, the **Tech Team** owns it. A salesperson who needs a customer added to (or removed from) the trip-creation whitelist should reach out to the Tech Team.

> This is a whitelisting feature, so it does **not** go through the Onboarding Team's Policy or Corporate Config. Whitelist changes are handled by Tech.

## Related / dependent settings
These work alongside trip-creation restriction:

- **Company Whitelist Key** – the Secret Manager list of company IDs allowed to create trips (`whitelist.company.for.restrict.trip.creation`).
- **Trip Approval Workflow** – approvals still apply once a trip is created.
- **Self Booking Tool (SBT)** – SBT availability has its own separate company whitelist.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `whitelist.company.for.restrict.trip.creation` — comma-separated list of company IDs permitted to create trips
- Checked at trip-creation time in trip-management-service.

## Sample questions this feature answers
- "Can we limit trip creation to only certain companies?"
- "How do we do a controlled rollout of trip creation?"
- "Why can't this company create a new trip?"
- "How do I add a customer to the trip-creation whitelist?"
- "Is restricting trip creation a whitelisting feature?"
- "Who do I contact to allow a restricted account to create trips?"
- "Can we block trip creation for certain accounts?"
