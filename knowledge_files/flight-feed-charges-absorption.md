---
feature_name: Flight Feed Charges Absorption
feature_id: flight-feed-charges-absorption
category: Invoicing, GST & Fees
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-06-07
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - sales-service
technical_keys:
  - enable_flight_feed_charges_absorption
tags:
  - flight charges
  - airline charges
  - feed charges
  - charge absorption
  - company absorbs
  - flight fees
  - airline fees
  - invoice charges
  - flight booking
  - fee absorption
---

# Flight Feed Charges Absorption

## Summary
This feature lets the company absorb flight feed (airline) charges rather than passing them on to the traveller or putting them on the invoice. When enabled, charges that would normally appear on the booking are borne by the company, so the traveller does not see or pay them.

## What this feature does
On flight bookings, there can be feed/airline charges. This setting decides who bears them:

- **Absorption enabled** – the **company absorbs** the flight feed/airline charges; they are not passed to the traveller or shown on the invoice.
- **Absorption disabled** – the charges are passed through to the traveller/invoice as normal.

This lets companies that want to shield travellers from certain charges take those costs on themselves.

## Customer experience
- When absorption is on, the traveller does not see the flight feed/airline charges on their booking or invoice — the company covers them.
- When absorption is off, those charges appear and are passed through as usual.
- The corporate controls its own cost exposure on flight bookings.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

Because charge absorption is part of the company's **Corporate Config**, a salesperson who wants to enable or explain it for a customer should reach out to the **Onboarding Team**. They turn flight feed charges absorption on for the company.

> Use the Tech Team only for whitelisting-based features. Flight feed charges absorption is a Corporate Config setting, so it stays with Onboarding.

## Related / dependent settings
These work alongside flight feed charges absorption and may also need to be set:

- **Convenience & Management Fees** – other fees that can apply to bookings (`management_fee`, `domestic_conv_fee_applicability`, `international_conv_fee_applicability`).
- **Voucher & Invoice GST Details** – how charges and GST appear on documents (`show_voucher_gst_details`).
- **Hotel/Flight GST for Personal Bookings** – GST handling on flight bookings (`enable_flight_gst`).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `enable_flight_feed_charges_absorption` — the company absorbs flight feed/airline charges instead of passing them to the traveller/invoice
- Applied during pricing/invoicing of flight bookings (sales-service).

## Sample questions this feature answers
- "Can the company absorb airline charges instead of passing them to travellers?"
- "What is flight feed charges absorption?"
- "Why don't I see airline charges on this invoice?"
- "Can we hide flight feed charges from the traveller?"
- "How do we make the company bear flight charges?"
- "Who do I contact to enable charge absorption?"
- "Is flight feed charges absorption configurable?"
