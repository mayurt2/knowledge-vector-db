---
feature_name: Invoice Traveler Details
feature_id: invoice-traveler-details
category: Invoicing, GST & Fees
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-06-16
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - sales-service
technical_keys:
  - invoice_traveler_details
tags:
  - invoice
  - traveler details
  - traveller details
  - invoice fields
  - guest details
  - passenger details
  - invoice content
  - billing details
  - invoice personalization
  - traveler information
---

# Invoice Traveler Details

## Summary
This feature controls which traveller fields appear on invoices. Companies differ in how much traveller information they want printed on a tax invoice — some need full traveller details for tracking and audit, others prefer a minimal invoice. This setting lets each company decide what traveller information shows up.

## What this feature does
When an invoice is generated, the platform uses this configuration to decide which **traveller fields** to include on the document — for example, traveller name and other identifying details. This tailors the invoice content to each company's reporting and compliance needs.

## Customer experience
- The corporate receives invoices that show exactly the traveller information it has chosen to display.
- Finance and audit teams can match invoices to travellers when the relevant fields are included.
- Companies that prefer cleaner invoices can keep traveller details minimal.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

Because invoice traveller details are part of the company's **Corporate Config**, a salesperson who wants to change or explain which traveller fields appear for a customer should reach out to the **Onboarding Team**. They configure the traveller details shown on invoices.

> Use the Tech Team only for whitelisting-based features. Invoice traveller details is a Corporate Config setting, so it stays with Onboarding.

## Related / dependent settings
These work alongside invoice traveller details and may also need to be set:

- **Separate Invoice** – whether invoices are generated separately or combined (`enable_separate_invoice`).
- **Voucher & Invoice GST Details** – GST details on invoices (`show_voucher_gst_details`).
- **Invoice Ledger** – running ledger view of invoices (`enable_invoice_ledger`).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `invoice_traveler_details` — controls which traveller fields appear on invoices
- Applied at invoice generation (sales-service).

## Sample questions this feature answers
- "Can we control which traveller details show on invoices?"
- "Does the invoice show the traveller's name?"
- "Can we hide traveller details on invoices for a customer?"
- "What traveller information appears on the invoice?"
- "How do we customise invoice content for a company?"
- "Who do I contact to change invoice traveller details?"
- "Is invoice traveller detail configurable?"
