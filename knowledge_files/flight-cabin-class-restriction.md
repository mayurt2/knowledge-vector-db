---
feature_name: Flight Cabin Class Restriction
feature_id: flight-cabin-class-restriction
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-06-22
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - FlightEntitlementsEntity.travelClass
  - eligibleTravelClasses
  - eligibleTravelClassLimit
  - isSearchRestricted
tags:
  - cabin class
  - travel class
  - economy only
  - business class
  - class restriction
  - flight class
  - premium economy
  - first class
  - search restriction
  - travel policy
  - flight
---

# Flight Cabin Class Restriction

## Summary
Flight Cabin Class Restriction limits which flight cabin classes employees are allowed to book — for example, Economy only, or Economy and Premium Economy but not Business. The company can also restrict the search itself so only allowed classes even appear, and can attach a separate spend limit to each allowed class. This is a flight-specific control.

## What this feature does
When an employee searches for or selects a flight, the system applies the company's cabin class rules:

- **Allowed classes** – defines exactly which cabin classes (Economy, Premium Economy, Business, First) employees may book.
- **Search restriction** – when enabled, the flight search only returns the allowed classes, so employees never even see disallowed options.
- **Per-class spend limit** – an optional budget can be attached to each allowed class (for example, a higher cap for Business on long-haul).

Together these let a company keep travel within an approved comfort tier while controlling cost. Booking a disallowed class is prevented, and booking an allowed class above its per-class limit is treated as out-of-policy.

## Customer experience
- Employees see and can book only the cabin classes their policy permits; if search is restricted, disallowed classes do not appear at all.
- If a per-class spend limit is set, an allowed-class flight priced above that limit is flagged out-of-policy.
- Different employee groups can have different allowed classes and limits within the same company.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because cabin class rules are part of the company's travel **Policy Config**, a salesperson who wants to restrict employees to certain classes (or set per-class limits) should reach out to the **Onboarding Team**. They configure the allowed classes, search restriction, and per-class limits per employee group.

> Use the Tech Team only for whitelisting-based features. Cabin class restriction is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside cabin class restriction:

- **Spend / Budget Cap** – the overall per-flight cap, which sits alongside per-class limits.
- **Flight Fare Type Restriction** – restricts fare types, often configured together with class rules.
- **Travel Mode Eligibility** – flights must be Allowed in the first place.
- **Trip Approval Workflow** – out-of-policy class/limit breaches are routed for approval.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `FlightEntitlementsEntity.travelClass` — the cabin class control
  - `eligibleTravelClasses` — the set of allowed cabin classes
  - `eligibleTravelClassLimit` — optional per-class spend limit
  - `isSearchRestricted` — when true, search returns only allowed classes
- Evaluated at flight search/selection time in trip-management-service.

## Sample questions this feature answers
- "Can we restrict employees to Economy only?"
- "How do I allow Business class only for senior staff?"
- "Can the flight search hide classes employees aren't allowed to book?"
- "Can we set a different spend limit per cabin class?"
- "Is the cabin class restriction configurable?"
- "What happens if an employee picks a disallowed class?"
- "Who do I contact to change cabin class rules for a customer?"
