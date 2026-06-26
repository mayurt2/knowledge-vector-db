---
feature_name: Travel Mode Eligibility
feature_id: travel-mode-eligibility
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-06-06
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - FlightEntitlementsEntity.entitlementEligibilityEnum
  - HotelEntitlementsEntity.entitlementEligibilityEnum
  - CabEntitlementsEntity.entitlementEligibilityEnum
  - BusEntitlementsEntity.entitlementEligibilityEnum
  - TrainEntitlementsEntity.entitlementEligibilityEnum
tags:
  - travel mode
  - eligibility
  - allowed mode
  - flight eligibility
  - hotel eligibility
  - cab eligibility
  - bus eligibility
  - train eligibility
  - mode access
  - travel policy
  - booking permission
---

# Travel Mode Eligibility

## Summary
Travel Mode Eligibility controls which types of travel an employee is even allowed to book. For each mode — Flight, Hotel, Cab, Bus, Train — the company can switch it on (Allowed) or off (Not-Allowed). If a mode is Not-Allowed, employees in that policy simply cannot raise a booking for it. This is the most basic policy gate that decides what shows up as a bookable option for an employee.

## What this feature does
When an employee opens the platform, the system reads the company's policy and checks the eligibility of each travel mode for that employee group:

- **Allowed** – the mode is available to book and appears as a normal option.
- **Not-Allowed** – the mode is hidden or blocked, and the employee cannot create a booking for it.

This is set independently for every mode, so a company can, for example, allow Flights and Hotels but block Cabs, or allow Train and Bus only for certain teams. It is the on/off master switch that sits above all the other per-mode policy rules (budget caps, advance purchase, class restrictions, and so on) — if a mode is Not-Allowed, none of those finer rules matter because the mode is unavailable in the first place.

## Customer experience
- Employees only see and can book the travel modes that are marked Allowed for their policy.
- If a mode is Not-Allowed, the employee will not be able to start a booking for it (the option is unavailable).
- Different employee groups within the same company can have different sets of allowed modes, so junior staff and senior staff may see different options.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because turning a travel mode on or off is part of the company's travel **Policy Config**, a salesperson who wants to enable or disable Flights, Hotels, Cabs, Bus, or Train for a customer should reach out to the **Onboarding Team**. They configure which modes are Allowed or Not-Allowed for each policy.

> Use the Tech Team only for whitelisting-based features. Mode eligibility is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These build on top of mode eligibility once a mode is Allowed:

- **Spend / Budget Cap** – the maximum amount allowed per booking for that mode.
- **Booking Process Mode** – whether the employee self-books or a travel desk books on their behalf.
- **Advance Purchase Rule** – minimum days before travel a booking must be made.
- **Flight Cabin Class Restriction** – which cabin classes are permitted (flight only).
- **Payment Configuration** – how the trip is paid for.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `FlightEntitlementsEntity.entitlementEligibilityEnum` — `ALLOWED` / `NOT_ALLOWED`
  - `HotelEntitlementsEntity.entitlementEligibilityEnum` — `ALLOWED` / `NOT_ALLOWED`
  - `CabEntitlementsEntity.entitlementEligibilityEnum` — `ALLOWED` / `NOT_ALLOWED`
  - `BusEntitlementsEntity.entitlementEligibilityEnum` — `ALLOWED` / `NOT_ALLOWED`
  - `TrainEntitlementsEntity.entitlementEligibilityEnum` — `ALLOWED` / `NOT_ALLOWED`
- Set per travel mode; snapshotted onto the trip's policy at trip creation in trip-management-service.

## Sample questions this feature answers
- "Can we block cab bookings for a company?"
- "How do I allow only flights and hotels for a customer?"
- "Why can't an employee book a train?"
- "Can different teams have different allowed travel modes?"
- "Is travel mode eligibility configurable?"
- "How do we turn off bus bookings for a policy?"
- "Who do I contact to enable a travel mode for a company?"
