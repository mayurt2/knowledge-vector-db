---
feature_name: Show Brand Name
feature_id: show-brand-name
category: Branding & White-Labeling
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-04-10
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - show_brand_name
tags:
  - brand name
  - hotel brand
  - mask brand
  - hide brand
  - generic property
  - white-label
  - branding
  - property name
  - hotel name
  - brand visibility
---

# Show Brand Name

## Summary
Show Brand Name controls whether the hotel brand name is shown to travelers or masked. Some companies want travelers to see the full hotel brand; others prefer to show generic property information instead (for example, to keep the experience neutral or aligned with their own white-label approach). This simple toggle lets the company decide how property branding appears.

## What this feature does
When travelers view hotel options and bookings, the platform can either show or hide the hotel's brand name:

- **Show brand name** — travelers see the actual hotel brand (e.g., the chain or property brand).
- **Mask brand name** — the brand name is hidden and generic property information is shown instead.

This lets a company tailor how much brand detail its travelers see, supporting both branded and white-labeled experiences.

## Customer experience
- With the brand shown, travelers recognize the hotel brand they are booking.
- With the brand masked, travelers see generic property details instead of the brand name.
- The choice keeps the booking experience consistent with how the company wants properties presented.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

Because this is a **Corporate Config** setting, a salesperson who wants to show or mask the hotel brand name for a customer should reach out to the **Onboarding Team**. They control how property branding appears to the company's travelers.

> Use the Tech Team only for whitelisting-based features. This is a standard Corporate Config toggle, so it stays with Onboarding.

## Related / dependent settings
These work alongside brand-name visibility and may also be relevant:

- **Company / Client Logo** – company and co-branded client logos on customer-facing surfaces (Corporate Config).
- **Trip PDF Export** – exported documents reflect the configured property presentation (Corporate Config).
- **Emergency Contact Text** – other customer-facing display settings (Corporate Config).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `show_brand_name` — when true, displays the hotel brand name to travelers; when false, masks it and shows generic property information.

## Sample questions this feature answers
- "Can we hide the hotel brand name from a company's travelers?"
- "Can we show generic property info instead of the brand?"
- "How do I turn the hotel brand name on or off for a customer?"
- "Does masking the brand name change the booking itself?"
- "Which team controls brand name visibility?"
- "Is showing the brand name configurable per company?"
- "What does show_brand_name do?"
