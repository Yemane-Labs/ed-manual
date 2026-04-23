# Equitable Dinners Platform — Email Manual

**For:** Ashley + anyone at OOH managing email content
**Maintained by:** Aki & Dino (the devs)
**Last updated:** 2026-04-22

---

## What this is

A practical guide to every email the platform sends automatically — when it goes out, who gets it, and exactly where you can edit it. No code knowledge required.

If you've ever wondered:
- "Where does the date in this reminder email come from?"
- "Can I change this copy myself, or do I need the devs?"
- "Why does this email still say 'Inclusivv' somewhere?"

This manual answers those.

---

## The 5 email templates that matter

These are where 95%+ of the platform's email volume goes. Start here.

| # | Template | When it sends | Relative volume |
|---:|---|---|---|
| 1 | [Attendee Confirmation](./01-attendee-confirmation.md) | Every RSVP | **High** — one per signup per conversation |
| 2 | [Welcome New Account](./02-welcome-new-account.md) | Every new signup | **High** — one per new user |
| 3 | [Conversation Notifications](./03-convo-notifications.md) | Pre-event and post-event reminders | **High** — up to 7 per guest per conversation (reminders, follow-ups) |
| 4 | [NPS / Feedback Survey](./04-nps-feedback.md) | After each conversation | **Medium** — one per guest + one per host per conversation |
| 5 | [Default (catch-all)](./05-default-catchall.md) | 20+ other low-volume emails | **Varies** — rarely sent individually but collectively significant |

*Actual send volume varies — the platform's pace depends on how many conversations you're running. As of April 2026 the platform sends roughly 100-200 emails per month across all templates.*

---

## The two things you'll edit most

### 1. Topic-specific email content (most powerful)

**Admin → Topics → Edit your topic → Email tab**

You'll find rows for each event (Pre-Conversation 1 Guest, Post-Conversation 1 Host, etc.) with editable Content + Subject fields. Different topics can have totally different email copy. This is where the bulk of your day-to-day email editing lives.

### 2. Mailchimp visual templates (for chrome/design)

**Mailchimp → Email Templates → Saved → ED — \[template name\] → Edit template**

Drag-and-drop visual editor. Use for: logo, footer, social links, copyright, overall design. Changes here apply to the chrome of all emails using that template.

---

## Two things you can't edit directly (request from the devs)

Platform-wide copy lives in code and requires the devs to change. Examples:

- Email subject lines that are hardcoded (e.g., "Thanks for joining Inclusivv")
- Sign-off wording ("With gratitude, The Equitable Dinners Team")
- Fixed phrasing inside an email (e.g., "If your plans change, click here...")
- The rating scale question on NPS emails

**How to request a change:** create a task in Asana (Inclusivv Platform Transition & Maintenance project) and assign it to the devs, with the email name + the exact copy you want. They'll batch these and ship them in one update.

---

## Good habits

- ✅ **Always test by sending yourself** — sign up with a dummy email, attend/register for a test conversation, see what lands
- ✅ **Edit one topic first** — change copy for one topic, send a test, then roll to others
- ✅ **Keep personalization merge tags alone** — `{{user_first_name}}`, `{{currentYear}}`, anything in curly braces or `*|VARS|*` are placeholders the system fills in at send time. Don't edit inside them.
- ❌ **Don't remove the NPS rating widget blocks** — the 1-10 rating is core to that email
- ❌ **Don't paste HTML you're unsure about** into Mailchimp visual editor — test first
- ❌ **Don't edit the live "inclusivv-*" templates in Mandrill** — always edit the "ED — \*" versions via Mailchimp, then "Send to Mandrill"

---

## Need help?

Create a task in Asana (Inclusivv Platform Transition & Maintenance project) and assign it to the devs. If a doc is unclear or out of date, let them know what confused you so it can be fixed.
