---
feature_name: HSN/SAC Code on Invoice
feature_id: hsn-code-invoice
category: Invoicing, GST & Fees
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-05-09
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - sales-service
technical_keys:
  - enable_hsn_code
tags:
  - hsn
  - sac
  - hsn code
  - sac code
  - tax code
  - invoice
  - gst
  - gst compliance
  - hsn sac
  - tax classification
  - invoice details
---

# HSN/SAC Code on Invoice

## Summary
This feature shows the HSN/SAC tax code on invoices. HSN (Harmonized System of Nomenclature) and SAC (Services Accounting Code) are standard codes used to classify goods and services for GST. Many corporates require these codes on their invoices for GST compliance and input-credit claims, and this setting makes them appear.

## What this feature does
When enabled, the system prints the relevant **HSN/SAC code** on the invoice, classifying the service (such as travel or accommodation) for GST purposes. This makes the invoice compliant with the GST requirements that many corporates must meet.

When disabled, the HSN/SAC code is not shown on the invoice.

## Customer experience
- The corporate receives invoices that include the HSN/SAC code, satisfying GST documentation requirements.
- Finance teams can process the invoice and claim input tax credit without chasing for the missing tax code.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

Because the HSN/SAC code display is part of the company's **Corporate Config**, a salesperson who wants to enable or explain it for a customer should reach out to the **Onboarding Team**. They turn the HSN code on for the company.

> Use the Tech Team only for whitelisting-based features. HSN/SAC code on invoice is a Corporate Config setting, so it stays with Onboarding.

## Related / dependent settings
These work alongside the HSN/SAC code and may also need to be set:

- **Voucher & Invoice GST Details** – GST details printed on documents (`show_voucher_gst_details`).
- **Inter-State GST (IGST)** – IGST vs intra-state treatment (`inter_state_gst`).
- **Separate Invoice** – whether invoices are generated separately or combined (`enable_separate_invoice`).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `enable_hsn_code` — shows the HSN/SAC tax code on invoices
- Applied at invoice generation (sales-service).

## Sample questions this feature answers
- "Can we show the HSN code on invoices for a customer?"
- "What is HSN/SAC code on the invoice?"
- "Why do some invoices not have the tax code?"
- "Does the invoice include the SAC code for GST?"
- "How do we make invoices GST-compliant with HSN codes?"
- "Who do I contact to enable the HSN code on invoices?"
- "Is the HSN code on invoices configurable?"
