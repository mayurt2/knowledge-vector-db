---
feature_name: Additional User Fields
feature_id: additional-user-fields
category: Cost Objects, Project Codes & Custom Fields
config_source: Corporate Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-06-10
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - user-service
  - sales-service
technical_keys:
  - additional_fields
tags:
  - additional fields
  - user fields
  - traveller data
  - custom information
  - booking fields
  - extra data
  - data capture
  - traveller details
  - configurable fields
  - user data
  - profile fields
---

# Additional User Fields

## Summary
Additional User Fields let a company collect extra pieces of information from users or travellers during booking. Beyond the standard details, a company can capture custom data it needs — for example identifiers, internal references, or traveller attributes — so the information is recorded at the point of booking. This gives companies flexibility to gather exactly the data their processes require.

## What this feature does
When configured for a company, the platform collects additional fields from the user/traveller during the booking flow:

- Extra data fields are presented to capture custom information beyond the standard booking details.
- The company defines what additional fields are collected, tailoring the capture to its needs.
- The captured values are recorded against the booking/user for downstream use such as reporting or compliance.

The additional fields are configured per company through Corporate Config, so each company can decide what extra information to collect.

## Customer experience
- During booking, travellers or bookers are prompted for the additional fields the company has defined.
- This ensures the company captures the custom information it needs without going outside the platform.
- Companies that don't need extra data simply leave the additional fields unconfigured.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — the additional fields are defined per company |

## Which team to connect with
**👉 Onboarding Team**

Because additional user fields are a **Corporate Config** setting, a salesperson who wants to set up or change the extra fields collected for a customer should reach out to the **Onboarding Team**. They define which additional fields are captured during booking.

> Use the Tech Team only for whitelisting-based features. This is a Corporate Config setting, so it stays with Onboarding.

## Related / dependent settings
These work alongside additional user fields:

- **Custom Fields** – corporate-defined fields captured against trips, bookings, and users (`TripCustomFieldsEntity`, `CorporateUserCustomFieldResponseDto`).
- **Cost Centres** and **Project Codes** – structured cost-object capture that complements free-form user data.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config — Corporate Entitlement Service
- **Key fields:**
  - `additional_fields` — defines the extra data fields collected from users/travellers during booking
- Read from Corporate Config; captured values are stored against the relevant user/booking records.

## Sample questions this feature answers
- "Can we collect extra information from travellers during booking?"
- "How do we add custom fields for users?"
- "Can a company capture additional data at booking time?"
- "What lets us gather custom traveller details?"
- "How do we set up additional user fields for a customer?"
- "Can the extra fields be different per company?"
- "Who do I contact to configure additional user fields?"
