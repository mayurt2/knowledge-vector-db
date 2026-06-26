---
feature_name: Disable Out-of-Policy Toggle
feature_id: disable-oop-toggle
category: Out-of-Policy (OOP) Handling
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-06-19
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - trip-management-service
  - corporate-entitlement-service
  - sales-service
technical_keys:
  - oop_toggle_disable
tags:
  - out of policy
  - OOP
  - OOP toggle
  - in-policy only
  - policy enforcement
  - hide toggle
  - compliant booking
  - travel policy
  - booking options
  - policy control
---

# Disable Out-of-Policy Toggle

## Summary
This feature controls whether travellers can flip an "out of policy" toggle to view and book options that fall outside the company travel policy. When the disable setting is ON, the toggle is hidden so employees only ever see in-policy options.

## What this feature does
The platform normally offers a toggle that lets a traveller switch to seeing out-of-policy options. This setting governs that toggle:

- **Disable ON** – the out-of-policy toggle is hidden; travellers see only in-policy options.
- **Disable OFF** – the toggle is available, so travellers can choose to view out-of-policy options.

It is a way to tighten compliance by removing the option to even browse out-of-policy choices.

## Customer experience
- With the toggle disabled, travellers only see options that comply with company policy — there is no switch to reveal out-of-policy choices.
- With it enabled, travellers can flip the toggle to view out-of-policy options.
- The setting shapes the choices presented during search and booking.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

This is a **Corporate Config** toggle, so the **Onboarding Team** owns it. A salesperson who wants to hide the out-of-policy toggle for a customer (in-policy only) should reach out to Onboarding.

> This is not a whitelisting feature, so the Tech Team is not involved.

## Related / dependent settings
These work alongside the OOP toggle control:

- **OOP Toggle Disable** – hides the out-of-policy toggle (`oop_toggle_disable`).
- **OOP Booking Popup** – warns/justifies on a policy breach.
- **Hide/Disable OOP Option** – removes the out-of-policy booking option entirely.
- **OOP Approval Routing** – routes out-of-policy bookings to a dedicated approval chain.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `oop_toggle_disable` — when ON, hides the out-of-policy toggle so only in-policy options are shown
- Applied to the search/booking options view.

## Sample questions this feature answers
- "Can we stop travellers from seeing out-of-policy options?"
- "How do we hide the out-of-policy toggle?"
- "Can we show only in-policy options to employees?"
- "What does the OOP toggle do?"
- "Is the out-of-policy toggle configurable per company?"
- "Who do I contact to disable the OOP toggle?"
- "How do we tighten policy compliance at search?"
