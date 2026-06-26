---
feature_name: Cost Object Additional Approver (Whitelisted)
feature_id: cost-object-additional-approver-whitelisted
category: Approvals
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-04-20
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - trip-management-service
  - sales-service
  - corporate-entitlement-service
technical_keys:
  - additional.approver.enabeled.company.id
  - TripMetadataEntity.costObjectMappingApprover
tags:
  - cost object approver
  - cost object additional approver
  - project code approver
  - extra approver
  - whitelisted approver
  - cost center approver
  - additional sign-off
  - approval mapping
  - corporate whitelist
  - approval hierarchy
  - cost object mapping
  - special approval
---

# Cost Object Additional Approver (Whitelisted)

## Summary
For specific corporates, this feature attaches **extra approvers based on the cost object or project code** on a trip — on top of the normal manager hierarchy. If a trip is charged to a particular cost object, the approver(s) mapped to that cost object are added to the approval flow. Because it is a specialised behaviour, it is **gated to whitelisted companies** via a Secret Manager key, so only corporates that have been explicitly enabled get this routing.

## What this feature does
When a trip is created for a whitelisted corporate, the system looks at the cost object / project code on the trip and adds the approvers mapped to it:

- **Cost-object-driven approvers** – approvers are determined by the trip's cost object or project code, recorded via `TripMetadataEntity.costObjectMappingApprover`.
- **On top of the hierarchy** – these approvers are added in addition to the normal manager approval chain, not instead of it.
- **Whitelisted only** – the behaviour is enabled solely for company IDs present in the whitelist key `additional.approver.enabeled.company.id`; other corporates are unaffected.

This lets specific organisations enforce that whoever owns a given cost object always reviews trips charged to it, beyond standard reporting-line approvals.

## Customer experience
- For enabled corporates, employees see additional approvers appear automatically based on the cost object or project code they select for a trip.
- The cost-object owner(s) receive the approval request alongside the regular manager chain.
- Companies not on the whitelist see no change to their approval flow.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** (via whitelisting) |
| Where is it configured? | **Whitelisting** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — enabled only for whitelisted company IDs |

## Which team to connect with
**👉 Tech Team**

Because this feature is gated by a **whitelisting (Secret Manager) key**, a salesperson who wants to enable cost-object-based additional approvers for a customer should reach out to the **Tech Team**. They add the company ID to the `additional.approver.enabeled.company.id` whitelist that turns the behaviour on.

> Whitelisting features are owned by Tech, not Onboarding. The cost-object additional approver is enabled through a Secret Manager key, so it sits with the **Tech Team**.

## Related / dependent settings
These work alongside this feature and may also need to be set:

- **Additional Approvers** – the policy-config-based extra approver set (`noOfAdditionalApprovers`), configured by Onboarding, which is distinct from this whitelisted cost-object approver.
- **Skip Cost-Center / Project-Code Approver** – conversely *bypasses* cost-object owner approval (Policy Config, Onboarding).
- **Approver Chain Definition** – the base manager hierarchy these approvers are added on top of (`EntitlementApproversEntity`).
- **Trip Approval Workflow** – the core approval setup for the trip (`noOfApprovers`).

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `additional.approver.enabeled.company.id` — whitelist of company IDs for which cost-object additional approvers are enabled
  - `TripMetadataEntity.costObjectMappingApprover` — the approver(s) mapped to the trip's cost object / project code
- Evaluated in trip-management-service at trip creation; only applied when the trip's company ID is present in the whitelist key.

## Sample questions this feature answers
- "Can we add approvers based on the cost object on a trip?"
- "Can the project-code owner be added as an extra approver?"
- "Is the cost-object approver available for all corporates?"
- "How do we enable cost-object-based additional approvers for a company?"
- "Which team enables the cost-object additional approver?"
- "Does this add approvers on top of the manager chain?"
- "Why isn't the cost-object approver showing up for my customer?"
- "Is this feature whitelisted?"
