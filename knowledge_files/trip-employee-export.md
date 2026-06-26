---
feature_name: Trip & Employee Export
feature_id: trip-employee-export
category: Reporting, Insights & Analytics
config_source: Corporate Config (employee export) + Whitelisting (trip export)
configurable: true
status: live
target_release_date: 2026-06-07
status_last_updated: 2026-06-26
contact_team: Onboarding Team (employee export) / Tech Team (trip export)
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - enable_employee_export
  - trip.export.corporate.whitelisted
tags:
  - export
  - data export
  - employee export
  - trip export
  - reporting export
  - download data
  - travel data
  - bulk export
  - employee data
  - trip data
  - reporting
  - csv export
---

# Trip & Employee Export

## Summary
Trip & Employee Export lets a company pull its travel and employee data out of the platform for reporting and analysis. It has two parts: exporting employee travel data, which is a per-corporate config flag, and exporting trip data, which is gated by a whitelist. Because the two parts are controlled differently, they may involve two different teams.

## What this feature does
This feature covers two distinct exports, each switched on in its own way:

- **Employee export** – allows export of employee travel data. This is a **Corporate Config** flag set per corporate.
- **Trip export** – allows export of trip data. This is controlled by a **whitelist**, so only whitelisted corporates can run trip exports.

A company can have one, both, or neither enabled depending on how each control is set.

## Customer experience
- Companies with employee export enabled can export employee travel data for their own reporting and analysis.
- Companies that are whitelisted for trip export can export trip data sets for offline use.
- If only one of the two is enabled, the customer can export that data set but not the other.
- Companies with neither enabled rely on in-platform reports and dashboards instead.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** (employee export) and **Whitelisting** (trip export) |
| Who configures it? | Onboarding Team (employee export) / Tech Team (trip export) |
| Is it per-company? | Yes — employee export per corporate config; trip export per corporate via whitelist |

## Which team to connect with
**👉 Onboarding Team (employee export) and Tech Team (trip export)**

This feature is split across two control mechanisms, so routing depends on which export the customer needs:

- For **employee export**, which is a **Corporate Config** flag, reach out to the **Onboarding Team** — they set `enable_employee_export` per corporate.
- For **trip export**, which is **whitelisting** based, reach out to the **Tech Team** — they add the corporate to the trip-export whitelist.

> The rule of thumb: Corporate Config goes to Onboarding, whitelisting goes to Tech. Because this feature uses both, both teams may be involved depending on the specific export requested.

## Related / dependent settings
These work alongside the exports and may also be relevant:

- **Reports Module (Whitelisted)** – in-platform reporting access.
- **Trip Webhook (Whitelisted)** – live outbound trip data feed.
- **Insights V2 / Flight Analytics** – analytics dashboards built on the same travel data.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config (employee export) + Whitelisting — Secret Manager Key (trip export)
- **Key fields:**
  - `enable_employee_export` — Corporate Config flag enabling employee travel data export
  - `trip.export.corporate.whitelisted` — corporates whitelisted for trip data export
- Employee export is read from corporate configuration; trip export is gated by the whitelist at export time.

## Sample questions this feature answers
- "Can a customer export their employee travel data?"
- "How do we enable trip export for a company?"
- "Who do I contact to turn on employee export?"
- "Who do I contact to turn on trip export?"
- "Why is employee export and trip export controlled separately?"
- "Is employee export a config flag or a whitelist?"
- "Can a company export both trips and employee data?"
- "Is data export configurable per corporate?"
