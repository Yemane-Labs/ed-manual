# Attendee Confirmation Email

**When it sends:** Every time someone RSVPs to a conversation. Also when you (as host) create a new conversation, you get one of these as confirmation.

**Who gets it:** The guest (or host, on creation).

**How often:** Fires once per RSVP — so volume scales with how active conversations are. Currently the most frequent guest-facing email.

---

## How the email is built

Every email on the platform is made of **two kinds of content**:

1. **Template chrome** — header, footer, logo, copyright, social links. Same across all emails.
2. **Dynamic content** — the parts that change per conversation (title, date, host name, etc.).

For this email, most of the body is dynamic — pulled live from the conversation and topic you set up in the admin.

---

## What you'll see in the email, and where it comes from

### 🟡 Header

| What the recipient sees | Where it comes from |
|---|---|
| Equitable Dinners logo | Global brand setting (applies to all emails). Ashley can upload via **Mailchimp → Content Studio**. |

### 📋 Subject line

| What the recipient sees | Where it comes from |
|---|---|
| "Get ready for your conversation, in partnership with \[Partner Name\]!" | Fixed wording — the partner name is dynamic. If you want to change the phrase itself, send the devs a request. |

### 🎯 Opening paragraph

| What the recipient sees | Where to edit |
|---|---|
| "Everything you need to know to join your **dinner** on **\[Topic title\]**, in partnership with **\[Partner Name\]**." | Topic title: **Admin → Topics → Edit → Title**<br>Partner name: **Admin → Customers → Edit** |

### 📅 Conversation details block

| What the recipient sees | Where to edit |
|---|---|
| Date (e.g., "Saturday, April 26, 2026") | **Admin → Conversations → Edit → Starts at** |
| Time range (e.g., "7:00 PM – 9:00 PM EST") | Same as above (derived from Starts at + Ends at) |
| **Location (in-person):** street address | **Admin → Conversations → Edit → Address** (Google autocomplete) |
| **Location (virtual):** "Online / Join Link" | Change by setting venue type to Virtual; join link auto-generated |
| **How to Join / Extra info** | **Admin → Conversations → Edit → Guest instructions** |

### 📅 "Add to Calendar" links

| What the recipient sees | Where to edit |
|---|---|
| Apple / Google / Outlook / Outlook.com / Yahoo! links | Auto-generated from the conversation date + title. **You can't edit these** — they appear on every attendee confirmation. |

### 🔘 Yellow "View Conversation Details" button

| What the recipient sees | Where to edit |
|---|---|
| Yellow button saying "View Conversation Details" that links to the conversation page | The URL is always the conversation's public URL (auto). The button label is fixed — send the devs a request if you want it changed. |

### 👥 Host information

| What the recipient sees | Where to edit |
|---|---|
| "Your host is \[Host Name\]." | Host's own user profile — they edit it themselves. **Admin → Guests/Hosts → Edit** if you need to fix it for them. |
| "You can reach \[first name\] at \[phone\] or \[email\]." | Same — host's profile |

### ✏️ Optional custom content

| What the recipient sees | Where to edit |
|---|---|
| Any custom text you want to add (e.g., "Please review this video before the conversation") | ⭐ **Admin → Topics → Edit → Email tab → Pre-event guest content** — this is your most powerful control. Rich text editor, HTML allowed. |

### 👋 Sign-off

| What the recipient sees | Where to edit |
|---|---|
| "With gratitude, The Equitable Dinners Team" | Platform-level default. Send the devs a request to change. |

### ⬇️ Footer

| What the recipient sees | Where to edit |
|---|---|
| Social icons, copyright line, OOH mailing address, unsubscribe link | **Mailchimp → Email Templates → Saved → ED — Attendee Confirmation → Edit template.** Visual editor. |

---

## ⭐ Quick reference: "I want to change X"

| Want to change | Edit here |
|---|---|
| The topic title shown in the email | Admin → Topics → Edit → Title |
| The date/time of the conversation | Admin → Conversations → Edit → Starts at |
| The physical location (in-person event) | Admin → Conversations → Edit → Address |
| The Zoom link | Not directly — change venue type to Virtual, platform generates it |
| Extra join instructions | Admin → Conversations → Edit → Guest instructions |
| **Custom pre-event content (e.g., "watch this video")** | ⭐ Admin → Topics → Edit → Email tab → Pre-event guest content |
| Host's contact info in email | Host's own profile (or Admin → Guests/Hosts → Edit) |
| Footer copyright / address / social links | Mailchimp visual editor on ED — Attendee Confirmation |
| The subject line wording | Request from the devs (small change, quick turnaround) |
| The yellow button label | Request from the devs |
| The "With gratitude / The Equitable Dinners Team" sign-off | Request from the devs (affects all emails) |

---

## What's fixed (not editable without the devs' help)

These are designed into the platform and require a code change:

- The phrasing of "Everything you need to know to join your..."
- The phrasing of "Your host is..."
- The "If your plans change" cancellation paragraph
- The "Thank you for taking part..." closing line
- The "With gratitude" valediction and "The Equitable Dinners Team" sign-off
- The yellow button label ("View Conversation Details")
- The subject line template

If you want any of these phrased differently, send a short list to the devs — they'll batch them into a single update.
