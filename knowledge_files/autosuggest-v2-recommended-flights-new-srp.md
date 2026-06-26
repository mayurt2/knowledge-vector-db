---
feature_name: Search Experience (Autosuggest V2, Recommended Flights, New SRP)
feature_id: autosuggest-v2-recommended-flights-new-srp
category: Search & Booking Experience
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-05-22
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - sales-service
  - b2b-aggregation
technical_keys:
  - autosuggestv2.enabled.for.corporates
  - recommended.flights.enabled.company.ids
  - new.srp.company.list
tags:
  - search experience
  - autosuggest
  - typeahead
  - search v2
  - recommended flights
  - new srp
  - search results page
  - flight recommendations
  - search ux
  - new search
  - whitelisting
  - booking experience
---

# Search Experience (Autosuggest V2, Recommended Flights, New SRP)

## Summary
This feature bundles the newer search experiences on the platform — the V2 search typeahead (autosuggest), recommended flights, and the new Search Results Page (SRP). Each is enabled for whitelisted users or corporates, so customers can be moved onto the improved search experience selectively.

## What this feature does
When a user or corporate is enabled, they get one or more of the upgraded search experiences:

- **Autosuggest V2** – an improved search typeahead that suggests destinations and options as the user types.
- **Recommended Flights** – flight recommendations surfaced to help travellers pick suitable options faster.
- **New SRP** – the redesigned Search Results Page with an updated layout and experience.

Each experience has its own whitelist, so they can be rolled out independently to different companies or users.

## Customer experience
- Enabled users see faster, smarter search suggestions as they type.
- Travellers booking flights see recommended options that help them choose more quickly.
- Enabled companies see the new Search Results Page layout when browsing results.
- Users and companies that are not enabled continue on the existing search experience.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Whitelisting** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — controlled per corporate / company ID, with autosuggest also at corporate level, via whitelist keys |

## Which team to connect with
**👉 Tech Team**

Because these search experiences are enabled through **whitelisting** (Secret Manager keys), a salesperson who wants to switch on autosuggest V2, recommended flights, or the new SRP for a customer should reach out to the **Tech Team**. They manage each of the three whitelists.

> Whitelisting-based features are always handled by the Tech Team. These are not Corporate Config or Policy settings, so they stay with Tech.

## Related / dependent settings
These work alongside the newer search experiences and may also be relevant:

- **Personalization** – tailors results to corporate preferences.
- **Previously-Booked Hotels** – surfaces past stays in search.
- **Women-Preferred Search** – safety-focused search filter.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `autosuggestv2.enabled.for.corporates` — corporates enabled for the V2 search typeahead
  - `recommended.flights.enabled.company.ids` — company IDs enabled for recommended flights
  - `new.srp.company.list` — companies enabled for the new Search Results Page
- Whitelists are evaluated at search time to decide which experience each user/company receives.

## Sample questions this feature answers
- "What is the new search experience?"
- "How do we enable autosuggest V2 for a corporate?"
- "What are recommended flights?"
- "How do we switch a company to the new SRP?"
- "Can these search upgrades be rolled out separately?"
- "Who do I contact to enable the new search results page?"
- "Why is a customer still on the old search?"
- "Is the new search experience configurable per company?"
