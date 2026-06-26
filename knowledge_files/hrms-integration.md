---
feature_name: HRMS Integration
feature_id: hrms-integration
category: Integrations
config_source: HRMS Connector (Employee Management Service)
configurable: true
status: live
target_release_date: 2026-04-15
status_last_updated: 2026-06-26
contact_team: Onboarding Team & Tech Team
related_services:
  - employee-management-service
  - sales-service
  - tartan-hrms-client
  - unifyx-hrms-client
technical_keys:
  - HrmsProvider (TARTAN / UNIFYX / SFTP)
  - employee_sync_connector (company_id, provider, connector_token, sync_enabled)
  - HRMSServiceFactory
  - EmployeeDataSyncService
  - unifyX.base.url (api.bindbee.dev)
  - tartan.base.url (node.tartanhq.com)
  - unifyx.scheduler.cron
  - employee.sync.kafka.topic
tags:
  - hrms
  - hrms integration
  - hr integration
  - employee sync
  - employee data sync
  - tartan
  - bindbee
  - unifyx
  - hrms aggregator
  - hris
  - employee onboarding
  - auto sync employees
  - directory sync
  - integration
---

# HRMS Integration

## Summary
HRMS Integration lets a company automatically sync its employee data from its existing HR system (HRMS/HRIS) into the travel platform, so the employee directory stays up to date without manual uploads. Instead of building a separate connector for every HR vendor, the platform connects through **HRMS aggregators** — **Tartan** and **Bindbee** — which in turn talk to hundreds of underlying HR systems. Once set up, new joiners, exits, and profile changes flow into the platform on a regular schedule.

## What this feature does
When a company enables HRMS Integration, the platform creates a **sync connector** for that company and pulls employee records from the company's HR system through the chosen aggregator:

- **Tartan** – HRMS aggregator connected via the `TARTAN` provider.
- **Bindbee** – HRMS aggregator connected via the `UNIFYX` provider (Bindbee is the aggregator behind the UnifyX connector).
- **SFTP** – an additional option for companies that prefer to drop employee files over secure file transfer instead of an API aggregator.

How the sync works:
- A **connector** is configured per company with the HR system's access token and the chosen provider, and a `sync_enabled` switch turns syncing on or off.
- A **scheduler** runs on a fixed schedule (cron) and, for every company with sync enabled, fetches the latest employee data from the aggregator (paginated for large directories).
- Fetched records are mapped into the platform's standard employee format and **published to the Sales Service** (via Kafka) so the employee base, profiles, and access stay current.
- The platform tracks **sync runs** (last sync time, counts, success/failure) so admins can see whether the latest sync worked.
- Individual employee lookups (e.g. by official email) can also be pulled on demand from the connected HR system.

## Customer experience
- The customer's employee list stays automatically up to date — new hires appear, leavers are removed, and changes (department, grade, manager, cost centre, etc.) flow through without manual spreadsheets.
- Admins can see the **last sync status and time**, and trigger a sync manually if needed.
- Because it works through aggregators (Tartan / Bindbee), the platform can connect to a wide range of HR systems the customer may already use, rather than needing a custom build per HR vendor.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **HRMS Connector** in the Employee Management Service (provider + connector token + sync toggle) |
| Who configures it? | Onboarding Team (to initiate) + Tech Team (to set up the connector, credentials & aggregator keys) |
| Is it per-company? | Yes — one sync connector per company, with its own provider and token |

## Which team to connect with
**👉 Onboarding Team (to start) + Tech Team (to set up the connection)**

HRMS Integration is an **integration**, not a simple on/off toggle, so it involves both teams:
- The **Onboarding Team** scopes the requirement with the customer — which HR system they use and which aggregator (Tartan or Bindbee) fits.
- The **Tech Team** does the technical setup: creating the per-company sync connector, securely storing the customer's HR access token, and managing the aggregator API keys/bearer tokens (held as Secret Manager keys).

> Tip for sales: treat this like an onboarding + integration request. Start with the Onboarding Team to capture the customer's HR system; the Tech Team then provisions and tests the connector before sync is switched on.

## Related / dependent settings
These work alongside HRMS Integration:

- **Whitelisted Email Domains** – the approved company email domains that synced employees must belong to.
- **Employee Export** – export the (now auto-synced) employee list/data.
- **Additional User Fields / Custom Fields (User)** – capture extra employee attributes that come from the HR system.
- **SSO & Login** – often paired with HRMS sync so identity and directory data stay aligned.
- **Cost Objects / Project Codes** – employee cost-centre/department data from HRMS can feed cost attribution.

## Technical reference (for Onboarding/Tech)
- **Owning service:** employee-management-service (Java 17)
- **Providers (`HrmsProvider` enum):** `TARTAN`, `UNIFYX` (Bindbee), `SFTP`
- **Provider routing:** `HRMSServiceFactory` returns `TartanHRMSServiceImpl` or `UnifyXHRMSServiceImpl` based on the connector's provider
- **Per-company config:** `employee_sync_connector` table — `company_id`, `provider`, `connector_token`, `sync_enabled`
- **Aggregator endpoints:**
  - Bindbee (UnifyX): `unifyX.base.url = https://api.bindbee.dev/api/hris/v1/employees` (with `unifyX.api.key` / `unifyX.bearer.token`)
  - Tartan: `tartan.base.url = https://node.tartanhq.com` (with `tartan.api.key`)
- **Scheduling:** `unifyx.scheduler.cron` drives periodic sync over all connectors where `sync_enabled = true`
- **Downstream:** synced data is published to the Sales Service via Kafka (`employee.sync.kafka.topic`, `unifyX.sync.kafka.topic`)
- **Key classes:** `EmployeeDataSyncService` / `EmployeeDataSyncServiceImpl`, `HRMSService`, `TartanHRMSServiceImpl`, `UnifyXHRMSServiceImpl`, `UnifyXScheduler`, `EmployeeDataSyncController`
- **Secrets:** aggregator API keys / bearer tokens are environment/Secret Manager managed (Tech Team)

## Sample questions this feature answers
- "Do we support HRMS integration?"
- "Which HRMS systems / aggregators do we connect to?"
- "What is Tartan and Bindbee integration?"
- "Can a customer's employee data sync automatically from their HR system?"
- "How does employee sync work?"
- "Can we connect to a customer's HRMS instead of uploading employees manually?"
- "Is HRMS integration live?"
- "Who do I contact to set up HRMS sync for a company?"
- "Can employees sync over SFTP instead of an API?"
