---
feature_name: Flight Add-ons (Seat, Meal, Baggage)
feature_id: flight-addons-seat-meal-baggage
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-05-18
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - FlightEntitlementsEntity.seatEligibility
  - FlightEntitlementsEntity.mealEligibility
  - FlightEntitlementsEntity.baggageEligibility
  - FlightEntitlementsEntity.seatLimit
  - FlightEntitlementsEntity.mealLimit
  - FlightEntitlementsEntity.baggageLimit
tags:
  - add-ons
  - ancillaries
  - seat selection
  - meal
  - baggage
  - extra baggage
  - seat limit
  - meal limit
  - baggage limit
  - flight extras
  - travel policy
  - flight
---

# Flight Add-ons (Seat, Meal, Baggage)

## Summary
Flight Add-ons control whether employees can buy paid extras on a flight — seat selection, in-flight meals, and extra baggage. Each add-on can be allowed or disallowed independently, and each can carry its own separate spend cap. This is a flight-specific control that lets companies manage ancillary spend on top of the base fare.

## What this feature does
When an employee books a flight, the system checks the company's policy for each add-on type:

- **Seat selection** – whether paid seat selection is allowed, and an optional spend limit for it.
- **Meals** – whether paid meals are allowed, and an optional spend limit.
- **Baggage** – whether extra baggage is allowed, and an optional spend limit.

Each add-on is independent, so a company can allow baggage but not paid seat selection, or allow all three with different caps. When an add-on is allowed but its price exceeds the configured limit, that add-on is treated as out-of-policy. This keeps ancillary costs under control while still giving employees needed extras.

## Customer experience
- Employees can buy only the add-ons their policy permits; disallowed add-ons are unavailable.
- If an add-on has a spend limit, choices above that limit are flagged as out-of-policy.
- Different employee groups can have different add-on permissions and limits within the same company.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because flight add-on rules are part of the company's travel **Policy Config**, a salesperson who wants to allow/disallow seat, meal, or baggage purchases (and set their limits) should reach out to the **Onboarding Team**. They configure each add-on's eligibility and spend cap per employee group.

> Use the Tech Team only for whitelisting-based features. Flight add-ons are **not** a whitelisting feature, so they stay with Onboarding.

## Related / dependent settings
These work alongside flight add-ons:

- **Spend / Budget Cap** – the per-flight base fare cap, separate from add-on caps.
- **Flight Cabin Class Restriction** – class rules that apply to the base fare.
- **Travel Mode Eligibility** – flights must be Allowed in the first place.
- **Trip Approval Workflow** – out-of-policy add-on spend is routed for approval.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `FlightEntitlementsEntity.seatEligibility` + `FlightEntitlementsEntity.seatLimit` — paid seat selection allowed + its cap
  - `FlightEntitlementsEntity.mealEligibility` + `FlightEntitlementsEntity.mealLimit` — paid meals allowed + its cap
  - `FlightEntitlementsEntity.baggageEligibility` + `FlightEntitlementsEntity.baggageLimit` — extra baggage allowed + its cap
- Evaluated at flight booking time in trip-management-service.

## Sample questions this feature answers
- "Can employees buy paid seat selection on flights?"
- "How do I allow extra baggage but block paid meals?"
- "Can we set a spend limit on flight add-ons?"
- "What happens if an add-on exceeds its limit?"
- "Are flight add-ons configurable?"
- "Can add-on rules differ by employee group?"
- "Who do I contact to change flight add-on rules for a customer?"
