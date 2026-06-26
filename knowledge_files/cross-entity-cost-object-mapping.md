---
feature_name: Cross-Entity Cost Object Mapping
feature_id: cross-entity-cost-object-mapping
category: Cost Objects, Project Codes & Custom Fields
config_source: Corporate Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-04-18
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - allow_cross_entity_cost_object_mapping_selection
tags:
  - cost object
  - cross entity
  - entity mapping
  - cost allocation
  - group company
  - inter-entity
  - cost object selection
  - spend attribution
  - cost centre mapping
  - multi-entity
  - booking mapping
---

# Cross-Entity Cost Object Mapping

## Summary
Cross-Entity Cost Object Mapping lets users select cost objects that belong to a different entity within the same company group when mapping a booking. Normally a booking is tagged with cost objects from the user's own entity; this setting opens up selection across sister entities in the group, which is useful when costs need to be charged to a different legal entity or business unit within the same corporate family.

## What this feature does
When enabled for a company, the platform widens cost-object selection during mapping:

- Users can choose cost objects (such as cost centres) that belong to **another entity within the company group**, not just their own entity.
- This supports scenarios where spend on a booking needs to be attributed to a different entity in the corporate structure.
- When disabled, cost-object selection is limited to the user's own entity.

The setting is controlled per company through Corporate Config, giving each company group the choice of whether to allow inter-entity cost object selection.

## Customer experience
- Users in a multi-entity group can map a booking's cost to the correct entity even when it differs from their own.
- This makes cost attribution accurate for groups where costs cross entity boundaries.
- Companies that want to keep cost objects strictly within each entity can leave the setting off.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — enabled or disabled per company |

## Which team to connect with
**👉 Onboarding Team**

Because cross-entity cost-object selection is a **Corporate Config** setting, a salesperson who wants to enable, disable, or explain it for a customer should reach out to the **Onboarding Team**. They turn on whether users can pick cost objects from other entities in the group.

> Use the Tech Team only for whitelisting-based features. This is a Corporate Config setting, so it stays with Onboarding.

## Related / dependent settings
These work alongside cross-entity cost-object mapping:

- **Cost Centres** – the cost-object list users select from (`costCentreEnabled`, `costCentreList`).
- **Project Codes** – another cost object that can be mapped to bookings (`projectCodeEnabled`).
- **Cost Object Mapping & ERP Sync (Whitelisted)** – ERP-synced cost-object mapping for whitelisted corporates.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config — Corporate Entitlement Service
- **Key fields:**
  - `allow_cross_entity_cost_object_mapping_selection` — when enabled, lets users select cost objects belonging to a different entity within the company group during mapping
- Read from Corporate Config; governs the scope of cost-object selection during booking mapping.

## Sample questions this feature answers
- "Can users pick cost objects from another entity in the group?"
- "Can we map a booking's cost to a different legal entity?"
- "How do we allow cross-entity cost object selection?"
- "Why can a user only see their own entity's cost objects?"
- "Does this help multi-entity company groups?"
- "Can cross-entity mapping be turned off for a customer?"
- "Who do I contact to enable cross-entity cost object mapping?"
