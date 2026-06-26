---
feature_name: Flight Fare Type Restriction
feature_id: flight-fare-type-restriction
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-04-17
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - FlightEntitlementsEntity.fareType
  - isFareTypeSearchRestricted
tags:
  - fare type
  - fare type restriction
  - corporate fare
  - retail fare
  - flexi fare
  - fare restriction
  - search restriction
  - allowed fares
  - travel policy
  - flight
---

# Flight Fare Type Restriction

## Summary
Flight Fare Type Restriction limits which fare types employees are allowed to book — for example, restricting to certain fare families such as corporate, retail, or flexible fares. The company can also restrict the search so only the allowed fare types appear. This is a flight-specific control that helps companies steer employees toward preferred or negotiated fares.

## What this feature does
When an employee searches for or selects a flight, the system applies the company's fare type rules:

- **Allowed fare types** – defines which fare types employees may book.
- **Search restriction** – when enabled, the flight search only returns the allowed fare types, so disallowed fares never appear.

This lets companies enforce use of preferred or negotiated fare types and avoid fare options that don't suit their travel program. Attempting to book a disallowed fare type is prevented; when search restriction is on, employees simply never see those fares.

## Customer experience
- Employees see and can book only the fare types their policy permits; if search is restricted, disallowed fare types do not appear at all.
- This helps employees pick the right fare without having to know the company's fare rules themselves.
- Different employee groups can have different allowed fare types within the same company.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because fare type rules are part of the company's travel **Policy Config**, a salesperson who wants to restrict employees to certain fare types (and optionally limit the search) should reach out to the **Onboarding Team**. They configure the allowed fare types and the fare-type search restriction per employee group.

> Use the Tech Team only for whitelisting-based features. Fare type restriction is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside fare type restriction:

- **Flight Cabin Class Restriction** – class rules are often configured together with fare type rules.
- **Spend / Budget Cap** – the per-flight spend cap that applies regardless of fare type.
- **Travel Mode Eligibility** – flights must be Allowed in the first place.
- **Cheaper Rate Suggestion** – may surface lower-priced fares for the same itinerary.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `FlightEntitlementsEntity.fareType` — the fare type control / allowed fare types
  - `isFareTypeSearchRestricted` — when true, search returns only allowed fare types
- Evaluated at flight search/selection time in trip-management-service.

## Sample questions this feature answers
- "Can we restrict employees to certain flight fare types?"
- "How do I make the search show only allowed fare types?"
- "Can we steer employees toward negotiated corporate fares?"
- "What happens if an employee picks a disallowed fare type?"
- "Is the fare type restriction configurable?"
- "Can fare type rules differ by employee group?"
- "Who do I contact to change fare type rules for a customer?"
