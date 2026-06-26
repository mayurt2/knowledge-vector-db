---
feature_name: Duplicate Booking Detection
feature_id: duplicate-booking-detection
category: Bookings & Duplicate Bookings
config_source: Policy Config (Corporate Entitlement Service) + Corporate Config
configurable: true
status: in-development
target_release_date: 2026-07-12
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - enableRestrictDuplicateBooking
  - duplicateBookingRules
  - enable_admin_restrict_duplicate_booking
  - flight_overlap_buffer
tags:
  - duplicate booking
  - overlapping trips
  - double booking
  - clash detection
  - flight overlap
  - same-day check-in
  - booking conflict
  - travel clash
  - duplicate restriction
  - overlap buffer
---

# Duplicate Booking Detection

## Summary
Duplicate Booking Detection spots when the same traveller is about to be booked for trips that overlap in time — for example two flights that cover the same window, or two hotels with check-ins on the same day. When the system finds such a clash it can either warn the booker or hard-block the duplicate, helping companies avoid wasted spend and accidental double bookings.

## What this feature does
When a booking is being made, the system checks the traveller's existing trips for time conflicts and decides what to do:

- **Warn** – the booker is shown a notice that a clashing trip already exists but can still proceed.
- **Hard-block** – the duplicate booking is prevented entirely until the clash is resolved.

It looks for two main kinds of clashes:
- **Flight overlap** – two flight segments that cover the same time window for the same traveller. A configurable **flight-overlap buffer (in minutes)** defines how much overlap is treated as a genuine clash, so minor gaps don't trigger false alarms.
- **Same-day hotel check-ins** – more than one hotel check-in for the same traveller on the same day.

The behaviour is driven from two places working together: the **policy-level rules and buffer** decide what counts as a duplicate, and a **corporate-level admin toggle** turns the restriction on for the company.

## Customer experience
- When a booker tries to create a booking that clashes with an existing trip, they see a clear duplicate-booking message.
- Depending on the configuration they are either allowed to continue (warning) or stopped (hard-block).
- The buffer setting means small, harmless overlaps don't get flagged, keeping the experience smooth for genuine itineraries.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (rules & overlap buffer) and **Corporate Config** (admin toggle) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — enabled and tuned per company |

## Which team to connect with
**👉 Onboarding Team**

Both pieces of this feature — the **Policy Config** rules/buffer and the **Corporate Config** admin toggle — are owned by the **Onboarding Team**. A salesperson who wants to enable duplicate detection for a customer, switch between warn and block, or adjust the flight-overlap buffer should reach out to Onboarding.

> This is not a whitelisting feature, so the Tech Team is not involved. Both config sources here sit with Onboarding.

## Related / dependent settings
These work alongside duplicate detection and may also need to be set:

- **Flight-Overlap Buffer** – the minutes of overlap that count as a clash (`flight_overlap_buffer`).
- **Duplicate Booking Rules** – the policy-level definition of what is treated as a duplicate (`duplicateBookingRules`).
- **Admin Restrict Toggle** – the company-level switch that activates the restriction (`enable_admin_restrict_duplicate_booking`).
- **Trip Approval Workflow** – approvals can still apply on top of duplicate checks.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config (Corporate Entitlement Service) + Corporate Config
- **Key fields:**
  - `enableRestrictDuplicateBooking` (Policy) — turns on duplicate restriction at policy level
  - `duplicateBookingRules` (Policy) — rule set defining what counts as a duplicate
  - `enable_admin_restrict_duplicate_booking` (Corporate Config) — admin-level toggle for the company
  - `flight_overlap_buffer` (Corporate Config) — minutes of flight overlap that qualify as a clash
- Evaluated against the traveller's existing trips in trip-management-service at booking time.

## Sample questions this feature answers
- "Can we stop a traveller from being booked on two overlapping flights?"
- "Does the system warn or block duplicate bookings?"
- "How do we detect same-day hotel check-ins for the same person?"
- "What is the flight overlap buffer and how do I change it?"
- "Can duplicate detection be turned on per company?"
- "Who do I contact to enable duplicate booking restrictions?"
- "Can we just warn instead of hard-blocking duplicates?"
