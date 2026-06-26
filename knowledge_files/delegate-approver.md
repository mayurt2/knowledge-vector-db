---
feature_name: Delegate Approver
feature_id: delegate-approver
category: Approvals
config_source: Employee Management (Employee / Approver Profile)
configurable: true
status: live
target_release_date: 2026-05-10
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - sales-service
  - b2b-aggregation
  - trip-management-service
technical_keys:
  - delegatedApproverUserId (create/update employee API)
  - delegatedApproverEmail (bulk upload)
  - CorporateEmployeeEntity.delegatedApprover (column delegated_approver)
  - TripApproversEntity.delegatedUserId (column delegated_user_id)
  - TripApproversEntity.isApprovedByDelegatedApprover
tags:
  - delegate approver
  - delegation
  - delegate approval
  - approver delegate
  - backup approver
  - alternate approver
  - approve on behalf
  - manager on leave
  - out of office approval
  - approval workflow
  - employee management
---

# Delegate Approver

## Summary
Delegate Approver lets a manager/approver nominate another user as their **delegate**, so that person can approve or reject trips **on the approver's behalf**. This is most useful when an approver is on leave or unavailable — instead of trips getting stuck waiting for them, the delegate can keep approvals moving. Importantly, this is *shared* authority, not a transfer: both the original approver and the delegate can act on the same trips.

## What this feature does
Each approver can have one delegate set on their employee profile. Once a delegate is configured:

- **Both can act** – Trips that need the original approver's sign-off also appear in the delegate's approval queue. Either the original approver **or** the delegate can approve/reject.
- **Approvals are tracked** – When the delegate is the one who approves, the platform records that the step was **approved by the delegate** (not the manager), so there's a clear audit trail of who actually acted.
- **Notifications route to the delegate** – Approval-request and reminder notifications are also sent to the delegate, and pending-trip counts show up for them too.
- **Covers all approval types** – Delegation applies to standard approvers, **out-of-policy (OOP) approvers**, and **additional approvers** across all travel services (flight, hotel, cab, bus, train).

## Customer experience
- When a manager goes on leave, their delegate sees the manager's pending trips and can approve/reject them, so travel doesn't stall.
- The original manager still retains full access — delegation adds a second person who can act, it doesn't remove the manager.
- In trip details, it's visible when an approval was done by the delegate rather than the manager.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Employee Management** — on the approver's employee profile (the "delegated approver" field) |
| Who configures it? | Company admins (in the admin portal) and/or the Onboarding Team |
| Is it per-company? | It's **per-employee** — set on each approver's record, one delegate per approver |

## Which team to connect with
**👉 Onboarding Team** (company admins can also set it themselves)

Delegate Approver is configured at the **employee level**, not through policy or corporate config and it is **not a whitelisted feature** — so there's nothing for Tech to switch on. A delegate is set on the approver's employee record via **Employee Management**:
- **Company admins** can do this directly in the admin portal when creating or editing a user (or via bulk employee upload).
- For help setting it up — or applying it across many employees — sales should reach out to the **Onboarding Team**.

> Because this lives on the employee/approver profile, the way to "give a manager a delegate" is to set the delegated approver on **that manager's** user record.

## Related / dependent settings
- **Trip Approval Workflow** – delegation operates within the approval chain; without approvals there's nothing to delegate.
- **Approver Chain Definition** – defines the approvers who can each have a delegate.
- **Additional Approvers** – additional approvers can also have delegates.
- **Out-of-Policy (OOP) Approval Routing** – OOP approvers are covered by delegation too.
- **Traveling-Manager Skip** – another rule that affects who ends up approving a trip.

## Important notes / limitations
- **No date range:** delegation is a **standing** setting, not a vacation window. There's no automatic start/end date — once set, it stays active until the delegate field is **cleared** on the employee record. (Practical tip for customers: remember to remove the delegate when it's no longer needed.)
- **One delegate per approver:** each approver can have a single delegate (not multiple).
- **A user cannot be their own delegate** (the system blocks this).

## Technical reference (for Onboarding/Tech)
- **Source of truth (sales-service):** `CorporateEmployeeEntity.delegatedApprover` → column `delegated_approver` (self-referential FK to another employee).
- **Set via Employee Management APIs:**
  - Create/update user: request field `delegatedApproverUserId` (`POST /private/users/create`, `PUT /private/users/update`; admin gateway `POST/PUT v1/corporate/admin/users/{create,update}`).
  - Bulk upload: field `delegatedApproverEmail`.
  - Self-delegation is rejected ("Delegate approver can't be same as this user").
- **Propagation to trips (b2b-aggregation):** at approver resolution, `TripUtil.getApproverIds` / `getOutOfPolicyApproverIds` build `approverVsDelegatedApproverIds` / `outOfPolicyApproverVsDelegatedApproverIds` from the approver's profile and pass them to trip-management.
- **Runtime enforcement (trip-management-service):**
  - `TripApproversEntity.delegatedUserId` (column `delegated_user_id`) and `isApprovedByDelegatedApprover` (column `is_approved_by_delegated_approver`).
  - `TripRepository` approval-queue queries match `user_id = :userId OR delegated_user_id = :userId`.
  - `SelfBookingTripStatusUpdateServiceImpl` sets `approvedByDelegatedApprover = true` when the acting user is the delegate; `TripUtil` routes next-approver notifications to the delegate (`setSendToDelegateApprover(true)`).
- **Gating:** none — no feature flag or whitelist property controls delegation; it's available once a delegate is set on the employee record.

## Sample questions this feature answers
- "Can an approver delegate their approvals to someone else?"
- "What happens to approvals when a manager is on leave?"
- "Is there a backup/alternate approver?"
- "Can someone approve trips on a manager's behalf?"
- "How do I set up a delegate approver?"
- "Does the manager still get to approve if a delegate is set?"
- "Can I set a delegate for a date range / while on vacation?"
- "Does delegation cover out-of-policy approvals?"
- "Who do I contact to set up a delegate approver?"
