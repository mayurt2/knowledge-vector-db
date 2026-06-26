---
feature_name: Insights Flight Analytics
feature_id: insights-flight-analytics
category: Reporting, Insights & Analytics
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-04-26
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - sales-service
  - b2b-aggregation
technical_keys:
  - insights.flight.whitelisted.corporates
  - insights.flight.whitelisted.userids
tags:
  - insights
  - flight analytics
  - flight insights
  - air travel reporting
  - analytics
  - reporting dashboard
  - flight spend
  - business intelligence
  - travel insights
  - air booking analytics
  - dashboard
  - reporting
---

# Insights Flight Analytics

## Summary
Insights Flight Analytics is a flight-specific view within the Insights reporting suite. It gives corporates dedicated analytics on their air travel — spend, routes, airlines, booking lead time, and savings — and is enabled for selected corporates and users through whitelisting.

## What this feature does
When a corporate or user is enabled for flight analytics, they unlock a dedicated flight-focused section of Insights:

- **Flight spend and trends** – a clear breakdown of how much is spent on flights over time.
- **Route and airline analysis** – visibility into top routes, preferred airlines, and travel patterns.
- **User-level access** – specific users can be granted access even when the whole corporate is not enabled.

Access is governed by two whitelists — one at the corporate level and one at the user level — so flight analytics can be opened up broadly or to just a few users.

## Customer experience
- Enabled corporates and users see a flight analytics area inside their Insights/reporting experience.
- They can review air-travel spend, top routes, airline mix, and related savings without building manual reports.
- Users who are not whitelisted do not see the flight-specific analytics views.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Whitelisting** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — controlled per corporate and per user ID via whitelist keys |

## Which team to connect with
**👉 Tech Team**

Because flight analytics is enabled through **whitelisting** (Secret Manager keys), a salesperson who wants to turn it on for a corporate or add specific users should reach out to the **Tech Team**. They manage both the corporate and user-ID whitelists.

> Whitelisting-based features are always handled by the Tech Team. This is not a Corporate Config or Policy setting, so it stays with Tech.

## Related / dependent settings
These work alongside Insights Flight Analytics and may also be relevant:

- **Insights V2** – the broader next-generation analytics dashboard, with its own whitelist.
- **Reports Module (Whitelisted)** – enables the underlying reporting module for a company.
- **Trip / Employee Export** – export of trip and employee travel data for offline reporting.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `insights.flight.whitelisted.corporates` — corporates enabled for flight analytics
  - `insights.flight.whitelisted.userids` — individual user IDs enabled for flight analytics
- Whitelists are evaluated at request time to decide whether the flight analytics views are shown.

## Sample questions this feature answers
- "What is Insights Flight Analytics?"
- "Can a customer see analytics specific to their flight bookings?"
- "How do we enable flight insights for a corporate?"
- "Can we give flight analytics to only certain users?"
- "Where can a customer see air-travel spend and top routes?"
- "Who do I contact to switch on flight analytics?"
- "Is flight analytics configurable per user?"
