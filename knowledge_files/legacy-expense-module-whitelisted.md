---
feature_name: Legacy Expense Module (Whitelisted)
feature_id: legacy-expense-module-whitelisted
category: Expense Management
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-04-04
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - trip-management-service
  - corporate-entitlement-service
  - sales-service
technical_keys:
  - old.expense.enabled.companyIds
tags:
  - legacy expense
  - old expense module
  - expense migration
  - whitelisted company
  - expense module
  - backward compatibility
  - expense system
  - grandfathered
  - expense management
  - module version
---

# Legacy Expense Module (Whitelisted)

## Summary
Legacy Expense Module (Whitelisted) keeps specific, whitelisted companies on the older expense module instead of moving them to the newer one. Some companies need to stay on the legacy experience — for example, because their processes or integrations depend on it — so their company IDs are added to a whitelist that pins them to the old module. Because this is controlled by a whitelist in the secret manager, it is a Tech Team action.

## What this feature does
The platform has a newer expense module, but certain companies can remain on the legacy version:

- **Pin to legacy module** — companies whose IDs are on the whitelist continue using the old expense module.
- **Everyone else uses the new module** — companies not on the whitelist get the current expense experience.
- **Whitelist-controlled** — membership is managed by adding/removing company IDs in the configured key.

This provides backward compatibility for companies that are not ready to move to the new module.

## Customer experience
- Whitelisted companies continue to see and use the legacy expense module they are familiar with.
- Non-whitelisted companies use the newer expense module.
- The experience stays consistent for companies that depend on the legacy behavior until they migrate.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** (via whitelist) |
| Where is it configured? | **Whitelisting** — Secret Manager Key |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — controlled by listing the company ID in the whitelist |

## Which team to connect with
**👉 Tech Team**

Because this feature is controlled by a **whitelist stored as a Secret Manager Key**, keeping a company on (or moving it off) the legacy expense module requires editing that whitelist of company IDs. This is a Tech Team action, not a standard Corporate Config change.

> This is a whitelisting feature, so it is handled by the **Tech Team**, not Onboarding. The Onboarding Team handles Corporate Config settings only.

## Related / dependent settings
These work alongside the legacy expense module and may also be relevant:

- **Local Expense** – enables travelers to log local/incidental expenses (Corporate Config).
- **Trip PDF Export** – export trip/expense details as a PDF (Corporate Config).
- **Trip Approval Workflow** – approvals that may apply to trips and expenses.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `old.expense.enabled.companyIds` — list of company IDs whitelisted to remain on the legacy expense module instead of the new one.

## Sample questions this feature answers
- "Can a company stay on the old expense module?"
- "Why is a company seeing the legacy expense experience?"
- "How do we keep a customer on the old expense system instead of the new one?"
- "Is the expense module choice a Corporate Config setting or a whitelist?"
- "Who do I contact to pin a company to the legacy expense module?"
- "How do companies get migrated off the old expense module?"
- "What does old.expense.enabled.companyIds control?"
