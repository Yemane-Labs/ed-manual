# The "Default" Email Template (Catch-All)

**When it sends:** Used as the wrapper for ~20 different low-volume transactional emails — RSVP cancellations, invite-related notifications, message notifications, CSV export confirmations, etc.
**Who gets it:** Varies per email type.
**How often:** Individually rare, but collectively the highest-volume template because many email types share it.

---

## What this template does

Think of this as the **shared email frame** for all the less-common platform emails. Rather than designing a unique template for each (e.g., "your RSVP was cancelled"), they all use this common shell so they look consistent with the ED brand.

**The body copy for each of those 20+ emails is stored in the platform code, not in admin or Mailchimp.** That means body changes to specific emails need the devs.

**But the chrome (header, footer, logo) is fully yours** to edit in Mailchimp — and editing here updates the chrome for all 20+ emails at once.

---

## The 20+ emails using this template

Roughly grouped:

**RSVP / attendance:**
- RSVP Confirmation (non-US community variant)
- New RSVP received (host notification)
- Guest cancelled RSVP (self-confirmation + host notification)

**Conversation lifecycle:**
- Conversation details changed (guest notification)
- Conversation cancelled (guest notification + host notification)
- New conversation created (host confirmation)

**Invitations:**
- Invitation to a specific conversation
- Invitation request accepted / denied
- Invitation receipts

**Messaging:**
- Message received from host
- Message received from guest

**Admin:**
- CSV export ready for download
- Partner admin invitation

**Platform:**
- User connection accepted

---

## What you can edit — and where

### 🎨 Chrome (updates all 20+ emails at once)

**Mailchimp → Saved → ED — Default → Edit template**

- Header logo
- Footer: social icons, copyright line, mailing address, unsubscribe

**⚠️ A change here touches every one of those 20+ emails.** If you accidentally break the chrome, many emails send broken. Test by sending yourself a preview before publishing.

### ✏️ Individual email bodies

Body copy for each of the 20+ emails lives in the platform code. To change them, send the devs a request with:
- **Which email** ("the one that goes out when a guest cancels their RSVP")
- **What you want it to say**

the devs will batch these into a single update.

---

## ⭐ Quick reference: "I want to change X"

| Want to change | Edit here |
|---|---|
| Logo, footer, copyright, social links — on all 20+ emails | **Mailchimp → Saved → ED — Default → Edit template** |
| The specific wording of a cancellation or invite email | Request from the devs — describe which email + desired copy |
| Subject line of a specific email | Request from the devs |

---

## Tips

- **Most of these emails are infrequent** — someone getting a "Conversation Cancelled" email isn't pleasant news anyway. Don't over-invest in perfecting rarely-sent emails.
- **If you find "Inclusivv" in a transactional email after launch**, it's likely in one of these 20+ email bodies. Flag it to the devs with: "I got email X and it still says Inclusivv."
- **The chrome is shared** — so rebranding the ED — Default template once rebrands all 20+ emails. High leverage.
