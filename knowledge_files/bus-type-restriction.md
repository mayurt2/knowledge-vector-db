---
feature_name: Bus Type Restriction
feature_id: bus-type-restriction
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-05-18
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - BusEntitlementsEntity.busType
tags:
  - bus type
  - bus restriction
  - AC bus
  - sleeper bus
  - bus category
  - bus policy
  - bus booking
  - travel class
  - spend limit
  - travel policy
---

# Bus Type Restriction

## Summary
This feature lets a company control which categories of bus its employees are allowed to book — for example, restricting bookings to certain AC or sleeper bus types. It keeps bus travel aligned with the company's comfort and cost expectations by limiting the bus types available at booking time.

## What this feature does
When an employee searches for or books a bus, the system checks the company's allowed bus types and only permits bookings that match:

- **Bus type** – the set of permitted bus categories (such as AC, non-AC, seater, or sleeper variants) that employees are allowed to book.

Buses that fall outside the permitted types are either filtered out or treated as out-of-policy, depending on the company's wider policy settings. This ensures employees book the class of bus the company intends to cover.

## Customer experience
- Employees see bus options filtered to (or flagged against) the bus types their company permits.
- A booking that matches an allowed bus type proceeds normally.
- A booking outside the allowed types is treated as out-of-policy and follows the company's out-of-policy rules (such as requiring approval).

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because permitted bus types are part of the company's travel **Policy Config**, a salesperson who wants to set or change which bus categories a customer's employees can book should reach out to the **Onboarding Team**.

> Use the Tech Team only for whitelisting-based features. Bus type restriction is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside the bus type restriction and may also need to be set:

- **Route Source–Destination Caps** – override the bus budget and advance-days for specific routes (`BusSourceDestinationEntitlementEntity`).
- **Modification Buffer Limits** – tolerances that allow small changes without re-approval.
- **Trip Approval Workflow** – approval routing for out-of-policy bus bookings.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `BusEntitlementsEntity.busType` — the permitted bus type(s) employees may book
- Snapshotted onto the trip's policy configuration in trip-management-service at trip creation.

## Sample questions this feature answers
- "Can we restrict which bus types employees can book?"
- "Can we limit employees to AC or sleeper buses only?"
- "What happens if an employee picks a bus type that isn't allowed?"
- "How do we set the allowed bus categories for a customer?"
- "Can bus type rules vary by employee group?"
- "Who do I contact to change the allowed bus types?"
- "Is the bus type restriction configurable per company?"
