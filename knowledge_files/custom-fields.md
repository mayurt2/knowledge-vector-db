---
feature_name: Custom Fields
feature_id: custom-fields
category: Cost Objects, Project Codes & Custom Fields
config_source: Corporate Config (Corporate Entitlement Service — corporate-defined)
configurable: true
status: live
target_release_date: 2026-05-03
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - user-service
  - sales-service
technical_keys:
  - TripCustomFieldsEntity
  - CorporateUserCustomFieldResponseDto
tags:
  - custom fields
  - custom data
  - metadata capture
  - trip fields
  - user fields
  - booking fields
  - reporting fields
  - compliance data
  - configurable fields
  - corporate fields
  - additional metadata
---

# Custom Fields

## Summary
Custom Fields let a company define its own data fields to capture against trips, bookings (per service type), and users. This gives each company the flexibility to collect whatever extra information it needs — for reporting, compliance, billing, or internal tracking — without being limited to the platform's standard fields. The fields are defined by the corporate and applied across the relevant booking and user flows.

## What this feature does
When configured for a company, the platform captures corporate-defined custom fields at several levels:

- **Trip-level custom fields** – arbitrary fields collected against a trip.
- **Booking-level custom fields (per service type)** – fields collected for specific services (hotel, flight, bus, train, cab), so different services can capture different data.
- **User-level custom fields** – fields collected against users/travellers, for profile or compliance data.

Because the fields are corporate-defined, each company can tailor exactly what metadata is captured. The data then flows into reporting and downstream processes wherever it is needed.

## Customer experience
- Companies can capture the exact extra information they need (e.g., internal references, compliance attributes, billing notes) that the standard fields don't cover.
- Employees and travellers fill in these custom fields during the relevant booking or profile flow.
- The captured data supports the company's reporting, compliance, and reconciliation needs.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** (Corporate Entitlement Service — corporate-defined) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — fields are defined per company |

## Which team to connect with
**👉 Onboarding Team**

Because custom fields are **corporate-defined Corporate Config**, a salesperson who wants to set up or change the custom fields captured for a customer should reach out to the **Onboarding Team**. They define the trip, booking, and user fields the company needs.

> Use the Tech Team only for whitelisting-based features. Custom fields are a Corporate Config capability, so they stay with Onboarding.

## Related / dependent settings
These work alongside custom fields:

- **Additional User Fields** – extra data collected from users/travellers during booking (`additional_fields`).
- **Cost Centres** and **Project Codes** – structured cost-object tagging that complements free-form custom fields.
- **Custom Fields per Service Type** – different fields can be captured for different booking services.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config — Corporate Entitlement Service (corporate-defined)
- **Key fields:**
  - `TripCustomFieldsEntity` — custom fields captured against trips and bookings (per service type)
  - `CorporateUserCustomFieldResponseDto` — custom fields captured against users/travellers
- Field definitions are corporate-defined in Corporate Config; captured values are stored against the trip, booking, or user records.

## Sample questions this feature answers
- "Can a company capture custom data on trips?"
- "Can we collect extra fields for specific booking types?"
- "Can custom fields be captured against users?"
- "How do we add a custom field a customer needs for reporting?"
- "Are custom fields different per service like hotel vs flight?"
- "How do we set up custom fields for compliance?"
- "Who do I contact to configure custom fields?"
