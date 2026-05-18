# Phishing Simulation Campaign Plan: MedDefense Health Systems

**Prepared by:** Security Awareness Program Manager
**Date:** 2026-05-18
**Version:** 1.0
**Classification:** Internal — Security Team and CISO Only

---

## 1. Campaign Overview

### Scope
- **Total employee population:** 1,200 employees across clinical, administrative, IT,
  executive, vendor-facing and research functions
- **Simulation platform:** GoPhish (self-hosted) or KnowBe4 Enterprise, deployed within
  MedDefense network boundary to prevent external data exposure
- **Initial rollout window:** 90 days (four waves)
- **Extended program horizon:** 18 months with quarterly review cycles

### Program Objectives

| Objective | Baseline (Current) | 90-Day Target | 18-Month Target |
|---|---|---|---|
| Organization-wide click rate | 56% | ≤35% | ≤15% |
| Phishing report rate | <5% (estimated) | ≥20% | ≥40% |
| Post-simulation training completion | Unknown | ≥85% | ≥95% |
| Repeat clicker rate (consecutive waves) | Unknown | ≤20% | ≤8% |

### Governance

| Role | Responsibility |
|---|---|
| CISO (Dr. Patricia Morales) | Final approval on all simulation templates before deployment |
| Security Program Manager | Campaign execution, metrics reporting, wave scheduling |
| HR Director (Maria Santos) | Escalation coordination; individual data access under defined criteria only |
| Legal Counsel | Template review for regulatory compliance (HIPAA, state privacy law) |
| Department Managers | Receive aggregate team metrics only — no individual click data |

**Result disclosure policy:** Individual simulation results are not shared with department
managers and do not appear in performance reviews. Aggregate team-level data (click rate
by department, report rate by department) is shared with managers monthly. Individual
data is accessible only to the Security Program Manager and CISO. HR escalation requires
a second confirmed offense plus formal escalation trigger as defined in Section 5.

---

## 2. Employee Segmentation

Segmentation is based on the six role categories from the MedDefense IAM audit (6x02)
and threat vectors documented in the Social Engineering Threat Profile (Task 1).

### Segment 1: Clinical Staff
- **Estimated population:** 480 employees (nurses, patient care technicians, clinical assistants)
- **Primary risk vectors:** EHR system impersonation, IT help desk vishing, credential
  harvesting during shift-start authentication cycles
- **Template assignment rationale:** EHR urgency lures (Epic account suspension),
  shift-handoff notification lures, IT security alert lures timed to 07:00-08:30 and
  19:00-20:30 windows
- **Exclusion criteria:** Staff on FMLA, medical leave or bereavement leave at time of
  wave delivery; staff who have reported a real phishing incident in the prior 14 days

### Segment 2: Administrative and Billing Staff
- **Estimated population:** 220 employees (scheduling, billing, insurance, front desk)
- **Primary risk vectors:** BEC executive impersonation, vendor invoice fraud,
  HIPAA compliance authority lures
- **Template assignment rationale:** CFO/CMO impersonation payment requests, vendor
  re-authentication lures, insurance portal credential harvesting
- **Exclusion criteria:** Staff processing active insurance claims under regulatory
  deadline at time of delivery (confirmed with department manager pre-wave)

### Segment 3: IT and System Administrators
- **Estimated population:** 65 employees (sysadmins, network engineers, help desk)
- **Primary risk vectors:** Privileged credential harvesting, MFA bypass vishing,
  vendor software update impersonation, targeted spear-phishing using internal terminology
- **Template assignment rationale:** Advanced templates only from Wave 2 onward;
  IT-specific lures referencing internal tools (Active Directory, VPN, patch management
  systems); spear-phishing with named personnel from Wave 3
- **Exclusion criteria:** Staff actively responding to a confirmed security incident
  at time of wave delivery; staff in on-call rotation during a declared maintenance window

### Segment 4: Executive and Senior Leadership
- **Estimated population:** 35 employees (C-suite, directors, department heads)
- **Primary risk vectors:** Spear-phishing with named internal references, BEC targeting
  (as originators and as targets), board communication impersonation
- **Template assignment rationale:** Intermediate templates in Wave 1; advanced BEC
  and wire fraud scenarios from Wave 2; all templates require CISO personal approval
  before deployment to this segment
- **Exclusion criteria:** Executives traveling internationally at time of delivery
  (anomalous login behavior may trigger real security alerts); board meeting weeks

### Segment 5: Vendor-Facing and Procurement Staff
- **Estimated population:** 85 employees (procurement, accounts payable, supply chain)
- **Primary risk vectors:** Vendor impersonation, invoice fraud, supply chain portal
  credential harvesting
- **Template assignment rationale:** Vendor re-authentication lures, fake invoice
  approval workflows, supply chain notification lures
- **Exclusion criteria:** Staff processing end-of-quarter procurement cycles
  (confirm dates with procurement manager pre-wave)

### Segment 6: Research and Compliance Staff
- **Estimated population:** 315 employees (researchers, compliance officers, legal, HR)
- **Primary risk vectors:** Regulatory authority lures (HIPAA, IRB, CMS),
  research data access requests, grant notification impersonation
- **Template assignment rationale:** HIPAA compliance alert lures, IRB audit
  notification lures, CMS portal re-authentication requests
- **Exclusion criteria:** Staff under active regulatory audit at time of wave delivery

---

## 3. Wave Schedule

**Cool-down policy:** No segment receives a simulation within 21 days of their previous
wave. Employees who clicked in the prior wave and completed remedial training are
eligible for the next wave. Employees who clicked and did not complete training are
flagged for HR coordination before the next wave targets them.

### Wave 1 — Baseline Assessment (Days 1–21)
- **Delivery window:** Days 8–14 (one week after program announcement)
- **Target segments:** All six segments
- **Difficulty tier:** Baseline — high sender legitimacy, single psychological mechanism,
  obvious-on-reflection lures
- **Templates assigned:**
  - Segments 1, 6: Epic account suspension alert (authority + urgency)
  - Segments 2, 5: Vendor invoice re-authentication (familiarity)
  - Segment 3: IT help desk password reset notification (authority)
  - Segment 4: Internal IT security compliance reminder (authority)
- **Delivery timing:**
  - Clinical (Segment 1): 07:15 and 19:15 (shift-start)
  - All others: Tuesday–Thursday, 09:00-11:00 (peak email processing window)
- **Objective:** Establish baseline click rate and report rate per segment
- **Cool-down:** 21 days minimum before Wave 2 targets same population

### Wave 2 — Intermediate Escalation (Days 29–49)
- **Delivery window:** Days 36–42
- **Target segments:** All six segments
- **Difficulty tier:** Intermediate — dual psychological mechanism, plausible but
  verifiable sender domain, operational consequence framing
- **Templates assigned:**
  - Segment 1: Epic EHR access expiry with patient care impact framing (authority + urgency)
  - Segment 2: CFO payment authorization request (authority + scarcity)
  - Segment 3: VPN certificate renewal with service interruption warning (authority + urgency)
  - Segment 4: Board document review request from spoofed legal counsel (authority + familiarity)
  - Segment 5: McKesson supply delivery hold requiring portal confirmation (urgency + familiarity)
  - Segment 6: HIPAA audit document submission deadline (fear + authority)
- **Delivery timing:** Same rationale as Wave 1; clinical segment timing maintained
- **Objective:** Measure improvement from Wave 1; identify repeat clickers
- **Cool-down:** 21 days minimum before Wave 3

### Wave 3 — Advanced Targeting (Days 57–77)
- **Delivery window:** Days 64–70
- **Target segments:** Segments 2, 3, 4, 5 (high-risk segments only)
- **Difficulty tier:** Advanced — multi-mechanism lures, internal named personnel
  references, BEC-style formatting with thread hijacking simulation
- **Templates assigned:**
  - Segment 2: BEC wire transfer — spoofed CFO email with prior thread context
  - Segment 3: Spear-phishing referencing internal patch management system by name
  - Segment 4: Board member impersonation with DocuSign credential harvest
  - Segment 5: Vendor account manager impersonation with banking detail update request
- **Delivery timing:** Monday morning (08:30) to exploit week-start cognitive load
- **Objective:** Test resilience against sophisticated targeted attacks; identify
  high-risk individuals requiring priority intervention
- **Cool-down:** 21 days minimum before Wave 4

### Wave 4 — Validation and Measurement (Days 78–90)
- **Delivery window:** Days 82–88
- **Target segments:** All six segments
- **Difficulty tier:** Mixed — repeat baseline lures for Segments 1 and 6 to measure
  improvement; intermediate lures for Segments 2, 5; advanced for Segments 3 and 4
- **Templates assigned:** Drawn from Wave 1 and Wave 2 library (no new templates)
- **Delivery timing:** Consistent with prior waves
- **Objective:** Measure 90-day behavior change against Wave 1 baseline;
  generate data for executive reporting and program continuation justification

---

## 4. Metrics Framework

### M1: Click Rate
- **Formula:** (Employees who clicked simulation link ÷ Employees who received simulation) × 100
- **Measurement interval:** Per wave, per segment
- **90-day target:** ≤35% organization-wide
- **18-month target:** ≤15% organization-wide
- **Deteriorating result:** Click rate increases wave-over-wave in any segment —
  indicates lure calibration error, training failure or population change; triggers
  immediate review of post-click intervention content for that segment

### M2: Report Rate
- **Formula:** (Employees who reported simulation as phishing ÷ Employees who received simulation) × 100
- **Measurement interval:** Per wave, per segment
- **90-day target:** ≥20% organization-wide
- **18-month target:** ≥40% organization-wide
- **Deteriorating result:** Report rate declines wave-over-wave — indicates reporting
  channel friction, fear of consequences or low confidence in IT responsiveness;
  triggers review of reporting mechanism and post-report feedback loop

### M3: Repeat Clicker Rate
- **Formula:** (Employees who clicked in wave N and wave N+1 ÷ Employees who received both waves) × 100
- **Measurement interval:** Calculated after each wave pair
- **90-day target:** ≤20%
- **18-month target:** ≤8%
- **Deteriorating result:** Rate exceeds 25% — indicates post-click intervention is
  ineffective; triggers mandatory review and redesign of remedial training module

### M4: Mean Time to Report (MTTR)
- **Formula:** Average time elapsed between simulation email delivery timestamp and
  employee report action, measured in minutes
- **Measurement interval:** Per wave
- **90-day target:** ≤240 minutes (4 hours)
- **18-month target:** ≤60 minutes
- **Deteriorating result:** MTTR increases — indicates employees are hesitating before
  reporting, potentially due to uncertainty about consequences or reporting channel usability

### M5: Post-Simulation Training Completion Rate
- **Formula:** (Employees who completed remedial training module within 7 days of
  click event ÷ Employees who clicked) × 100
- **Measurement interval:** 7 days post-wave
- **90-day target:** ≥85%
- **18-month target:** ≥95%
- **Deteriorating result:** Completion rate below 70% — indicates training module is
  inaccessible, too long or not sufficiently prompted; triggers LMS review and
  manager notification at aggregate level

### M6: False Positive Report Rate
- **Formula:** (Real legitimate emails reported as phishing ÷ Total phishing reports submitted) × 100
- **Measurement interval:** Continuous; reviewed monthly
- **90-day target:** ≤15%
- **18-month target:** ≤8%
- **Deteriorating result:** Rate exceeds 20% — indicates over-sensitization;
  employees are reporting real emails and creating SOC alert fatigue;
  triggers review of post-simulation guidance and reporting criteria education

---

## 5. Escalation Criteria

Simulation results are training events by default. The following conditions escalate
a result from a training event to a security team investigation:

### Escalation Tier 1 — Priority Remediation (Security Team Only)
**Trigger:** Employee clicks in three consecutive waves after completing remedial training
following each prior click.
**Action:** Security Program Manager flags employee ID (not name) to CISO. CISO
determines whether additional one-on-one training or access restriction review is warranted.
HR is not notified at this tier.

### Escalation Tier 2 — HR Coordination
**Trigger:** Employee clicks in three consecutive waves AND fails to complete remedial
training after two of those waves AND holds privileged access (Segments 3 or 4).
**Action:** Security Program Manager escalates to CISO and HR Director with individual
data under the formal HR escalation protocol. HR determines appropriate response.
Performance review impact is prohibited per Maria Santos's standing directive.

### Escalation Tier 3 — Security Investigation
**Trigger:** Employee clicks a simulation link AND within 72 hours exhibits anomalous
access behavior (after-hours privileged access, bulk data export, lateral movement
detected by SIEM) — indicating the simulation may have revealed an active threat actor
or an insider threat in progress.
**Action:** Immediate escalation to Security Operations. Treat as potential live incident.
Do not inform the employee that the trigger was a simulation. Follow IR playbook.

### Escalation Tier 4 — Insider Threat Review
**Trigger:** Employee exhibits a combination of behavioral indicators across two or more
waves: consistent clicking on authority-based lures targeting privileged access,
simultaneous anomalous access patterns in SIEM, and recent HR-documented grievance
or performance concern.
**Action:** Refer to insider threat framework (Task 8). Do not act on simulation data
alone. Simulation data is one indicator among several required for insider threat designation.

---

## 6. Exclusion and Ethics Policy

### Exclusion Criteria
The following employees are excluded from simulation waves:

- Employees on FMLA, medical leave, bereavement leave or approved personal leave
  at the time of wave delivery
- Employees who have reported a confirmed real phishing incident in the prior 14 days
- Employees actively responding to a declared security incident
- New employees within their first 30 days (receive awareness training instead)
- Employees who have formally requested exclusion and received CISO approval
  (documented; valid for one wave cycle only)

### Aggregate vs. Individual Disclosure Framework

| Data Type | Who Can Access | Conditions |
|---|---|---|
| Individual click/report data | Security Program Manager, CISO | Standard operations |
| Individual data | HR Director | Tier 2+ escalation only, formal protocol |
| Individual data | Department Managers | Never, under any standard condition |
| Aggregate team data | Department Managers | Monthly report, no individual identification |
| Program metrics | Executive Leadership | Quarterly board report, aggregate only |

### Post-Simulation Support
- All employees who click receive an immediate, non-punitive educational intervention
  (landing page explaining the simulation, what to look for and how to report)
- Employees who experience distress following a simulation event may contact the
  Employee Assistance Program (EAP); HR will not be notified that the trigger was
  a simulation result
- No public identification of individuals who clicked; team-level data is never
  presented in a format that allows reverse identification of individuals in small teams
  (fewer than 5 members — data is suppressed)

### Governance Sign-Off Requirements
Before any template is deployed:

1. Security Program Manager drafts template and maps it to threat profile vector
2. Legal Counsel reviews for HIPAA compliance and state privacy law alignment
3. CISO reviews and approves template content and targeting segment
4. For templates targeting Segment 4 (Executive): CISO personal sign-off required;
   no delegation permitted
5. For templates referencing named internal personnel: HR Director must confirm
   the named individual has been informed they may appear in simulation content
6. Approved templates are logged in the template registry with approval date,
   approver names and target segment before deployment
