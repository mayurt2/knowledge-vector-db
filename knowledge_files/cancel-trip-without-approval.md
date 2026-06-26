---
feature_name: Cancel Trip Without Approval
feature_id: cancel-trip-without-approval
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-06-09
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - tripCancelWithoutApprovalEligibilityEnum
  - FlightEntitlementsEntity.tripCancelWithoutApprovalEligibilityEnum
  - HotelEntitlementsEntity.tripCancelWithoutApprovalEligibilityEnum
tags:
  - cancellation
  - cancel trip
  - cancel without approval
  - cancellation policy
  - self cancel
  - approval to cancel
  - trip cancel
  - cancel permission
  - travel policy
  - booking cancellation
---

# Cancel Trip Without Approval

## Summary
This feature controls whether an employee can cancel a booked trip on their own, or whether cancelling requires approval first. It is set per travel mode, so a company can let employees freely cancel a cab but require sign-off before cancelling a flight, for example.

## What this feature does
When an employee asks to cancel a confirmed booking, the system checks the cancellation eligibility configured for that travel mode in the company's policy:

- **Allowed (without approval)** – the employee can cancel the trip themselves, no sign-off needed.
- **Not allowed (without approval)** – the cancellation must be approved by the designated approver before it goes through.

Because it is set per mode, companies can apply tighter control where cancellations are costly (such as non-refundable flights) while keeping low-stakes modes flexible. This protects the company from unnecessary cancellation losses while still allowing convenient self-service where appropriate.

## Customer experience
- For modes where self-cancellation is allowed, the employee can cancel directly and immediately.
- For modes where it is not allowed, the employee submits a cancellation request that an approver must review before it is actioned.
- Different employee groups can have different cancellation rules within the same company.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because the cancellation rule is part of the company's travel **Policy Config**, a salesperson who wants to set whether employees can self-cancel or must get approval should reach out to the **Onboarding Team**. They configure the cancel-without-approval eligibility per travel mode and employee group.

> Use the Tech Team only for whitelisting-based features. The cancellation rule is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside the cancellation rule:

- **Trip Approval Workflow** – defines the approvers who review cancellation requests when approval is required.
- **Post-Booking Modification** – the related control for changing (rather than cancelling) a booked trip.
- **Travel Mode Eligibility** – the mode must be Allowed in the first place.
- **Payment Configuration** – affects how refunds are handled after cancellation.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `tripCancelWithoutApprovalEligibilityEnum` — controls whether self-cancellation is permitted
  - Set per travel mode (e.g. `FlightEntitlementsEntity.tripCancelWithoutApprovalEligibilityEnum`, `HotelEntitlementsEntity.tripCancelWithoutApprovalEligibilityEnum`)
- Evaluated at cancellation time; cancellations requiring approval are routed per approval config in trip-management-service.

## Sample questions this feature answers
- "Can employees cancel a flight without approval?"
- "How do I require approval before a trip is cancelled?"
- "Can cancellation rules differ by travel mode?"
- "What happens when an employee tries to cancel a booked trip?"
- "Is the cancellation policy configurable?"
- "How do we stop employees from cancelling flights on their own?"
- "Who do I contact to change the cancellation policy for a customer?"
