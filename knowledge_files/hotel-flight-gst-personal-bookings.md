---
feature_name: Hotel & Flight GST for Personal Bookings
feature_id: hotel-flight-gst-personal-bookings
category: Invoicing, GST & Fees
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-04-24
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - sales-service
technical_keys:
  - enable_hotel_gst
  - enable_flight_gst
tags:
  - gst
  - personal booking
  - hotel gst
  - flight gst
  - personal travel
  - gst capture
  - leisure booking
  - self booking
  - gst on personal
  - tax on personal bookings
---

# Hotel & Flight GST for Personal Bookings

## Summary
This feature captures and applies GST for hotel or flight bookings made under the personal-booking configuration — bookings an employee makes for personal/leisure travel through the platform. When enabled, GST is handled for these personal hotel and/or flight bookings, so the right tax treatment and documentation are produced.

## What this feature does
Under the personal-booking setup, this configuration decides whether GST is captured/applied for personal hotel and flight bookings:

- **Hotel GST enabled** – GST is captured/applied for personal **hotel** bookings.
- **Flight GST enabled** – GST is captured/applied for personal **flight** bookings.

This lets companies that allow personal bookings keep GST handling correct for those bookings, separately for hotels and flights.

## Customer experience
- An employee making a personal hotel or flight booking gets GST handled correctly on that booking.
- The tax treatment and documentation reflect the personal-booking GST configuration, keeping records accurate.
- Hotels and flights can be controlled independently, so a company can apply GST to one and not the other.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company, separately for hotels and flights |

## Which team to connect with
**👉 Onboarding Team**

Because GST for personal bookings is part of the company's **Corporate Config**, a salesperson who wants to enable or explain it for a customer should reach out to the **Onboarding Team**. They turn on hotel and/or flight GST under the personal-booking configuration.

> Use the Tech Team only for whitelisting-based features. Personal-booking GST is a Corporate Config setting, so it stays with Onboarding.

## Related / dependent settings
These work alongside personal-booking GST and may also need to be set:

- **Voucher & Invoice GST Details** – GST details printed on documents (`show_voucher_gst_details`).
- **Inter-State GST (IGST)** – IGST vs intra-state treatment (`inter_state_gst`).
- **GSTIN Default / R4 GST** – defaulting GST capture for whitelisted clients (Tech Team).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `enable_hotel_gst` — captures/applies GST for personal hotel bookings
  - `enable_flight_gst` — captures/applies GST for personal flight bookings
- Applied within the personal-booking flow (sales-service).

## Sample questions this feature answers
- "Can we capture GST on personal hotel bookings?"
- "Does GST apply to personal flight bookings?"
- "How is GST handled for personal/leisure travel?"
- "Can we enable hotel GST but not flight GST for a company?"
- "What is personal-booking GST?"
- "Who do I contact to enable GST on personal bookings?"
- "Is GST for personal bookings configurable?"
