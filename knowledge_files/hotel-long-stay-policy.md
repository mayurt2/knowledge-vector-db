---
feature_name: Hotel Long Stay Policy
feature_id: hotel-long-stay-policy
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-06-15
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - enableLongStay
  - longStayDays
  - domesticLongStayBudget
  - internationalLongStayBudget
tags:
  - long stay
  - extended stay
  - hotel budget
  - long stay budget
  - duration based budget
  - spend limit
  - domestic long stay
  - international long stay
  - hotel policy
  - travel policy
---

# Hotel Long Stay Policy

## Summary
The Long Stay Policy gives companies special budget handling for extended hotel stays. Because longer stays usually negotiate lower nightly rates, a company can define how many days qualifies as a "long stay" and then apply a different (often lower) per-night budget for those stays — with separate caps for domestic and international travel.

## What this feature does
When an employee books a hotel for an extended duration, the system can switch from the standard nightly budget to a dedicated long-stay budget:

- **Enable long stay** – turns the long-stay handling on or off for the company.
- **Long stay days** – the threshold: once a stay is this many days or longer, it counts as a long stay and the long-stay budgets apply.
- **Domestic long-stay budget** – the per-night cap used for qualifying long stays within the home country.
- **International long-stay budget** – the per-night cap used for qualifying long stays in other countries.

This lets companies reflect the lower negotiated rates that hotels typically offer for longer bookings, keeping spend in line with real costs for extended trips.

## Customer experience
- For stays at or beyond the long-stay threshold, employees see hotels evaluated against the long-stay budget instead of the standard nightly budget.
- Shorter stays continue to use the regular domestic/international hotel budgets.
- A long-stay booking within the long-stay budget proceeds normally; one above it follows the company's out-of-policy rules.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because the long-stay policy is part of the company's travel **Policy Config**, a salesperson who wants to enable it or change the threshold and budgets for a customer should reach out to the **Onboarding Team**. They configure whether long stay is enabled, the day threshold, and the domestic/international long-stay budgets.

> Use the Tech Team only for whitelisting-based features. The long-stay policy is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside the long-stay policy and may also need to be set:

- **Hotel Domestic & International Budgets** – the standard nightly budgets used for shorter stays (`HotelEntitlementsEntity.budget`, `internationalBudget`).
- **City-Based Hotel Caps** – city-specific overrides that can also carry their own long-stay budget (`HotelCityEntitlementEntity`).
- **Hotel Quality / Rating Restrictions** – limit which hotels are bookable by star or Google rating.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `enableLongStay` — turns long-stay handling on/off
  - `longStayDays` — number of days at which a stay becomes a long stay
  - `domesticLongStayBudget` — per-night cap for domestic long stays
  - `internationalLongStayBudget` — per-night cap for international long stays
- Snapshotted onto the trip's policy configuration in trip-management-service at trip creation.

## Sample questions this feature answers
- "Can we set a different hotel budget for long stays?"
- "After how many days does a stay count as a long stay?"
- "Can long-stay budgets be different for domestic and international trips?"
- "How do we enable the long-stay policy for a customer?"
- "Why is a long booking using a different budget than a short one?"
- "Who do I contact to change the long-stay threshold or budget?"
- "Is the long-stay policy configurable per company?"
