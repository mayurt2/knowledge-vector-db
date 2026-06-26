---
feature_name: Missed Savings, Lowest Sourcing & Price Types
feature_id: missed-savings-lowest-sourcing-price-types
category: Bookings & Duplicate Bookings
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-05-28
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - trip-management-service
  - sales-service
  - corporate-entitlement-service
technical_keys:
  - enable_missed_savings
  - enable_lowest_sourcing
  - show_all_price_types
tags:
  - missed savings
  - lowest sourcing
  - price types
  - savings visibility
  - negotiated rates
  - public rates
  - cheapest fare
  - rate comparison
  - cost savings
  - fare transparency
---

# Missed Savings, Lowest Sourcing & Price Types

## Summary
This feature gives bookers more visibility into savings and pricing. It surfaces "missed savings" — the gap between the cheapest available fare and what was actually booked — shows the lowest-sourced rates, and exposes all available price types. Together these help bookers compare negotiated versus public rates and make more cost-aware choices.

## What this feature does
There are three related controls that can be switched on per company:

- **Missed Savings** – highlights the difference between the cheapest available fare and the fare that was chosen/booked, making lost savings visible.
- **Lowest Sourcing** – shows the lowest-sourced rate available for an option, so the best price is surfaced.
- **All Price Types** – exposes every available price type (for example negotiated/corporate and public rates) to the booker for comparison.

Used together, these drive savings transparency and let bookers and managers see how their bookings stack up against the best available options.

## Customer experience
- Bookers see how much potential saving was missed when a more expensive option is chosen.
- The lowest available sourced rate is surfaced during search.
- All applicable price types are shown side by side, making negotiated-vs-public comparisons clear.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — each toggle is set per company |

## Which team to connect with
**👉 Onboarding Team**

All three of these are **Corporate Config** toggles, so the **Onboarding Team** owns them. A salesperson who wants to enable missed-savings visibility, lowest sourcing, or all price types for a customer should reach out to Onboarding.

> These are not whitelisting features, so the Tech Team is not involved.

## Related / dependent settings
These work together for savings and pricing visibility:

- **Missed Savings Toggle** – enables the savings-gap display (`enable_missed_savings`).
- **Lowest Sourcing Toggle** – surfaces the lowest-sourced rate (`enable_lowest_sourcing`).
- **Show All Price Types** – exposes every price type to the booker (`show_all_price_types`).
- **Contracted Fare Display Text** – how negotiated/corporate rates are labelled.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `enable_missed_savings` — shows the gap between cheapest available and booked fare
  - `enable_lowest_sourcing` — surfaces the lowest-sourced rate
  - `show_all_price_types` — exposes all available price types to the booker
- Applied during search and booking display.

## Sample questions this feature answers
- "Can we show travellers how much they could have saved?"
- "What is missed savings and how do we turn it on?"
- "Can the platform show the lowest available rate?"
- "How do we compare negotiated rates against public fares?"
- "Can we show all price types to the booker?"
- "Who do I contact to enable savings visibility for a company?"
- "Are these savings features configurable per company?"
