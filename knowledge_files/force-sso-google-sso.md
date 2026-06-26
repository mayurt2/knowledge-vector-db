---
feature_name: Force SSO / Google SSO
feature_id: force-sso-google-sso
category: SSO & Login
config_source: Corporate Config
configurable: true
status: in-development
target_release_date: 2026-08-18
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - user-service
  - sales-service
technical_keys:
  - force_sso_enabled
  - google_sso_enabled
  - enable_for_all
tags:
  - sso
  - single sign-on
  - force sso
  - google sso
  - login method
  - authentication
  - sso enforcement
  - identity provider
  - secure login
  - sign-in
---

# Force SSO / Google SSO

## Summary
Force SSO / Google SSO controls how a company's users sign in. A company can force users to log in via SSO (blocking other login methods) for tighter security and central control, and/or enable Google SSO so users can sign in with their Google accounts. SSO enforcement can apply to all users or just a subset, giving flexibility during rollouts.

## What this feature does
These settings shape the company's login experience:

- **Force SSO** — when enabled, users must sign in through SSO; other login methods are blocked (`force_sso_enabled`).
- **Google SSO** — enables Google-based single sign-on so users can authenticate with Google (`google_sso_enabled`).
- **Apply to all or a subset** — `enable_for_all` determines whether the SSO enforcement applies to every user or only a subset, which is helpful for phased rollouts.

Together these let a company standardize and secure how its users access the platform.

## Customer experience
- Where Force SSO is on, users sign in only through the company's SSO, giving a single, consistent login path.
- Where Google SSO is enabled, users can sign in with their Google accounts.
- During a phased rollout, enforcement can be limited to a subset of users so the company can migrate gradually.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company (and can apply to all users or a subset) |

## Which team to connect with
**👉 Onboarding Team**

Because these are **Corporate Config** settings, a salesperson who wants to force SSO login, enable Google SSO, or control whether SSO applies to all users or a subset should reach out to the **Onboarding Team**. They configure how the company's users authenticate.

> Use the Tech Team only for whitelisting-based features. SSO enforcement is a standard Corporate Config setup, so it stays with Onboarding.

## Related / dependent settings
These work alongside SSO enforcement and may also be relevant:

- **SSO Provider Configuration** – the provider and connection details needed for SSO to work (Corporate Config).
- **Whitelisted Email Domains** – approved domains for adding/self-registering users (Corporate Config).
- **Block Onboarding Notification** – new-user messaging controls during rollouts (Corporate Config).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `force_sso_enabled` — when true, forces users to log in via SSO and blocks other login methods.
  - `google_sso_enabled` — when true, enables Google SSO sign-in.
  - `enable_for_all` — whether SSO enforcement applies to all users or only a subset.

## Sample questions this feature answers
- "Can we force a company's users to log in only via SSO?"
- "Can users sign in with Google?"
- "Can we roll out SSO to just some users first?"
- "How do I block password login and require SSO for a customer?"
- "Which team configures SSO and Google login?"
- "Is SSO enforcement configurable per company?"
- "What do force_sso_enabled, google_sso_enabled, and enable_for_all do?"
