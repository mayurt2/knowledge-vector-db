---
feature_name: Custom Pricing & Rate-Tag Suppression (Whitelisted)
feature_id: custom-pricing-rate-tag-whitelisted
category: Search & Booking Experience
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-05-05
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - sales-service
  - b2b-aggregation
technical_keys:
  - awa.custom.price.enabled.for.corporates
  - skip-rate-tag.enabled.corporates
tags:
  - custom pricing
  - awa pricing
  - rate tag
  - rate tagging
  - pricing rules
  - discount tagging
  - special pricing
  - negotiated rates
  - booking pricing
  - whitelisting
  - rate suppression
  - pricing experience
---

# Custom Pricing & Rate-Tag Suppression (Whitelisted)

## Summary
This feature covers two pricing-related controls for bookings: AWA custom pricing, which applies special pricing for selected corporates and users, and rate-tag suppression, which stops rate tags from being sent for certain corporates. Both are enabled through whitelisting and affect how rates and discounts are priced and tagged in bookings.

## What this feature does
When enabled, these controls change pricing and tagging behaviour:

- **AWA custom pricing** – applies custom (special/negotiated) pricing for whitelisted corporates and users.
- **Rate-tag suppression** – stops rate tags from being sent for whitelisted corporates, which affects how rates and discounts are tagged in bookings.

Each is controlled by its own whitelist, so custom pricing and rate-tag suppression can be applied independently to different corporates.

## Customer experience
- Corporates and users with AWA custom pricing enabled see their special/negotiated pricing applied in bookings.
- Corporates with rate-tag suppression enabled do not have rate tags sent, changing how rate and discount information is tagged.
- Corporates and users that are not whitelisted use standard pricing and rate-tagging behaviour.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Whitelisting** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — custom pricing per corporate/user; rate-tag suppression per corporate, via whitelist keys |

## Which team to connect with
**👉 Tech Team**

Because both custom pricing and rate-tag suppression are enabled through **whitelisting** (Secret Manager keys), a salesperson who wants to apply special pricing or suppress rate tags for a customer should reach out to the **Tech Team**. They manage both whitelists.

> Whitelisting-based features are always handled by the Tech Team. These are not Corporate Config or Policy settings, so they stay with Tech.

## Related / dependent settings
These work alongside custom pricing and rate-tag suppression and may also be relevant:

- **Personalization** – tailors the experience to corporate preferences.
- **Search Experience (Autosuggest V2 / New SRP)** – newer search and results-page experiences.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `awa.custom.price.enabled.for.corporates` — corporates (and users) enabled for AWA custom pricing
  - `skip-rate-tag.enabled.corporates` — corporates for which rate-tag sending is suppressed
- Whitelists are evaluated at pricing/booking time to decide whether custom pricing applies and whether rate tags are sent.

## Sample questions this feature answers
- "What is AWA custom pricing?"
- "How do we apply special pricing for a corporate?"
- "What does rate-tag suppression do?"
- "How do we stop rate tags from being sent for a corporate?"
- "Who do I contact to set up custom pricing?"
- "Can custom pricing and rate-tag suppression be set independently?"
- "Why are rate tags missing for a customer's bookings?"
- "Is custom pricing configurable per corporate?"
