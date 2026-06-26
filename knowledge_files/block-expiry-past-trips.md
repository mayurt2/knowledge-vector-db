---
feature_name: Block Expiry for Past Trips
feature_id: block-expiry-past-trips
category: Trip Lifecycle
config_source: Corporate Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-04-19
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - block_expire_past_trips
  - expire_past_trips_buffer
tags:
  - past trips
  - block expiry
  - trip expiry
  - grace period
  - expiry buffer
  - trip lifecycle
  - prevent expiry
  - past dated trip
  - expiry control
  - travel date
  - buffer window
---

# Block Expiry for Past Trips

## Summary
Block Expiry for Past Trips stops trips whose travel dates have already passed from being automatically expired. Without this control, a trip dated in the past could be swept up by auto-expiry logic; this setting protects those trips so they remain available for review, reconciliation, or late actioning. It also supports an optional grace-period buffer, so a trip is only protected (or expired) once it is a set number of days past its date.

## What this feature does
When auto-expiry runs, this setting changes how it treats trips whose dates are already in the past:

- **Block past-trip expiry** – when enabled, trips whose travel dates have already passed are **not** auto-expired, so they stay intact instead of being closed out.
- **Grace-period buffer** – an optional buffer that adds a cushion of days around the trip's past date, so the rule only takes effect once the trip is that many days old. This avoids prematurely protecting (or expiring) trips that just crossed their date.

Both controls are set per company through Corporate Config, giving each company control over how past-dated trips are handled.

## Customer experience
- Trips with travel dates in the past are preserved rather than disappearing into an Expired status, so teams can still review, reconcile, or complete actions on them.
- With the buffer in place, the rule applies only after a defined number of days, giving a predictable, configurable window.
- Companies that prefer to keep past trips off the books can adjust the buffer to suit their process.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — the flag and buffer are set per company |

## Which team to connect with
**👉 Onboarding Team**

Because blocking past-trip expiry and its buffer are **Corporate Config** settings, a salesperson who wants to enable, disable, or adjust them for a customer should reach out to the **Onboarding Team**. They configure both the block flag and the grace-period buffer.

> Use the Tech Team only for whitelisting-based features. This is a Corporate Config setting, so it stays with Onboarding.

## Related / dependent settings
These work alongside the past-trip expiry control:

- **Trip Auto-Expiry** – the core setting that expires unactioned trips after a window (`trip_auto_expire_duration`).
- **Expire Past Trips (System)** – a tech-controlled scheduled job that expires trips whose dates have passed; this Corporate Config setting governs whether a company opts out for past trips.
- **Trip Expiry Notification** – notifies when a trip is about to expire or has expired (`enable_expire_trip_notification`).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config — Corporate Entitlement Service
- **Key fields:**
  - `block_expire_past_trips` — when enabled, prevents trips with past travel dates from being auto-expired
  - `expire_past_trips_buffer` — an optional grace-period buffer (in days) applied around the past date before the rule takes effect
- Evaluated by the trip lifecycle / expiry logic in trip-management-service when processing past-dated trips.

## Sample questions this feature answers
- "Can we stop past-dated trips from being auto-expired?"
- "Why did a trip in the past not expire?"
- "Is there a grace period before a past trip expires?"
- "How do we add a buffer for expiring old trips?"
- "Can a company keep its past trips instead of expiring them?"
- "What controls expiry for trips with travel dates that have already passed?"
- "Who do I contact to change how past trips are expired?"
