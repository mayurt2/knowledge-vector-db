---
feature_name: Employee Web-App & Flight Module (Whitelisted)
feature_id: employee-webapp-flight-module-whitelisted
category: Search & Booking Experience
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-04-03
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - sales-service
  - b2b-aggregation
technical_keys:
  - emp.webapp.enabled.companyid
  - flight.companyid.enable
tags:
  - employee webapp
  - web app
  - employee portal
  - flight module
  - flight booking
  - self booking
  - employee experience
  - web booking
  - flight enablement
  - whitelisting
  - booking experience
  - module enablement
---

# Employee Web-App & Flight Module (Whitelisted)

## Summary
This feature enables the employee web-app experience and the flight-booking module for whitelisted companies. Together they let a company's employees self-serve on the web app and book flights, and each is controlled by its own company-level whitelist.

## What this feature does
When a company is enabled, employees gain access to the web app and/or the flight module:

- **Employee web-app** – turns on the employee-facing web-app experience for a company.
- **Flight module** – enables the flight-booking module so employees can search and book flights.
- **Company-level control** – each capability is enabled per company ID via its own whitelist.

A company can have one or both enabled depending on how the whitelists are set.

## Customer experience
- Employees at enabled companies can use the web-app experience to manage and make bookings.
- Where the flight module is enabled, employees can search for and book flights.
- Companies that are not enabled do not see the web-app and/or flight module.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Whitelisting** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — both the web app and flight module are enabled per company ID via whitelist keys |

## Which team to connect with
**👉 Tech Team**

Because the employee web-app and flight module are enabled through **whitelisting** (Secret Manager keys), a salesperson who wants to turn either on for a company should reach out to the **Tech Team**. They manage both company-level whitelists.

> Whitelisting-based features are always handled by the Tech Team. These are not Corporate Config or Policy settings, so they stay with Tech.

## Related / dependent settings
These work alongside the web-app and flight module and may also be relevant:

- **B2B App Navigator** – improved navigation experience.
- **Search Experience (Autosuggest V2 / Recommended Flights / New SRP)** – newer flight search experiences.
- **Frequent Flyer** – loyalty numbers on flight bookings.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `emp.webapp.enabled.companyid` — company IDs enabled for the employee web-app experience
  - `flight.companyid.enable` — company IDs enabled for the flight-booking module
- Whitelists are evaluated at request time to decide whether the web app and flight module are available.

## Sample questions this feature answers
- "How do we enable the employee web app for a company?"
- "How do we turn on flight booking for a company?"
- "Can the web app and flight module be enabled separately?"
- "Who do I contact to switch on the employee web app?"
- "Why can't a company's employees book flights?"
- "Is the flight module enabled per company?"
- "Is the employee web app configurable per company?"
