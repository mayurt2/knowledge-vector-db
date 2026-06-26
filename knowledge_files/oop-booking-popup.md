---
feature_name: Out-of-Policy Booking Popup
feature_id: oop-booking-popup
category: Out-of-Policy (OOP) Handling
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-05-21
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - trip-management-service
  - corporate-entitlement-service
  - sales-service
technical_keys:
  - enable_oop_popup
tags:
  - out of policy
  - OOP
  - policy breach
  - popup
  - justification
  - acknowledgement
  - policy warning
  - non-compliant booking
  - travel policy
  - booking prompt
---

# Out-of-Policy Booking Popup

## Summary
When a fare or rate breaches the company's travel policy, this feature shows the traveller an out-of-policy (OOP) popup. The traveller must acknowledge it — and often provide a justification or reason — before they can proceed with the booking. It ensures policy breaches are visible and consciously confirmed.

## What this feature does
When a booking option breaks a policy rule, the platform interrupts the flow with an OOP popup:

- **Popup enabled** – the traveller sees a clear out-of-policy notice and must acknowledge/justify before continuing.
- **Popup disabled** – no interrupt is shown for the breach (subject to other OOP controls).

This makes out-of-policy choices deliberate and captures a reason that can flow into approvals and reporting.

## Customer experience
- When a chosen fare or rate is out of policy, the traveller is shown a popup explaining the breach.
- They acknowledge it and, where required, enter a justification before proceeding.
- The captured reason supports downstream approval and visibility.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — enabled per company |

## Which team to connect with
**👉 Onboarding Team**

This is a **Corporate Config** toggle, so the **Onboarding Team** owns it. A salesperson who wants to enable the out-of-policy popup for a customer should reach out to Onboarding.

> This is not a whitelisting feature, so the Tech Team is not involved.

## Related / dependent settings
These work alongside the OOP popup:

- **OOP Popup Toggle** – enables the out-of-policy popup (`enable_oop_popup`).
- **Disable OOP Toggle** – controls whether travellers can flip an out-of-policy toggle.
- **Hide/Disable OOP Option** – removes the out-of-policy booking option entirely.
- **OOP Approval Routing** – routes out-of-policy bookings to a dedicated approval chain.
- **Policy Config** – defines what counts as out of policy.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `enable_oop_popup` — shows the out-of-policy acknowledgement/justification popup on a policy breach
- Triggered during booking when a fare/rate breaches policy.

## Sample questions this feature answers
- "What happens when a traveller picks an out-of-policy fare?"
- "Can we show a popup when a booking breaches policy?"
- "Does the traveller have to justify an out-of-policy choice?"
- "How do we make policy breaches visible at booking?"
- "Is the OOP popup configurable per company?"
- "Who do I contact to enable the out-of-policy popup?"
- "Can we capture a reason for out-of-policy bookings?"
