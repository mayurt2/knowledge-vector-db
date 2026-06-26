---
feature_name: Voucher & Invoice GST Details
feature_id: voucher-invoice-gst-details
category: Invoicing, GST & Fees
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-04-20
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - sales-service
technical_keys:
  - show_voucher_gst_details
  - enable_project_code_gst
tags:
  - gst
  - voucher
  - invoice
  - gst details
  - tax details
  - project code
  - project code gst
  - gst entity
  - booking voucher
  - gstin
  - tax invoice
---

# Voucher & Invoice GST Details

## Summary
This feature controls whether GST (tax) details are printed on the booking voucher and invoices that a corporate receives. When enabled, the GST entity information — such as the company's GST identity used for the booking — appears on the documents, which corporates need for tax filing and input-credit claims. For companies that book against project codes, the GST entity can be linked to the project so the correct tax details are carried through.

## What this feature does
When a booking is completed, the system generates a voucher and invoice. Based on the company's configuration, it decides what GST information to print:

- **Show voucher GST details** – the GST entity details are printed on the booking voucher and invoice, so the document is GST-compliant and ready for accounting.
- **Project-code-linked GST** – when a booking is made against a project code, the GST entity information tied to that project code is carried onto the documents. This lets companies that route spend by project keep the correct GST identity on each booking.

If the feature is off, vouchers and invoices are generated without the detailed GST entity information.

## Customer experience
- The corporate's traveller or admin downloads a voucher/invoice that already shows the correct GST details — no manual entry needed.
- Finance teams can claim input tax credit because the GST identity is correctly printed.
- For project-based companies, each booking carries the GST entity tied to its project code, so reconciliation by project is clean.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company, and project-code GST applies to companies that use project codes |

## Which team to connect with
**👉 Onboarding Team**

Because GST display on vouchers and invoices is part of the company's **Corporate Config**, a salesperson who wants to turn this on or explain it for a customer should reach out to the **Onboarding Team**. They enable the voucher GST details and configure project-code-linked GST entities.

> Use the Tech Team only for whitelisting-based features. This is a Corporate Config setting, so it stays with Onboarding.

## Related / dependent settings
These work alongside voucher/invoice GST details and may also need to be set:

- **HSN/SAC Code on Invoice** – shows the tax code alongside GST details (`enable_hsn_code`).
- **Inter-State GST (IGST)** – decides IGST vs intra-state treatment based on states (`inter_state_gst`).
- **Hotel/Flight GST for Personal Bookings** – GST capture on personal bookings (`enable_hotel_gst`, `enable_flight_gst`).
- **GSTIN Default / R4 GST** – defaulting GST capture for whitelisted clients (Tech Team).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `show_voucher_gst_details` — prints GST entity details on the booking voucher and invoice
  - `enable_project_code_gst` — carries the GST entity linked to a booking's project code onto the documents
- Applied at voucher/invoice generation in the booking flow (sales-service).

## Sample questions this feature answers
- "Can we show GST details on the voucher and invoice for a customer?"
- "Does the invoice carry the GST number for tax filing?"
- "Can GST be linked to a project code?"
- "How do we make vouchers GST-compliant?"
- "Who do I contact to enable GST details on documents?"
- "Can different project codes have different GST entities?"
- "Is GST display on invoices configurable?"
