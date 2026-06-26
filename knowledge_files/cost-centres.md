---
feature_name: Cost Centres
feature_id: cost-centres
category: Cost Objects, Project Codes & Custom Fields
config_source: Corporate Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-04-17
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - costCentreEnabled
  - costCentreList
tags:
  - cost centre
  - cost center
  - spend attribution
  - department budget
  - cost allocation
  - expense tagging
  - budget tracking
  - cost object
  - finance reporting
  - departmental spend
  - tagging
---

# Cost Centres

## Summary
Cost Centres let a company tag trips and bookings with a cost centre from a corporate-managed list. This attributes travel spend to the right department, team, or budget, so finance can see who is spending what. It is a core building block for spend reporting and budget control, with the list of valid cost centres maintained per company.

## What this feature does
When enabled for a company, the platform lets bookings and trips carry a cost centre tag:

- **Enable cost centres** – turns on the ability to tag trips/bookings with a cost centre.
- **Cost centre list** – a corporate-managed list of valid cost centres the company defines; users select from this list when booking.

Tagging spend to a cost centre means each trip can be attributed to a department or budget line, feeding accurate spend reports and reconciliation. Both the toggle and the list are managed per company through Corporate Config.

## Customer experience
- When booking, employees pick a cost centre from the company's defined list, attributing the spend to the right department or budget.
- Finance teams get clean, attributable spend data broken down by cost centre.
- Because the list is corporate-managed, only valid, approved cost centres are available for selection.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — the toggle and the list are set per company |

## Which team to connect with
**👉 Onboarding Team**

Because the cost centre toggle and list are **Corporate Config** settings, a salesperson who wants to enable cost centres or update the list for a customer should reach out to the **Onboarding Team**. They turn the feature on and maintain the company's cost centre list.

> Use the Tech Team only for whitelisting-based features. This is a Corporate Config setting, so it stays with Onboarding.

## Related / dependent settings
These work alongside cost centres for spend attribution:

- **Project Codes** – tag trips with project codes for cost allocation (`projectCodeEnabled`).
- **Custom Fields** – capture additional metadata against trips and bookings.
- **Cross-Entity Cost Object Mapping** – allow cost objects from a different entity in the group (`allow_cross_entity_cost_object_mapping_selection`).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config — Corporate Entitlement Service
- **Key fields:**
  - `costCentreEnabled` — turns on cost centre tagging for the company
  - `costCentreList` — the corporate-managed list of valid cost centres users select from
- Read from Corporate Config; selected cost centres are captured against trips/bookings for spend attribution.

## Sample questions this feature answers
- "Can we tag trips with a cost centre?"
- "How do we attribute travel spend to a department?"
- "Where does the list of cost centres come from?"
- "Can we enable cost centres for a customer?"
- "How do we add or change cost centres for a company?"
- "How is travel spend allocated to budgets?"
- "Who do I contact to set up cost centres?"
