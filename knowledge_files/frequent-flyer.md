---
feature_name: Frequent Flyer
feature_id: frequent-flyer
category: Search & Booking Experience
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-06-21
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - sales-service
  - b2b-aggregation
technical_keys:
  - frequent.flyer.enabled.flag
tags:
  - frequent flyer
  - loyalty number
  - airline loyalty
  - mileage program
  - frequent flyer number
  - flight booking
  - traveller profile
  - loyalty
  - air miles
  - booking experience
  - whitelisting
  - employee profile
---

# Frequent Flyer

## Summary
The Frequent Flyer feature lets employees store and use their airline frequent-flyer numbers when booking flights, so their loyalty miles and benefits are credited to their accounts. It is controlled by a global enablement flag.

## What this feature does
When the frequent-flyer flag is enabled, the flight booking flow supports loyalty numbers:

- **Store frequent-flyer numbers** – employees can save their airline loyalty numbers.
- **Apply on flight bookings** – the stored number is used when booking flights so miles and benefits are credited.
- **Flag-controlled** – a single global enablement flag turns the capability on.

When the flag is off, the frequent-flyer capability is not available in the booking flow.

## Customer experience
- Employees can add their frequent-flyer numbers and have them applied automatically to flight bookings.
- This ensures travellers earn loyalty miles and receive airline benefits on corporate trips.
- When the feature is not enabled, the frequent-flyer option does not appear in the flight flow.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Whitelisting / enablement flag** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Controlled by a global enablement flag |

## Which team to connect with
**👉 Tech Team**

Because the frequent-flyer capability is gated by a **flag / whitelisting** controlled in Secret Manager, a salesperson who wants it switched on should reach out to the **Tech Team**. They manage the enablement flag.

> Whitelisting and flag-based features are always handled by the Tech Team. This is not a Corporate Config or Policy setting, so it stays with Tech.

## Related / dependent settings
These work alongside frequent flyer and may also be relevant:

- **Search Experience (Autosuggest V2 / Recommended Flights / New SRP)** – the broader flight search experience.
- **Personalization** – tailors results to corporate preferences.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting / enablement flag — Secret Manager Key
- **Key fields:**
  - `frequent.flyer.enabled.flag` — global flag enabling the frequent-flyer capability on flight bookings
- The flag is evaluated to decide whether the frequent-flyer option is shown and applied in the flight flow.

## Sample questions this feature answers
- "Can employees add their frequent-flyer numbers?"
- "How do we enable frequent flyer on flight bookings?"
- "Are airline loyalty miles credited on corporate flights?"
- "Who do I contact to switch on frequent flyer?"
- "Is frequent flyer controlled by a flag?"
- "Why don't I see the frequent-flyer option when booking a flight?"
- "Is the frequent-flyer feature configurable?"
