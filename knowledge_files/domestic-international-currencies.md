---
feature_name: Domestic & International Currencies
feature_id: domestic-international-currencies
category: Bookings & Duplicate Bookings
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-06-22
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - trip-management-service
  - sales-service
  - corporate-entitlement-service
technical_keys:
  - domestic_currencies
  - international_currencies
tags:
  - currency
  - domestic currency
  - international currency
  - currency classification
  - pricing
  - booking classification
  - multi-currency
  - currency list
  - domestic vs international
  - currency config
---

# Domestic & International Currencies

## Summary
This feature defines, per company, which currencies are treated as domestic and which are treated as international. These lists are used to classify bookings and pricing correctly — for example deciding whether a booking is domestic or international based on the currency involved.

## What this feature does
Two comma-separated currency lists are maintained for the company:

- **Domestic Currencies** – the currencies considered domestic for that company.
- **International Currencies** – the currencies considered international for that company.

The platform uses these lists to classify bookings and apply the right pricing and policy treatment, so a transaction in a listed currency is handled as the correct type.

## Customer experience
- Bookings are classified as domestic or international based on the configured currency lists.
- Pricing and policy behaviour follow that classification consistently.
- The lists work behind the scenes; travellers simply get the correct treatment for their booking.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — both lists are set per company |

## Which team to connect with
**👉 Onboarding Team**

These are **Corporate Config** lists, so the **Onboarding Team** owns them. A salesperson who needs to set or update which currencies count as domestic or international for a customer should reach out to Onboarding.

> These are not whitelisting features, so the Tech Team is not involved.

## Related / dependent settings
These relate to currency-based classification:

- **Domestic Currencies List** – currencies treated as domestic (`domestic_currencies`).
- **International Currencies List** – currencies treated as international (`international_currencies`).
- **Approval Workflow** – domestic vs international trips can have different approver counts.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `domestic_currencies` — comma-separated list of currencies treated as domestic
  - `international_currencies` — comma-separated list of currencies treated as international
- Used to classify bookings and pricing.

## Sample questions this feature answers
- "How does the system decide if a booking is domestic or international?"
- "Can we set which currencies are domestic for a company?"
- "Where do I configure international currencies?"
- "Why is a booking being treated as international?"
- "Are the currency lists configurable per company?"
- "Who do I contact to update the currency classification?"
- "Can multiple currencies be domestic for one company?"
