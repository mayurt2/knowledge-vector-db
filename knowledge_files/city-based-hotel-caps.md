---
feature_name: City-Based Hotel Caps
feature_id: city-based-hotel-caps
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-04-30
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - HotelCityEntitlementEntity
tags:
  - city budget
  - city hotel cap
  - metro budget
  - location based budget
  - hotel cap override
  - city specific limit
  - hotel budget
  - spend limit
  - hotel policy
  - travel policy
---

# City-Based Hotel Caps

## Summary
City-Based Hotel Caps let a company override its standard hotel budget for specific cities. Because hotel prices vary a lot by location, a company can set a higher cap in expensive metros (like Mumbai or Delhi) and keep the standard cap everywhere else. Each city override can also carry its own advance-booking days and long-stay budget.

## What this feature does
When an employee books a hotel in a city that has an override, the system uses the city-specific rules instead of the standard hotel budget:

- **City-specific budget** – a per-night cap that applies only in that city, overriding the company's default domestic/international hotel budget.
- **Per-city advance days** – an optional advance-booking requirement specific to the city.
- **Per-city long-stay budget** – an optional separate cap for extended stays in that city.

For any city without an override, the standard hotel budget continues to apply. This gives companies fine-grained control so they can be realistic about costs in high-price locations without raising budgets everywhere.

## Customer experience
- When booking in a city that has an override, employees see hotels evaluated against that city's specific cap rather than the company default.
- In all other cities, the normal hotel budget applies.
- A booking within the city-specific cap proceeds normally; one above it follows the company's out-of-policy rules.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because city-based hotel caps are part of the company's travel **Policy Config**, a salesperson who wants to add a city override or change a city's cap for a customer should reach out to the **Onboarding Team**. They configure the city, its budget, and any per-city advance-days or long-stay budget.

> Use the Tech Team only for whitelisting-based features. City-based caps are **not** a whitelisting feature, so they stay with Onboarding.

## Related / dependent settings
These work alongside city-based hotel caps and may also need to be set:

- **Hotel Domestic & International Budgets** – the default budgets used where no city override exists (`HotelEntitlementsEntity.budget`, `internationalBudget`).
- **Long Stay Policy** – the company-wide long-stay rules that a city override can supplement (`enableLongStay`, `longStayDays`).
- **Hotel Quality / Rating Restrictions** – quality rules that still apply within each city.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `HotelCityEntitlementEntity` — per-city hotel override holding the city, its budget, optional advance-days, and optional long-stay budget
- Snapshotted onto the trip's policy configuration in trip-management-service at trip creation.

## Sample questions this feature answers
- "Can we set a higher hotel budget for metros like Mumbai or Delhi?"
- "Can hotel caps vary by city?"
- "How do we override the standard hotel budget for a specific city?"
- "Can a city have its own long-stay budget or advance-days?"
- "What happens in cities without a specific cap?"
- "Who do I contact to add a city-specific hotel cap?"
- "Is the city-based hotel cap configurable per company?"
