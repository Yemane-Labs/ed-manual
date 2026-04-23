# Conversation Notification Emails (Pre- and Post-Event Reminders)

**When it sends:** At several points in a conversation's lifecycle — 36 hours before, 7 days before, after the event, follow-ups days/weeks later.
**Who gets it:** Guests and hosts (separate versions for each).
**How often:** Multiple times per conversation — up to 7 events per guest/host. The workhorse of the platform.

---

## 📌 This is the most editable template for you

Unlike every other email, the **body of these emails is stored per-topic in the admin**. That means you can have totally different content for "Thriving Together Atlanta" reminders vs "Belonging" reminders, per event type.

**One template, many messages, all editable by you.**

---

## The 7+ emails sharing this template

| Email | When it sends | To |
|---|---|---|
| Pre-Conversation 1 — Guest | 36 hours before the event | All registered guests |
| Pre-Conversation 1 — Host | 36 hours before the event | The host |
| Pre-Conversation 2 — Host | 7 days before the event | The host (extra lead-time reminder) |
| Post-Conversation 1 — Guest | Shortly after the event (18 hours / 3 days / 1 week — you configure) | All guests who attended |
| Post-Conversation 1 — Host | Same timing, but for host | The host |
| Post-Conversation 2 — Guest | A second follow-up days/weeks later | Guests |
| Post-Conversation 2 — Host | Same, but for host | The host |
| Pre-Premium Event | Before a paid event | Guests who purchased |

Each one is a separate row in the Topic's admin — and each has **its own content and subject you control**.

---

## How the rendering works (plain English)

1. Someone registers for a conversation on Topic "X"
2. 36 hours before the event, the platform looks up Topic X's admin settings
3. It finds the "Pre-Conversation 1 Guest" row and reads the content you wrote there
4. It drops that content into the ED-branded email shell and sends

Key insight: **edit once per topic**, the same content goes to everyone who registers for that topic.

---

## Where to edit everything

### ⭐ The body content (per-topic, per-event)

**Admin → Topics → Edit \[your topic\] → Email tab**

You'll see a list of all the events (Pre 1 Guest, Pre 1 Host, Post 1 Guest, etc.). Click any row to edit:

- **Content** — the full HTML body of the email. Rich text editor. Supports images, links, formatting.
- **Subject** — subject line specific to this event
- **Send date** (post-event only) — pick from: 18 hours, 3 days, 1 week, 2 weeks, 3 weeks, 1 month, 2 months after event

### 🎨 The wrapping chrome (header, footer, logo)

**Mailchimp → Saved → ED — Convo Notifications → Edit template**

Shared across all 7 events. Edit once, applies everywhere.

### 👋 Sign-off

Platform-level default. Send the devs a request.

---

## ⭐ Quick reference: "I want to change X"

| Want to change | Edit here |
|---|---|
| The 36-hour reminder for guests attending "Thriving Together" | Admin → Topics → Thriving Together → Edit → Email tab → **Pre-Conversation 1 Guest** → edit Content |
| The 36-hour reminder for hosts | Same path → **Pre-Conversation 1 Host** → edit Content |
| Post-event thank-you email timing (send 3 days after instead of 1 week) | Same path → **Post-Conversation 1** → change Send date |
| Add an image to a reminder email | Paste the image URL into the Content field as `<img src="...">` or upload via Mailchimp Content Studio first |
| Copy/style of the header/footer/logo | Mailchimp visual editor on ED — Convo Notifications |
| Subject line for a specific event | Admin → Topics → Edit → Email tab → \[event\] → Subject |
| "With gratitude / The Equitable Dinners Team" sign-off | Request from the devs (platform-wide change) |

---

## Common patterns

### "I want every topic to have the same pre-event reminder copy"

Then you have to copy-paste that content into each topic's Pre-Conversation 1 row. There's no global default. Consider this when writing: copy you'll want to re-use across 5+ topics should be short and generic.

### "I want one topic to have special copy"

That's exactly what this system was built for. Edit just that topic's row. Others stay untouched.

### "I want to add a new event — e.g., email 2 weeks before"

Can't add new events in the Topic admin without code changes (the events are predefined). But you can extend existing events — use the "Post-Conversation 2" with a longer Send Date for a late follow-up.

---

## Tips

- **Start with one topic to test** — edit Thriving Together's Pre-Convo 1 Guest content, send yourself a test (sign up as a dummy user), see how it lands. Then replicate to other topics.
- **HTML is allowed in Content field** — use for styling, images, links. Keep inline styles only; no `<script>`.
- **Don't write `{{user_first_name}}` or other placeholders inside the Content field** — those won't be replaced. Use the email's greeting (handled by the wrapper chrome) for personalization.
- **New topics get default templates** — when you create a new Topic, the system seeds standard copy you can override.
