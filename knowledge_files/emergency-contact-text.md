---
feature_name: Emergency Contact Text
feature_id: emergency-contact-text
category: Notifications & Communications
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-04-16
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - emergency_contact_text
tags:
  - emergency contact
  - helpline
  - 24x7 support
  - traveler support
  - contact info
  - emergency number
  - support text
  - safety
  - duty of care
  - assistance
---

# Emergency Contact Text

## Summary
Emergency Contact Text lets a company show its travelers a custom, free-text emergency contact message — for example, a 24x7 helpline number or a dedicated travel-desk contact. This puts the right point of contact in front of travelers when they need help, supporting the company's duty-of-care commitments without any custom development.

## What this feature does
A company can enter any free-text emergency contact details, and the platform displays that text to travelers on relevant surfaces. With this feature configured:

- **Custom helpline information is shown** — travelers see exactly the contact details the company provides (phone number, email, instructions, etc.).
- **Fully free-text** — the company controls the wording, so it can include a 24x7 line, a regional contact, or specific escalation instructions.
- **Company-specific** — each company can show its own emergency contact information.

This is commonly used to surface a 24x7 traveler support or emergency helpline.

## Customer experience
- Travelers can see the company's emergency contact information when they need assistance during travel.
- The message reassures travelers that there is a clear point of contact for emergencies.
- The exact text is decided by the company, so it matches the company's own support setup.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

Because this is a **Corporate Config** setting, a salesperson who wants to set up or update the emergency contact message for a customer should reach out to the **Onboarding Team**. They enter and maintain the free-text contact details shown to travelers.

> Use the Tech Team only for whitelisting-based features. This is a standard Corporate Config field, so it stays with Onboarding.

## Related / dependent settings
These work alongside emergency contact information and may also be relevant:

- **Disable Flight Notification** – turns off flight notifications to travelers (Corporate Config).
- **Block Onboarding Notification** – suppresses welcome notifications to new users (Corporate Config).
- **Company / Client Logo** – branding shown to travelers on customer-facing surfaces (Corporate Config).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `emergency_contact_text` — free-text field holding the emergency/helpline contact information displayed to travelers.

## Sample questions this feature answers
- "Can we show a 24x7 helpline number to a company's travelers?"
- "How do I add emergency contact details for a customer?"
- "Can travelers see who to call in an emergency?"
- "Is the emergency contact message customizable per company?"
- "Which team sets up the emergency contact text?"
- "Can we display custom support contact info to travelers?"
- "What does emergency_contact_text do?"
