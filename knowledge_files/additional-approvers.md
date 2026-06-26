---
feature_name: Additional Approvers
feature_id: additional-approvers
category: Approvals
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-05-15
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - noOfAdditionalApprovers
  - EntitlementAdditionalApproversEntity
tags:
  - additional approvers
  - extra approvers
  - secondary approvers
  - additional sign-off
  - extra sign-off
  - supplementary approval
  - approval chain
  - approver count
  - special approval
  - second-line approver
  - approval hierarchy
  - extra reviewers
---

# Additional Approvers

## Summary
Additional Approvers let a company add a **secondary set of approvers** on top of its main approval chain. These are extra sign-offs that come into play for special cases — for example, when a trip needs an additional review beyond the standard manager hierarchy. The number of additional approvers is configurable from **ONE to FIVE**, so a company can layer on as many extra reviewers as its process requires.

## What this feature does
When a trip is created and the company has additional approvers enabled, the system appends an extra group of approvers to the approval flow beyond the main approver chain:

- **Configurable count** – a company chooses how many additional approvers are required, anywhere from **ONE to FIVE** (`noOfAdditionalApprovers`).
- **Defined separately** – the additional approvers themselves are defined as their own set (`EntitlementAdditionalApproversEntity`), distinct from the primary approver chain.
- **Extra sign-off layer** – these approvers act as a supplementary review, useful for special cases that need more oversight than the standard chain provides.

This is most often used when certain trips require sign-off from people who are not part of the regular reporting-manager hierarchy.

## Customer experience
- The employee sees the additional approvers as part of the overall approval path, after or alongside the main chain.
- Each additional approver receives the request and must sign off for the trip to proceed.
- The booking is only confirmed once both the main chain and the additional approvers have completed their reviews (subject to other settings).

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, with a configurable count of ONE–FIVE |

## Which team to connect with
**👉 Onboarding Team**

Because additional approvers are part of the company's travel **Policy Config**, a salesperson who wants to add, remove, or change the count of extra approvers for a customer should reach out to the **Onboarding Team**. They set the number of additional approvers and define who those approvers are.

> Use the Tech Team only for whitelisting-based features. Additional approvers are **not** a whitelisting feature, so they stay with Onboarding.

## Related / dependent settings
These work alongside additional approvers and may also need to be set:

- **Trip Approval Workflow** – the core setup that drives how the main chain operates (`noOfApprovers`).
- **Approver Chain Definition** – defines the primary approver chain that additional approvers sit on top of (`EntitlementApproversEntity`).
- **Skip In-Policy Approvals** – auto-approve in-policy trips so extra sign-offs are only triggered for out-of-policy trips.
- **Cost Object Additional Approver (Whitelisted)** – a separate cost-object-driven extra approver gated to specific corporates.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `noOfAdditionalApprovers` (ONE–FIVE) — number of additional approvers required
  - `EntitlementAdditionalApproversEntity` — the definitions of the additional approvers themselves
- Snapshotted onto the trip in trip-management-service at trip creation so the additional approver set is locked for that trip.

## Sample questions this feature answers
- "Can we add extra approvers beyond the manager chain?"
- "How many additional approvers can a company have?"
- "What are additional approvers used for?"
- "Can a trip require a second set of sign-offs?"
- "How do I add a supplementary approver for a customer?"
- "Is the number of additional approvers configurable?"
- "What's the difference between the main chain and additional approvers?"
