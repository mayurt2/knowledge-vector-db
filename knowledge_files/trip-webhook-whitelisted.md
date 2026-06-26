---
feature_name: Trip Webhook (Whitelisted)
feature_id: trip-webhook-whitelisted
category: Reporting, Insights & Analytics
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-05-20
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - trip-management-service
  - sales-service
technical_keys:
  - trip.webhook.enabled.corporates
tags:
  - webhook
  - trip webhook
  - outbound webhook
  - trip events
  - data push
  - integration
  - trip data feed
  - real-time events
  - api integration
  - system integration
  - reporting
  - data sync
---

# Trip Webhook (Whitelisted)

## Summary
The Trip Webhook feature pushes trip-event data out to a customer's own systems in near real time. When a trip is created, updated, or changes status, the platform sends the relevant trip data to the customer's endpoint so they can sync it into their internal tools, dashboards, or reporting systems. It is enabled for selected corporates through whitelisting.

## What this feature does
When a corporate is enabled for trip webhooks, trip events are automatically delivered to the customer's configured endpoint:

- **Outbound trip events** – trip data is pushed out as trips are created or change state.
- **Near real-time delivery** – the customer receives updates without having to pull data manually.
- **Corporate-level control** – webhooks are enabled per corporate via the whitelist.

Corporates that are not whitelisted do not receive any outbound trip events.

## Customer experience
- Enabled corporates receive trip data automatically in their own systems as trips happen.
- This lets the customer keep their internal reporting, finance, or travel tools in sync with the platform.
- Corporates that are not enabled continue to use standard reporting and exports instead of live webhooks.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Whitelisting** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — enabled per corporate via the whitelist key |

## Which team to connect with
**👉 Tech Team**

Because outbound trip webhooks are enabled through **whitelisting** (Secret Manager keys), a salesperson who wants to set up a trip data feed for a customer should reach out to the **Tech Team**. They add the corporate to the webhook whitelist and coordinate the endpoint setup.

> Whitelisting-based features are always handled by the Tech Team. This is not a Corporate Config or Policy setting, so it stays with Tech.

## Related / dependent settings
These work alongside trip webhooks and may also be relevant:

- **Trip / Employee Export** – batch export of trip and employee data for offline reporting.
- **Reports Module (Whitelisted)** – in-platform reporting access for a company.
- **Insights V2** – next-generation analytics dashboard.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `trip.webhook.enabled.corporates` — corporates enabled to receive outbound trip-event webhooks
- The whitelist is evaluated when trip events occur to decide whether to push data to the corporate's endpoint.

## Sample questions this feature answers
- "Can we push trip data to a customer's own system?"
- "How do we set up a trip webhook for a corporate?"
- "Does the platform send trip events in real time?"
- "Which customers get outbound trip webhooks?"
- "Who do I contact to enable a trip data feed?"
- "Can a customer sync trips into their internal tools automatically?"
- "Is the trip webhook configurable per corporate?"
