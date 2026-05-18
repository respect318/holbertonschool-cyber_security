# Social Engineering Threat Profile: MedDefense Health Systems

**Prepared by:** QA Test
**Date:** 2026-05-18
**Distribution:** Security Team, CISO, HR (Section 5 only)

---

## 1. Target Analysis

### Population A: Clinical Staff (Nurses, Patient Care Technicians, Clinical Assistants)
**Targeting frequency:** Highest. Clinical staff receive the greatest volume of targeted
social engineering lures in healthcare sector phishing data.
**Attacker access objective:** EHR credential capture for ePHI access or lateral movement
into clinical network segments.
**Exploitation timing:** Shift-start windows (07:00-08:30 and 19:00-20:30). Staff are
authenticating to Epic, reviewing handoff notes, and operating under shift-transition
cognitive load. Credential prompts during this window are processed with reduced scrutiny.

### Population B: Administrative and Billing Staff
**Targeting frequency:** High. Finance and billing staff are secondary targets due to
access to payment systems, insurance portals and patient financial records.
**Attacker access objective:** ACH/wire transfer fraud, BEC for financial diversion,
access to patient billing data for identity theft at scale.
**Exploitation timing:** Month-end close cycles, insurance reimbursement deadlines and
payroll processing windows. Staff are under deadline pressure and process high volumes
of external communications, reducing per-message scrutiny.

### Population C: IT and System Administrators
**Targeting frequency:** Moderate in volume, highest in impact. Privileged account
holders are targeted less frequently but with more sophisticated, tailored lures.
**Attacker access objective:** Domain admin credential capture, VPN access, ability to
disable security controls or establish persistent access across the MedDefense network.
**Exploitation timing:** Maintenance windows, patch deployment cycles and incident
response periods. During active incidents, administrators are operating under pressure
and may process credential prompts without full verification.

---

## 2. Attack Vector Inventory

### Vector 1: EHR System Impersonation (Email)
**Description:** Email lure mimicking Epic EHR system notifications, password expiry
alerts or access suspension warnings sent to clinical staff email addresses.
**Example lure:** "Your Epic account will be suspended in 24 hours due to a failed
security verification. Click here to restore access before your next shift."
**Attacker objective:** EHR credential capture for ePHI access.
**Targeted asset:** Epic EHR, downstream ePHI repositories.

### Vector 2: Business Email Compromise (BEC) — Executive Impersonation
**Description:** Attacker spoofs or compromises a senior executive email account
(CFO, CMO or CISO) and directs administrative or finance staff to perform an urgent
wire transfer or vendor payment change.
**Example lure:** Email appearing to originate from CFO: "I am in a board meeting and
cannot take calls. Please process this vendor payment update immediately. Confirm
when done."
**Attacker objective:** Financial fraud via ACH diversion or unauthorized wire transfer.
**Targeted asset:** Accounts payable systems, banking portals, finance staff credentials.

### Vector 3: Vendor and Supply Chain Impersonation (Email + Portal)
**Description:** Attacker impersonates a known medical supply vendor, software provider
or HIPAA compliance service, sending invoices, contract updates or required portal
re-authentication requests.
**Example lure:** "Your McKesson Medical Supplies account requires re-verification to
process your pending order. Log in to confirm your shipping address and payment details."
**Attacker objective:** Credential capture for vendor portal access or financial data
exfiltration.
**Targeted asset:** Procurement systems, vendor portals, payment authorization workflows.

### Vector 4: Vishing — IT Help Desk Impersonation
**Description:** Caller impersonates MedDefense IT help desk, claiming to be responding
to a reported issue or performing a mandatory security check. Caller requests credentials,
MFA codes or remote access authorization.
**Example scenario:** "Hi, this is IT support. We've detected unusual login activity on
your account and need to verify your identity. Can you confirm your username and the
code that just appeared on your phone?"
**Attacker objective:** MFA bypass, credential capture, unauthorized remote access.
**Targeted asset:** VPN credentials, Active Directory accounts, MFA tokens.

---

## 3. Lure Effectiveness Analysis

| Rank | Lure Category | Mechanism | Healthcare Factor | Click Rate Range |
|---|---|---|---|---|
| 1 | EHR system authority/urgency | Authority + Urgency | Blocking EHR access stops patient care delivery | 45–62% |
| 2 | Executive impersonation (BEC) | Authority + Scarcity | Hierarchy compliance is strong in clinical organizations | 38–51% |
| 3 | IT help desk credential verification | Authority + Familiarity | Routine IT interactions normalize credential requests | 32–47% |
| 4 | Regulatory/HIPAA compliance alerts | Fear + Authority | HIPAA violation consequences are well understood by staff | 28–41% |
| 5 | Vendor invoice and payment update | Familiarity + Urgency | High volume of legitimate vendor communications reduces suspicion | 22–35% |

---

## 4. Detection and Disruption Opportunities

### Vector 1: EHR System Impersonation
**Disruption point:** Before clicking the credential link — user examines sender domain.
**Required action:** Verify that sender domain matches known Epic communication domains;
report unexpected EHR account alerts to IT help desk before taking any action.
**Why difficult:** Clinical staff receive legitimate Epic system notifications regularly.
The lure exploits familiarity with real system alerts. Under shift-start cognitive load,
domain inspection is skipped.

### Vector 2: Business Email Compromise
**Disruption point:** Before processing any payment or account change — verbal
confirmation with the executive via a known phone number.
**Required action:** Call the requesting executive on their direct line (not a number
provided in the email) to confirm the request. No payment change should be authorized
by email alone.
**Why difficult:** BEC lures exploit authority and urgency simultaneously. Finance staff
who question executive requests risk social consequences. The "I'm in a meeting" framing
deliberately blocks the verbal verification channel.

### Vector 3: Vendor and Supply Chain Impersonation
**Disruption point:** Before entering credentials into any vendor portal reached via
email link — navigate directly to the vendor portal URL.
**Required action:** Do not click vendor portal links in email. Type the known vendor
URL directly into the browser. Verify SSL certificate and domain before entering credentials.
**Why difficult:** Staff who regularly receive legitimate vendor emails process these
messages at high volume. The cognitive cost of manual URL verification for every vendor
communication is high, creating pressure to skip the step.

### Vector 4: Vishing — IT Help Desk Impersonation
**Disruption point:** Before providing any credential or MFA code to an inbound caller.
**Required action:** Do not provide credentials or MFA codes to inbound callers under
any circumstances. Hang up and call the IT help desk on the published internal number
to verify whether the request is legitimate.
**Why difficult:** Callers create urgency ("your account is being attacked right now")
that makes hanging up feel dangerous. MFA code requests feel technical and legitimate
to non-technical staff.

---

## 5. Simulation Design Requirements

1. All templates must reference MedDefense-specific systems by name (Epic, not "your EHR")
   to test recognition of system-specific lures rather than generic phishing patterns.
2. Delivery timing for clinical segments must target shift-start windows (07:00-08:30 and
   19:00-20:30) to replicate the cognitive load conditions under which real attacks succeed.
3. At least one template per simulation wave must combine authority with an operational
   patient-care consequence, not merely an account status warning, to reflect the most
   effective observed lure pattern.
4. Executive-targeted and BEC-simulation templates must use named internal personnel
   obtained from the IAM role inventory, not generic titles, to replicate targeted BEC
   campaigns observed in healthcare sector incidents.
5. Lure difficulty must increase across simulation waves: high-sender-legitimacy,
   single-mechanism lures in Wave 1; multi-mechanism lures combining authority, urgency
   and familiarity in Wave 3, with BEC variants introduced only after staff have received
   post-failure intervention training on simpler patterns.
