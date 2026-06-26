---
feature_name: Skip In-Policy Approvals
feature_id: skip-in-policy-approvals
category: Approvals
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-06-03
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - skipInPolicyApprovers
  - skipInPolicyApproversIntnl
tags:
  - skip approval
  - in-policy approval
  - auto-approve
  - bypass approval
  - policy compliant
  - out-of-policy approval
  - faster booking
  - approval exemption
  - compliant bookings
  - domestic approval
  - international approval
  - approval automation
---

# Skip In-Policy Approvals

## Summary
Skip In-Policy Approvals lets compliant trips **bypass the approval chain entirely**. When a booking falls fully within the company's travel policy, there is no need to slow it down with manual sign-offs — it is auto-approved. Only **out-of-policy** trips are then routed to approvers for manual review. This dramatically speeds up the booking experience for employees who book within the rules, while keeping oversight focused where it matters. It can be configured separately for **domestic** and **international** trips.

## What this feature does
When a trip is created, the system checks whether the booking is within the company's travel policy:

- **In-policy trip** – if Skip In-Policy Approvals is enabled, the trip skips the approval chain and proceeds straight to booking.
- **Out-of-policy trip** – the trip is routed through the normal approval chain so an approver can review the breach.
- **Domestic vs international** – the behaviour is controlled independently for each, so a company can auto-approve in-policy domestic trips while still requiring approval for international trips (or vice versa) using `skipInPolicyApprovers` and `skipInPolicyApproversIntnl`.

The result is that approvers only spend time on trips that actually breach policy, while compliant bookings flow through automatically.

## Customer experience
- Employees who book within policy see their trips approved instantly with no waiting on a manager.
- Employees who book outside policy still go through the standard approval flow.
- Approvers receive far fewer requests — only the trips that genuinely need a decision — reducing approval fatigue and stalled trips.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, separately for domestic and international |

## Which team to connect with
**👉 Onboarding Team**

Because this is part of the company's travel **Policy Config**, a salesperson who wants to enable auto-approval of in-policy trips for a customer should reach out to the **Onboarding Team**. They turn the setting on or off and decide whether it applies to domestic trips, international trips, or both.

> Use the Tech Team only for whitelisting-based features. Skip In-Policy Approvals is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside Skip In-Policy Approvals and may also need to be set:

- **Trip Approval Workflow** – the core approval setup that applies when a trip is *not* skipped (`noOfApprovers`, `noOfApproversIntnl`).
- **Approver Chain Definition** – defines who reviews out-of-policy trips (`EntitlementApproversEntity`).
- **Skip Cost-Center / Project-Code Approver** – separately bypass cost-center or project-code owner approval steps.
- **Out-of-Policy (OOP) Approval Routing** – the path that out-of-policy trips follow when they are not skipped.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `skipInPolicyApprovers` — when enabled, in-policy **domestic** trips bypass the approval chain
  - `skipInPolicyApproversIntnl` — when enabled, in-policy **international** trips bypass the approval chain
- Evaluated at trip creation in trip-management-service; only trips flagged as out-of-policy are routed to approvers.

## Sample questions this feature answers
- "Can in-policy trips skip approval?"
- "Do compliant bookings still need a manager sign-off?"
- "How do we make booking faster for trips within policy?"
- "Can we auto-approve domestic trips but not international ones?"
- "Why are only out-of-policy trips going to approvers?"
- "How do I reduce the number of approvals a manager gets?"
- "Is skip-in-policy approval configurable separately for international travel?"
