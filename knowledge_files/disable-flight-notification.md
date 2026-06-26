---
feature_name: Disable Flight Notification
feature_id: disable-flight-notification
category: Notifications & Communications
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-05-08
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - disable_flight_notification
tags:
  - flight notification
  - disable notification
  - turn off notifications
  - whatsapp notification
  - email notification
  - traveler messaging
  - flight alerts
  - notification opt-out
  - communication preferences
  - silence notifications
---

# Disable Flight Notification

## Summary
Disable Flight Notification lets a company switch off all flight-related notifications (such as WhatsApp messages and emails) that would otherwise be sent to its travelers. Some companies prefer that their travelers are not messaged directly by the platform — for example, when the company manages traveler communications through its own travel desk. Turning this on keeps the booking working as usual while keeping the traveler's inbox quiet for flight updates.

## What this feature does
When a flight booking event occurs (booking confirmation, schedule change, reminder, etc.), the platform normally sends the traveler a notification over channels like WhatsApp and email. With this feature enabled:

- **Flight notifications are suppressed** — the traveler does not receive automated flight messages.
- **Bookings still proceed normally** — only the outbound messaging to the traveler is turned off; the trip, ticket, and records are unaffected.
- **Other notification types are unaffected** — this control is specific to flight notifications and does not silence unrelated communications.

This is typically used by companies that do not want the platform messaging their travelers directly about flights.

## Customer experience
- Travelers at the company do **not** receive WhatsApp/email notifications for flight-related events.
- The booking experience is otherwise unchanged — flights are still searched, booked, and recorded.
- The company can rely on its own internal channels (travel desk, HR, internal tools) to keep travelers informed if needed.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

Because this is a **Corporate Config** setting, a salesperson who wants to turn flight notifications on or off for a customer should reach out to the **Onboarding Team**. They control whether the company's travelers are messaged for flight events.

> Use the Tech Team only for whitelisting-based features. This is a standard Corporate Config toggle, so it stays with Onboarding.

## Related / dependent settings
These work alongside flight notification controls and may also be relevant:

- **Emergency Contact Text** – free-text helpline info shown to travelers (Corporate Config).
- **Block Onboarding Notification** – suppresses welcome notifications to new users (Corporate Config).
- **Trip Communication (Whitelisted)** – broader trip lifecycle communications, currently restricted to whitelisted corporates.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `disable_flight_notification` — when true, suppresses outbound flight notifications (WhatsApp/email) to the company's travelers.

## Sample questions this feature answers
- "Can we stop sending flight notifications to a company's travelers?"
- "How do I turn off WhatsApp flight messages for a customer?"
- "The client doesn't want their travelers emailed about flights — is that possible?"
- "Does disabling flight notifications affect the booking itself?"
- "Which team configures flight notification settings?"
- "Can flight notifications be turned off per company?"
- "What does disable_flight_notification do?"
