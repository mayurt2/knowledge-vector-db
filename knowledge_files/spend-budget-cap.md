---
feature_name: Spend / Budget Cap
feature_id: spend-budget-cap
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-05-24
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - FlightEntitlementsEntity.budget
  - HotelEntitlementsEntity.budget
  - CabEntitlementsEntity.budget
  - BusEntitlementsEntity.budget
  - TrainEntitlementsEntity.budget
tags:
  - budget
  - spend cap
  - spend limit
  - budget cap
  - per-night cap
  - fare limit
  - out-of-policy
  - hotel budget
  - flight budget
  - travel policy
  - cost control
  - price limit
---

# Spend / Budget Cap

## Summary
The Spend / Budget Cap sets the maximum amount an employee may spend on a single booking for a given travel mode. For hotels this is typically a per-night cap, for flights a per-flight (per-trip) cap, and similar caps apply for cab, bus, and train. If an employee tries to book something above the cap, the booking is flagged as out-of-policy and usually needs approval (or is blocked, depending on the company's setup).

## What this feature does
When an employee selects an option to book, the system compares its price against the budget cap configured for that mode in the company's policy:

- **Within the cap** – the booking is in-policy and proceeds normally.
- **Above the cap** – the booking is marked out-of-policy. Depending on the company's broader rules, it may require approval, show a warning, or be disallowed.

The cap is defined per travel mode, so a company can set, for example, a per-night hotel limit and a separate per-flight limit. This keeps travel spend predictable and lets companies enforce different budgets for different employee groups (for example, higher caps for senior staff).

## Customer experience
- Employees see whether the option they are choosing is within their allowed budget.
- Options above the budget are clearly marked as out-of-policy, and the employee may be asked to provide a reason or seek approval.
- Different employee groups can have different caps, so what is in-policy for one employee may be out-of-policy for another.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because budget caps are part of the company's travel **Policy Config**, a salesperson who wants to set or change spend limits for a customer should reach out to the **Onboarding Team**. They configure the per-mode budget amounts and which employee groups they apply to.

> Use the Tech Team only for whitelisting-based features. Budget caps are **not** a whitelisting feature, so they stay with Onboarding.

## Related / dependent settings
These work alongside budget caps:

- **Travel Mode Eligibility** – the mode must be Allowed before a cap applies.
- **Price Hike Tolerance Limit** – how much a fare may rise between selection and booking.
- **Trip Approval Workflow** – out-of-policy (over-budget) bookings are typically routed for approval.
- **Flight Cabin Class Restriction** – a per-class spend limit can apply on top of the overall cap.
- **Flight Add-ons** – seat/meal/baggage add-ons carry their own separate spend caps.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `FlightEntitlementsEntity.budget` — per-flight spend cap
  - `HotelEntitlementsEntity.budget` — per-night spend cap
  - `CabEntitlementsEntity.budget` — per-booking spend cap
  - `BusEntitlementsEntity.budget` — per-booking spend cap
  - `TrainEntitlementsEntity.budget` — per-booking spend cap
- Evaluated at selection/booking time; over-cap bookings flagged out-of-policy and routed per approval config in trip-management-service.

## Sample questions this feature answers
- "How do I set a per-night hotel budget for a company?"
- "Can we cap how much an employee spends on a flight?"
- "What happens if an employee books above the budget?"
- "Can different teams have different spend limits?"
- "Is the budget cap configurable?"
- "How do we control travel spend for a customer?"
- "Who do I contact to change a company's spend limits?"
