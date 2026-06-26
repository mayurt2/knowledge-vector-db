---
feature_name: Reports Module (Whitelisted)
feature_id: reports-module-whitelisted
category: Reporting, Insights & Analytics
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-04-10
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - sales-service
  - b2b-aggregation
technical_keys:
  - report.companyid.enable
tags:
  - reports
  - reporting module
  - reports access
  - company reports
  - reporting
  - analytics
  - travel reports
  - mis reports
  - spend reports
  - dashboard
  - whitelisting
  - data export
---

# Reports Module (Whitelisted)

## Summary
The Reports Module gives a company access to the platform's reporting area, where they can view and download reports on their travel bookings and spend. It is switched on for specific companies through whitelisting, so reporting is only visible to companies that have been enabled for it.

## What this feature does
When a company is enabled for the Reports Module, the reporting section becomes available to that company:

- **Reporting access** – the company can open the reports area and view standard travel and spend reports.
- **Company-level control** – reporting is enabled per company ID, so it can be rolled out selectively.

Companies that are not on the whitelist do not see the reporting module.

## Customer experience
- Enabled companies see the reports section and can generate or download reports on their bookings and spend.
- The reporting area gives a consolidated view of travel activity for the company.
- Companies that are not enabled do not see the reporting option.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Whitelisting** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — enabled per company ID via the whitelist key |

## Which team to connect with
**👉 Tech Team**

Because the Reports Module is enabled through **whitelisting** (Secret Manager keys), a salesperson who wants to turn on reporting for a company should reach out to the **Tech Team**. They add the company ID to the reporting whitelist.

> Whitelisting-based features are always handled by the Tech Team. This is not a Corporate Config or Policy setting, so it stays with Tech.

## Related / dependent settings
These work alongside the Reports Module and may also be relevant:

- **Insights V2** – the next-generation analytics dashboard, with its own whitelist.
- **Insights Flight Analytics** – flight-specific analytics views.
- **Trip / Employee Export** – export of trip and employee travel data for offline reporting.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `report.companyid.enable` — company IDs enabled for the reporting module
- The whitelist is evaluated at request time to decide whether the reporting module is available to the company.

## Sample questions this feature answers
- "How do we enable reports for a company?"
- "Why can't a customer see the reporting section?"
- "Is the reports module available to all companies?"
- "Who do I contact to switch on reporting for a customer?"
- "Can reporting be turned on for just one company?"
- "Where does a customer download their travel reports?"
- "Is the reports module configurable?"
