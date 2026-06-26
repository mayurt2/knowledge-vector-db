---
feature_name: Trip PDF Export
feature_id: trip-pdf-export
category: Expense Management
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-05-04
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - trip-management-service
  - sales-service
technical_keys:
  - trip_pdf_export_allowed
tags:
  - pdf export
  - trip export
  - expense export
  - download pdf
  - trip report
  - expense report
  - document export
  - export trip details
  - reporting
  - downloadable document
---

# Trip PDF Export

## Summary
Trip PDF Export lets users download trip and expense details as a PDF document. This gives travelers and companies an easy, shareable record of a trip — useful for filing, reimbursement, internal reporting, or simply keeping a copy. Turning this on enables the export option for the company's users.

## What this feature does
When enabled, users can generate a PDF of their trip/expense details:

- **Export to PDF** — trip and expense information is compiled into a downloadable PDF document.
- **Shareable record** — the exported file can be saved, printed, or forwarded as needed.
- **Reporting support** — provides a clean summary of a trip's details and associated spend.

This makes it easy for a company's users to produce a portable record of their travel.

## Customer experience
- Users can download a PDF summarizing their trip and expense details.
- The document is convenient for reimbursement, filing, or internal reporting.
- Having an exportable record improves transparency and record-keeping for the company.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — set per company |

## Which team to connect with
**👉 Onboarding Team**

Because this is a **Corporate Config** setting, a salesperson who wants to allow PDF export of trip/expense details for a customer should reach out to the **Onboarding Team**. They control whether the export option is available to the company's users.

> Use the Tech Team only for whitelisting-based features. This is a standard Corporate Config toggle, so it stays with Onboarding.

## Related / dependent settings
These work alongside trip PDF export and may also be relevant:

- **Local Expense** – enables travelers to log local/incidental expenses (Corporate Config).
- **Legacy Expense Module (Whitelisted)** – keeps whitelisted companies on the legacy expense module (Whitelisting).
- **Company / Client Logo** – branding that can appear on exported documents (Corporate Config).

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `trip_pdf_export_allowed` — when true, allows users to export trip/expense details as a PDF.

## Sample questions this feature answers
- "Can users download trip details as a PDF?"
- "How do I enable PDF export of expenses for a customer?"
- "Can travelers get a printable record of their trip?"
- "Is the trip PDF export option configurable per company?"
- "Which team turns on PDF export?"
- "Can exported PDFs be used for reimbursement?"
- "What does trip_pdf_export_allowed do?"
