---
feature_name: Self Booking Tool (SBT)
feature_id: self-booking-tool-sbt
category: Self Booking Tool (SBT)
config_source: Corporate Config + Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-04-07
status_last_updated: 2026-06-26
contact_team: Onboarding Team + Tech Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - isSbtEnabled
  - whitelisted.companyId.for.sbt
  - whitelisted.approval.managers.for.sbt
tags:
  - self booking tool
  - SBT
  - self service booking
  - employee booking
  - book travel
  - SBT approver
  - corporate policy
  - automated approval
  - travel booking
  - self-serve
---

# Self Booking Tool (SBT)

## Summary
The Self Booking Tool (SBT) lets employees search and book their own travel within the company's travel policy, with approvals applied automatically. Whether SBT is available, and which managers can act as SBT approvers, can be gated per corporate using a mix of corporate configuration and whitelisting.

## What this feature does
SBT puts the booking flow directly in the hands of employees, while keeping policy and approvals in place:

- **Self-service search & book** – employees find and book travel themselves.
- **Policy applied automatically** – the company's travel policy governs what they can book.
- **Approvals applied automatically** – the relevant approval flow runs without manual setup per booking.

Availability and approver control are gated in two ways:
- **Enablement (Corporate Config)** – `isSbtEnabled` turns SBT on for the company.
- **Whitelisting (Secret Manager)** – which companies can use SBT and which managers act as SBT approvers are controlled by whitelist keys.

## Customer experience
- Employees at SBT-enabled companies search and book travel on their own.
- Policy rules shape the available options, and approvals are applied automatically.
- Designated managers act as approvers for SBT bookings where whitelisted.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** (enablement) and **Whitelisting** (company & approver lists) |
| Who configures it? | Onboarding Team (enablement) and Tech Team (whitelists) |
| Is it per-company? | Yes — enabled and gated per company |

## Which team to connect with
**👉 Onboarding Team (enablement) and Tech Team (whitelists)**

This feature spans two config sources, so two teams are involved:

- **Onboarding Team** – owns the **Corporate Config** enablement (`isSbtEnabled`). Contact them to switch SBT on for a company.
- **Tech Team** – owns the **whitelisting keys in Secret Manager** that control which companies can use SBT and which managers are SBT approvers. Contact them to add or change those whitelists.

> Because SBT uses both Corporate Config and Whitelisting, route enablement requests to Onboarding and whitelist (company/approver) requests to Tech.

## Related / dependent settings
These work alongside SBT:

- **SBT Enablement** – turns SBT on for the company (`isSbtEnabled`).
- **SBT Company Whitelist** – which companies can use SBT (`whitelisted.companyId.for.sbt`).
- **SBT Approver Whitelist** – which managers act as SBT approvers (`whitelisted.approval.managers.for.sbt`).
- **Trip Approval Workflow** – the approval chain that SBT bookings flow through.
- **Travel Policy / Policy Config** – defines what employees can book via SBT.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config (enablement) + Whitelisting — Secret Manager Keys
- **Key fields:**
  - `isSbtEnabled` (Corporate Config) — enables the Self Booking Tool for the company
  - `whitelisted.companyId.for.sbt` (Whitelisting) — company IDs permitted to use SBT
  - `whitelisted.approval.managers.for.sbt` (Whitelisting) — managers permitted to act as SBT approvers
- Enablement is checked at corporate level; whitelist keys gate company and approver eligibility.

## Sample questions this feature answers
- "What is the Self Booking Tool?"
- "Can employees book their own travel within policy?"
- "How do we enable SBT for a company?"
- "Who can act as an SBT approver?"
- "Which team handles SBT enablement versus the whitelists?"
- "Is SBT gated per company?"
- "Who do I contact to add a company or approver to SBT?"
- "Are approvals applied automatically in SBT?"
