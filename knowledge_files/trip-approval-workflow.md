---
feature_name: Trip Approval Workflow
feature_id: trip-approval-workflow
category: Approvals
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-06-04
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - noOfApprovers
  - noOfApproversIntnl
  - approverLevel
  - EntitlementApproversEntity
  - noOfAdditionalApprovers
tags:
  - approval
  - trip approval
  - multi-level approval
  - approver
  - manager approval
  - approval chain
  - approval hierarchy
  - sign-off
  - workflow
  - travel policy
---

# Trip Approval Workflow

## Summary
The Trip Approval Workflow controls how employee trip requests get reviewed and approved before any booking is confirmed. When an employee raises a trip, it can be routed to one or more approvers (such as their reporting manager or a designated approver) who must sign off before the trip is booked. This ensures every trip follows the company's travel policy and budget rules.

## What this feature does
When an employee creates a trip on the platform, the system checks the company's approval configuration and decides who needs to approve it:

- **No approval needed** – the trip proceeds straight to booking (used by companies that fully trust policy controls).
- **Single-level approval** – one approver (typically the reporting manager) reviews and approves before booking.
- **Multi-level approval** – the trip moves through a chain of up to **5 approvers** in sequence; each must approve before it reaches the next.

The approval setup can apply in two ways:
- **All services (Global)** – one approval setup applies to every type of booking (hotel, flight, bus, train, cab).
- **Service-wise (Trip-based)** – different approval rules for different services or trip types.

Domestic and international trips can also have **different numbers of approvers**, so a company can require stricter sign-off for international travel.

## Customer experience
- The employee sees the approval status of their trip (Pending, Approved, Rejected) and who it is currently waiting on.
- Approvers receive a request to review the trip and can approve or reject it, often with a reason.
- Only after all required approvals are completed is the booking confirmed (subject to other settings such as "trigger booking only after approval").

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because this is part of the company's travel **Policy Config**, a salesperson who wants to set up, change, or explain the approval workflow for a customer should reach out to the **Onboarding Team**. They configure the number of approvers, the approver chain, and whether approval is global or service-wise.

> Use the Tech Team only for whitelisting-based features. Approval workflow is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside the core approval workflow and may also need to be set:

- **Approver Chain Definition** – defines exactly who the approvers are and their order (`EntitlementApproversEntity`).
- **Additional Approvers** – an extra set of approvers beyond the main chain (`noOfAdditionalApprovers`).
- **Skip In-Policy Approvals** – auto-approve trips that are fully within policy, so only out-of-policy trips need manual approval.
- **Sub-Trip Approval** – approve each segment of a trip separately (Corporate Config).
- **Traveling-Manager Skip** – skip an approver who is themselves travelling on the trip (Corporate Config).
- **Out-of-Policy (OOP) Approval Routing** – special approval path for trips that breach policy.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `noOfApprovers` (NONE–FIVE) — number of domestic approvers
  - `noOfApproversIntnl` — number of international approvers
  - `approverLevel` — `GLOBAL` (All services) vs `TRIP_BASED` (Service-wise)
  - `EntitlementApproversEntity` — ordered approver definitions (approverOrder, approverType, approverUserId, applicableOn)
  - `noOfAdditionalApprovers` (ONE–FIVE) — additional approver count
- Snapshotted onto `TripConfigsEntity` / `TripMetadataEntity` in trip-management-service at trip creation.

## Sample questions this feature answers
- "How does trip approval work?"
- "Can we set up multi-level approval for a customer?"
- "Can domestic and international trips have different approvers?"
- "How many approvers can a trip have?"
- "Can approval be different for flights vs hotels?"
- "Who do I contact to change the approval flow for a company?"
- "Is the approval workflow configurable?"
