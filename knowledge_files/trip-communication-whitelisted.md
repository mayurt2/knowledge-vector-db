---
feature_name: Trip Communication (Whitelisted)
feature_id: trip-communication-whitelisted
category: Notifications & Communications
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-04-09
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - trip-management-service
  - corporate-entitlement-service
  - sales-service
technical_keys:
  - trip.communication.corporate.whitelisted
tags:
  - trip communication
  - trip notification
  - approval updates
  - reminders
  - trip lifecycle
  - traveller communication
  - approver notification
  - whitelisted corporate
  - step-wise approval
  - trip alerts
---

# Trip Communication (Whitelisted)

## Summary
Trip Communication delivers trip lifecycle messages — such as trip creation, step-wise approval updates, and reminders — to the relevant travellers and approvers. This capability is currently restricted to whitelisted corporates, meaning a company must be explicitly added to a whitelist before these communications are turned on. Because it is gated by a whitelist managed in the secret manager, enabling it for a company is a Tech Team action.

## What this feature does
For companies that are whitelisted, the platform sends communications across the trip's lifecycle:

- **Trip creation** — notifies relevant parties when a trip is raised.
- **Step-wise approval updates** — keeps travellers and approvers informed as the trip moves through each approval stage.
- **Reminders** — nudges the right people when action is pending.

Because this feature is **whitelist-gated**, it only applies to companies whose IDs have been added to the configured whitelist. Companies not on the whitelist do not receive these trip lifecycle communications through this channel.

## Customer experience
- Travellers and approvers at whitelisted companies receive timely updates as a trip is created, moves through approvals, and approaches deadlines.
- Approvers are reminded when their action is pending, helping trips move forward without manual chasing.
- Companies that are not whitelisted do not get these communications until they are added.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** (via whitelist) |
| Where is it configured? | **Whitelisting** — Secret Manager Key |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — controlled by adding the company to the whitelist |

## Which team to connect with
**👉 Tech Team**

Because this feature is controlled by a **whitelist stored as a Secret Manager Key**, enabling trip communications for a customer requires adding the company to that whitelist. This is a Tech Team action, not a standard Corporate Config change.

> This is a whitelisting feature, so it is handled by the **Tech Team**, not Onboarding. The Onboarding Team handles Corporate Config settings only.

## Related / dependent settings
These work alongside trip communications and may also be relevant:

- **Trip Approval Workflow** – defines the approval stages that generate step-wise approval updates.
- **Disable Flight Notification** – separate Corporate Config control for flight notifications.
- **Block Onboarding Notification** – Corporate Config control for new-user welcome messages.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `trip.communication.corporate.whitelisted` — list of corporate IDs whitelisted to receive trip lifecycle communications (creation, step-wise approval updates, reminders).

## Sample questions this feature answers
- "Can we turn on trip creation and approval notifications for a company?"
- "Why isn't a company getting trip approval update messages?"
- "How do approvers get reminded about pending trips?"
- "Is trip communication available for all customers or only some?"
- "Who do I contact to enable trip communications for a customer?"
- "Is this a whitelisting feature or a Corporate Config setting?"
- "What does trip.communication.corporate.whitelisted control?"
