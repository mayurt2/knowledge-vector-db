---
feature_name: GSTIN Default & R4 GST (Whitelisted)
feature_id: gstin-default-r4-gst-whitelisted
category: Invoicing, GST & Fees
config_source: Whitelisting (Secret Manager Key) / global flag
configurable: true
status: live
target_release_date: 2026-06-23
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - sales-service
technical_keys:
  - default.gst.enable.client.id
  - enable.gst.r4.b2b
tags:
  - gst
  - gstin
  - r4 gst
  - default gst
  - whitelisting
  - secret manager
  - client id
  - b2b
  - gst capture
  - gst flag
  - global flag
---

# GSTIN Default & R4 GST (Whitelisted)

## Summary
This feature governs two GST controls that are driven by whitelisting and a global flag rather than per-company Corporate Config. GST (GSTIN) capture can be **defaulted on** for specific client IDs that are whitelisted, and a **global R4 GST flag** governs newer GST handling across the B2B booking flows. Because these are controlled by whitelisting (a Secret Manager key) and a global flag, they are owned by the Tech Team.

## What this feature does
Two related controls:

- **Default GST for whitelisted clients** – GSTIN capture can be turned on by default for specified client IDs. Only the client IDs added to the whitelist get GST capture defaulted on.
- **R4 GST global flag** – a global flag that governs the newer ("R4") GST handling across B2B booking flows. When on, the newer GST handling applies to the relevant flows.

Together, these decide where GST capture is defaulted and which GST handling logic is used in B2B.

## Customer experience
- For whitelisted clients, GST (GSTIN) capture is on by default, so those clients don't have to opt in for each booking.
- With the R4 GST flag enabled, the newer GST handling is applied consistently across B2B booking flows.
- Clients not on the whitelist follow the standard GST behaviour.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Whitelisting (Secret Manager Key)** for client IDs; **global flag** for R4 GST |
| Who configures it? | Tech Team |
| Is it per-company? | Default GST is per whitelisted client ID; R4 GST is a global flag |

## Which team to connect with
**👉 Tech Team**

Because these controls are driven by **whitelisting (a Secret Manager key)** and a **global flag** — not by Corporate Config — a salesperson who needs a client ID whitelisted for default GST, or has a question about the R4 GST flag, should reach out to the **Tech Team**. They manage the whitelist and the global flag.

> Whitelisting-based and global-flag features are owned by Tech, unlike per-company Corporate Config settings which go to Onboarding.

## Related / dependent settings
These work alongside default GST / R4 GST and may also need to be set:

- **Voucher & Invoice GST Details** – GST details printed on documents (`show_voucher_gst_details`, Corporate Config).
- **Inter-State GST (IGST)** – IGST vs intra-state treatment (`inter_state_gst`, Corporate Config).
- **Hotel/Flight GST for Personal Bookings** – GST capture on personal bookings (`enable_hotel_gst`, `enable_flight_gst`, Corporate Config).

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting via Secret Manager key + global flag
- **Key fields:**
  - `default.gst.enable.client.id` — whitelist of client IDs for which GSTIN capture is defaulted on (Secret Manager key)
  - `enable.gst.r4.b2b` — global flag governing the newer R4 GST handling across B2B booking flows
- Read at booking/invoicing time in the B2B flows (sales-service).

## Sample questions this feature answers
- "Can we default GST capture on for a specific client?"
- "How do we whitelist a client ID for GST?"
- "What is the R4 GST flag?"
- "Who controls default GST for B2B bookings?"
- "Why is GST defaulted on for one client but not another?"
- "Who do I contact to enable default GST for a client ID?"
- "Is default GST handled through Corporate Config or whitelisting?"
