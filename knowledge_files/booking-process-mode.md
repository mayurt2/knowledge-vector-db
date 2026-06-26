---
feature_name: Booking Process Mode
feature_id: booking-process-mode
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-04-24
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - bookingProcessModeEnum
  - FlightEntitlementsEntity.bookingProcessModeEnum
  - HotelEntitlementsEntity.bookingProcessModeEnum
tags:
  - booking process
  - travel desk
  - self booking
  - self-book
  - travel desk led
  - agent booking
  - booking mode
  - who books
  - travel policy
  - managed booking
---

# Booking Process Mode

## Summary
Booking Process Mode controls who actually makes the booking for a given travel mode — the employee themselves (Self-Book) or a company travel desk that books on the employee's behalf (Travel-Desk-Led). This is set per mode, so a company can let employees self-book flights while routing hotels through a travel desk, for example.

## What this feature does
When an employee wants to travel, the system checks the booking process mode configured for that travel mode in the company's policy:

- **Self-Book** – the employee searches and books directly on the platform.
- **Travel-Desk-Led** – the employee raises a request, and a designated travel desk team completes the booking on their behalf.

Because it is set per mode, a company can mix the two approaches — for instance, self-booking for cabs and trains, but travel-desk-led for international flights where more oversight is wanted. This lets companies balance employee convenience with central control.

## Customer experience
- In Self-Book mode, the employee completes the booking themselves end to end.
- In Travel-Desk-Led mode, the employee submits their travel need and the travel desk handles the actual booking, keeping the employee informed of status.
- Different modes (and different employee groups) can use different booking processes within the same company.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because the booking process is part of the company's travel **Policy Config**, a salesperson who wants to switch a customer between self-booking and travel-desk-led booking should reach out to the **Onboarding Team**. They configure the booking process mode for each travel mode and employee group.

> Use the Tech Team only for whitelisting-based features. Booking process mode is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside booking process mode:

- **Travel Mode Eligibility** – the mode must be Allowed before a booking process applies.
- **Trip Approval Workflow** – approvals can still apply regardless of who books.
- **Payment Configuration** – how the booking is paid for.
- **Trigger Booking After Approval** – whether the actual booking waits for approval (flight).

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `bookingProcessModeEnum` — `TRAVEL_DESK_LED` / `SELF_BOOK`
  - Set per travel mode (e.g. `FlightEntitlementsEntity.bookingProcessModeEnum`, `HotelEntitlementsEntity.bookingProcessModeEnum`)
- Snapshotted onto the trip's policy at trip creation in trip-management-service.

## Sample questions this feature answers
- "Can a travel desk book on behalf of employees?"
- "How do I let employees self-book flights but route hotels through a desk?"
- "What is travel-desk-led booking?"
- "Can different travel modes use different booking processes?"
- "Is the booking process mode configurable?"
- "How do we set up self-booking for a company?"
- "Who do I contact to change who books trips for a customer?"
