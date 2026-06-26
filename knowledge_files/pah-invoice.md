---
feature_name: Pay-At-Hotel (PAH) Invoice
feature_id: pah-invoice
category: Invoicing, GST & Fees
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-05-25
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - sales-service
technical_keys:
  - pah_invoice
tags:
  - pah
  - pay at hotel
  - pay-at-hotel
  - invoice
  - guest invoice
  - pah invoice
  - hotel invoice
  - pah flag
  - billing
  - post-paid hotel
---

# Pay-At-Hotel (PAH) Invoice

## Summary
This feature controls invoicing for Pay-At-Hotel (PAH) bookings — bookings where the guest settles the room charges directly at the hotel rather than paying upfront through the platform. When PAH invoicing is enabled, the system generates a guest invoice and shows the PAH flag on the booking, so it is clear the amount is to be collected at the hotel. When disabled, PAH invoicing is turned off.

## What this feature does
When a booking is made on a Pay-At-Hotel basis, the company's configuration decides how it is invoiced:

- **PAH enabled (PAH_TRUE)** – the system generates a **guest invoice** for the PAH booking and shows the **PAH flag**, clearly indicating that payment is collected at the hotel.
- **PAH disabled (PAH_FALSE)** – PAH invoicing is switched off; the booking is not processed under the Pay-At-Hotel invoicing path.

This lets companies that allow guests to pay at the hotel keep correct documentation while still tracking the booking on the platform.

## Customer experience
- For PAH bookings, the guest receives an invoice that reflects the Pay-At-Hotel arrangement, and the PAH flag makes the payment mode obvious.
- Corporate admins can distinguish PAH bookings from prepaid bookings in their records.
- If PAH invoicing is off, the company simply does not use the Pay-At-Hotel invoicing flow.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

Because PAH invoicing is part of the company's **Corporate Config**, a salesperson who wants to enable or explain Pay-At-Hotel invoicing for a customer should reach out to the **Onboarding Team**. They set the PAH invoice flag on or off.

> Use the Tech Team only for whitelisting-based features. PAH invoice is a Corporate Config setting, so it stays with Onboarding.

## Related / dependent settings
These work alongside PAH invoicing and may also need to be set:

- **Voucher & Invoice GST Details** – GST details printed on the guest invoice (`show_voucher_gst_details`).
- **Separate Invoice** – whether each booking/component gets its own invoice (`enable_separate_invoice`).
- **Invoice Traveler Details** – which traveller fields appear on the invoice (`invoice_traveler_details`).
- **HSN/SAC Code on Invoice** – tax code on the invoice (`enable_hsn_code`).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `pah_invoice` — `PAH_TRUE` generates a guest invoice and shows the PAH flag; `PAH_FALSE` disables PAH invoicing
- Applied at invoice generation in the booking flow (sales-service).

## Sample questions this feature answers
- "Can we generate an invoice for Pay-At-Hotel bookings?"
- "What does the PAH flag on a booking mean?"
- "Does the guest get an invoice when they pay at the hotel?"
- "How do we turn off PAH invoicing for a company?"
- "What is a PAH invoice?"
- "Who do I contact to enable Pay-At-Hotel invoicing?"
- "Is PAH invoicing configurable per company?"
