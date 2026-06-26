---
feature_name: Price Hike Tolerance Limit
feature_id: price-hike-tolerance-limit
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-04-19
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - FlightEntitlementsEntity.priceHikeLimit
  - HotelEntitlementsEntity.priceHikeLimit
  - BusEntitlementsEntity.priceHikeLimit
tags:
  - price hike
  - price hike limit
  - price tolerance
  - fare increase
  - rate increase
  - price change
  - out-of-policy
  - fare jump
  - travel policy
  - price protection
---

# Price Hike Tolerance Limit

## Summary
The Price Hike Tolerance Limit controls how much a fare or rate is allowed to rise between the moment an employee selects an option and the moment it is booked. Live travel prices can change in seconds, so this setting defines an acceptable increase. If the price jumps beyond the tolerance before booking completes, the trip is treated as out-of-policy. It applies to Flight, Hotel, and Bus.

## What this feature does
Between selection and final booking, the system re-checks the live price and compares the increase against the configured tolerance for that mode:

- **Within tolerance** – the small price rise is accepted and the booking proceeds in-policy.
- **Beyond tolerance** – the larger price jump makes the booking out-of-policy. Depending on the company's broader rules, it may require approval, prompt re-confirmation, or be blocked.

Because it is set per mode (Flight, Hotel, Bus), a company can allow a tighter or looser tolerance for each. This protects employees and companies from unexpectedly paying much more than the price they originally saw.

## Customer experience
- If a price rises only slightly within the allowed tolerance, the employee can complete the booking smoothly.
- If the price jumps beyond the tolerance, the employee is alerted that the booking is now out-of-policy and may need to re-confirm or seek approval.
- Different employee groups can have different tolerance limits within the same company.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because the price hike tolerance is part of the company's travel **Policy Config**, a salesperson who wants to set how much fare/rate increase is tolerated for a customer should reach out to the **Onboarding Team**. They configure the price-hike limit per mode (Flight, Hotel, Bus) and employee group.

> Use the Tech Team only for whitelisting-based features. The price hike tolerance is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside the price hike tolerance:

- **Spend / Budget Cap** – another check on the final price of the booking.
- **Trip Approval Workflow** – out-of-policy (over-tolerance) bookings are typically routed for approval.
- **Cheaper Rate Suggestion** – may surface a lower fare for the same itinerary (flight).
- **Travel Mode Eligibility** – the mode must be Allowed in the first place.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `FlightEntitlementsEntity.priceHikeLimit` — tolerated fare increase for flights
  - `HotelEntitlementsEntity.priceHikeLimit` — tolerated rate increase for hotels
  - `BusEntitlementsEntity.priceHikeLimit` — tolerated fare increase for bus
- Evaluated between selection and booking confirmation; over-tolerance bookings flagged out-of-policy in trip-management-service.

## Sample questions this feature answers
- "What happens if the flight price goes up before booking?"
- "How do I set how much a fare can rise before it's out-of-policy?"
- "Can we limit price increases between selection and booking?"
- "Does the price hike limit apply to hotels and bus too?"
- "Is the price hike tolerance configurable?"
- "How do we protect employees from sudden fare jumps?"
- "Who do I contact to change the price hike limit for a customer?"
