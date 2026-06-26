---
feature_name: Hyper Care
feature_id: hyper-care
category: Admin & Account Settings
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-03-28
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - sales-service
technical_keys:
  - is_hyper_care
tags:
  - hyper care
  - hypercare
  - go-live support
  - heightened support
  - account monitoring
  - early support
  - onboarding support
  - white-glove support
  - go live
  - priority support
---

# Hyper Care

## Summary
Hyper Care places a company in a heightened support and monitoring mode, typically during the early go-live period after onboarding. When a company is in hyper care, the team keeps a closer watch on its activity and provides extra attention so any issues are caught and resolved quickly, giving the new customer a smooth start.

## What this feature does
This flag marks a company as being in a special, closely-monitored support state:

- **Hyper care on** – the company is flagged for heightened support and monitoring, usually right after go-live, so teams can proactively track and assist.
- **Hyper care off** – the company is treated as a standard account with normal support and monitoring.

Hyper care is generally a temporary state used during the critical early phase of a customer's journey, and is turned off once the account is stable.

## Customer experience
- A company in hyper care receives extra attention and faster response to issues during its early days on the platform.
- Teams monitor the account more closely to spot and resolve problems proactively.
- Once the account is settled, hyper care is removed and the company moves to standard support.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — enabled or disabled per company, usually around go-live |

## Which team to connect with
**👉 Onboarding Team**

Because hyper care is set through the company's **Corporate Config**, a salesperson who wants to place a customer in (or remove them from) hyper care should reach out to the **Onboarding Team**. They set the `is_hyper_care` flag, typically during the go-live phase.

> Use the Tech Team only for whitelisting-based features. Hyper care is part of Corporate Config and is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside hyper care and may also need to be considered:

- **Demo / Internal / Test Account Flags** – other account-state settings (Corporate Config + Whitelisting).
- **Super-Admin / Admin Assignment** – ensures the right people manage the account during go-live.
- **Onboarding Configuration** – the broader setup applied when a company first goes live.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `is_hyper_care` — marks the company as being in heightened support/monitoring mode
- Typically toggled on during early go-live and off once the account is stable.

## Sample questions this feature answers
- "What is hyper care mode?"
- "How do we put a new customer in hyper care?"
- "Can we enable extra monitoring for a company during go-live?"
- "How do we remove a company from hyper care?"
- "Is hyper care configurable per company?"
- "Who do I contact to set hyper care for a customer?"
- "When should an account be in hyper care?"
