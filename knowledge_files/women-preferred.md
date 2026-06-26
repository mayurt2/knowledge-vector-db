---
feature_name: Women-Preferred Search
feature_id: women-preferred
category: Search & Booking Experience
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-05-18
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - sales-service
  - b2b-aggregation
technical_keys:
  - womenpreferred.enabled.corporates
tags:
  - women preferred
  - women friendly
  - female friendly
  - safety filter
  - women safety
  - search filter
  - safe stay
  - female travelers
  - women preferred hotels
  - search experience
  - safety tagging
  - whitelisting
---

# Women-Preferred Search

## Summary
Women-Preferred Search adds a safety-focused, female-friendly filter or tag to the search experience, helping women travellers find stays that are more suited to their safety and comfort needs. It is enabled for selected corporates through whitelisting.

## What this feature does
When a corporate is enabled for women-preferred search, the search experience surfaces women-friendly options:

- **Women-preferred filter / tagging** – properties suited for women travellers are highlighted or filterable in search.
- **Corporate-level control** – enabled per corporate via the whitelist.

Corporates that are not whitelisted do not see the women-preferred filter or tagging.

## Customer experience
- Travellers at enabled corporates can filter for or see women-preferred stays during search.
- This helps female travellers quickly identify safer, more suitable options.
- Travellers at corporates that are not enabled do not see the women-preferred option.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Whitelisting** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — enabled per corporate via the whitelist key |

## Which team to connect with
**👉 Tech Team**

Because women-preferred search is enabled through **whitelisting** (Secret Manager keys), a salesperson who wants to turn it on for a corporate should reach out to the **Tech Team**. They add the corporate to the women-preferred whitelist.

> Whitelisting-based features are always handled by the Tech Team. This is not a Corporate Config or Policy setting, so it stays with Tech.

## Related / dependent settings
These work alongside women-preferred search and may also be relevant:

- **Personalization** – tailors search results to the corporate's preferences.
- **Previously-Booked Hotels** – surfaces hotels the company has booked before.
- **Search Experience (Autosuggest V2 / New SRP)** – newer search and results-page experiences.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `womenpreferred.enabled.corporates` — corporates enabled for the women-preferred search filter/tagging
- The whitelist is evaluated at search time to decide whether the women-preferred experience is shown.

## Sample questions this feature answers
- "What is the women-preferred feature?"
- "Can travellers filter for women-friendly stays?"
- "How do we enable women-preferred search for a corporate?"
- "Is there a safety filter for female travellers?"
- "Who do I contact to switch on women-preferred search?"
- "Can women-preferred be turned on for just one company?"
- "Is women-preferred search configurable per corporate?"
