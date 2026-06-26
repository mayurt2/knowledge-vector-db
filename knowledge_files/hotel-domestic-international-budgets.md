---
feature_name: Hotel Domestic & International Budgets
feature_id: hotel-domestic-international-budgets
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-05-19
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - HotelEntitlementsEntity.budget
  - internationalBudget
  - domesticCurrency
  - internationalCurrency
  - budgetMultipier
tags:
  - hotel budget
  - spend limit
  - domestic budget
  - international budget
  - hotel cap
  - per night limit
  - currency
  - budget multiplier
  - hotel policy
  - travel policy
  - spend cap
---

# Hotel Domestic & International Budgets

## Summary
This feature lets a company set separate spending caps for hotel stays depending on whether the trip is domestic or international. Each cap can also use its own currency, so an Indian company can set a rupee limit for domestic stays and (for example) a dollar limit for international stays. An optional budget multiplier can scale these caps when needed.

## What this feature does
When an employee searches for or books a hotel, the system applies the right budget based on the destination:

- **Domestic budget** – the per-night spend cap for hotel stays within the home country, expressed in the domestic currency.
- **International budget** – a separate per-night spend cap for hotel stays in other countries, expressed in the international currency.
- **Budget multiplier** – an optional factor that scales the base budget up or down (for example, to temporarily allow a higher cap during peak season or for a special group) without changing the underlying budget value.

Because domestic and international budgets are independent, a company can be generous on international travel while keeping domestic spend tight, or vice versa. The currencies are also independent, so each budget is shown and enforced in the correct money.

## Customer experience
- Employees see hotels filtered or flagged against the budget that applies to their trip (domestic or international).
- A booking that is within budget proceeds normally; a booking above budget is treated as out-of-policy and follows the company's out-of-policy rules (such as requiring approval).
- The budget shown to the traveller is in the appropriate currency for their destination.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because hotel budgets and currencies are part of the company's travel **Policy Config**, a salesperson who wants to set up or change a customer's domestic/international hotel caps should reach out to the **Onboarding Team**. They configure the budget amounts, the currencies, and any multiplier.

> Use the Tech Team only for whitelisting-based features. Hotel budgets are **not** a whitelisting feature, so they stay with Onboarding.

## Related / dependent settings
These work alongside the core hotel budgets and may also need to be set:

- **Long Stay Policy** – separate budgets for extended stays (`enableLongStay`, `longStayDays`).
- **City-Based Hotel Caps** – override the standard budget for specific cities (`HotelCityEntitlementEntity`).
- **Hotel Quality / Rating Restrictions** – limit which hotels are bookable by star or Google rating.
- **Modification Buffer Limits** – tolerances that allow small price changes without re-approval.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `HotelEntitlementsEntity.budget` — domestic per-night hotel spend cap
  - `internationalBudget` — international per-night hotel spend cap
  - `domesticCurrency` — currency used for the domestic budget
  - `internationalCurrency` — currency used for the international budget
  - `budgetMultipier` — optional factor applied to scale the budget
- Snapshotted onto the trip's policy configuration in trip-management-service at trip creation.

## Sample questions this feature answers
- "Can we set different hotel budgets for domestic and international trips?"
- "Can the international hotel budget be in a different currency?"
- "How is the per-night hotel cap configured for a company?"
- "What is the budget multiplier used for?"
- "Can we keep domestic hotel spend low but allow more for international stays?"
- "Who do I contact to change a customer's hotel budget?"
- "Is the hotel spend limit configurable per company?"
