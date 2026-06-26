---
feature_name: Super-Admin Assignment
feature_id: super-admin-assignment
category: Admin & Account Settings
config_source: Corporate Config
configurable: true
status: live
target_release_date: 2026-05-10
status_last_updated: 2026-06-26
contact_team: Onboarding Team
related_services:
  - corporate-entitlement-service
  - user-service
  - sales-service
technical_keys:
  - employee_type
  - ADMIN
  - SUPER_ADMIN
tags:
  - admin
  - super admin
  - admin role
  - account admin
  - admin assignment
  - company admin
  - admin access
  - roles and permissions
  - user roles
  - admin rights
  - super-admin
  - account owner
---

# Super-Admin Assignment

## Summary
Super-Admin Assignment controls which corporate users hold elevated Admin or Super-Admin roles on the platform. These roles decide who is allowed to manage the company's settings, employees, and travel policies. By designating the right people, a company makes sure that only trusted users can change how the account behaves.

## What this feature does
Every user on a company's account is given an employee type. Most are regular employees, but a select few can be marked as Admins or Super-Admins:

- **Admin** – can manage day-to-day account operations such as adding/removing employees, viewing reports, and handling routine settings for the company.
- **Super-Admin** – the highest level of access, with full control over the company's configuration, users, and policies, including the ability to manage other admins.

When a user is assigned one of these roles, the platform unlocks the relevant admin tools and controls for them. Anyone without an admin role sees only the standard employee experience.

## Customer experience
- Designated Admins and Super-Admins see additional management options in their account (such as user management, settings, and reporting).
- Regular employees do not see these controls and cannot change company-level settings.
- The company always knows who its admins are, so accountability for account changes is clear.

## Configurability
| Question | Answer |
|---|---|
| Can this be configured? | **Yes** |
| Where is it configured? | **Corporate Config** |
| Who configures it? | Onboarding Team |
| Is it per-company? | Yes — admin/super-admin roles are assigned per company, to specific users |

## Which team to connect with
**👉 Onboarding Team**

Because admin and super-admin roles are set as part of the company's **Corporate Config**, a salesperson who needs to assign, change, or explain who holds admin rights for a customer should reach out to the **Onboarding Team**. They set the `employee_type` for the relevant users.

> Use the Tech Team only for whitelisting-based features. Admin assignment is part of Corporate Config and is **not** a whitelisting feature, so it stays with Onboarding.

## Related / dependent settings
These work alongside admin assignment and may also need to be considered:

- **Roles & Permissions** – the specific capabilities each role can access.
- **Employee Management** – adding, removing, and grouping employees, which admins control.
- **Employee Export** – exporting the employee list, an admin-level capability.
- **Travel Policy Config** – policies that admins and super-admins can manage.

## Technical reference (for Onboarding/Tech)
- **Config source:** Corporate Config
- **Key fields:**
  - `employee_type` — designates a user's role on the account
    - `ADMIN` — elevated admin role for managing the company account
    - `SUPER_ADMIN` — highest level of access, full control over the company's settings, users, and policies
- Determines which management tools and controls are surfaced to the user.

## Sample questions this feature answers
- "How do we make someone an admin for a company?"
- "What's the difference between Admin and Super-Admin?"
- "Who can manage a company's settings and users?"
- "Can we assign more than one admin to an account?"
- "How do I change who the super-admin is for a customer?"
- "Is the admin role configurable per company?"
- "Who do I contact to set up admin access for a customer?"
