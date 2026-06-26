---
feature_name: Whitelisted Email Domains
feature_id: whitelisted-email-domains
category: SSO & Login
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-05-31
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - user-service
  - sales-service
technical_keys:
  - email_suffix
tags:
  - email domain
  - whitelisted domains
  - approved domains
  - email suffix
  - self-registration
  - user onboarding
  - domain restriction
  - corporate account
  - access control
  - allowed email
---

# Whitelisted Email Domains

## Summary
Whitelisted Email Domains defines the approved email domains for a company. Only users whose email addresses are on these approved domains can be added to — or self-register under — the corporate account. This keeps the company's account restricted to genuine employees and prevents unauthorized people from joining. Despite the word "whitelisted" in the name, this is a Corporate Config setting handled by the Onboarding Team, not a secret-manager whitelist.

## What this feature does
The platform checks a user's email domain against the company's approved list:

- **Approved domains only** — users with emails on the configured domains can be added or can self-register.
- **Blocks others** — users with emails outside the approved domains are not allowed onto the corporate account.
- **Supports multiple domains** — a company can list more than one approved email suffix where needed.

This ensures the company's account stays limited to legitimate, intended users.

## Customer experience
- Employees with approved company email addresses can be added or sign themselves up smoothly.
- People with non-approved email domains are prevented from joining the corporate account.
- The company keeps a clean, controlled user base tied to its own email domains.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

Even though the name says "whitelisted," this is a **Corporate Config** setting — **not** a secret-manager whitelist. A salesperson who wants to set or update the approved email domains for a customer should reach out to the **Onboarding Team**, who manage the company's allowed email suffixes.

> Important: do **not** route this to the Tech Team. The Tech Team only handles true secret-manager whitelist features. Approved email domains are configured in Corporate Config by Onboarding.

## Related / dependent settings
These work alongside approved email domains and may also be relevant:

- **Force SSO / Google SSO** – controls login methods for the company's users (Corporate Config).
- **SSO Provider Configuration** – identity provider connection details (Corporate Config).
- **Block Onboarding Notification** – new-user messaging controls during onboarding (Corporate Config).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `email_suffix` — the approved email domain(s); only users with emails on these domains can be added or self-register under the corporate account.

## Sample questions this feature answers
- "Can we restrict a company's account to specific email domains?"
- "How do I set the approved email domains for a customer?"
- "Can users self-register only with company email addresses?"
- "Is the 'whitelisted email domains' setting a Tech whitelist or Corporate Config?"
- "Which team configures approved email domains?"
- "Can a company have more than one approved email domain?"
- "What does email_suffix do?"
