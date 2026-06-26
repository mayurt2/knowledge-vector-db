---
feature_name: Demo / Internal / Test Account Flags
feature_id: demo-internal-test-account-flags
category: Admin & Account Settings
config_source: Corporate Config (is_test_company) + Whitelisting (demo/internal lists)
configurable: true
status: live
target_release_date: 2026-06-02
status_last_updated: 2026-06-26
contact_team: Onboarding Team & Tech Team
related_services:
  - corporate-entitlement-service
  - sales-service
technical_keys:
  - is_test_company
  - demo.account.companyIds
  - internal.corporates
tags:
  - test account
  - demo account
  - internal account
  - test company
  - non-production account
  - sandbox account
  - account flags
  - excluded from reporting
  - demo company
  - internal corporate
  - test flag
---

# Demo / Internal / Test Account Flags

## Summary
Demo / Internal / Test Account Flags let the platform mark a company as a demo, internal, or test account rather than a real paying customer. Marking an account this way changes how the platform behaves for it and ensures it is excluded from real business reporting and metrics — keeping dashboards and revenue numbers accurate.

## What this feature does
These flags classify a company as non-real for one of three purposes:

- **Test company** – used for testing the platform; behavior is altered and the account is kept out of real reporting.
- **Demo account** – used for demonstrations/sales walkthroughs; treated specially so it does not pollute live data.
- **Internal corporate** – an internal company account (e.g., used by staff) that should not count as a real customer.

There are two control points:
- **Corporate Config** – the `is_test_company` flag marks a single company as a test company directly in its config.
- **Whitelisting (Secret Manager Keys)** – central lists (`demo.account.companyIds`, `internal.corporates`) identify demo and internal companies across the platform.

When any of these apply, the company's activity is treated as non-production and excluded from real reporting.

## Customer experience
- A flagged account behaves differently from a real customer account in certain platform areas.
- The account's bookings and activity are excluded from real business reports and metrics.
- This keeps live dashboards clean and prevents test/demo activity from being mistaken for genuine business.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** (`is_test_company`) and **Whitelisting** (demo/internal lists) |
| Who configures it? | Onboarding Team (test company) / Tech Team (demo & internal whitelists) |
| Is it per-company? | Yes — set per company, via config flag or whitelist membership |

## Which team to connect with
This feature spans **both** Corporate Config and Whitelisting, so the right team depends on which flag is needed:

**👉 Onboarding Team** — for the **test company** flag (`is_test_company`), which lives in Corporate Config.

**👉 Tech Team** — for the **demo** and **internal** classifications, which are whitelisting-based and managed via Secret Manager Keys (`demo.account.companyIds`, `internal.corporates`).

> Use Onboarding for the Corporate Config flag and Tech for the whitelisting lists. If a customer needs more than one classification, both teams may need to be involved.

## Related / dependent settings
These work alongside the account flags and may also need to be considered:

- **Hyper Care** – another account-state setting used around go-live (Corporate Config).
- **Reporting & Analytics** – which excludes flagged accounts from real metrics.
- **Other Whitelisting Flags** – similarly managed corporate lists controlled via Secret Manager Keys.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config + Whitelisting (Secret Manager Keys)
- **Key fields:**
  - `is_test_company` (Corporate Config) — marks a single company as a test account
  - `demo.account.companyIds` (Whitelisting) — list of company IDs treated as demo accounts
  - `internal.corporates` (Whitelisting) — list of internal corporate accounts
- Flagged companies have altered behavior and are excluded from real reporting.

## Sample questions this feature answers
- "How do we mark a company as a test account?"
- "Can we set up a demo account for a sales walkthrough?"
- "How do we flag an internal corporate?"
- "Why is a test company showing up in reports?"
- "Who do I contact to mark an account as demo or internal?"
- "What's the difference between test, demo, and internal accounts?"
- "Is the test company flag configurable?"
- "How do we exclude an account from real reporting?"
