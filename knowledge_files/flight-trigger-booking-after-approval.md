---
feature_name: Flight Trigger Booking After Approval
feature_id: flight-trigger-booking-after-approval
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-05-13
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - FlightEntitlementsEntity.triggerBookingPostApproval
tags:
  - trigger booking after approval
  - book after approval
  - post approval booking
  - approval first
  - hold booking
  - book on approval
  - approval workflow
  - fare hold
  - travel policy
  - flight
---

# Flight Trigger Booking After Approval

## Summary
Flight Trigger Booking After Approval controls the order of approval and booking. When this is on, the actual flight booking is only placed once all required approvals are complete — instead of booking the flight first and approving afterwards. This avoids confirming (and paying for) a flight that may later be rejected. It is a flight-specific control that works hand in hand with the approval workflow.

## What this feature does
When an employee raises a flight that needs approval, the system uses this setting to decide when the booking actually happens:

- **On (trigger booking post-approval)** – the flight is not booked until every approval is complete; only then is the actual booking placed.
- **Off** – the flight may be booked first and approval handled around it (the default sequence without this control).

Booking only after approval prevents the company from holding or paying for flights that end up rejected, which reduces cancellation costs and rework. Because live fares can move between approval and booking, this setting typically pairs with the price-hike tolerance to handle any fare change at the time of the final booking.

## Customer experience
- When on, the employee's flight is confirmed only after approvers sign off; until then it is pending rather than booked.
- This means no flight is paid for or held until it is actually approved.
- Different employee groups can have this behaviour set differently within the same company.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because this booking-vs-approval sequencing is part of the company's travel **Policy Config**, a salesperson who wants flights to be booked only after approval for a customer should reach out to the **Onboarding Team**. They configure the trigger-booking-post-approval setting per employee group.

> Use the Tech Team only for whitelisting-based features. This setting is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside trigger-booking-after-approval:

- **Trip Approval Workflow** – defines the approvers whose sign-off gates the booking.
- **Price Hike Tolerance Limit** – handles fare changes between approval and final booking.
- **Travel Mode Eligibility** – flights must be Allowed in the first place.
- **Booking Process Mode** – who places the booking once approval is complete.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `FlightEntitlementsEntity.triggerBookingPostApproval` — when true, the actual flight booking is placed only after approval completes
- Coordinated with the approval workflow in trip-management-service; final booking triggered post-approval.

## Sample questions this feature answers
- "Can we book the flight only after approval is done?"
- "How do I stop flights from being booked before they're approved?"
- "What's the difference between booking first vs booking after approval?"
- "Does this avoid paying for flights that get rejected?"
- "Is trigger-booking-after-approval configurable?"
- "What happens to the fare if it changes before the post-approval booking?"
- "Who do I contact to enable book-after-approval for a customer?"
