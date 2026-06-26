---
feature_name: Company / Client Logo
feature_id: company-client-logo
category: Branding & White-Labeling
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-04-11
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - company_logo_enabled
  - client_logo_enabled
  - client_logo_image_format
  - client_logo_name
tags:
  - logo
  - company logo
  - client logo
  - branding
  - co-branding
  - white-label
  - voucher branding
  - portal branding
  - document branding
  - custom logo
  - brand identity
---

# Company / Client Logo

## Summary
Company / Client Logo lets a company display its own logo — and optionally a co-branded client logo — across customer-facing surfaces such as vouchers, the portal, and documents. This gives the experience a branded, professional look that matches the company's identity. Both the format and name of the client logo are configurable, so the right image is shown in the right places.

## What this feature does
The platform can render branding on customer-facing surfaces, controlled by a few settings:

- **Company logo** — show the company's logo (turned on via `company_logo_enabled`).
- **Client logo** — show an additional co-branded client logo (turned on via `client_logo_enabled`).
- **Client logo format** — specify the image format used for the client logo (`client_logo_image_format`).
- **Client logo name** — specify the file/name reference for the client logo (`client_logo_name`).

Together these let a company present a branded or co-branded experience on vouchers, the portal, and generated documents.

## Customer experience
- Travelers and other users see the company's branding on vouchers, the portal, and documents.
- Where co-branding is set up, both the company logo and the client logo can appear together.
- The branded surfaces feel consistent with the company's own identity, reinforcing trust.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

Because logo and branding settings live in **Corporate Config**, a salesperson who wants to enable a company logo, add a co-branded client logo, or change the logo format/name should reach out to the **Onboarding Team**. They configure which logos appear and how.

> Use the Tech Team only for whitelisting-based features. Logo branding is a standard Corporate Config setup, so it stays with Onboarding.

## Related / dependent settings
These work alongside logo branding and may also be relevant:

- **Show Brand Name** – shows or masks the hotel brand name to travelers (Corporate Config).
- **Emergency Contact Text** – free-text helpline info shown on customer-facing surfaces (Corporate Config).
- **Trip PDF Export** – exported documents may carry the configured branding (Corporate Config).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `company_logo_enabled` — toggles display of the company logo.
  - `client_logo_enabled` — toggles display of the co-branded client logo.
  - `client_logo_image_format` — image format of the client logo.
  - `client_logo_name` — name/reference for the client logo file.

## Sample questions this feature answers
- "Can we put a company's logo on their vouchers and portal?"
- "Can we show a co-branded client logo alongside the company logo?"
- "What image format can we use for the client logo?"
- "How do I set up custom branding for a customer?"
- "Which team configures logos and branding?"
- "Is logo branding configurable per company?"
- "What do company_logo_enabled and client_logo_enabled do?"
