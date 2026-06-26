---
feature_name: Show Property Number & Hide Remarks
feature_id: show-property-number-hide-remarks
category: Bookings & Duplicate Bookings
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-06-08
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - trip-management-service
  - sales-service
  - corporate-entitlement-service
technical_keys:
  - show_property_number
  - hide_remarks
tags:
  - property number
  - hotel property
  - remarks
  - notes field
  - booking display
  - hotel booking
  - hide field
  - show field
  - booking details
  - display control
---

# Show Property Number & Hide Remarks

## Summary
This feature controls two display elements in the booking experience: it can show the hotel property number to travellers, and it can hide the remarks/notes field. Companies use these toggles to tailor what booking detail their travellers see.

## What this feature does
Two independent display controls can be set per company:

- **Show Property Number** – when on, the hotel's property number is displayed to travellers so they can identify the exact property.
- **Hide Remarks** – when on, the remarks/notes field is removed from the booking experience so travellers don't see (or enter) free-text remarks.

Together they let a company fine-tune the level of detail and the fields shown in hotel bookings.

## Customer experience
- Travellers see the hotel property number when "Show Property Number" is enabled, helping them identify the right property.
- The remarks/notes field is hidden when "Hide Remarks" is enabled, giving a cleaner booking screen.
- Both behaviours follow the company's configuration.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — each toggle is set per company |

## Which team to connect with
**👉 Onboarding Team**

Both toggles are **Corporate Config** settings, so the **Onboarding Team** owns them. A salesperson who wants to show the property number or hide the remarks field for a customer should reach out to Onboarding.

> These are not whitelisting features, so the Tech Team is not involved.

## Related / dependent settings
These control booking-screen display:

- **Show Property Number** – displays the hotel property number (`show_property_number`).
- **Hide Remarks** – removes the remarks/notes field (`hide_remarks`).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `show_property_number` — shows the hotel property number to travellers
  - `hide_remarks` — hides the remarks/notes field in the booking experience
- Applied to the hotel booking display.

## Sample questions this feature answers
- "Can we show the hotel property number to travellers?"
- "How do we hide the remarks field in bookings?"
- "Can these display options be set per company?"
- "Where do I turn on the property number display?"
- "How do I remove the notes field from the booking screen?"
- "Who do I contact to change these display settings?"
- "Are show-property-number and hide-remarks configurable?"
