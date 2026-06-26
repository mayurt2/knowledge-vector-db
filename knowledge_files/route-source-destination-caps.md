---
feature_name: Route (Source–Destination) Caps
feature_id: route-source-destination-caps
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-04-19
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - FlightSourceDestinationEntitlementEntity
  - BusSourceDestinationEntitlementEntity
tags:
  - route budget
  - source destination
  - route cap
  - flight route budget
  - bus route budget
  - origin destination
  - budget override
  - advance days
  - spend limit
  - travel policy
---

# Route (Source–Destination) Caps

## Summary
Route Caps let a company override the standard flight or bus budget for specific origin–destination routes. For a frequently travelled or business-critical route, a company can set a higher (or different) cap and its own advance-booking days, while every other route keeps the default budget.

## What this feature does
When an employee books a flight or bus on a route that has an override, the system applies the route-specific rules instead of the standard budget:

- **Route-specific budget** – a fare cap that applies only to bookings from a particular source to a particular destination, overriding the company's default flight or bus budget.
- **Per-route advance days** – an optional advance-booking requirement specific to that route.

This is handled separately for flights and buses, so a company can fine-tune key routes for each mode. Any route without an override continues to use the company's standard budget. This lets companies be realistic about routes where fares are naturally higher without loosening budgets across the board.

## Customer experience
- When booking on a route that has an override, employees see options evaluated against the route-specific cap rather than the company default.
- On all other routes, the normal flight or bus budget applies.
- A booking within the route-specific cap proceeds normally; one above it follows the company's out-of-policy rules.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because route caps are part of the company's travel **Policy Config**, a salesperson who wants to add a route override or change a route's cap for a customer should reach out to the **Onboarding Team**. They configure the source, destination, route budget, and any per-route advance-days for flights and buses.

> Use the Tech Team only for whitelisting-based features. Route caps are **not** a whitelisting feature, so they stay with Onboarding.

## Related / dependent settings
These work alongside route caps and may also need to be set:

- **Flight / Bus Standard Budgets** – the default budgets used where no route override exists.
- **Bus Type Restriction** – which bus types are bookable (`BusEntitlementsEntity.busType`).
- **Modification Buffer Limits** – tolerances that allow small changes without re-approval.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `FlightSourceDestinationEntitlementEntity` — per-route flight override holding source, destination, budget, and optional advance-days
  - `BusSourceDestinationEntitlementEntity` — per-route bus override holding source, destination, budget, and optional advance-days
- Snapshotted onto the trip's policy configuration in trip-management-service at trip creation.

## Sample questions this feature answers
- "Can we set a higher budget for a specific flight route?"
- "Can budgets vary by source and destination?"
- "How do we override the flight or bus budget for a key business route?"
- "Can a route have its own advance-booking days?"
- "What happens on routes without a specific cap?"
- "Who do I contact to add a route-specific cap?"
- "Is the route-based budget configurable per company?"
