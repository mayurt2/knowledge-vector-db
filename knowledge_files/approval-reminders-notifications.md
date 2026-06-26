---
feature_name: Approval Reminders & Notifications
feature_id: approval-reminders-notifications
category: Approvals
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-03-28
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - trip-management-service
  - sales-service
technical_keys:
  - send.reminder.time.threshold
  - kafka.trip.reminder.topic
  - trip.communication.corporate.whitelisted
tags:
  - approval reminders
  - approval notifications
  - pending approval reminder
  - reminder notification
  - approver reminder
  - stalled trip
  - time threshold
  - kafka reminder
  - whitelisted notification
  - approval follow-up
  - nudge approver
  - approval alert
---

# Approval Reminders & Notifications

## Summary
Approval Reminders & Notifications make sure trips do not stall while waiting on an approver. When an approval has been **pending for longer than a configured time threshold**, the system sends a reminder notification to the approver, nudging them to act. This keeps the approval pipeline moving and prevents trips from getting stuck. The feature is currently **sent only to whitelisted corporates**, controlled via a Secret Manager key.

## What this feature does
When a trip approval has been pending, the system tracks how long it has waited and triggers reminders:

- **Time-threshold trigger** – once a pending approval crosses the configured wait time (`send.reminder.time.threshold`), a reminder is queued.
- **Event-driven delivery** – reminders are published to a Kafka topic (`kafka.trip.reminder.topic`) which drives the notification to the approver.
- **Whitelisted corporates only** – reminders are sent only for corporates present in the whitelist (`trip.communication.corporate.whitelisted`); other corporates do not receive these reminders.

The goal is to reduce the number of trips that sit idle because an approver simply forgot or missed the original request.

## Customer experience
- Approvers in enabled corporates receive a follow-up reminder when they have a pending trip approval that has been waiting too long.
- Employees benefit from faster turnaround because their trips are less likely to stall awaiting a forgotten approval.
- Corporates not on the whitelist do not receive these reminder notifications.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** (via whitelisting) |
| Where is it configured? | **Whitelisting** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — sent only to whitelisted corporates; time threshold is configurable |

## Which team to connect with
**👉 Tech Team**

Because approval reminders are gated by a **whitelisting (Secret Manager) key** and rely on a Kafka-driven pipeline, a salesperson who wants to enable reminders for a customer should reach out to the **Tech Team**. They add the corporate to the `trip.communication.corporate.whitelisted` list and set the reminder time threshold.

> Whitelisting features are owned by Tech, not Onboarding. Approval reminders are enabled through a Secret Manager key, so they sit with the **Tech Team**.

## Related / dependent settings
These work alongside approval reminders and may also need to be set:

- **Trip Approval Workflow** – the core approval setup that determines who the pending approver is (`noOfApprovers`).
- **Approver Chain Definition** – defines the approver who receives the reminder (`EntitlementApproversEntity`).
- **Skip In-Policy Approvals** – fewer pending approvals to remind about when in-policy trips are auto-approved.
- **Trigger Booking After Approval** – reminders help complete approvals so booking can proceed.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `send.reminder.time.threshold` — how long an approval may stay pending before a reminder is sent
  - `kafka.trip.reminder.topic` — Kafka topic that carries reminder events to the notification pipeline
  - `trip.communication.corporate.whitelisted` — whitelist of corporates eligible to receive reminder notifications
- Implemented in trip-management-service; reminders are produced to the Kafka topic and delivered only for whitelisted corporates.

## Sample questions this feature answers
- "Do approvers get reminders for pending approvals?"
- "How do we stop trips from stalling at approval?"
- "After how long is a reminder sent to an approver?"
- "Is the approval reminder available for all corporates?"
- "How do we enable approval reminders for a customer?"
- "Which team enables approval reminder notifications?"
- "Can we configure the reminder time threshold?"
- "Why aren't my customer's approvers getting reminders?"
