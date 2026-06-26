---
feature_name: Previously-Booked Hotels
feature_id: previously-booked-hotels
category: Search & Booking Experience
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-03-29
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - sales-service
  - b2b-aggregation
technical_keys:
  - previously.booked.enabled.corporates
tags:
  - previously booked
  - booking history
  - repeat hotels
  - past bookings
  - search experience
  - hotel recommendations
  - rebooking
  - frequent hotels
  - search results
  - personalization
  - whitelisting
  - booking convenience
---

# Previously-Booked Hotels

## Summary
Previously-Booked Hotels highlights and surfaces hotels that a company has booked before, making them easy to find and rebook in search. This speeds up repeat bookings and encourages consistency in where employees stay. It is enabled for selected corporates through whitelisting.

## What this feature does
When a corporate is enabled, the search experience gives prominence to hotels the company has stayed at before:

- **Surfaces past stays** – previously-booked hotels are highlighted or grouped within search results.
- **Faster rebooking** – travellers can quickly rebook familiar, approved properties.
- **Corporate-level control** – enabled per corporate via the whitelist.

Corporates that are not whitelisted do not get the previously-booked highlighting.

## Customer experience
- Travellers at enabled corporates see hotels their company has booked before prominently in search.
- This makes it faster to rebook trusted, frequently used properties.
- Travellers at corporates that are not enabled see standard search results without this highlighting.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Whitelisting** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — enabled per corporate via the whitelist key |

## Which team to connect with
**👉 Tech Team**

Because previously-booked highlighting is enabled through **whitelisting** (Secret Manager keys), a salesperson who wants to turn it on for a corporate should reach out to the **Tech Team**. They add the corporate to the previously-booked whitelist.

> Whitelisting-based features are always handled by the Tech Team. This is not a Corporate Config or Policy setting, so it stays with Tech.

## Related / dependent settings
These work alongside previously-booked hotels and may also be relevant:

- **Personalization** – tailors search results to the corporate's preferences.
- **Women-Preferred Search** – safety-focused search filter.
- **Search Experience (Autosuggest V2 / New SRP)** – newer search and results-page experiences.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `previously.booked.enabled.corporates` — corporates enabled for surfacing previously-booked hotels
- The whitelist is evaluated at search time to decide whether previously-booked hotels are highlighted.

## Sample questions this feature answers
- "Can travellers see hotels their company booked before?"
- "How do we enable previously-booked hotels for a corporate?"
- "Does the platform highlight repeat hotels in search?"
- "Who do I contact to switch on previously-booked hotels?"
- "Can this be turned on for just one company?"
- "How can travellers quickly rebook a familiar hotel?"
- "Is previously-booked hotels configurable per corporate?"
