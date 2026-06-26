---
feature_name: Cost Object Mapping & ERP Sync (Whitelisted)
feature_id: cost-object-mapping-erp-sync-whitelisted
category: Cost Objects, Project Codes & Custom Fields
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-05-27
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - cost.object.mapping.enabled.corporates
  - sync.erp.enabled.corporates
tags:
  - cost object mapping
  - ERP sync
  - whitelisting
  - cost center tagging
  - expense integration
  - ERP integration
  - cost allocation
  - finance sync
  - whitelisted corporates
  - expense ERP
  - secret manager
---

# Cost Object Mapping & ERP Sync (Whitelisted)

## Summary
This feature enables cost-object mapping (tagging bookings with expense/ERP cost centres) and synchronization of that data with the customer's ERP system — but only for corporates that have been whitelisted. Because it integrates with external finance/ERP systems and is gated by a whitelist, it is controlled at the tech level through Secret Manager keys rather than self-serve Corporate Config.

## What this feature does
For whitelisted corporates, the platform enables two related capabilities:

- **Cost object mapping** – tagging bookings with expense/ERP cost centres so spend is attributed correctly for the customer's finance systems.
- **ERP synchronization** – pushing the mapped cost-object data into the customer's ERP system, keeping the platform and the customer's finance backend aligned.

Both capabilities are enabled per corporate via whitelist keys. A corporate must be added to the relevant whitelist for the capability to apply — this is not a per-company toggle that Onboarding flips in Corporate Config.

## Customer experience
- Whitelisted corporates get bookings tagged with ERP-aligned cost centres and synced into their ERP, removing manual reconciliation.
- Finance teams see travel spend flow directly into their ERP with the correct cost-object mapping.
- Corporates not on the whitelist do not have ERP sync; enabling it requires being added to the whitelist.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** — via whitelist (not self-serve Corporate Config) |
| Where is it configured? | **Whitelisting / Secret Manager Key** |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — corporates are added to the whitelist by company ID |

## Which team to connect with
**👉 Tech Team**

Because cost-object mapping and ERP sync are gated by **whitelist keys in Secret Manager**, a salesperson who wants a corporate enabled for this must reach out to the **Tech Team**. They add the corporate to the `cost.object.mapping.enabled.corporates` and `sync.erp.enabled.corporates` whitelists.

> Rule of thumb: Whitelisting via Secret Manager key → Tech Team. This is a whitelisting feature, so it does not go through Onboarding's Corporate Config.

## Related / dependent settings
These work alongside ERP-synced cost-object mapping:

- **Cost Centres** – the cost-object structure that gets mapped (`costCentreEnabled`, `costCentreList`).
- **Project Codes** – another cost object that can flow into ERP (`projectCodeEnabled`).
- **Cross-Entity Cost Object Mapping** – allows cost objects from a different entity in the group (`allow_cross_entity_cost_object_mapping_selection`).

## Technical reference (for Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `cost.object.mapping.enabled.corporates` — whitelist of corporates for which cost-object mapping is enabled
  - `sync.erp.enabled.corporates` — whitelist of corporates for which ERP synchronization is enabled
- Evaluated from system/Secret Manager configuration against the corporate; not a per-company Corporate Config toggle.

## Sample questions this feature answers
- "Can we sync cost objects to a customer's ERP?"
- "How do we enable ERP integration for a corporate?"
- "Why is ERP sync only available for some corporates?"
- "How is a corporate added to the cost object mapping whitelist?"
- "Who controls the ERP sync whitelist?"
- "Is ERP sync a Corporate Config setting or a whitelist?"
- "Who do I contact to enable cost object mapping and ERP sync?"
