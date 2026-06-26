---
feature_name: Payment Configuration
feature_id: payment-configuration
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-05-15
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - paymentConfigurationEnum
  - FlightEntitlementsEntity.paymentConfigurationEnum
  - HotelEntitlementsEntity.paymentConfigurationEnum
tags:
  - payment
  - payment configuration
  - pay now
  - prepaid wallet
  - BTC
  - bill to company
  - btc wallet
  - online payment
  - wallet
  - travel policy
  - billing
---

# Payment Configuration

## Summary
Payment Configuration controls how a trip is paid for. The company can decide whether the employee pays online at the time of booking (Pay Now), the trip is paid from a prepaid company wallet (Prepaid Wallet), or the cost is billed to the company on credit through a Bill-to-Company wallet (BTC Wallet). This is set per travel mode, so different modes can settle differently.

## What this feature does
When a booking is made, the system applies the payment method configured for that travel mode in the company's policy:

- **Pay Now (Online)** – the employee pays at the time of booking using an online payment method.
- **Prepaid Wallet** – the booking is settled from a wallet the company has pre-funded.
- **BTC Wallet (Bill-to-Company)** – the cost is charged to the company on credit and invoiced/settled later, so the employee pays nothing out of pocket.

Because it is set per mode, a company can, for example, use BTC for flights and hotels but a prepaid wallet for cabs. This lets companies control cash flow and decide whether employees ever pay directly.

## Customer experience
- In Pay Now mode, the employee completes an online payment when booking.
- In Prepaid Wallet or BTC Wallet mode, the employee does not pay directly — the company-funded wallet or company credit covers the cost.
- The payment method an employee sees depends on the mode being booked and their policy group.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because the payment method is part of the company's travel **Policy Config**, a salesperson who wants to set or change how a customer pays for trips should reach out to the **Onboarding Team**. They configure the payment method for each travel mode and employee group.

> Use the Tech Team only for whitelisting-based features. Payment configuration is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside payment configuration:

- **Travel Mode Eligibility** – the mode must be Allowed before a payment method applies.
- **Spend / Budget Cap** – limits the amount being paid regardless of method.
- **Booking Process Mode** – who places the booking that gets paid.
- **Trip Approval Workflow** – approvals may gate spend before payment is made.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `paymentConfigurationEnum` — `PAY_NOW` / `PREPAID_WALLET` / `BTC_WALLET`
  - Set per travel mode (e.g. `FlightEntitlementsEntity.paymentConfigurationEnum`, `HotelEntitlementsEntity.paymentConfigurationEnum`)
- Snapshotted onto the trip's policy at trip creation in trip-management-service.

## Sample questions this feature answers
- "How do I set up Bill-to-Company payment for a customer?"
- "What is the difference between prepaid wallet and BTC wallet?"
- "Can employees pay online at booking time?"
- "Can different travel modes use different payment methods?"
- "Is the payment method configurable?"
- "How do we make sure employees don't pay out of pocket?"
- "Who do I contact to change a company's payment configuration?"
