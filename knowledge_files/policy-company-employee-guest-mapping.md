---
feature_name: Policy ↔ Company / Employee / Guest Mapping
feature_id: policy-company-employee-guest-mapping
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-05-30
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - CorporateEntitlementCompanyPolicyMapping
  - CorporateEmployeeEntitlementMappingEntity
  - CorporateGuestEntitlementMappingEntity
  - isDefault
  - allowNewGuest
tags:
  - policy mapping
  - default policy
  - company policy
  - employee assignment
  - guest policy
  - policy assignment
  - guest booking
  - company mapping
  - policy linking
  - travel policy
---

# Policy ↔ Company / Employee / Guest Mapping

## Summary
This feature controls how a travel policy is connected to a company and its people. It associates a policy with one or more companies, marks which policy is the company's default, and can assign specific employees or guests to a specific policy. It also controls whether new guests can be added under a company.

## What this feature does
Once policies are defined, they need to be linked to the right people. This mapping handles those connections:

- **Company association** – links a policy to a company so it becomes available for that company's travellers.
- **Default policy** – marks one policy as the company default, used when no more specific rule or assignment applies.
- **Employee assignment** – assigns specific employees directly to a specific policy, overriding the default for those individuals.
- **Guest assignment** – assigns specific guests (non-employee travellers) to a specific policy.
- **Allow new guest** – controls whether new guest travellers can be added under the company.

Together with policy targeting rules, this determines exactly which policy each traveller — employee or guest — ends up under.

## Customer experience
- Each traveller automatically books under the correct policy: their assigned policy if they have one, otherwise the company default.
- Guests travelling on behalf of the company are governed by the policy mapped to them.
- If new guests are not allowed, attempts to add a new guest traveller are prevented, keeping the traveller list controlled.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — mappings are set per company, with optional per-employee and per-guest assignments |

## Which team to connect with
**👉 Onboarding Team**

Because policy mapping is part of the company's travel **Policy Config**, a salesperson who wants to link a policy to a company, set the default policy, assign specific employees or guests, or control new guests should reach out to the **Onboarding Team**.

> Use the Tech Team only for whitelisting-based features. Policy mapping is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside policy mapping and may also need to be set:

- **Policy Targeting Rules** – the grade/department/entity/business-unit rules that route employees to a policy (`PolicyRuleEntity`, `PolicyRuleConditionEntity`).
- **Hotel / Flight / Bus Budgets** – the actual budgets defined inside each mapped policy.
- **Trip Approval Workflow** – approval rules carried by each policy.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `CorporateEntitlementCompanyPolicyMapping` — links a policy to a company; carries `isDefault` to mark the company default and `allowNewGuest` to control adding new guests
  - `CorporateEmployeeEntitlementMappingEntity` — assigns a specific employee to a specific policy
  - `CorporateGuestEntitlementMappingEntity` — assigns a specific guest to a specific policy
  - `isDefault` — flags the default policy for a company
  - `allowNewGuest` — controls whether new guest travellers may be added
- Resolved when determining the applicable policy for a traveller at trip creation.

## Sample questions this feature answers
- "How is a policy linked to a company?"
- "How do we set the default policy for a company?"
- "Can we assign a specific employee to a specific policy?"
- "Can guests be put on their own policy?"
- "How do we stop new guests from being added?"
- "Who do I contact to change a company's default policy or assignments?"
- "Is the policy-to-company mapping configurable per company?"
