---
feature_name: Modification & Block Buffer Limits
feature_id: modification-block-buffer-limits
category: Travel Policies & Spend Limits
config_source: Policy Config (Corporate Entitlement Service)
configurable: true
status: live
target_release_date: 2026-06-02
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - BufferLimitsEntity
tags:
  - modification buffer
  - price buffer
  - tolerance
  - block limit
  - advance days buffer
  - re-approval
  - modification policy
  - buffer limit
  - spend limit
  - travel policy
---

# Modification & Block Buffer Limits

## Summary
Buffer Limits define how much tolerance a policy allows when a trip is modified after it was first booked or approved. Small changes — a slight price increase, a minor shift in advance-booking days — can be permitted automatically within these buffers, so the trip does not have to go through approval again for every tiny adjustment.

## What this feature does
When an employee modifies an existing trip, the system compares the change against the company's buffer limits and decides whether it is small enough to allow without re-approval:

- **Price percentage buffer** – how much the price may rise (as a percentage) and still be allowed without re-approval.
- **Advance-days buffer** – how much the advance-booking timing may move and still be within tolerance.
- **Fixed amount / percentage modification buffer** – a tolerance expressed as a fixed amount or a percentage, defined separately for domestic and international trips.
- **Block limit** – a ceiling beyond which a modification is blocked or must go back through approval.

Together these let companies permit reasonable, small changes smoothly while still catching large changes that need fresh review.

## Customer experience
- When an employee makes a small change within the allowed buffers, the modification goes through without needing a fresh approval.
- When a change exceeds the buffers (or hits the block limit), it is treated as out-of-policy and routed for re-approval or blocked.
- This keeps everyday minor changes friction-free while preserving control over significant ones.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Policy Config** (Corporate Entitlement Service) |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company policy, and can vary by employee group via policy rules |

## Which team to connect with
**👉 Onboarding Team**

Because buffer limits are part of the company's travel **Policy Config**, a salesperson who wants to set or change the modification tolerances or block limit for a customer should reach out to the **Onboarding Team**.

> Use the Tech Team only for whitelisting-based features. Buffer limits are **not** a whitelisting feature, so they stay with Onboarding.

## Related / dependent settings
These work alongside the buffer limits and may also need to be set:

- **Trip Approval Workflow** – where a modification that exceeds the buffers gets routed for re-approval.
- **Hotel / Flight / Bus Budgets** – the base budgets the buffers are measured against.
- **Out-of-Policy (OOP) Approval Routing** – the path a blocked or over-buffer modification follows.

## Technical reference (for Onboarding/Tech)
- **Config source:** Policy Config — Corporate Entitlement Service
- **Key fields:**
  - `BufferLimitsEntity` — holds the modification tolerances, including:
    - price percentage buffer
    - advance-days buffer
    - fixed amount / percentage modification buffer (domestic and international)
    - block limit
- Snapshotted onto the trip's policy configuration in trip-management-service at trip creation.

## Sample questions this feature answers
- "Can a trip be modified slightly without going through approval again?"
- "How much can the price increase before re-approval is needed?"
- "What is the block limit on modifications?"
- "Can the modification buffer differ for domestic and international trips?"
- "What happens if a change exceeds the allowed buffer?"
- "Who do I contact to change the modification tolerances?"
- "Are the buffer limits configurable per company?"
