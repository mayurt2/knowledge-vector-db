---
feature_name: Flight Minimum Eligible Distance
feature_id: flight-minimum-eligible-distance
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-05-03
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - FlightEntitlementsEntity.minEligibleDistance
tags:
  - minimum distance
  - min eligible distance
  - short haul
  - distance rule
  - flight distance
  - short hop
  - mode steering
  - cost saving
  - travel policy
  - flight
---

# Flight Minimum Eligible Distance

## Summary
Flight Minimum Eligible Distance sets a minimum trip distance below which flights are not permitted. The aim is to stop employees from flying very short routes where a cheaper mode (train, bus, or cab) makes more sense. If the trip distance is below the configured threshold, flights are not allowed for that journey. This is a flight-specific control.

## What this feature does
When an employee tries to book a flight, the system checks the trip distance against the minimum eligible distance configured in the company's policy:

- **At or above the threshold** – flights are permitted for that journey.
- **Below the threshold** – flights are not permitted, steering the employee toward a cheaper mode for the short hop.

This helps companies cut unnecessary cost and emissions on short routes by reserving flights for longer journeys where they genuinely save time. It works as a gate specific to flights, on top of overall flight eligibility.

## Customer experience
- For longer trips at or above the threshold, employees can book flights normally.
- For short trips below the threshold, flights are unavailable and the employee is guided to use another travel mode.
- Different employee groups can have different minimum distance thresholds within the same company.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because the minimum flight distance is part of the company's travel **Policy Config**, a salesperson who wants to set a short-distance flight cutoff for a customer should reach out to the **Onboarding Team**. They configure the minimum eligible distance per employee group.

> Use the Tech Team only for whitelisting-based features. Minimum eligible distance is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside the minimum eligible distance:

- **Travel Mode Eligibility** – flights must be Allowed in the first place; this adds a distance condition.
- **Spend / Budget Cap** – another cost-control check on flight bookings.
- **Advance Purchase Rule** – another in-policy check on flight bookings.
- **Trip Approval Workflow** – handles approvals where short-distance exceptions are needed.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `FlightEntitlementsEntity.minEligibleDistance` — minimum trip distance below which flights are not permitted
- Evaluated at flight search/selection time in trip-management-service.

## Sample questions this feature answers
- "Can we stop employees from flying very short routes?"
- "How do I set a minimum distance for flights?"
- "Why can't an employee book a flight for a short trip?"
- "Can the minimum flight distance differ by employee group?"
- "Is the minimum eligible distance configurable?"
- "How do we steer short trips to train or cab?"
- "Who do I contact to set a short-distance flight cutoff for a customer?"
