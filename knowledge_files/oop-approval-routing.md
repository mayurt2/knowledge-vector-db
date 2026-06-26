---
feature_name: Out-of-Policy Approval Routing
feature_id: oop-approval-routing
category: Out-of-Policy (OOP) Handling
config_source: Corporate Config + Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-05-19
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - enable_oop_popup
  - oop_toggle_disable
  - disable_oop_option
tags:
  - out of policy
  - OOP
  - OOP approval
  - approval routing
  - exception approval
  - justification
  - policy breach
  - approver
  - approval chain
  - travel policy
---

# Out-of-Policy Approval Routing

## Summary
When a booking breaches policy, this feature routes it to a dedicated out-of-policy (OOP) approval chain along with a captured justification or reason. Approvers see the OOP tag and can approve or reject the exception, giving companies controlled handling of policy breaches.

## What this feature does
Out-of-policy bookings are treated differently from normal in-policy bookings in the approval flow:

- **OOP routing** – a booking that breaches policy is sent down a dedicated approval path.
- **Justification captured** – the reason the booking is out of policy travels with the request.
- **OOP tag** – approvers can clearly see the booking is an exception and approve or reject it accordingly.

This relies on two things working together: the **Corporate Config** controls the visibility/handling of out-of-policy bookings (popup, toggle, option), while the **Policy Config** defines what actually counts as out of policy.

## Customer experience
- A traveller making an out-of-policy booking provides a justification and submits it for approval.
- The request is routed to the OOP approval chain, clearly tagged as an exception.
- Approvers review the breach and reason, then approve or reject it.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** (visibility/handling) and **Policy Config** (what counts as OOP) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy and config |

## Which team to connect with
**👉 Onboarding Team**

Both config sources for this feature sit with Onboarding: the **Corporate Config** toggles that control out-of-policy visibility/handling, and the **Policy Config** that defines what counts as out of policy. A salesperson who wants to set up OOP approval routing for a customer should reach out to the **Onboarding Team**.

> This is not a whitelisting feature, so the Tech Team is not involved. Both the Corporate Config and Policy Config pieces are owned by Onboarding.

## Related / dependent settings
These work alongside OOP approval routing:

- **OOP Booking Popup** – warns/justifies on a policy breach (`enable_oop_popup`).
- **Disable OOP Toggle** – hides the toggle to view out-of-policy options (`oop_toggle_disable`).
- **Hide/Disable OOP Option** – removes the out-of-policy booking option entirely (`disable_oop_option`).
- **Policy Config** – defines the rules that determine what is out of policy.
- **Trip Approval Workflow** – the broader approval chain into which OOP routing fits.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config (visibility/handling) + Policy Config (Corporate Entitlement Service — what counts as OOP)
- **Key fields:**
  - `enable_oop_popup` (Corporate Config) — out-of-policy acknowledgement/justification popup
  - `oop_toggle_disable` (Corporate Config) — hides the out-of-policy toggle
  - `disable_oop_option` (Corporate Config) — removes the out-of-policy booking option
- Policy Config defines what counts as out of policy; out-of-policy bookings carry an OOP tag and justification into the approval chain.

## Sample questions this feature answers
- "How are out-of-policy bookings approved?"
- "Do out-of-policy bookings go to a special approval chain?"
- "Is a justification captured for policy exceptions?"
- "Can approvers see that a booking is out of policy?"
- "Where is what-counts-as-OOP defined versus how it's handled?"
- "Who do I contact to set up OOP approval routing?"
- "Can approvers reject an out-of-policy exception?"
