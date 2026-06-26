---
feature_name: Project Codes
feature_id: project-codes
category: Cost Objects, Project Codes & Custom Fields
config_source: Corporate Config (Corporate Entitlement Service) + Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-05-16
status_last_updated: 2026-06-26
contact_team: Onboarding Team (and Tech Team for whitelisting)
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - projectCodeEnabled
  - allowCrossProjectCode
  - enable_project_code_gst
  - corporate.code.enabled.company.ids
tags:
  - project code
  - cost allocation
  - project tagging
  - cross project
  - GST linkage
  - corporate code
  - cost object
  - spend attribution
  - whitelisting
  - billing code
  - project billing
---

# Project Codes

## Summary
Project Codes let a company tag trips with a project code so travel spend can be allocated to the right project. The feature supports optional cross-project assignment (booking against a project other than the user's default) and optional GST linkage for tax handling. Separately, a whitelist gates corporate-code capture for specific companies, which is controlled at the tech level. Most controls are per-company Corporate Config, while the whitelist is a Secret Manager key.

## What this feature does
When enabled for a company, the platform lets trips carry project codes and related controls:

- **Enable project codes** – turns on tagging trips with project codes for cost allocation.
- **Allow cross-project code** – lets users assign a project code other than their default/own project, supporting cross-project bookings.
- **Project code GST linkage** – links the project code to GST details for correct tax handling on bookings.
- **Corporate-code capture (whitelisted)** – for specific companies on a whitelist, corporate-code capture is enabled; this is gated by a tech-controlled whitelist key rather than per-company Corporate Config.

The first three are managed per company through Corporate Config. The corporate-code whitelist is a Secret Manager key maintained by the Tech Team.

## Customer experience
- Employees can tag trips with a project code so spend is attributed to the correct project.
- With cross-project assignment, users can book against projects beyond their own when their work requires it.
- GST linkage ensures tax details flow correctly with the project code.
- For whitelisted companies, corporate-code capture is enabled for billing/compliance needs.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** (project code toggles) **and Whitelisting / Secret Manager Key** (corporate-code capture) |
| Who configures it? | Onboarding Team (Corporate Config); Tech Team (whitelist) |
| Is it per-company? | Yes — toggles per company; the whitelist also targets specific company IDs |

## Which team to connect with
**👉 Onboarding Team (and Tech Team for the whitelist)**

Because the project code toggles (`projectCodeEnabled`, `allowCrossProjectCode`, `enable_project_code_gst`) are **Corporate Config** settings, a salesperson should reach out to the **Onboarding Team** to enable project codes, allow cross-project assignment, or link GST.

However, the corporate-code capture whitelist (`corporate.code.enabled.company.ids`) is a **Secret Manager key**, so adding a company to that whitelist must go through the **Tech Team**. This is a multi-source feature, so connect with both teams depending on what is needed.

> Rule of thumb: Corporate Config toggles → Onboarding Team. Whitelisting via Secret Manager key → Tech Team.

## Related / dependent settings
These work alongside project codes:

- **Cost Centres** – tag trips/bookings with a cost centre (`costCentreEnabled`, `costCentreList`).
- **Custom Fields** – capture additional metadata against trips and bookings.
- **Cost Object Mapping & ERP Sync (Whitelisted)** – ERP-synced cost-center tagging for whitelisted corporates.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config — Corporate Entitlement Service (toggles); Secret Manager Key (whitelist)
- **Key fields:**
  - `projectCodeEnabled` — turns on project code tagging for the company (Corporate Config)
  - `allowCrossProjectCode` — allows assigning a project code beyond the user's own project (Corporate Config)
  - `enable_project_code_gst` — links project codes to GST details (Corporate Config)
  - `corporate.code.enabled.company.ids` — whitelist of company IDs for which corporate-code capture is enabled (Secret Manager Key, Tech-controlled)
- Toggles are read from Corporate Config; the whitelist is evaluated from system configuration.

## Sample questions this feature answers
- "Can we tag trips with project codes?"
- "Can users book against a different project than their own?"
- "How do we link GST to project codes?"
- "How do we enable corporate-code capture for a specific company?"
- "Why is corporate code capture enabled only for some companies?"
- "Who handles the project code whitelist?"
- "Who do I contact to turn on project codes for a customer?"
- "Is cross-project assignment configurable?"
