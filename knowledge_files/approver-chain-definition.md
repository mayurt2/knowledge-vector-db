---
feature_name: Approver Chain Definition
feature_id: approver-chain-definition
category: Approvals
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-06-07
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - EntitlementApproversEntity
  - approverOrder
  - approverType
  - approverUserId
  - applicableOn
tags:
  - approver chain
  - approval chain
  - approver order
  - approver sequence
  - designated approver
  - custom approver
  - service-wise approver
  - approval hierarchy
  - approver definition
  - reporting manager
  - sign-off order
  - approval routing
---

# Approver Chain Definition

## Summary
The Approver Chain Definition specifies exactly **who** approves an employee's trip and in **what order** they do so. While the Trip Approval Workflow decides *how many* approvers a trip needs, this feature names the actual people (or roles) in the chain and sequences them. Approvers can be set globally for all bookings, or customised per service (hotel, flight, bus, train, cab), giving a company precise control over who signs off on which kind of travel.

## What this feature does
When a trip is created and approval is required, the system reads the company's approver chain to build the sequence of sign-offs:

- **Ordered chain** – each approver is given a position (`approverOrder`) so the trip moves from approver 1, to approver 2, and so on until the chain is complete.
- **Approver type** – an approver can be a role-based approver (such as the reporting manager) or a specific named user, defined by `approverType`.
- **Specific person** – when a fixed individual must always approve, that user is pinned via `approverUserId`.
- **Where it applies** – `applicableOn` controls whether an approver applies globally (all services) or only to a particular service such as flights or hotels.

This lets a company say, for example, "for hotels, the manager approves first and then the travel desk; for flights, the manager approves first and then the finance head."

## Customer experience
- The employee can see the full approval path for their trip and exactly who it is currently waiting on.
- Each approver receives the request in the correct sequence — the next approver is only notified once the previous one has signed off.
- Because the chain can differ by service, an employee booking a flight may see a different set of approvers than the same employee booking a hotel.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can be defined globally or per service |

## Which team to connect with
**👉 Onboarding Team**

Because the approver chain lives in the company's travel **Policy Config**, a salesperson who wants to define, reorder, or change who approves a customer's trips should reach out to the **Onboarding Team**. They set up the ordered approver list, choose role-based versus named approvers, and decide whether the chain is global or service-specific.

> Use the Tech Team only for whitelisting-based features. The approver chain is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside the approver chain and may also need to be set:

- **Trip Approval Workflow** – decides how many approvers are required (`noOfApprovers`, `noOfApproversIntnl`).
- **Additional Approvers** – a secondary set of approvers beyond this main chain (`noOfAdditionalApprovers`).
- **Skip In-Policy Approvals** – auto-approve trips fully within policy so the chain is only invoked for out-of-policy trips.
- **Traveling-Manager Skip** – skip a chain approver who is themselves travelling on the trip (Corporate Config).
- **Sub-Trip Approval** – run the chain on each segment of a trip separately (Corporate Config).

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `EntitlementApproversEntity` — ordered approver definitions for the company
  - `approverOrder` — the position of each approver in the sequence
  - `approverType` — role-based vs specific-user approver
  - `approverUserId` — the specific user pinned as an approver
  - `applicableOn` — scope of the approver: global (all services) or a specific service (hotel/flight/bus/train/cab)
- Snapshotted onto the trip in trip-management-service at trip creation so the chain is locked for that trip.

## Sample questions this feature answers
- "Who actually approves a trip for this company?"
- "Can we set a custom approver for flights but a different one for hotels?"
- "In what order do approvers get the request?"
- "Can we pin a specific person as an approver?"
- "Can the approver be different per service?"
- "How do I change who signs off on a customer's trips?"
- "Is the approver chain configurable?"
- "Can we have a global approver for all bookings?"
