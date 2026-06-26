---
feature_name: Guest Policy Allowed
feature_id: guest-policy-allowed
category: Guest Bookings
config_source: Corporate Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-04-02
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - allow_guest_policy
tags:
  - guest booking
  - guest traveller
  - non-employee
  - guest policy
  - visitor booking
  - candidate travel
  - guest travel
  - external traveller
  - book for guest
  - guest controls
  - travel policy
---

# Guest Policy Allowed

## Summary
Guest Policy Allowed lets a company book travel for guest travellers — people who are not employees, such as visitors, candidates, consultants, or partners — through the corporate account. When enabled, these guest bookings are made under a guest travel policy so the company's controls still apply, rather than booking outside the system. This makes it easy and compliant to arrange travel for non-employees.

## What this feature does
When this setting is turned on for a company, the platform supports booking for guest travellers:

- Bookings can be created for **non-employee travellers** (visitors, interview candidates, contractors, partners, and similar).
- These guest bookings are governed by a **guest travel policy**, so the company's policy controls are still applied rather than bypassed.
- Guest travel flows through the corporate account, keeping it visible, trackable, and within the company's spend and policy framework.

The feature is switched on or off per company through Corporate Config. The specific policy that applies to guests is determined by a related setting (Applicable Guest Policy Type).

## Customer experience
- Travel desks and bookers can arrange travel for guests directly within the corporate platform instead of going off-system.
- Guest bookings still respect the company's chosen policy controls, keeping spend compliant.
- Visitors, candidates, and other non-employees can be hosted smoothly without setting them up as full employees.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — enabled or disabled per company |

## Which team to connect with
**👉 Onboarding Team**

Because allowing guest bookings is a **Corporate Config** setting, a salesperson who wants to enable, disable, or explain it for a customer should reach out to the **Onboarding Team**. They turn guest policy on or off and coordinate which guest policy applies.

> Use the Tech Team only for whitelisting-based features. This is a Corporate Config setting, so it stays with Onboarding.

## Related / dependent settings
These work alongside guest booking:

- **Applicable Guest Policy Type** – defines which policy applies to guests: ZERO, DEFAULT, or APPROVAL_HIERARCHY (`applicable_guest_policy`).
- **Trip Approval Workflow** – relevant when guests are routed through the approval hierarchy.
- **Travel Policy Config** – the company policy controls that guest bookings can inherit.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config — Corporate Entitlement Service
- **Key fields:**
  - `allow_guest_policy` — when enabled, permits bookings for guest (non-employee) travellers under a guest travel policy
- Read from Corporate Config; works in conjunction with `applicable_guest_policy` to determine which policy governs guest travel.

## Sample questions this feature answers
- "Can we book travel for non-employees?"
- "How do we enable guest bookings for a company?"
- "Can a company book travel for candidates or visitors?"
- "Do guest bookings follow the company's travel policy?"
- "What lets us book guests through the corporate account?"
- "Can guest booking be switched off for a customer?"
- "Who do I contact to allow guest policy?"
