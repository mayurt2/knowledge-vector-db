---
feature_name: Trip Auto-Expiry
feature_id: trip-auto-expiry
category: Trip Lifecycle
config_source: Corporate Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-06-09
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - trip_auto_expire_duration
tags:
  - trip expiry
  - auto expiry
  - trip lifecycle
  - expire trip
  - stale trip
  - dashboard cleanup
  - inactive trip
  - trip timeout
  - unactioned trip
  - expiry window
  - hold release
---

# Trip Auto-Expiry

## Summary
Trip Auto-Expiry automatically closes out trips that an employee creates but never acts on. If a trip is not booked or approved within a time window the company has configured, the system marks it as expired. This keeps trip dashboards clean, removes clutter from abandoned requests, and frees up any selections (such as held fares or rooms) that were tied to the unactioned trip.

## What this feature does
When an employee raises a trip but does not move it forward (no booking made, no approval completed) within the configured window, the system steps in:

- It tracks how long each trip has been sitting without action.
- Once the trip crosses the **auto-expire duration** set for that company, it is automatically marked as **expired**.
- Expired trips drop off active dashboards, so teams only see trips that are genuinely live.
- Any held or pending selections associated with the trip are released, so they no longer count against the company.

The expiry window is defined per company through Corporate Config, so a company that wants employees to act quickly can set a short window, while another can allow more time.

## Customer experience
- Employees see only their active, relevant trips on the dashboard — abandoned drafts and stale requests are cleared out automatically.
- A trip that the employee never booked or got approved simply moves to an **Expired** status after the configured period.
- Travel desks and admins get a cleaner view, making it easier to focus on trips that still need action.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — the expiry window is set per company |

## Which team to connect with
**👉 Onboarding Team**

Because the auto-expire window is a **Corporate Config** setting, a salesperson who wants to turn this on, change the duration, or explain it for a customer should reach out to the **Onboarding Team**. They configure how long a trip can stay unactioned before it expires.

> Use the Tech Team only for whitelisting-based features. Trip auto-expiry is a Corporate Config setting, so it stays with Onboarding.

## Related / dependent settings
These work alongside trip auto-expiry and may also be relevant:

- **Block Expiry for Past Trips** – prevents trips whose dates are already in the past from being auto-expired (`block_expire_past_trips`).
- **Trip Expiry Notification** – sends a notification when a trip is about to expire or has expired (`enable_expire_trip_notification`).
- **Expire Past Trips (System)** – a tech-controlled scheduled job that expires trips whose travel dates have passed.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config — Corporate Entitlement Service
- **Key fields:**
  - `trip_auto_expire_duration` — the time window after which an unactioned (not booked / not approved) trip is auto-expired
- The duration is read from Corporate Config and applied by the trip lifecycle logic in trip-management-service.

## Sample questions this feature answers
- "How do trips expire automatically?"
- "Can we set how long a trip stays open before it expires?"
- "What happens to a trip nobody books or approves?"
- "Why did a trip move to Expired status on its own?"
- "Can we change the auto-expiry window for a customer?"
- "Does an abandoned trip stay on the dashboard forever?"
- "Who do I contact to configure trip auto-expiry?"
