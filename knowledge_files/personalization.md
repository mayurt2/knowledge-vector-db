---
feature_name: Personalization
feature_id: personalization
category: Search & Booking Experience
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-05-12
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - sales-service
  - b2b-aggregation
technical_keys:
  - personalization.enabled.corporates
tags:
  - personalization
  - personalized search
  - location mapping
  - property mapping
  - tailored results
  - search experience
  - relevance
  - smart search
  - custom results
  - recommendations
  - whitelisting
  - corporate preferences
---

# Personalization

## Summary
Personalization tailors the search and booking experience to a corporate's preferences — for example, mapping preferred locations or properties so that the most relevant options surface first. It is enabled for selected corporates through whitelisting.

## What this feature does
When a corporate is enabled for personalization, the experience is adapted to that company's preferences:

- **Location / property-mapping personalization** – preferred locations and properties are mapped so relevant options are prioritized.
- **More relevant results** – travellers see options that better match the corporate's typical needs.
- **Corporate-level control** – enabled per corporate via the whitelist.

Corporates that are not whitelisted get the standard, non-personalized experience.

## Customer experience
- Travellers at enabled corporates see search results tailored to their company's preferred locations and properties.
- This makes finding the right option faster and more relevant.
- Travellers at corporates that are not enabled see standard, non-personalized results.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Whitelisting** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — enabled per corporate via the whitelist key |

## Which team to connect with
**👉 Tech Team**

Because personalization is enabled through **whitelisting** (Secret Manager keys), a salesperson who wants to turn it on for a corporate should reach out to the **Tech Team**. They add the corporate to the personalization whitelist.

> Whitelisting-based features are always handled by the Tech Team. This is not a Corporate Config or Policy setting, so it stays with Tech.

## Related / dependent settings
These work alongside personalization and may also be relevant:

- **Previously-Booked Hotels** – surfaces hotels the company has booked before.
- **Women-Preferred Search** – safety-focused search filter.
- **Search Experience (Autosuggest V2 / New SRP)** – newer search and results-page experiences.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `personalization.enabled.corporates` — corporates enabled for personalization (e.g., location/property-mapping)
- The whitelist is evaluated at search time to decide whether the personalized experience is applied.

## Sample questions this feature answers
- "What does personalization do?"
- "Can search results be tailored to a corporate's preferences?"
- "How do we enable personalization for a company?"
- "What is location or property-mapping personalization?"
- "Who do I contact to switch on personalization?"
- "Can personalization be turned on for just one corporate?"
- "Is personalization configurable per corporate?"
