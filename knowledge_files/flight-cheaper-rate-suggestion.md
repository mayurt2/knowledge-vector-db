---
feature_name: Flight Cheaper Rate Suggestion
feature_id: flight-cheaper-rate-suggestion
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-06-15
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - FlightEntitlementsEntity.cheaperRateEligibility
tags:
  - cheaper rate
  - cheaper fare
  - fare suggestion
  - savings prompt
  - lower fare
  - cost saving
  - cheaper alternative
  - fare nudge
  - travel policy
  - flight
---

# Flight Cheaper Rate Suggestion

## Summary
Flight Cheaper Rate Suggestion enables the platform to prompt an employee with a cheaper available fare for the same itinerary. When an employee is about to book a flight, if a lower-priced fare exists for the same route and timing, the system can surface it so the employee (or company) saves money. This is a flight-specific control.

## What this feature does
When an employee selects a flight, the system checks whether a cheaper fare is available for the same itinerary and, if cheaper-rate suggestion is enabled in the company's policy:

- **Enabled** – the employee is prompted with the cheaper available fare for the same itinerary, encouraging them to choose the lower-cost option.
- **Disabled** – no cheaper-rate prompt is shown; the employee proceeds with their selected fare.

This is a savings nudge that helps companies reduce travel spend without hard-blocking the employee's choice. It works alongside budget caps and price-hike checks as part of the company's overall cost-control toolkit.

## Customer experience
- When enabled, employees see a clear prompt offering a cheaper fare for the same flight itinerary and can switch to it.
- The suggestion is a nudge — it helps employees make a cost-conscious choice rather than forcing one.
- Whether the prompt appears depends on the policy of the employee's group.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because the cheaper-rate suggestion is part of the company's travel **Policy Config**, a salesperson who wants to turn this savings prompt on or off for a customer should reach out to the **Onboarding Team**. They configure the cheaper-rate eligibility per employee group.

> Use the Tech Team only for whitelisting-based features. Cheaper rate suggestion is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside the cheaper rate suggestion:

- **Spend / Budget Cap** – the hard limit, where cheaper-rate is a softer nudge.
- **Price Hike Tolerance Limit** – protects against fare increases between selection and booking.
- **Flight Fare Type Restriction** – defines which fare types are eligible to be suggested.
- **Travel Mode Eligibility** – flights must be Allowed in the first place.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `FlightEntitlementsEntity.cheaperRateEligibility` — enables prompting a cheaper available fare for the same itinerary
- Evaluated at flight selection time in trip-management-service.

## Sample questions this feature answers
- "Can the platform suggest a cheaper flight fare?"
- "How do I enable cheaper-rate prompts for a company?"
- "Does this force employees to take the cheaper fare or just suggest it?"
- "Can the cheaper-rate suggestion be turned off?"
- "Is the cheaper rate suggestion configurable?"
- "How do we encourage employees to save on flights?"
- "Who do I contact to enable cheaper-rate suggestions for a customer?"
