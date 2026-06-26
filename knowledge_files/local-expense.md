---
feature_name: Local Expense
feature_id: local-expense
category: Expense Management
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-03-30
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - local_expense
tags:
  - local expense
  - incidental expense
  - expense logging
  - out-of-pocket
  - reimbursement
  - travel expense
  - expense management
  - log expense
  - miscellaneous expense
  - expense claim
---

# Local Expense

## Summary
Local Expense enables travelers to log local and incidental expenses incurred during a trip — for example, meals, local transport, or other out-of-pocket costs that aren't part of the main booking. Turning this on gives a company a way for its travelers to capture these expenses on the platform alongside their trip.

## What this feature does
When enabled, travelers gain the ability to record local/incidental expenses:

- **Log local expenses** — travelers add expenses they incur during a trip beyond the core bookings.
- **Capture incidentals** — small or miscellaneous costs (meals, local transport, etc.) can be recorded in one place.
- **Tie expenses to the trip** — local expenses are associated with the traveler's trip, keeping spend organized.

This supports companies that want their travelers to track day-to-day travel spend on the platform.

## Customer experience
- Travelers can add local and incidental expenses while traveling.
- All trip-related spend is captured in one place, making it easier to review and process.
- Companies get better visibility into the full cost of a trip, not just the bookings.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

Because this is a **Corporate Config** setting, a salesperson who wants to enable local expense logging for a customer should reach out to the **Onboarding Team**. They control whether travelers can record local/incidental expenses.

> Use the Tech Team only for whitelisting-based features. This is a standard Corporate Config toggle, so it stays with Onboarding.

## Related / dependent settings
These work alongside local expense logging and may also be relevant:

- **Trip PDF Export** – export trip/expense details as a PDF (Corporate Config).
- **Legacy Expense Module (Whitelisted)** – keeps whitelisted companies on the legacy expense module (Whitelisting).
- **Trip Approval Workflow** – approvals may apply to trips and associated spend.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `local_expense` — when true, enables travelers to log local/incidental expenses.

## Sample questions this feature answers
- "Can travelers log local expenses like meals and local transport?"
- "How do I enable incidental expense logging for a customer?"
- "Can out-of-pocket costs be captured against a trip?"
- "Does this let travelers record expenses beyond the booking?"
- "Which team turns on local expense logging?"
- "Is local expense configurable per company?"
- "What does local_expense do?"
