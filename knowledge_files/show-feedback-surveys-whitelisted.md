---
feature_name: Show Feedback Surveys (Whitelisted)
feature_id: show-feedback-surveys-whitelisted
category: Admin & Account Settings
config_source: Whitelisting (Secret Manager Key)
configurable: true
status: live
target_release_date: 2026-05-11
status_last_updated: 2026-06-26
contact_team: Tech Team
related_services:
  - sales-service
technical_keys:
  - show.feedback.enabled.corporates
tags:
  - feedback
  - survey
  - in-app survey
  - feedback prompt
  - feedback survey
  - nps
  - customer feedback
  - survey whitelisting
  - feedback enabled
  - in-app feedback
---

# Show Feedback Surveys (Whitelisted)

## Summary
Show Feedback Surveys enables in-app feedback and survey prompts for selected corporates. When a company is whitelisted for this feature, its users see feedback or survey prompts inside the app — letting the company gather user opinions and helping the platform understand customer sentiment. This is controlled centrally for specific corporates rather than per-company self-service.

## What this feature does
This feature decides whether feedback/survey prompts appear in the app for a company's users:

- **Whitelisted** – the company's users see in-app feedback or survey prompts and can submit responses.
- **Not whitelisted** – no feedback/survey prompts are shown to that company's users.

Because it is a whitelisting feature, the company is added to a centrally managed list of corporates for whom feedback surveys are enabled.

## Customer experience
- Users in a whitelisted company see in-app prompts inviting them to give feedback or complete a survey.
- Responses help the company and the platform understand satisfaction and gather improvement ideas.
- Companies that are not whitelisted do not see these prompts at all.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Whitelisting** (Secret Manager Key) |
| Who configures it? | Tech Team |
| Is it per-company? | Yes — by adding the company to the whitelisted corporates list |

## Which team to connect with
**👉 Tech Team**

Because this feature is controlled through **whitelisting** (a Secret Manager Key), a salesperson who wants to enable feedback/survey prompts for a customer should reach out to the **Tech Team**. They add the corporate to the `show.feedback.enabled.corporates` whitelist.

> Whitelisting features like this one are managed via Secret Manager Keys, so they go to the Tech Team rather than the Onboarding Team.

## Related / dependent settings
These work alongside feedback surveys and may also need to be considered:

- **Other Whitelisting Flags** – similarly managed corporate lists controlled via Secret Manager Keys.
- **Demo / Internal / Test Account Flags** – may change how prompts and reporting behave for non-real accounts.

## Technical reference (for Onboarding/Tech)
- **Config source:** Whitelisting — Secret Manager Key
- **Key fields:**
  - `show.feedback.enabled.corporates` — list of corporate IDs for whom in-app feedback/survey prompts are enabled
- Adding a corporate to this list turns on feedback/survey prompts for that company's users.

## Sample questions this feature answers
- "Can we show feedback surveys to a customer's users?"
- "How do we enable in-app feedback prompts for a company?"
- "Why isn't a customer seeing the feedback survey?"
- "Is the feedback survey controlled by whitelisting?"
- "Who do I contact to turn on surveys for a corporate?"
- "Can we enable NPS/feedback for a specific company?"
- "How do we add a corporate to the feedback whitelist?"
