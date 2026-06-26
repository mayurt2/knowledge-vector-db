---
feature_name: Traveling-Manager Skip
feature_id: traveling-manager-skip
category: Approvals
config_source: Corporate Config (Sales Service)
configurable: true
status: live
target_release_date: 2026-04-22
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - sales-service
  - trip-management-service
  - corporate-entitlement-service
technical_keys:
  - skip_traveling_managers
tags:
  - traveling manager skip
  - skip traveling manager
  - self-approval
  - manager on trip
  - approver on trip
  - skip approver
  - approval chain
  - next approver
  - co-traveller manager
  - auto-skip approver
  - approval routing
  - manager approval
---

# Traveling-Manager Skip

## Summary
Traveling-Manager Skip prevents a manager from having to **approve a trip they are travelling on themselves**. When the approver who would normally sign off is also listed as a traveller on the same trip, the system automatically **skips** that approver — avoiding awkward self-approval — and passes the decision to the **next approver** in the chain. This keeps the approval process clean and compliant when managers travel alongside their team.

## What this feature does
When a trip is created and approval is required, the system checks whether any approver in the chain is also a traveller on that trip:

- **Detect self-approval** – if a manager/approver appears as a traveller on the same trip, they are flagged.
- **Automatic skip** – that approver is removed from the approval decision for this trip (`skip_traveling_managers`), so they are not asked to approve their own travel.
- **Pass to next approver** – approval automatically moves to the next approver in the chain, ensuring the trip still receives independent sign-off.

This is common when a manager and their direct reports travel together; the manager should not be the one approving their own seat on the trip.

## Customer experience
- A manager who is travelling on a trip is not bothered with an approval request for their own travel.
- The trip still gets reviewed — it simply routes to the next approver in line.
- Employees see a clean approval path without a redundant self-approval step.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** (Sales Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — enabled per corporate via Corporate Config |

## Which team to connect with
**👉 Onboarding Team**

Because Traveling-Manager Skip is part of the company's **Corporate Config**, a salesperson who wants to enable this behaviour for a customer should reach out to the **Onboarding Team**. They turn the `skip_traveling_managers` setting on or off for the corporate.

> Use the Tech Team only for whitelisting-based features. Traveling-Manager Skip is a Corporate Config setting, **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside Traveling-Manager Skip and may also need to be set:

- **Trip Approval Workflow** – the core approval setup that the next approver follows (`noOfApprovers`).
- **Approver Chain Definition** – defines the chain so the system knows who the "next approver" is (`EntitlementApproversEntity`).
- **Additional Approvers** – extra approvers who may still apply even when the traveling manager is skipped (`noOfAdditionalApprovers`).
- **Sub-Trip Approval** – per-segment approval that the skip logic also respects (Corporate Config).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config — Sales Service
- **Key fields:**
  - `skip_traveling_managers` — when enabled, any approver who is also a traveller on the trip is skipped, and approval passes to the next approver
- Evaluated in sales-service / trip-management-service when building the approver list for a trip.

## Sample questions this feature answers
- "What happens if the approving manager is also travelling on the trip?"
- "Can we avoid managers approving their own trips?"
- "Does the trip still get approved if the manager is a traveller?"
- "Who approves when the approver is on the trip themselves?"
- "Can we automatically skip an approver who is travelling?"
- "How do I enable traveling-manager skip for a customer?"
- "Is the traveling-manager skip configurable?"
