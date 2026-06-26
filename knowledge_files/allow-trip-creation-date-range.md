---
feature_name: Allow Trip Creation with Date Range
feature_id: allow-trip-creation-date-range
category: Bookings & Duplicate Bookings
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-06-01
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - trip-management-service
  - corporate-entitlement-service
  - sales-service
technical_keys:
  - allow_trip_creation_with_date_range
tags:
  - date range
  - flexible dates
  - trip creation
  - start date
  - end date
  - tentative trip
  - flexible booking
  - date window
  - planning
  - unknown dates
---

# Allow Trip Creation with Date Range

## Summary
This feature lets bookers create a trip using a flexible start and end date range instead of locking in fixed dates. It is useful when the exact travel dates aren't known yet — for example when a trip is being planned in advance and only a rough window is available.

## What this feature does
When enabled, the trip-creation flow accepts a date **range** (a start window and an end window) rather than a single fixed departure and return date:

- **Range allowed** – the booker can set up the trip against an approximate window and finalise specifics later.
- **Range not allowed** – the booker must provide exact dates up front (default behaviour).

This makes it easier to begin planning and routing a trip for approval before every detail is confirmed.

## Customer experience
- Bookers see the option to enter a date range when creating a trip.
- They can start the trip and proceed through planning/approval even without exact dates.
- For companies where this is off, the standard fixed-date flow applies.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — enabled per company |

## Which team to connect with
**👉 Onboarding Team**

This is a **Corporate Config** setting, so the **Onboarding Team** owns it. A salesperson who wants to let a customer create trips with flexible date ranges should reach out to Onboarding to enable it.

> This is not a whitelisting feature, so the Tech Team is not involved.

## Related / dependent settings
These work alongside flexible trip-date creation:

- **Date Range Toggle** – the company-level switch enabling range-based creation (`allow_trip_creation_with_date_range`).
- **Trip Approval Workflow** – approvals can run on the planned trip before dates are finalised.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `allow_trip_creation_with_date_range` — enables creating a trip with a start/end date range instead of fixed dates
- Applied at trip-creation time in trip-management-service.

## Sample questions this feature answers
- "Can a booker create a trip without exact dates?"
- "Does the platform support a date range for trips?"
- "How do we let customers plan trips with flexible dates?"
- "Can we enable tentative trip dates for a company?"
- "Is the date-range option configurable per company?"
- "Who do I contact to turn on flexible trip dates?"
- "What if the traveller doesn't know the exact dates yet?"
