---
feature_name: Convenience & Management Fees
feature_id: convenience-management-fees
category: Invoicing, GST & Fees
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-06-12
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - sales-service
technical_keys:
  - management_fee
  - domestic_conv_fee_applicability
  - international_conv_fee_applicability
tags:
  - convenience fee
  - management fee
  - fees
  - service fee
  - transaction fee
  - domestic fee
  - international fee
  - contracted
  - non-contracted
  - fee applicability
  - booking charges
---

# Convenience & Management Fees

## Summary
This feature lets corporates be charged a **management fee** and **convenience fees** on their bookings. Convenience fees can be applied differently for domestic and international travel, with separate applicability rules that decide whether the fee applies to contracted rates, non-contracted rates, both, or none. This gives flexibility in how each company is billed for the service.

## What this feature does
The platform can add two kinds of charges to a company's bookings:

- **Management fee** – a fee charged to the corporate for managing their travel programme.
- **Convenience fees** – fees applied per booking, with **separate domestic and international applicability rules**.

For both domestic and international convenience fees, the applicability is set to one of:

- **NONE** – no convenience fee is applied.
- **CONTRACTED_ONLY** – the fee applies only to contracted (negotiated) rates.
- **NON_CONTRACTED_ONLY** – the fee applies only to non-contracted (public/market) rates.
- **BOTH** – the fee applies to both contracted and non-contracted rates.

This lets a company, for example, charge a convenience fee on non-contracted domestic bookings but waive it on contracted international bookings.

## Customer experience
- The corporate sees the management fee and any applicable convenience fees reflected on their bookings/invoices.
- Because domestic and international rules are separate, the fee a traveller or company incurs depends on the trip type and whether the rate is contracted.
- Companies can be billed in a way that matches their commercial agreement.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company, with separate domestic and international rules |

## Which team to connect with
**👉 Onboarding Team**

Because management and convenience fees are part of the company's **Corporate Config**, a salesperson who wants to set up or explain fees for a customer should reach out to the **Onboarding Team**. They configure the management fee and the domestic/international convenience fee applicability.

> Use the Tech Team only for whitelisting-based features. Convenience and management fees are Corporate Config settings, so they stay with Onboarding.

## Related / dependent settings
These work alongside convenience and management fees and may also need to be set:

- **Flight Feed/Airline Charges Absorption** – whether the company absorbs airline charges (`enable_flight_feed_charges_absorption`).
- **Voucher & Invoice GST Details** – how fees and GST appear on documents (`show_voucher_gst_details`).
- **Separate Invoice** – whether fee-bearing bookings are invoiced separately (`enable_separate_invoice`).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `management_fee` — management fee charged to the corporate
  - `domestic_conv_fee_applicability` — `NONE` / `CONTRACTED_ONLY` / `NON_CONTRACTED_ONLY` / `BOTH` for domestic convenience fee
  - `international_conv_fee_applicability` — `NONE` / `CONTRACTED_ONLY` / `NON_CONTRACTED_ONLY` / `BOTH` for international convenience fee
- Applied during pricing/invoicing of bookings (sales-service).

## Sample questions this feature answers
- "Can we charge a management fee to a corporate?"
- "How do convenience fees work for domestic vs international bookings?"
- "Can we apply a convenience fee only on non-contracted rates?"
- "What does CONTRACTED_ONLY mean for convenience fees?"
- "Can we waive convenience fees on contracted bookings?"
- "Who do I contact to set up fees for a customer?"
- "Are management and convenience fees configurable per company?"
