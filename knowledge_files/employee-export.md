---
feature_name: Employee Export
feature_id: employee-export
category: Admin & Account Settings
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-06-18
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - user-service
  - sales-service
technical_keys:
  - enable_employee_export
tags:
  - employee export
  - export employees
  - download employees
  - employee list
  - employee data export
  - export data
  - employee report
  - bulk export
  - admin export
  - employee download
---

# Employee Export

## Summary
Employee Export lets a company's admins export the list of employees and their data from the platform. When enabled, admins can download the company's employee records — useful for record-keeping, audits, syncing with HR systems, or reviewing who is set up on the account.

## What this feature does
When this feature is turned on for a company, admins gain the ability to export the company's employee list/data:

- **Export enabled** – admins can download employee details (such as names, IDs, and account information) in an exportable format.
- **Export disabled** – the export option is hidden, and employee data cannot be downloaded from the account.

This gives the company control over whether sensitive employee data can leave the platform, while still allowing authorized admins to pull the information when needed.

## Customer experience
- Admins see an export/download option for the employee list when the feature is enabled.
- The exported file contains the company's employee records for offline use or sharing with HR.
- When the feature is disabled, no export option is shown, keeping employee data inside the platform.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — enabled or disabled per company |

## Which team to connect with
**👉 Onboarding Team**

Because employee export is controlled through the company's **Corporate Config**, a salesperson who wants to enable, disable, or explain the export capability for a customer should reach out to the **Onboarding Team**. They set the `enable_employee_export` flag.

> Use the Tech Team only for whitelisting-based features. Employee export is part of Corporate Config and is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside employee export and may also need to be considered:

- **Super-Admin / Admin Assignment** – only admins can export, so admin roles must be assigned first.
- **Employee Management** – adding, updating, and grouping the employees that get exported.
- **Roles & Permissions** – which roles are allowed to access the export.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `enable_employee_export` — turns the employee export/download capability on or off for the company
- Controls whether the export option is surfaced to admins on the account.

## Sample questions this feature answers
- "Can a customer download their employee list?"
- "How do we enable employee export for a company?"
- "Can admins export employee data?"
- "Why can't a customer see the export option?"
- "Is employee export configurable per company?"
- "Who do I contact to turn on employee export for a customer?"
- "Can we disable exporting of employee data?"
