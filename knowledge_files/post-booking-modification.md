---
feature_name: Post-Booking Modification
feature_id: post-booking-modification
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-04-25
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - FlightEntitlementsEntity.modification
  - HotelEntitlementsEntity.modification
tags:
  - modification
  - post-booking modification
  - amend booking
  - change booking
  - reschedule
  - date change
  - modify trip
  - flight modification
  - hotel modification
  - travel policy
---

# Post-Booking Modification

## Summary
Post-Booking Modification controls whether an already-booked trip can be changed after it is confirmed — for example, rescheduling a flight or amending hotel dates. It applies to Flights and Hotels. When modification is turned off, a confirmed booking is locked and cannot be amended (the employee would need to cancel and rebook, subject to those rules).

## What this feature does
After a flight or hotel is booked, the system checks whether modification is permitted for that mode in the company's policy:

- **Modification allowed** – the employee can change the confirmed booking (such as flight date/time or hotel stay dates), subject to airline/hotel rules and fare differences.
- **Modification not allowed** – the confirmed booking is locked; no in-place changes are possible.

This lets companies decide how much flexibility employees have after booking. Allowing modifications is convenient but can incur change fees and fare differences, so some companies prefer to restrict it.

## Customer experience
- Where modification is allowed, the employee can request a change to their confirmed flight or hotel booking and see any applicable fare difference or fee.
- Where it is not allowed, the modification option is unavailable on the confirmed booking.
- Flights and hotels can have different modification settings, and different employee groups can differ too.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because post-booking modification is part of the company's travel **Policy Config**, a salesperson who wants to allow or restrict changes to confirmed flight/hotel bookings should reach out to the **Onboarding Team**. They configure the modification setting for flights and hotels per employee group.

> Use the Tech Team only for whitelisting-based features. Post-booking modification is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside post-booking modification:

- **Cancel Trip Without Approval** – the related control for cancelling (rather than changing) a booked trip.
- **Trip Approval Workflow** – modifications can be subject to approval depending on the company's setup.
- **Price Hike Tolerance Limit** – relevant when a modification changes the fare/rate.
- **Travel Mode Eligibility** – the mode must be Allowed in the first place.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `FlightEntitlementsEntity.modification` — whether confirmed flights can be modified
  - `HotelEntitlementsEntity.modification` — whether confirmed hotel bookings can be modified
- Evaluated when a modification is requested in trip-management-service; subject to supplier (airline/hotel) rules.

## Sample questions this feature answers
- "Can employees change a flight after booking?"
- "How do I allow hotel date changes after booking?"
- "Can we lock confirmed bookings so they can't be modified?"
- "Do flights and hotels have separate modification settings?"
- "Is post-booking modification configurable?"
- "What happens when modification is turned off?"
- "Who do I contact to allow booking changes for a customer?"
