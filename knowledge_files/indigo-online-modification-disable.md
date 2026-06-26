---
feature_name: Indigo Online Modification Disable
feature_id: indigo-online-modification-disable
category: Bookings & Duplicate Bookings
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-05-31
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - trip-management-service
  - sales-service
technical_keys:
  - indigo.online.modification.disabled.company.ids
tags:
  - indigo
  - flight modification
  - online modification
  - offline change
  - airline
  - self-service
  - amendment
  - flight change
  - whitelist
  - disabled modification
---

# Indigo Online Modification Disable

## Summary
For specified companies, this feature turns off self-service online modification of Indigo flight bookings. When it is active, travellers and bookers cannot change those Indigo bookings themselves online — the changes must instead be handled offline through the support team.

## What this feature does
When a company's ID is on the disabled list, the platform hides or blocks the online modification option for Indigo flight bookings:

- **Company on the list** – online Indigo modification is disabled; changes go through offline/support.
- **Company not on the list** – normal online modification remains available.

This is used when a company's Indigo bookings need to be amended through a controlled, support-assisted process rather than self-service.

## Customer experience
- Travellers and bookers at affected companies don't see the self-service modify option for Indigo flights.
- They are directed to handle the change offline via support.
- All other airlines and companies retain their usual online modification flow.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Whitelisting** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — companies are listed by ID in the key |

## Which team to connect with
**👉 Tech Team**

Because this is driven by a **whitelisting key in Secret Manager** (a list of company IDs), the **Tech Team** owns it. A salesperson who needs a company added to or removed from the Indigo online-modification disable list should reach out to the Tech Team.

> This is a whitelisting feature, so it does **not** go through Onboarding's Policy or Corporate Config. Whitelist changes are handled by Tech.

## Related / dependent settings
These relate to Indigo modification handling:

- **Disabled Company IDs Key** – the Secret Manager list of company IDs for which Indigo online modification is off (`indigo.online.modification.disabled.company.ids`).
- **Offline/Support Modification Flow** – the support-assisted path travellers use instead.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `indigo.online.modification.disabled.company.ids` — comma-separated list of company IDs for which self-service Indigo online modification is disabled
- Checked when a modification request for an Indigo flight is initiated.

## Sample questions this feature answers
- "Can we stop a company from modifying Indigo flights online?"
- "Why can't this customer change their Indigo booking themselves?"
- "How do we force Indigo changes through support?"
- "Is disabling Indigo online modification a whitelisting feature?"
- "How do I add a company to the Indigo modification disable list?"
- "Who do I contact to turn off self-service Indigo changes?"
- "Does this affect other airlines too?"
