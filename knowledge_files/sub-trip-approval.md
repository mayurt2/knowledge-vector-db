---
feature_name: Sub-Trip Approval
feature_id: sub-trip-approval
category: Approvals
config_source: Corporate Config (Sales Service)
configurable: true
status: live
target_release_date: 2026-04-16
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - sales-service
  - trip-management-service
  - corporate-entitlement-service
technical_keys:
  - subtrip_approval
tags:
  - sub-trip approval
  - subtrip approval
  - segment approval
  - per-segment approval
  - itinerary approval
  - partial approval
  - independent approval
  - multi-segment trip
  - hotel approval
  - flight approval
  - approval workflow
  - granular approval
---

# Sub-Trip Approval

## Summary
Sub-Trip Approval changes how a multi-segment trip is approved. Instead of approving the **whole trip at once**, each sub-trip — an individual hotel, flight, bus, or other segment of the itinerary — is approved **separately**. This lets approvers sign off on parts of an itinerary independently, so an approved flight can move forward even while a hotel on the same trip is still awaiting review. It gives companies finer, segment-level control over their approval process.

## What this feature does
When a trip contains multiple segments and Sub-Trip Approval is enabled, the system breaks the approval into per-segment decisions:

- **Per-segment sign-off** – each sub-trip (hotel, flight, bus segment, etc.) goes through its own approval decision rather than being bundled into a single trip-level approval.
- **Independent progress** – approvers can approve or reject individual segments; one segment's status does not block the others.
- **Granular control** – useful for complex itineraries where different parts may need different scrutiny or move at different speeds.

This contrasts with the default behaviour, where the entire trip is approved or rejected as one unit.

## Customer experience
- The employee sees approval status broken down by segment, so they know exactly which parts of their trip are approved and which are still pending.
- An approved segment can proceed to booking even while another segment on the same trip waits for a decision.
- Approvers review and decide on each segment individually, which is clearer for mixed itineraries.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** (Sales Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — enabled per corporate via Corporate Config |

## Which team to connect with
**👉 Onboarding Team**

Because Sub-Trip Approval is part of the company's **Corporate Config**, a salesperson who wants to enable per-segment approval for a customer should reach out to the **Onboarding Team**. They turn the `subtrip_approval` setting on or off for the corporate.

> Use the Tech Team only for whitelisting-based features. Sub-Trip Approval is a Corporate Config setting, **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside Sub-Trip Approval and may also need to be set:

- **Trip Approval Workflow** – the core approval setup applied to each segment or the whole trip (`noOfApprovers`).
- **Approver Chain Definition** – defines who approves each segment (`EntitlementApproversEntity`).
- **Traveling-Manager Skip** – skip an approver who is themselves travelling on a segment (Corporate Config).
- **Skip In-Policy Approvals** – auto-approve segments that are fully within policy.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config — Sales Service
- **Key fields:**
  - `subtrip_approval` — when enabled, each sub-trip (segment) is approved independently rather than the trip being approved as a whole
- Applied in sales-service and reflected in the trip's approval state in trip-management-service, where each segment carries its own approval status.

## Sample questions this feature answers
- "Can each part of a trip be approved separately?"
- "Can a flight be approved while the hotel is still pending?"
- "What is sub-trip approval?"
- "Can approvers sign off on individual segments?"
- "Do we have to approve the whole itinerary at once?"
- "How do I enable per-segment approval for a customer?"
- "Is sub-trip approval configurable?"
