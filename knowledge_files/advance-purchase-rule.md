---
feature_name: Advance Purchase Rule
feature_id: advance-purchase-rule
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-05-29
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - FlightEntitlementsEntity.advanceDays
  - HotelEntitlementsEntity.advanceDays
  - CabEntitlementsEntity.advanceDays
  - BusEntitlementsEntity.advanceDays
  - TrainEntitlementsEntity.advanceDays
tags:
  - advance purchase
  - advance days
  - advance booking
  - lead time
  - book in advance
  - early booking
  - last minute
  - out-of-policy
  - travel policy
  - booking window
---

# Advance Purchase Rule

## Summary
The Advance Purchase Rule requires bookings to be made a minimum number of days before the travel date. The idea is to encourage early booking, which is usually cheaper. If an employee books too close to the travel date (fewer than the required advance days), the trip falls out of policy. This is set per travel mode.

## What this feature does
When an employee makes a booking, the system compares how many days are left until travel against the minimum advance days configured for that mode:

- **Booked early enough** (at or beyond the required advance days) – the booking is in-policy.
- **Booked too late** (fewer than the required advance days) – the booking is flagged out-of-policy. Depending on the company's broader rules, it may require approval, show a warning, or be disallowed.

Because it is set per mode, a company can require, say, 7 days advance notice for flights but a shorter window for cabs. This helps reduce last-minute, higher-cost bookings.

## Customer experience
- Employees booking well ahead of travel see no issue.
- Employees booking close to the travel date are warned that the booking is out-of-policy and may need approval or a reason.
- Different employee groups can have different advance-day requirements within the same company.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because the advance purchase requirement is part of the company's travel **Policy Config**, a salesperson who wants to set or change the minimum advance-booking days for a customer should reach out to the **Onboarding Team**. They configure the advance-days value per travel mode and employee group.

> Use the Tech Team only for whitelisting-based features. The advance purchase rule is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside the advance purchase rule:

- **Travel Mode Eligibility** – the mode must be Allowed before the rule applies.
- **Spend / Budget Cap** – another in-policy/out-of-policy check on the same booking.
- **Trip Approval Workflow** – out-of-policy (late) bookings are typically routed for approval.
- **Price Hike Tolerance Limit** – guards against price changes near the travel date.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `FlightEntitlementsEntity.advanceDays` — minimum days before travel for flights
  - `HotelEntitlementsEntity.advanceDays` — minimum days for hotels
  - `CabEntitlementsEntity.advanceDays` — minimum days for cabs
  - `BusEntitlementsEntity.advanceDays` — minimum days for bus
  - `TrainEntitlementsEntity.advanceDays` — minimum days for train
- Evaluated at booking time; bookings inside the window flagged out-of-policy and routed per approval config in trip-management-service.

## Sample questions this feature answers
- "Can we require employees to book flights at least 7 days in advance?"
- "What happens if an employee books at the last minute?"
- "How do I set a minimum advance-booking window for a company?"
- "Can different travel modes have different advance-day rules?"
- "Is the advance purchase rule configurable?"
- "How do we discourage last-minute bookings?"
- "Who do I contact to change the advance-booking policy for a customer?"
