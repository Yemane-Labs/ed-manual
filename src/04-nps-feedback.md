# NPS / Feedback Survey Email

**When it sends:** After a conversation happens.
**Who gets it:** Guests and hosts (separate versions).
**How often:** Once per guest + once per host per conversation.

---

## What's special about this email

Most emails just show text and maybe a button. This one has a **rating widget** — a row of 1-10 buttons guests can click directly in the email. The rating lands on a follow-up page where they can add a comment.

The rating widget is built into the template — don't remove it.

---

## What you can edit

### ✏️ The intro copy (above the rating widget) — per-topic, per-event

**Admin → Topics → Edit \[your topic\] → Email tab → "during_conversation_guest" or "during_conversation_host" → Content**

Write whatever you want above the rating scale:
- "Thanks for joining! How was it?"
- "We'd love your feedback on today's conversation..."
- Or a longer prompt with specific questions

**Guest vs Host have separate rows** — edit each if you want different prompts for each audience.

### 🎯 Subject line (per-topic, per-event)

Same admin page — each event has its own Subject field.

### 🎨 Chrome (header, footer, logo, rating widget layout)

**Mailchimp → Saved → ED — NPS → Edit template**

---

## What you can't edit (without the devs' help)

- The rating scale labels ("Not at all likely" / "Extremely likely" / "Your opinion matters") — these are fixed copy
- The actual question ("How likely are you to recommend this experience?") — it's a system-wide setting; the devs can change via a rare super-admin flow
- Switching from 1-10 scale to 1-5 (or any other structure) — bigger code change

---

## ⭐ Quick reference: "I want to change X"

| Want to change | Edit here |
|---|---|
| The intro text above the rating for guests | Admin → Topics → Edit → Email tab → **during_conversation_guest** → Content |
| The intro text for hosts | Same path → **during_conversation_host** → Content |
| The rating question ("How likely are you to recommend...") | Platform-wide — request from the devs |
| The "Your opinion matters" header | Platform-wide — request from the devs |
| Subject line | Admin → Topics → Edit → Email tab → \[event\] → Subject |
| Header, footer, logo, social links | Mailchimp visual editor → ED — NPS |

---

## What happens after a guest rates

1. Guest clicks a rating button (e.g., "8")
2. Lands on a page pre-filled with their rating
3. Can add a comment
4. Submits — now visible to you in **Admin → Feedback**

So the feedback closes the loop back into the platform — you can review ratings + comments per conversation.

---

## Tips

- **Guest and Host are different people** — make sure the copy speaks to each audience correctly. A guest wants to be thanked and asked about their experience. A host might want to be asked how the discussion went, what worked, what to improve.
- **Keep intro copy short** — the whole point is to get them to click a rating. Don't bury the widget.
- **Test by sending yourself** (register as a dummy user, attend a test conversation, wait for the email).
