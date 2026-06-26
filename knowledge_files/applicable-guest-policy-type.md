---
feature_name: Applicable Guest Policy Type
feature_id: applicable-guest-policy-type
category: Guest Bookings
config_source: Corporate Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-04-06
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - applicable_guest_policy
tags:
  - guest policy
  - guest booking
  - policy type
  - approval hierarchy
  - default policy
  - zero policy
  - non-employee
  - guest travel
  - policy selection
  - travel policy
  - guest controls
---

# Applicable Guest Policy Type

## Summary
Applicable Guest Policy Type defines exactly which policy applies when a company books travel for guest travellers. It lets a company choose between no guest policy, using the company's default policy, or routing guests through the approval hierarchy. This gives precise control over how strictly guest bookings (for visitors, candidates, and other non-employees) are governed.

## What this feature does
When guest bookings are allowed, this setting determines which policy rules apply to those guests. There are three options:

- **ZERO** – no guest policy is applied; guests are not governed by a specific guest policy.
- **DEFAULT** – guests follow the company's **default policy**, so guest travel is treated under the standard company rules.
- **APPROVAL_HIERARCHY** – guests follow the **approval hierarchy**, meaning guest bookings move through the company's approval chain like other trips.

The selected option is set per company through Corporate Config and works hand-in-hand with the setting that allows guest bookings in the first place.

## Customer experience
- Companies can decide how tightly guest travel is controlled — from no special policy, to the standard company policy, to full approval routing.
- Choosing the approval hierarchy means guest bookings require sign-off just like employee trips, adding oversight for non-employee travel.
- The choice is applied consistently to all guest bookings for the company.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — the policy type is selected per company |

## Which team to connect with
**👉 Onboarding Team**

Because the guest policy type is a **Corporate Config** setting, a salesperson who wants to choose or change which policy applies to guests for a customer should reach out to the **Onboarding Team**. They set the value to ZERO, DEFAULT, or APPROVAL_HIERARCHY.

> Use the Tech Team only for whitelisting-based features. This is a Corporate Config setting, so it stays with Onboarding.

## Related / dependent settings
These work alongside the guest policy type:

- **Guest Policy Allowed** – the master switch that permits guest bookings in the first place (`allow_guest_policy`).
- **Trip Approval Workflow** – relevant when guests are set to follow the APPROVAL_HIERARCHY option.
- **Travel Policy Config** – the default company policy that guests inherit under the DEFAULT option.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config — Corporate Entitlement Service
- **Key fields:**
  - `applicable_guest_policy` — selects which policy governs guests: `ZERO` (no guest policy), `DEFAULT` (use the default company policy), or `APPROVAL_HIERARCHY` (guests follow the approval hierarchy)
- Read from Corporate Config; depends on `allow_guest_policy` being enabled for guest bookings to occur.

## Sample questions this feature answers
- "Which policy applies to guest travellers?"
- "Can guests be put through the approval hierarchy?"
- "What does ZERO vs DEFAULT vs APPROVAL_HIERARCHY mean for guests?"
- "Can guest bookings use the company's default policy?"
- "How do we make guest travel require approval?"
- "How do we change the guest policy type for a customer?"
- "Who do I contact to set the applicable guest policy?"
