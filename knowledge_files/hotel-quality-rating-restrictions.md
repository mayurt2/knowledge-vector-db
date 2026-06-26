---
feature_name: Hotel Quality & Rating Restrictions
feature_id: hotel-quality-rating-restrictions
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
  - hotelRatings
  - googleRatings
  - hardBlockHotelRatings
  - hardBlockGoogleRatings
tags:
  - hotel rating
  - star rating
  - google rating
  - hotel quality
  - hard block
  - soft preference
  - hotel restriction
  - quality threshold
  - hotel policy
  - travel policy
---

# Hotel Quality & Rating Restrictions

## Summary
This feature lets a company control the quality of hotels its employees can book by setting minimum thresholds on hotel star ratings and Google ratings. The thresholds can act as a soft preference (low-rated hotels are discouraged or flagged but still bookable) or as a hard block (low-rated hotels cannot be booked at all).

## What this feature does
When an employee searches for hotels, the system evaluates each option against the company's rating rules:

- **Hotel ratings** – the minimum acceptable star rating(s) for a hotel.
- **Google ratings** – the minimum acceptable Google review rating(s) for a hotel.
- **Hard block on hotel ratings** – when on, hotels below the star-rating threshold are blocked entirely and cannot be booked.
- **Hard block on Google ratings** – when on, hotels below the Google-rating threshold are blocked entirely and cannot be booked.

When the hard-block flags are off, the rating thresholds behave as a soft preference: lower-rated hotels may still appear and be bookable (typically as out-of-policy), but the company's preferred quality is signalled. When the hard-block flags are on, those hotels are removed from the bookable set.

## Customer experience
- Employees see hotels that meet the company's quality bar prioritised, and lower-quality hotels flagged or hidden depending on the rules.
- With a soft preference, a traveller can still choose a lower-rated hotel but it is treated as out-of-policy.
- With a hard block, lower-rated hotels are simply not bookable, so the traveller only sees options that meet the company's standards.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because hotel quality and rating rules are part of the company's travel **Policy Config**, a salesperson who wants to set or change the rating thresholds (or switch them between soft preference and hard block) for a customer should reach out to the **Onboarding Team**.

> Use the Tech Team only for whitelisting-based features. Rating restrictions are **not** a whitelisting feature, so they stay with Onboarding.

## Related / dependent settings
These work alongside the rating restrictions and may also need to be set:

- **Hotel Domestic & International Budgets** – the spend caps applied alongside quality rules.
- **City-Based Hotel Caps** – city-specific budget overrides.
- **Long Stay Policy** – separate budgets for extended stays.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `hotelRatings` — minimum acceptable hotel star rating(s)
  - `googleRatings` — minimum acceptable Google review rating(s)
  - `hardBlockHotelRatings` — if true, hotels below the star threshold are blocked from booking
  - `hardBlockGoogleRatings` — if true, hotels below the Google-rating threshold are blocked from booking
- Snapshotted onto the trip's policy configuration in trip-management-service at trip creation.

## Sample questions this feature answers
- "Can we restrict employees to a minimum hotel star rating?"
- "Can we block hotels with low Google ratings?"
- "What's the difference between a soft preference and a hard block on ratings?"
- "Can a traveller still book a low-rated hotel?"
- "How do we set the minimum hotel quality for a customer?"
- "Who do I contact to change the hotel rating rules?"
- "Is the hotel rating restriction configurable per company?"
