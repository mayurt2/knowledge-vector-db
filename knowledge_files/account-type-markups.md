---
feature_name: Account Type & Markups
feature_id: account-type-markups
category: Admin & Account Settings
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-06-15
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - sales-service
technical_keys:
  - account_type
  - markup_premium
  - markup_budget
tags:
  - account type
  - markup
  - markups
  - premium markup
  - budget markup
  - fare markup
  - rate markup
  - pricing
  - account classification
  - premium account
  - budget account
  - margin
---

# Account Type & Markups

## Summary
Account Type & Markups define how a company is classified for pricing and what markups are applied to the fares and rates it sees. The account type sets the company's pricing tier, while the premium and budget markups adjust the prices shown on the platform — letting the business tailor margins and offerings to each customer.

## What this feature does
This feature combines a company's pricing classification with the markups applied to its fares/rates:

- **Account type** – classifies the company into a pricing category, which influences how rates and offerings are presented.
- **Premium markup** – an adjustment applied to premium fares/rates for the company.
- **Budget markup** – an adjustment applied to budget fares/rates for the company.

Together these determine the final fares and rates a company's users see, allowing pricing and margins to be tuned per customer based on their account type.

## Customer experience
- A company's users see fares and rates that reflect the company's account type and the configured markups.
- Premium and budget options are adjusted according to the company's markup settings.
- This lets each customer be offered pricing aligned with their negotiated terms or tier.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — account type and markups are set per company |

## Which team to connect with
**👉 Onboarding Team**

Because account type and markups are set through the company's **Corporate Config**, a salesperson who wants to set or change a customer's pricing classification or markups should reach out to the **Onboarding Team**. They configure `account_type`, `markup_premium`, and `markup_budget`.

> Use the Tech Team only for whitelisting-based features. Account type and markups are part of Corporate Config and are **not** a whitelisting feature, so they stay with Onboarding.

## Related / dependent settings
These work alongside account type and markups and may also need to be considered:

- **Pricing & Fare Display** – how the marked-up fares/rates are shown to users.
- **Demo / Internal / Test Account Flags** – non-real accounts may be treated differently for pricing and reporting.
- **Other Corporate Config Pricing Settings** – additional commercial terms set per company.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `account_type` — the company's pricing/account classification
  - `markup_premium` — markup applied to premium fares/rates
  - `markup_budget` — markup applied to budget fares/rates
- Together these determine the final fares/rates shown to the company's users.

## Sample questions this feature answers
- "How do we set a company's account type?"
- "Can we change the markup for a customer?"
- "What's the difference between premium and budget markup?"
- "How are a company's fares adjusted by markup?"
- "Is the account type configurable per company?"
- "Who do I contact to update a customer's markups?"
- "How do we classify a company's pricing tier?"
