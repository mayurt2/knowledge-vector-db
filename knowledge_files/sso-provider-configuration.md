---
feature_name: SSO Provider Configuration
feature_id: sso-provider-configuration
category: SSO & Login
config_source: Corporate Config
configurable: true
status: in-development
target_release_date: 2026-07-19
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - user-service
  - sales-service
technical_keys:
  - sso_provider
  - client_tenant_id
  - client_id
  - authorization_endpoint
  - token_endpoint
  - client_secret
tags:
  - sso provider
  - sso configuration
  - identity provider
  - idp integration
  - oauth
  - tenant id
  - client id
  - authorization endpoint
  - token endpoint
  - single sign-on
  - authentication setup
---

# SSO Provider Configuration

## Summary
SSO Provider Configuration holds the connection settings needed to integrate a company's identity provider for single sign-on. This includes the provider name and the technical details — tenant ID, client ID, authorization and token endpoints, and the client secret — that let the platform securely connect to the company's SSO system. Once configured, the company's users can sign in through their own identity provider.

## What this feature does
This configuration captures everything required to connect to a company's SSO/identity provider:

- **Provider name** — which SSO provider is being used (`sso_provider`).
- **Tenant and client identifiers** — `client_tenant_id` and `client_id` identify the company's tenant and application.
- **Endpoints** — `authorization_endpoint` and `token_endpoint` are the provider URLs used during sign-in.
- **Client secret** — `client_secret` is the credential used to authenticate the connection.

With these in place, the SSO login experience (including Force SSO or Google SSO) can work against the company's identity provider.

## Customer experience
- Users sign in through their company's own identity provider, using familiar corporate credentials.
- The integration enables a seamless, secure single sign-on experience.
- The company maintains central control over access through its identity provider.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

Because these are **Corporate Config** settings, a salesperson who needs to set up or update a company's SSO provider details (provider, tenant ID, client ID, endpoints, secret) should reach out to the **Onboarding Team**. They configure the connection to the company's identity provider.

> Use the Tech Team only for whitelisting-based features. SSO provider setup is a standard Corporate Config task, so it stays with Onboarding.

## Related / dependent settings
These work alongside SSO provider configuration and may also be relevant:

- **Force SSO / Google SSO** – enforces SSO login and/or enables Google SSO (Corporate Config).
- **Whitelisted Email Domains** – approved domains for adding/self-registering users (Corporate Config).
- **Block Onboarding Notification** – new-user messaging controls during rollouts (Corporate Config).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `sso_provider` — the SSO provider name.
  - `client_tenant_id` — the company's tenant identifier.
  - `client_id` — the client/application identifier.
  - `authorization_endpoint` — provider authorization URL.
  - `token_endpoint` — provider token URL.
  - `client_secret` — credential used to authenticate the SSO connection.

## Sample questions this feature answers
- "What details do we need to set up SSO for a company?"
- "How do I configure a company's identity provider?"
- "Where do the tenant ID and client ID go for SSO?"
- "What are the authorization and token endpoints used for?"
- "Which team sets up the SSO provider connection?"
- "Is SSO provider configuration per company?"
- "What do sso_provider, client_id, and client_secret do?"
