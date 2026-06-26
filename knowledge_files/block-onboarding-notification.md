---
feature_name: Block Onboarding Notification
feature_id: block-onboarding-notification
category: Notifications & Communications
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-05-06
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - user-service
  - sales-service
technical_keys:
  - block_onboarding_notification
tags:
  - onboarding notification
  - welcome notification
  - block notification
  - suppress notification
  - bulk onboarding
  - new user notification
  - silent onboarding
  - user activation
  - notification control
  - welcome email
---

# Block Onboarding Notification

## Summary
Block Onboarding Notification lets a company suppress the automated onboarding and welcome notifications that are normally sent to new users when they are added to the platform. This is especially useful during bulk onboarding, where adding many users at once could otherwise trigger a flood of welcome messages. The company can add users quietly and communicate with them on its own schedule.

## What this feature does
When a new user is created on the platform, the system normally sends an onboarding/welcome notification. With this feature enabled:

- **Welcome notifications are suppressed** — new users are not automatically messaged when their account is created.
- **Ideal for bulk onboarding** — large batches of users can be added without each one receiving an automated message.
- **Accounts are still created normally** — only the onboarding notification is blocked; user setup and access are unaffected.

This gives companies control over when and how their new users first hear from the platform.

## Customer experience
- Newly added users do **not** receive an automatic welcome/onboarding notification.
- Their accounts are created and ready to use as normal.
- The company can choose to communicate with users via its own channels or at a later, coordinated time.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

Because this is a **Corporate Config** setting, a salesperson who wants to block (or re-enable) onboarding notifications for a customer — for example during a large rollout — should reach out to the **Onboarding Team**. They control whether new users get automated welcome messages.

> Use the Tech Team only for whitelisting-based features. This is a standard Corporate Config toggle, so it stays with Onboarding.

## Related / dependent settings
These work alongside onboarding notification controls and may also be relevant:

- **Disable Flight Notification** – turns off flight notifications to travelers (Corporate Config).
- **Emergency Contact Text** – free-text helpline info shown to travelers (Corporate Config).
- **Whitelisted Email Domains** – approved domains for adding/self-registering users (Corporate Config).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `block_onboarding_notification` — when true, suppresses automated onboarding/welcome notifications to newly created users.

## Sample questions this feature answers
- "Can we stop welcome emails when we bulk-add users for a company?"
- "How do I turn off onboarding notifications for new users?"
- "The client is uploading a large user list — can we avoid messaging everyone?"
- "Does blocking onboarding notifications stop the account from being created?"
- "Which team configures onboarding notification settings?"
- "Can welcome notifications be suppressed per company?"
- "What does block_onboarding_notification do?"
