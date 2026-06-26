---
feature_name: Hide / Disable Out-of-Policy Option
feature_id: hide-disable-oop-option
category: Out-of-Policy (OOP) Handling
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-06-05
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - trip-management-service
  - corporate-entitlement-service
  - sales-service
technical_keys:
  - disable_oop_option
tags:
  - out of policy
  - OOP
  - disable OOP
  - block non-compliant
  - policy enforcement
  - remove option
  - compliant booking
  - travel policy
  - strict policy
  - no exceptions
---

# Hide / Disable Out-of-Policy Option

## Summary
This feature removes the out-of-policy booking option entirely, so non-compliant bookings simply cannot be made. It is the strictest of the out-of-policy controls — rather than warning or hiding a toggle, it takes away the ability to book outside policy at all.

## What this feature does
When this setting is on, the platform does not offer any path to book an out-of-policy option:

- **Disable ON** – out-of-policy bookings are not possible; only compliant bookings can be completed.
- **Disable OFF** – out-of-policy options remain available (subject to popup/toggle settings).

This gives companies a hard enforcement of their travel policy with no exceptions at booking time.

## Customer experience
- Travellers cannot select or complete an out-of-policy booking — the option is simply not there.
- Only in-policy options can be booked.
- This is the most restrictive setting compared to the OOP popup (warn) or OOP toggle (hide the switch).

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

This is a **Corporate Config** toggle, so the **Onboarding Team** owns it. A salesperson who wants to fully block out-of-policy bookings for a customer should reach out to Onboarding.

> This is not a whitelisting feature, so the Tech Team is not involved.

## Related / dependent settings
These work alongside disabling the OOP option:

- **Disable OOP Option** – removes the out-of-policy booking option entirely (`disable_oop_option`).
- **OOP Booking Popup** – warns/justifies on a policy breach (a softer control).
- **Disable OOP Toggle** – hides the toggle to view out-of-policy options.
- **OOP Approval Routing** – relevant only when out-of-policy bookings are allowed.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `disable_oop_option` — when ON, removes the out-of-policy booking option so non-compliant bookings cannot be made
- Applied to booking options so only in-policy bookings can be completed.

## Sample questions this feature answers
- "Can we completely block out-of-policy bookings?"
- "How do we stop non-compliant bookings entirely?"
- "What's the difference between disabling the OOP option and the OOP popup?"
- "Can we enforce strict policy with no exceptions?"
- "Is disabling the out-of-policy option configurable per company?"
- "Who do I contact to remove out-of-policy booking?"
- "How do we ensure only in-policy bookings are made?"
