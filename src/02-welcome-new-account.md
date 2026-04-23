# Welcome Email (New Account)

**When it sends:** Anytime someone creates a new account on the platform.
**Who gets it:** The new user.
**How often:** Once per new signup — first impression of the platform.

---

## How the email is built

Unlike the Attendee Confirmation email, the welcome email's **entire body lives in Mailchimp**. That means **you can rewrite the whole thing in the visual editor** without needing the devs.

Only two things are pulled live from the user's account:
- Their first name (for the greeting)
- Their email address (occasionally used in the body)

Everything else — headline, paragraphs, CTAs, images — is yours to edit.

---

## What you'll see in the email, and where it comes from

### 🟡 Header

| What the recipient sees | Where it comes from |
|---|---|
| Equitable Dinners logo | Global brand setting |

### 📋 Subject line

| What the recipient sees | Where to edit |
|---|---|
| "Thanks for joining Inclusivv" (currently) | ⚠️ Needs a rewrite to "Thanks for joining Equitable Dinners" — send the devs a request |

### ✏️ Body (this is mostly yours to control)

| What the recipient sees | Where to edit |
|---|---|
| Greeting (e.g., "Hi \[First Name\]!") | Use `{{user_first_name}}` placeholder in Mailchimp visual editor wherever you want the name to appear |
| Welcome message paragraph(s) | Fully editable in **Mailchimp → Saved → ED — Welcome New Account** |
| Reference to user's email | Use `{{user_email}}` placeholder if you want to show it anywhere |
| Images, CTAs, buttons, onboarding checklists | Fully editable in Mailchimp visual builder — add/remove/rearrange blocks |

### 👋 Sign-off & Footer

| What the recipient sees | Where to edit |
|---|---|
| "With gratitude, The Equitable Dinners Team" | Platform-level — send the devs a request to change |
| Social icons, copyright, address, unsubscribe | Mailchimp visual editor |

---

## ⭐ Quick reference: "I want to change X"

| Want to change | Edit here |
|---|---|
| The welcome message copy (any of it) | **Mailchimp → Saved → ED — Welcome New Account → Edit template.** The full body is yours. |
| Subject line (currently mentions Inclusivv) | Request from the devs |
| Add onboarding checklist, links, CTAs | Mailchimp visual editor — drop in new blocks |
| Change the image or images | Mailchimp visual editor |
| Where the user's name appears | Move the `{{user_first_name}}` placeholder around |

---

## Tips for editing this one

- **Use `{{user_first_name}}` in the greeting** so each recipient sees their own name.
- **Keep it short** — this is the first email. Welcome, point them to 1-2 actions, done.
- **Test with yourself** — sign up with a test email and see what lands.
- **Don't reuse Inclusivv-era copy** — this email is a blank canvas. Let it sound like ED from the first word.
