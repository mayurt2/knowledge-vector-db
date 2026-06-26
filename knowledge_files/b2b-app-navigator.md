---
feature_name: B2B App Navigator
feature_id: b2b-app-navigator
category: Search & Booking Experience
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-04-26
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - b2b-aggregation
  - sales-service
technical_keys:
  - b2b.app.navigator.whitelisted.corporates
  - b2b.app.navigator.whitelisted.emails
tags:
  - app navigator
  - b2b navigator
  - navigation
  - app ui
  - navigation menu
  - b2b app
  - user experience
  - app navigation
  - ui experience
  - whitelisting
  - email whitelist
  - booking experience
---

# B2B App Navigator

## Summary
The B2B App Navigator is an updated navigation experience in the B2B app, making it easier for users to move around the platform. It is enabled for whitelisted corporates and, where needed, for specific individual emails through whitelisting.

## What this feature does
When a corporate or email is enabled, the B2B App Navigator UI becomes available:

- **Updated navigation** – an improved way to navigate the B2B app.
- **Corporate-level control** – enabled for whole corporates via the corporate whitelist.
- **Email-level control** – can also be enabled for specific individual emails, useful for targeted rollouts or pilots.

Users who are neither in a whitelisted corporate nor on the email whitelist use the existing navigation.

## Customer experience
- Users at enabled corporates (or specific whitelisted emails) see the new app navigator UI.
- Navigation around the B2B app becomes easier and more intuitive.
- Users who are not enabled continue with the existing navigation experience.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Whitelisting** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — enabled per corporate and also per individual email via whitelist keys |

## Which team to connect with
**👉 Tech Team**

Because the B2B App Navigator is enabled through **whitelisting** (Secret Manager keys), a salesperson who wants to turn it on for a corporate or for specific emails should reach out to the **Tech Team**. They manage both the corporate and email whitelists.

> Whitelisting-based features are always handled by the Tech Team. This is not a Corporate Config or Policy setting, so it stays with Tech.

## Related / dependent settings
These work alongside the B2B App Navigator and may also be relevant:

- **Employee Web-App & Flight Module (Whitelisted)** – enables the employee web-app experience.
- **Search Experience (Autosuggest V2 / New SRP)** – newer search and results-page experiences.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `b2b.app.navigator.whitelisted.corporates` — corporates enabled for the B2B app navigator
  - `b2b.app.navigator.whitelisted.emails` — specific emails enabled for the B2B app navigator
- Whitelists are evaluated at request time to decide whether the navigator UI is shown.

## Sample questions this feature answers
- "What is the B2B app navigator?"
- "How do we enable the app navigator for a corporate?"
- "Can we enable the navigator for just specific users by email?"
- "Who do I contact to switch on the B2B app navigator?"
- "Can the navigator be piloted with a few emails first?"
- "Why does a user still see the old navigation?"
- "Is the B2B app navigator configurable per corporate?"
