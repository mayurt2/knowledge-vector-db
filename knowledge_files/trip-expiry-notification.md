---
feature_name: Trip Expiry Notification
feature_id: trip-expiry-notification
category: Trip Lifecycle
config_source: Corporate Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-05-24
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - enable_expire_trip_notification
tags:
  - trip expiry
  - expiry notification
  - trip alert
  - notification
  - trip lifecycle
  - expiry reminder
  - trip warning
  - about to expire
  - email alert
  - expired trip
  - reminder
---

# Trip Expiry Notification

## Summary
Trip Expiry Notification keeps employees and travel teams informed when a trip is approaching its expiry or has already expired. Instead of trips quietly disappearing from dashboards, the system can send a heads-up so the right people can act in time — for example, by booking or getting the trip approved before it lapses. This reduces surprises and missed bookings caused by silent auto-expiry.

## What this feature does
When enabled for a company, the system sends notifications tied to the trip's expiry lifecycle:

- **About to expire** – a warning that a trip is nearing its auto-expiry window, prompting the employee to take action.
- **Has expired** – a notification confirming that a trip has moved to Expired status.

This gives employees a chance to act before a trip lapses and ensures teams are aware once a trip has expired. The notification is switched on or off per company through Corporate Config.

## Customer experience
- Employees receive a timely alert when their trip is about to expire, so they can book or push for approval before it's too late.
- If a trip does expire, the relevant people are notified rather than discovering it by chance.
- Companies that prefer minimal messaging can leave the notification off.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — enabled or disabled per company |

## Which team to connect with
**👉 Onboarding Team**

Because the expiry notification toggle is a **Corporate Config** setting, a salesperson who wants to enable, disable, or explain it for a customer should reach out to the **Onboarding Team**. They turn the notification on or off for the company.

> Use the Tech Team only for whitelisting-based features. This is a Corporate Config setting, so it stays with Onboarding.

## Related / dependent settings
These work alongside trip expiry notifications:

- **Trip Auto-Expiry** – the core setting that defines the window after which an unactioned trip expires (`trip_auto_expire_duration`).
- **Block Expiry for Past Trips** – prevents past-dated trips from being expired (`block_expire_past_trips`).
- **Expire Past Trips (System)** – a tech-controlled scheduled job that expires trips whose dates have passed.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config — Corporate Entitlement Service
- **Key fields:**
  - `enable_expire_trip_notification` — when enabled, sends notifications when a trip is about to expire or has expired
- The flag is read from Corporate Config and triggers notification dispatch within the trip lifecycle logic in trip-management-service.

## Sample questions this feature answers
- "Do employees get notified when a trip is about to expire?"
- "Can we alert users before their trip expires?"
- "Is there a notification when a trip has expired?"
- "How do we turn on trip expiry alerts for a company?"
- "Why isn't a customer getting expiry notifications?"
- "Can expiry notifications be switched off?"
- "Who do I contact to enable trip expiry notifications?"
