---
feature_name: Skip Cost-Center / Project-Code Approver
feature_id: skip-cost-center-project-code-approver
category: Approvals
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-05-16
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - skipInCostCenterApprover
  - skipInProjectCodeApprover
tags:
  - skip cost center approver
  - skip project code approver
  - cost center owner
  - project code owner
  - bypass approval step
  - approval exemption
  - cost center approval
  - project code approval
  - approval chain
  - skip approver
  - finance approval
  - approval routing
---

# Skip Cost-Center / Project-Code Approver

## Summary
Some companies attach an automatic approval step to the **owner of a cost center** or the **owner of a project code** whenever a trip is charged to one. This feature lets a company optionally **bypass those specific approval steps** — the cost-center owner step, the project-code owner step, or both — while keeping the rest of the approval chain intact. It is useful when a company wants cost-object tracking on trips without forcing the cost-center or project-code owner to sign off on every booking.

## What this feature does
When a trip is associated with a cost center or project code, the system would normally route an approval to the relevant owner. This feature lets that be turned off selectively:

- **Skip cost-center owner approval** – when enabled, the cost-center owner is not added as an approver for the trip (`skipInCostCenterApprover`).
- **Skip project-code owner approval** – when enabled, the project-code owner is not added as an approver for the trip (`skipInProjectCodeApprover`).
- **Independent control** – each can be toggled on its own, so a company can skip the cost-center step while still keeping the project-code step (or the reverse).

The main approval chain (managers and other approvers) is unaffected — only these specific cost-object-driven steps are bypassed.

## Customer experience
- Employees booking trips against a cost center or project code do not have their trip held up waiting on that owner's sign-off.
- The approval path the employee sees is shorter, omitting the skipped owner step.
- Cost-center and project-code owners receive fewer approval requests, reducing bottlenecks for high-volume cost objects.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, independently for cost center and project code |

## Which team to connect with
**👉 Onboarding Team**

Because these are part of the company's travel **Policy Config**, a salesperson who wants to bypass the cost-center owner or project-code owner approval steps for a customer should reach out to the **Onboarding Team**. They toggle each skip setting independently.

> Use the Tech Team only for whitelisting-based features. Skipping cost-center / project-code approval is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside this feature and may also need to be set:

- **Trip Approval Workflow** – the core approval setup that the rest of the chain follows (`noOfApprovers`).
- **Approver Chain Definition** – defines the main approvers who remain in the chain (`EntitlementApproversEntity`).
- **Skip In-Policy Approvals** – separately bypass the whole chain for trips that are within policy.
- **Cost Object Additional Approver (Whitelisted)** – conversely, *adds* approvers based on cost object for whitelisted corporates.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `skipInCostCenterApprover` — when enabled, the cost-center owner approval step is bypassed
  - `skipInProjectCodeApprover` — when enabled, the project-code owner approval step is bypassed
- Evaluated at trip creation in trip-management-service; the skipped owner is simply not inserted into the trip's approver list.

## Sample questions this feature answers
- "Can we skip the cost-center owner approval?"
- "Can we bypass the project-code owner sign-off?"
- "Can we track cost centers without making the owner approve every trip?"
- "Can we skip cost-center approval but keep project-code approval?"
- "Why is the cost-center owner being asked to approve trips?"
- "How do I remove the project-code approval step for a customer?"
- "Is skipping cost-center / project-code approval configurable?"
