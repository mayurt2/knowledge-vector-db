---
feature_name: Contracted Fare Display Text
feature_id: contracted-fare-display-text
category: Bookings & Duplicate Bookings
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-04-07
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - trip-management-service
  - sales-service
  - corporate-entitlement-service
technical_keys:
  - contracted_display_text
tags:
  - contracted fare
  - negotiated rate
  - corporate rate
  - display label
  - fare label
  - branding
  - custom text
  - rate naming
  - special fare
  - rate display
---

# Contracted Fare Display Text

## Summary
This feature lets a company set a custom label for its contracted or negotiated fares — for example showing them as "Corporate Rate" — so the business can brand how its special rates appear to bookers. It is a presentation setting that changes the wording, not the rate itself.

## What this feature does
When a custom display text is set, the platform uses it as the label whenever a contracted/negotiated fare is shown:

- **Custom text set** – contracted fares appear with the company's chosen label (e.g. "Corporate Rate", "Negotiated Fare").
- **No custom text** – a default label is used.

This gives companies control over how their negotiated rates are presented and recognised by their travellers.

## Customer experience
- Bookers see negotiated/contracted fares labelled with the company's chosen wording.
- The label makes it clear which options are the company's special rates.
- Only the wording changes — pricing and availability are unaffected.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — the label is set per company |

## Which team to connect with
**👉 Onboarding Team**

This is a **Corporate Config** setting, so the **Onboarding Team** owns it. A salesperson who wants to set or change how a customer's contracted fares are labelled should reach out to Onboarding.

> This is not a whitelisting feature, so the Tech Team is not involved.

## Related / dependent settings
These relate to how rates are shown:

- **Contracted Display Text** – the custom label for negotiated fares (`contracted_display_text`).
- **Show All Price Types** – exposes negotiated and public price types for comparison.
- **Missed Savings / Lowest Sourcing** – broader savings and rate-visibility controls.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `contracted_display_text` — custom label shown for contracted/negotiated fares
- Applied to fare display in search and booking results.

## Sample questions this feature answers
- "Can we rename negotiated fares to 'Corporate Rate'?"
- "How do we brand the label on contracted fares?"
- "Can the company customise how special rates appear?"
- "Where do I change the contracted fare label?"
- "Is the fare display text configurable per company?"
- "Who do I contact to set a custom rate label?"
- "Does changing the label affect the price?"
