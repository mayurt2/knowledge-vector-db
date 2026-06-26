---
feature_name: Insights V2
feature_id: insights-v2
category: Reporting, Insights & Analytics
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-05-07
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - sales-service
  - b2b-aggregation
technical_keys:
  - insights.v2.whitelisted.corporates
  - insights.v2.whitelisted.userids
  - insights.v2.ask.ai.whitelisted.corporates
tags:
  - insights
  - analytics
  - reporting dashboard
  - insights v2
  - ask ai
  - ai query
  - business intelligence
  - spend analytics
  - travel insights
  - dashboard
  - data analytics
  - reporting
---

# Insights V2

## Summary
Insights V2 is the next-generation analytics and reporting dashboard that gives corporates a richer, more visual view of their travel spend, booking patterns, and policy compliance. It is enabled for selected corporates and users, and optionally includes an "Ask AI" capability that lets users ask plain-language questions about their travel data and get instant answers.

## What this feature does
When a corporate or user is enabled for Insights V2, they get access to an upgraded analytics experience on top of the standard reporting:

- **Richer dashboards** – modern, interactive views of travel spend, bookings, savings, and trends.
- **User-level access** – individual users can be granted access even when not every user in the corporate has it.
- **Ask AI (optional)** – for corporates whitelisted specifically for the AI capability, users can type natural-language questions (for example, "How much did we spend on flights last quarter?") and receive answers drawn from their own travel data.

Access is controlled through three separate whitelists, so a corporate can have the dashboard, specific users can have it, and the AI layer can be switched on independently.

## Customer experience
- Enabled corporates and users see the Insights V2 dashboard in place of, or alongside, the standard reporting view.
- The visuals are more interactive and easier to read, with drill-downs into spend and booking categories.
- Where Ask AI is enabled, users see a query box and can ask questions in plain language instead of building reports manually.
- Users who are not whitelisted continue to see the existing reporting experience.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Whitelisting** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — controlled per corporate and per user ID via whitelist keys |

## Which team to connect with
**👉 Tech Team**

Because Insights V2 is turned on through **whitelisting** (Secret Manager keys), a salesperson who wants to enable the dashboard, add specific users, or switch on Ask AI for a customer should reach out to the **Tech Team**. They manage the corporate, user-ID, and AI whitelists.

> Whitelisting-based features are always handled by the Tech Team. This is not a Corporate Config or Policy setting, so it stays with Tech.

## Related / dependent settings
These work alongside Insights V2 and may also be relevant:

- **Insights Flight Analytics** – flight-specific analytics, controlled by its own whitelist.
- **Reports Module (Whitelisted)** – enables the underlying reporting module for a company.
- **Trip / Employee Export** – export of trip and employee travel data for offline reporting.
- **Ask AI Whitelist** – separate switch that adds the natural-language query layer on top of the V2 dashboard.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `insights.v2.whitelisted.corporates` — corporates enabled for the Insights V2 dashboard
  - `insights.v2.whitelisted.userids` — individual user IDs enabled for Insights V2
  - `insights.v2.ask.ai.whitelisted.corporates` — corporates enabled for the optional Ask AI query capability
- Whitelists are evaluated at request time to decide whether the V2 experience and the AI layer are shown.

## Sample questions this feature answers
- "What is Insights V2?"
- "How do we enable the new analytics dashboard for a customer?"
- "Can we give Insights V2 to only some users in a company?"
- "What is the Ask AI feature in Insights?"
- "Can a customer ask questions about their travel data in plain language?"
- "Who do I contact to switch on Insights V2 for a corporate?"
- "Is Insights V2 configurable per user?"
- "Is the AI query feature available to everyone?"
