---
feature_name: Policy Targeting Rules
feature_id: policy-targeting-rules
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-05-04
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - PolicyRuleEntity
  - PolicyRuleConditionEntity
  - GRADE
  - DEPARTMENT
  - ENTITY
  - BUSINESS_UNIT
  - INCLUDE
  - EXCLUDE
tags:
  - policy targeting
  - policy rules
  - employee group
  - grade based policy
  - department policy
  - include exclude
  - business unit
  - policy assignment
  - eligibility rules
  - travel policy
---

# Policy Targeting Rules

## Summary
Policy Targeting Rules decide which employees a particular travel policy applies to. Instead of giving everyone the same policy, a company can build named rule sets that match employees by their Grade, Department, Entity, or Business Unit — and either include or exclude listed values. This makes it possible to say things like "apply this policy only to Grades L1–L3" or "apply it to everyone except the Sales department."

## What this feature does
Each policy can carry one or more rules, and each rule is made up of conditions that match employee attributes:

- **Match by attribute** – conditions match on **Grade**, **Department**, **Entity**, or **Business Unit**.
- **Include or exclude** – a condition can **include** the listed values (the policy applies only to those) or **exclude** them (the policy applies to everyone except those).
- **Named rule sets** – rules are grouped so a company can describe a clear audience for each policy (for example, a premium policy for senior grades and a standard policy for the rest).

When an employee creates a trip, the system evaluates these rules to find the policy that applies to them, so the right budgets, approvals, and restrictions are enforced for each group.

## Customer experience
- Different employee groups experience different policies — for example, senior grades may see higher budgets while others see the standard caps.
- Employees do not pick a policy themselves; the targeting rules quietly route each person to the policy meant for them.
- Because rules can include or exclude by attribute, companies can carve out exceptions cleanly without creating duplicate policies.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — rules are defined per company policy and target employee groups within that company |

## Which team to connect with
**👉 Onboarding Team**

Because policy targeting is part of the company's travel **Policy Config**, a salesperson who wants to control which employees a policy applies to (by grade, department, entity, or business unit) should reach out to the **Onboarding Team**. They build the rule sets and set the include/exclude conditions.

> Use the Tech Team only for whitelisting-based features. Policy targeting is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside policy targeting rules and may also need to be set:

- **Policy ↔ Company / Employee / Guest Mapping** – associates a policy with companies and assigns specific employees or guests (`CorporateEntitlementCompanyPolicyMapping`, `CorporateEmployeeEntitlementMappingEntity`).
- **Hotel / Flight / Bus Budgets** – the budgets each targeted group will receive.
- **Trip Approval Workflow** – approval rules that can vary by the same employee groups.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `PolicyRuleEntity` — a named rule set attached to a policy
  - `PolicyRuleConditionEntity` — a single condition within a rule:
    - attribute type: `GRADE`, `DEPARTMENT`, `ENTITY`, `BUSINESS_UNIT`
    - operation: `INCLUDE` (apply only to listed values) or `EXCLUDE` (apply to all except listed values)
- Evaluated when resolving the applicable policy for an employee at trip creation.

## Sample questions this feature answers
- "Can a policy apply only to certain grades?"
- "Can we exclude a department from a policy?"
- "How do we target a policy to a specific business unit?"
- "Can senior employees get a different policy than everyone else?"
- "What attributes can we use to decide who a policy applies to?"
- "Who do I contact to change which employees a policy covers?"
- "Are policy targeting rules configurable per company?"
