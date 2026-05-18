# Phishing Email Templates: MedDefense Health Systems

**Inventory:** T-EPIC-01 (Baseline), T-MFA-02 (Baseline), T-HR-03 (Intermediate),
T-BEC-04 (Advanced)
**Ethics review completed:** 2026-05-18
**Approved by:** Dr. Patricia Morales, CISO
Do not deploy without campaign plan sign-off. See phishing_campaign_plan.md.

---

## T-EPIC-01: Epic EHR Account Management (Baseline)

**Target segment:** SEG-B (General clinical floor staff)
**Tier:** Baseline
**Mechanism:** Authority + Urgency
**Expected click rate (first exposure):** 40–58%
**Deployment:** Weekdays 07:15–08:30. Do not deploy during ICU or OR shift windows.

---

```
From:    Epic Health Systems Notifications <notifications@epic-healthsystems.net>
To:      [First Name Last Name] <[employee@meddefense.org]>
Subject: ACTION REQUIRED: Epic account security verification required —
         access suspended in 48 hours
```

---

Dear [First Name],

A failed security verification has been recorded against your Epic EHR account.

Per MedDefense IT Security Policy, accounts with failed verifications are suspended
after 48 hours to protect patient data. Your access to patient records, medication
administration logs and clinical documentation will be unavailable during suspension.

To complete verification and maintain uninterrupted access, click the secure link
below before 11:59 PM on [DATE+2]:

    [SIMULATION_LINK]

If you believe this message was sent in error, contact the IT helpdesk at ext. 4-HELP
or help@meddefense.org before the deadline to request a manual review.

Epic Health Systems | Account Security
Sent on behalf of MedDefense Health Systems Information Security

---

**Attacker notes:** A real attacker registers epic-healthsystems.net 72 hours before
launch and adds DKIM signing to pass spam filters. The credential harvest page matches
the actual Epic login interface pixel-for-pixel. The attacker embeds the target's actual
username in the URL to pre-populate the login form, removing one friction point between
click and credential submission. A pixel tracker in the email header confirms delivery
before the campaign wave is sent, so the attacker knows the email was opened.

---

## T-MFA-02: IT Helpdesk MFA Enrollment (Baseline)

**Target segment:** SEG-C (Administrative and billing staff)
**Tier:** Baseline
**Mechanism:** Familiarity + Authority
**Expected click rate (first exposure):** 32–47%
**Deployment:** Tuesday–Thursday, 09:00–11:00. Deploy during active MFA rollout window
from 6x02 IAM project to maximize familiarity effect. Do not deploy to IT staff (SEG-D).

---

```
From:    MedDefense IT Helpdesk <it-helpdesk@meddefense-support.org>
To:      [First Name Last Name] <[employee@meddefense.org]>
Subject: Action required: Complete MFA enrollment by [DATE+5] to maintain
         system access
```

---

Dear [First Name],

As part of MedDefense's ongoing security compliance program, all staff are required
to complete Multi-Factor Authentication (MFA) enrollment by [DATE+5].

This requirement applies to your account. Accounts that have not completed enrollment
by the deadline will require an in-person IT verification appointment before access
is restored, which may take up to 3 business days during peak periods.

Enrollment takes approximately four minutes. Click the link below to begin:

    [SIMULATION_LINK]

You will be prompted to download the Microsoft Authenticator app if you have not
already done so. Your existing password will not change.

If you have already completed enrollment and received this message in error, please
disregard. No action is required.

MedDefense IT Helpdesk
helpdesk@meddefense.org | ext. 4-HELP
Monday–Friday, 07:00–19:00

---

**Attacker notes:** A real attacker times this campaign to coincide with a publicized
IT rollout so the email matches what employees are already expecting. The spoofed domain
meddefense-support.org is registered to look like an internal IT vendor domain. The
attacker uses the MFA enrollment page to capture both the existing credential and the
newly registered authenticator seed, achieving full account takeover including MFA bypass.
The "four minutes" framing reduces perceived cost of compliance and increases click-through.

---

## T-HR-03: HR Open Enrollment Benefits Deadline (Intermediate)

**Target segment:** SEG-C and SEG-E (Administrative, billing and finance staff)
**Tier:** Intermediate
**Mechanism:** Urgency + Scarcity
**Expected click rate (first exposure):** 28–44%
**Deployment:** Wave 2 only. Deploy Monday 08:30 during open enrollment period or
simulate open enrollment period in campaign calendar. Cross-departmental — do not
exclude based on role beyond stated segments.

---

```
From:    MedDefense Human Resources <hr-benefits@meddefense-hr.net>
To:      [First Name Last Name] <[employee@meddefense.org]>
Subject: Final reminder: Benefits enrollment closes [DATE+3] —
         missed deadline requires 12-month wait
```

---

Dear [First Name],

This is your final reminder that the MedDefense annual benefits enrollment window
closes at 11:59 PM on [DATE+3].

Employees who do not complete enrollment by the deadline will remain on their current
plan selections with no changes permitted until the next open enrollment period
in [YEAR+1]. Changes to health, dental, vision and FSA contributions cannot be
processed after the window closes under IRS regulations.

Your current enrollment status: **Incomplete**

To review your options and confirm your selections, log in to the benefits portal:

    [SIMULATION_LINK]

If you have already submitted your enrollment and are receiving this message, your
submission may not have been recorded. Log in to confirm your selections are saved.

MedDefense Human Resources
Benefits Administration
hr-benefits@meddefense.org | ext. 4-HR

---

**Attacker notes:** A real attacker researches the organization's actual benefits
enrollment calendar (often published in employee handbooks or HR portal footers) and
times the campaign to the real deadline window. The "your submission may not have been
recorded" line targets employees who already completed enrollment, reactivating urgency
in a population that would otherwise ignore the message. The IRS regulatory reference
adds authority framing without requiring verification. The harvested portal credentials
provide access to employee PII including SSN, dependent information and banking details
for direct deposit.

---

## T-BEC-04: Executive Wire Fraud (Advanced)

**Target segment:** SEG-F and SEG-E (Executive and finance staff)
**Tier:** Advanced
**Mechanism:** Authority + Social proof
**Expected click rate (first exposure):** 35–52%
**Deployment:** Wave 3 only. Monday 08:30. Requires CISO personal sign-off before
deployment. Named personnel (CFO) must be confirmed with HR before use. Do not deploy
to more than 15 recipients in a single wave to prevent cross-comparison between recipients.

---

```
From:    Robert Nguyen <r.nguyen@meddefense-exec.org>
To:      [Finance Staff First Name] <[employee@meddefense.org]>
Subject: Urgent: Vendor payment authorization needed before close of business
```

---

[First Name],

I am in back-to-back board sessions until 5 PM and cannot take calls.

We need to process a vendor payment authorization for the Q2 infrastructure contract
before close of business today. Legal confirmed the terms this morning and the vendor
requires acknowledgment of the payment schedule before they release the deliverables.

Please review the attached authorization summary and confirm receipt so I can close
this out with the board before end of day.

    [SIMULATION_LINK]

Do not loop in procurement on this — legal is handling the vendor relationship directly
on this contract. I will brief the full team next week.

Robert Nguyen
Chief Financial Officer
MedDefense Health Systems
r.nguyen@meddefense.org | (direct line suppressed during board session)

---

**Attacker notes:** A real attacker harvests the CFO's name, title and email format
from LinkedIn and the organization's public website before launch. The spoofed domain
meddefense-exec.org is registered to visually match the legitimate domain at a glance.
The "do not loop in procurement" instruction is the critical social engineering element:
it isolates the target from the verification channel they would normally use. A real
attacker follows up with a phone call from a spoofed number 30 minutes after the email
if there is no response, adding voice authority to the written lure. The document link
delivers a credential harvest page styled as a SharePoint or DocuSign portal. Wire
instructions are embedded in the harvested document to complete the fraud chain without
further contact.
