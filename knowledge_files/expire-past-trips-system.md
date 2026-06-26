---
feature_name: Expire Past Trips (System Job)
feature_id: expire-past-trips-system
category: Trip Lifecycle
config_source: System / Secret Manager Key
configurable: false
status: live
target_release_date: 2026-05-03
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - trip-management-service
  - corporate-entitlement-service
technical_keys:
  - expire.past.trips.default.buffer
  - job.cron.expire.past.trip
tags:
  - past trips
  - scheduled job
  - cron job
  - trip expiry
  - system job
  - batch job
  - trip lifecycle
  - default buffer
  - automated expiry
  - travel date passed
  - global setting
---

# Expire Past Trips (System Job)

## Summary
Expire Past Trips is a system-level scheduled job that periodically scans for trips whose travel dates have already passed and marks them as expired. It uses a default buffer so trips are only expired once they are a set number of days past their date. This is platform plumbing — a global, tech-controlled behavior rather than a per-company setting — that keeps the system tidy by clearing out trips that can no longer be acted on.

## What this feature does
The job runs automatically on a schedule (a cron) and handles trips whose dates are in the past:

- It scans for trips whose travel dates have passed.
- It applies a **default buffer** — a number of days after the trip's date — before considering it eligible for expiry, so trips that just crossed their date are not expired immediately.
- It marks the qualifying trips as **expired**.

Both the schedule (cron) and the default buffer are controlled centrally at the system level (Secret Manager / configuration keys), not through per-company Corporate Config. This is a global behavior that applies across the platform.

## Customer experience
- Trips whose travel dates have long passed are cleared out automatically, keeping dashboards and reports focused on relevant trips.
- Because it runs on a schedule, the cleanup happens consistently in the background with no manual effort.
- The behavior is uniform across companies; individual companies can influence handling of their past trips through related Corporate Config settings (such as Block Expiry for Past Trips), but the job itself is system-wide.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **No** — tech-controlled global setting |
| Where is it configured? | **System / Secret Manager Key** (cron schedule and default buffer) |
| Who configures it? | Tech Team |
| Is it per-company? | No — it is a global, platform-wide behavior |

## Which team to connect with
**👉 Tech Team**

Because the schedule and default buffer for this job live in **system configuration / Secret Manager keys** (not Corporate Config), any change to its timing or buffer must go through the **Tech Team**. A salesperson cannot have this turned on or off per company — it is a global system behavior.

> Per-company influence over past-trip handling is done via Corporate Config (e.g., Block Expiry for Past Trips), which is owned by the Onboarding Team. The system job itself stays with Tech.

## Related / dependent settings
These interact with the system expiry job:

- **Block Expiry for Past Trips** – a per-company Corporate Config setting that prevents a company's past-dated trips from being expired (`block_expire_past_trips`).
- **Expire Past Trips Buffer (Corporate)** – a per-company buffer that can adjust the grace window (`expire_past_trips_buffer`).
- **Trip Auto-Expiry** – expires unactioned trips after a configured window (`trip_auto_expire_duration`).

## Technical reference (for Tech)
- **Config source:** System / Secret Manager Key (global)
- **Key fields:**
  - `expire.past.trips.default.buffer` — the default number of days after a trip's travel date before it becomes eligible for expiry
  - `job.cron.expire.past.trip` — the cron schedule that drives when the past-trip expiry job runs
- Implemented as a scheduled job in trip-management-service; values are sourced from system configuration, not per-corporate Corporate Config.

## Sample questions this feature answers
- "How are trips with past travel dates expired?"
- "Is there a scheduled job that expires old trips?"
- "What is the default buffer before a past trip expires?"
- "Can we change how often the past-trip expiry job runs?"
- "Is past-trip expiry configurable per company?"
- "Who controls the cron for expiring past trips?"
- "Why was a trip dated weeks ago marked as expired?"
