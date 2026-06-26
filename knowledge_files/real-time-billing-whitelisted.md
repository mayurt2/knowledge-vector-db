---
feature_name: Real-Time Billing (Whitelisted)
feature_id: real-time-billing-whitelisted
category: Reporting, Insights & Analytics
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-03-29
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - sales-service
technical_keys:
  - sales.enable.realtime.billing.whitelisted.userids
tags:
  - billing
  - real-time billing
  - instant billing
  - invoicing
  - live billing
  - billing automation
  - finance
  - reporting
  - billing feed
  - whitelisting
  - sales billing
  - on-the-fly billing
---

# Real-Time Billing (Whitelisted)

## Summary
Real-Time Billing generates billing information as bookings happen, rather than in a batch later. It is enabled for selected user IDs through whitelisting, so the live billing experience is available only to users who have been switched on for it.

## What this feature does
When a user is enabled for real-time billing, billing is processed live as transactions occur:

- **Live billing** – billing details are produced in real time instead of through a delayed or batch process.
- **User-level control** – enabled per user ID via the whitelist, so it can be rolled out to specific users.

Users who are not whitelisted continue to use the standard billing flow.

## Customer experience
- Whitelisted users see billing reflected in real time as bookings are made.
- This gives faster visibility into charges and supports quicker reconciliation.
- Users who are not enabled continue with the standard billing timing.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Whitelisting** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Controlled per user ID via the whitelist key |

## Which team to connect with
**👉 Tech Team**

Because real-time billing is enabled through **whitelisting** (Secret Manager keys), a salesperson who wants to switch it on for specific users should reach out to the **Tech Team**. They add the user IDs to the real-time billing whitelist.

> Whitelisting-based features are always handled by the Tech Team. This is not a Corporate Config or Policy setting, so it stays with Tech.

## Related / dependent settings
These work alongside real-time billing and may also be relevant:

- **Reports Module (Whitelisted)** – in-platform reporting access.
- **Trip / Employee Export** – export of trip and employee travel data.
- **Insights V2** – next-generation analytics dashboard.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `sales.enable.realtime.billing.whitelisted.userids` — user IDs enabled for real-time billing
- The whitelist is evaluated at request time to decide whether real-time billing applies for a user.

## Sample questions this feature answers
- "What is real-time billing?"
- "How do we enable real-time billing for a user?"
- "Can real-time billing be turned on for only some users?"
- "Who do I contact to switch on live billing?"
- "Why is a user still on standard billing?"
- "Is real-time billing controlled per user ID?"
- "Is real-time billing configurable?"
