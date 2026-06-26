---
feature_name: Invoice Ledger
feature_id: invoice-ledger
category: Invoicing, GST & Fees
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-04-30
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - sales-service
technical_keys:
  - enable_invoice_ledger
tags:
  - invoice
  - ledger
  - invoice ledger
  - running ledger
  - admin view
  - invoice tracking
  - accounts
  - billing history
  - statement
  - reconciliation
---

# Invoice Ledger

## Summary
This feature enables an invoice ledger view so that company admins can track all their invoices in a single running ledger. Instead of looking up invoices one by one, admins get a consolidated, statement-style view of invoices over time, which makes reconciliation and tracking far easier.

## What this feature does
When enabled, the platform exposes an **invoice ledger** for the company:

- Invoices are listed in a **running ledger** view, showing them in sequence over time.
- Admins can track invoices, follow their billing history, and reconcile against their own records from one place.

When disabled, the ledger view is not shown and invoices are accessed individually.

## Customer experience
- Company admins open the invoice ledger and see all invoices in one running, statement-like view.
- Reconciliation becomes simpler because invoices are tracked together rather than retrieved one at a time.
- Finance teams get a clear billing history for the company.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

Because the invoice ledger is part of the company's **Corporate Config**, a salesperson who wants to enable or explain the ledger view for a customer should reach out to the **Onboarding Team**. They turn the invoice ledger on for the company.

> Use the Tech Team only for whitelisting-based features. The invoice ledger is a Corporate Config setting, so it stays with Onboarding.

## Related / dependent settings
These work alongside the invoice ledger and may also need to be set:

- **Separate Invoice** – whether invoices are generated separately or combined (`enable_separate_invoice`).
- **Voucher & Invoice GST Details** – GST details on the invoices listed in the ledger (`show_voucher_gst_details`).
- **Invoice Traveler Details** – traveller fields shown on invoices (`invoice_traveler_details`).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `enable_invoice_ledger` — enables the running invoice ledger view for company admins
- Surfaced in the admin invoicing view (sales-service).

## Sample questions this feature answers
- "Can a company see all its invoices in one ledger?"
- "How do admins track invoices over time?"
- "What is the invoice ledger view?"
- "Can we enable a running ledger of invoices for a customer?"
- "How do customers reconcile their invoices?"
- "Who do I contact to turn on the invoice ledger?"
- "Is the invoice ledger configurable?"
