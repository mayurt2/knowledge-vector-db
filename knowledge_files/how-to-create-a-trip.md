---
feature_name: How to Create a Trip
feature_id: how-to-create-a-trip
category: How-To / Usage Guides
config_source: Not applicable (standard platform capability)
configurable: false
status: live
target_release_date: 2026-03-20
status_last_updated: 2026-06-26
contact_team: Onboarding Team / Support
related_services:
  - trip-management-service
  - b2b-aggregation
  - sales-service
  - corporate-entitlement-service
technical_keys:
  - TripService.createTripService
  - SBTService.createTripService (Self Booking Tool flow)
  - TripRequest / SelfBookingTripRequest
  - PrivateTripController / PrivateSBTController
platforms:
  - Mobile App
  - Web App
tags:
  - create trip
  - how to create trip
  - new trip
  - book a trip
  - raise a trip
  - trip creation
  - mobile app
  - web app
  - self booking
  - start a trip
  - add traveller
  - booking flow
  - usage guide
---

# How to Create a Trip

## Summary
Creating a trip is the starting point for booking travel on the platform. A user picks who is travelling and where, adds the travel they need (hotel, flight, cab, bus, train), and submits the trip — which then goes through the company's policy and approval rules before bookings are confirmed. **Trips can be created on both the Mobile App and the Web App**, so users can raise a trip from their phone on the go or from a desktop browser.

> 📱💻 **Available on both platforms:** Users can create a trip from the **Mobile App** and the **Web App**. The steps and information captured are the same on both; only the screen layout differs.

## What this covers
This guide explains the typical flow a user follows to create a trip. The exact screens depend on whether the user is self-booking or a travel desk/admin is booking on their behalf, but the core steps are the same.

### Step-by-step: creating a trip
1. **Start a new trip** – From the home screen (Mobile App or Web App), choose **Create Trip / New Trip**.
2. **Add traveller(s)** – Select who the trip is for: yourself, a colleague, or a guest (if guest bookings are enabled for the company). Multiple travellers can be added where allowed.
3. **Enter trip details** – Add the destination and travel dates. Some companies allow a flexible **date range** instead of fixed dates.
4. **Add travel services** – Add what's needed for the trip: **hotel, flight, cab, bus, or train**. Each service is searched and shortlisted within the company's travel policy.
5. **Capture required information** – Depending on company setup, the user may be asked for **cost centre, project code, or custom fields** (e.g. trip purpose).
6. **Policy check** – As selections are made, the platform checks them against the company's travel policy. In-policy options proceed normally; out-of-policy choices may show an **out-of-policy (OOP) popup** asking for a justification.
7. **Submit the trip** – The user submits the trip for booking. If the company uses an approval workflow, the trip is routed to the approver(s) for sign-off.
8. **Booking confirmation** – Once any required approvals are complete, the booking is confirmed and the traveller receives the confirmation/voucher.

## User experience
- **Mobile App:** ideal for travellers booking on the go; the create-trip flow is optimised for smaller screens with the same steps.
- **Web App:** ideal for travel desks/admins and for booking detailed or multi-traveller trips on a larger screen.
- **Self Booking Tool (SBT):** if enabled, employees can create and submit their own trips directly (subject to policy and approval).
- **Travel desk / admin booking:** an admin or travel desk can create a trip on behalf of an employee or guest.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **No** — creating a trip is a standard platform capability available to users |
| Where is it configured? | Not applicable — but the *experience* depends on settings like approvals, OOP, guest policy, cost objects, and Self Booking Tool |
| Who configures the surrounding rules? | Onboarding Team (policy/approvals/cost objects), Tech Team (whitelisted experiences) |
| Available on? | **Both Mobile App and Web App** |

## Which team to connect with
**👉 Onboarding Team / Support**

Creating a trip is a core capability, so there's nothing to "switch on." If a customer wants the trip-creation experience to behave differently — for example to require approvals, capture project codes, allow guest trips, or enable the Self Booking Tool — that's controlled by the **surrounding settings**, which the **Onboarding Team** configures. For general "how do I create a trip?" help, point the user to **Support**.

> The *ability* to create a trip is always available. What changes per company is the policy, approval, and field-capture behaviour around it — those are configured by Onboarding (and Tech for whitelisted experiences).

## Related / dependent settings
These shape what the user sees while creating a trip:

- **Trip Approval Workflow** – whether the trip needs approval before booking.
- **Self Booking Tool (SBT)** – lets employees create and book their own trips.
- **Out-of-Policy (OOP) Handling** – popup/justification when a selection breaches policy.
- **Guest Policy Allowed** – whether trips can be created for guest travellers.
- **Cost Centres / Project Codes / Custom Fields** – information captured during trip creation.
- **Allow Trip Creation with Date Range** – flexible dates instead of fixed dates.
- **Duplicate Booking Detection** – warns/blocks overlapping trips at creation time.

## Technical reference (for Onboarding/Tech)
- **Owning service:** trip-management-service (with b2b-aggregation for the booking experience)
- **Create-trip entry points:**
  - Travel desk / standard flow: `TripService.createTripService` (`TripRequest`) — `PrivateTripController`
  - Self Booking Tool flow: `SBTService.createTripService` (`SelfBookingTripRequest`) — `PrivateSBTController`
  - Out-of-policy create flow: `PrivateTripOOPController` (`/popup/create/trip`)
- **At creation** the trip snapshots company configuration into `TripConfigsEntity` / `TripMetadataEntity` (approval level, sub-trip approval, OOP options, flight overlap buffer, etc.).
- **Both Mobile App and Web App** call the same backend create-trip APIs; the platform difference is UI only.

## Sample questions this feature answers
- "How do I create a trip?"
- "How does a user start a new trip?"
- "Can trips be created on mobile?"
- "Can I create a trip from the web app?"
- "Is trip creation available on both mobile and web?"
- "What are the steps to raise a trip?"
- "Can I create a trip for a colleague or guest?"
- "Can an employee create their own trip?"
- "What happens after I submit a trip?"
