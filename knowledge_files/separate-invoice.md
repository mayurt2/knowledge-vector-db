---
feature_name: Separate Invoice
feature_id: separate-invoice
category: Invoicing, GST & Fees
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-05-13
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - sales-service
technical_keys:
  - enable_separate_invoice
tags:
  - invoice
  - separate invoice
  - split invoice
  - combined invoice
  - per booking invoice
  - billing
  - invoice format
  - individual invoice
  - invoice generation
  - itemized invoice
---

# Separate Invoice

## Summary
This feature controls whether the platform generates separate invoices — for example, one per booking or per component — instead of bundling everything into a single combined invoice. Some corporates prefer an individual invoice for each booking for easier tracking and accounting, while others prefer one consolidated invoice.

## What this feature does
When a company has bookings to be invoiced, this setting decides the invoice format:

- **Separate invoices enabled** – each booking (or component) gets its **own invoice**, useful for companies that track or bill at a granular level.
- **Separate invoices disabled** – a **single combined invoice** is generated covering the relevant bookings/components.

This lets each company match invoicing to how its finance team prefers to process documents.

## Customer experience
- With separate invoices, the corporate receives an individual invoice per booking/component, making it easy to attribute costs.
- With a combined invoice, the company gets a single document, reducing the number of invoices to handle.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

Because separate-invoice behaviour is part of the company's **Corporate Config**, a salesperson who wants to enable or explain it for a customer should reach out to the **Onboarding Team**. They configure whether invoices are generated separately or combined.

> Use the Tech Team only for whitelisting-based features. Separate invoice is a Corporate Config setting, so it stays with Onboarding.

## Related / dependent settings
These work alongside separate invoicing and may also need to be set:

- **Invoice Ledger** – running ledger view of the invoices (`enable_invoice_ledger`).
- **Voucher & Invoice GST Details** – GST details on each invoice (`show_voucher_gst_details`).
- **Invoice Traveler Details** – traveller fields shown on invoices (`invoice_traveler_details`).
- **HSN/SAC Code on Invoice** – tax code on invoices (`enable_hsn_code`).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `enable_separate_invoice` — generates separate invoices (per booking/component) instead of a single combined invoice
- Applied at invoice generation (sales-service).

## Sample questions this feature answers
- "Can we generate a separate invoice for each booking?"
- "Does the customer get one combined invoice or many?"
- "Can invoices be split per component?"
- "How do we set up individual invoices for a company?"
- "What's the difference between separate and combined invoices?"
- "Who do I contact to enable separate invoices?"
- "Is separate invoicing configurable?"
