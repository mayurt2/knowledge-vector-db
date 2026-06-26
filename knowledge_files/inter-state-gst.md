---
feature_name: Inter-State GST (IGST)
feature_id: inter-state-gst
category: Invoicing, GST & Fees
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-06-10
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - sales-service
technical_keys:
  - inter_state_gst
tags:
  - gst
  - igst
  - inter-state gst
  - intra-state gst
  - cgst
  - sgst
  - tax treatment
  - place of supply
  - state gst
  - invoice tax
  - gst compliance
---

# Inter-State GST (IGST)

## Summary
This feature decides how GST is applied on a booking based on where the supplier and the customer are located. When the supplier and customer are in **different states**, inter-state GST (IGST) treatment is applied. When they are in the **same state**, intra-state treatment (CGST + SGST) applies. This keeps invoices GST-compliant according to the place-of-supply rules.

## What this feature does
At invoice time, the system compares the state of the supplier with the state of the customer:

- **Inter-state (different states)** – IGST is applied as a single combined tax component.
- **Intra-state (same state)** – the tax is split into CGST and SGST components.

This ensures the correct GST type and split is shown on the invoice, matching Indian GST regulations, so corporates can claim input credit correctly.

## Customer experience
- The corporate receives invoices with the correct GST treatment for each booking, without manual intervention.
- Finance teams see IGST or CGST+SGST depending on the booking's place of supply, which keeps tax records and credit claims accurate.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

Because inter-state GST treatment is part of the company's **Corporate Config**, a salesperson who wants to enable or explain IGST handling for a customer should reach out to the **Onboarding Team**. They configure the inter-state GST behaviour.

> Use the Tech Team only for whitelisting-based features. Inter-state GST is a Corporate Config setting, so it stays with Onboarding.

## Related / dependent settings
These work alongside inter-state GST and may also need to be set:

- **Voucher & Invoice GST Details** – GST details printed on documents (`show_voucher_gst_details`).
- **HSN/SAC Code on Invoice** – tax code on invoices (`enable_hsn_code`).
- **Hotel/Flight GST for Personal Bookings** – GST capture on personal bookings (`enable_hotel_gst`, `enable_flight_gst`).
- **GSTIN Default / R4 GST** – defaulting GST capture for whitelisted clients (Tech Team).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `inter_state_gst` — applies IGST when supplier and customer states differ; otherwise intra-state (CGST + SGST) treatment
- Applied at invoice generation based on supplier vs customer state (sales-service).

## Sample questions this feature answers
- "How is GST applied when the hotel and the company are in different states?"
- "What's the difference between IGST and CGST/SGST on our invoices?"
- "Can we enable inter-state GST treatment for a customer?"
- "Why does my invoice show IGST instead of CGST and SGST?"
- "How does place of supply affect the GST on invoices?"
- "Who do I contact to set up inter-state GST?"
- "Is inter-state GST configurable?"
