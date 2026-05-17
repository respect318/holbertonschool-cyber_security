# MedDefense Business Impact Analysis
**Version:** 1.0
**Classification:** Confidential
**Prepared by:** Fransa work'
**Date:** 2026-05-18
**CISO approval:** _________________________ Date: _________

## Executive Summary
This Business Impact Analysis (BIA) evaluates the critical IT infrastructure of MedDefense to determine the operational, financial, regulatory, and most importantly, patient safety impacts of system downtime. The highest-risk systems identified are the Network Core, Medical Device Integration Gateway, and Epic EHR. An immediate recovery gap exists wherein historical DR plans do not align with the strict Maximum Tolerable Downtime (MTD) required for patient life safety. Immediate action is recommended to align backup frequencies with the newly established Recovery Point Objectives (RPO) and to test Tier 1 system recovery procedures.

## Methodology
This BIA prioritizes systems based on a patient-first impact scale. 
* **Tier 1:** Life safety and immediate clinical impact (MTD < 8 hours).
* **Tier 2:** Critical clinical operations (MTD 8-24 hours).
* **Tier 3:** Important operational support (MTD 24-72 hours).
* **Tier 4:** Business support (MTD > 72 hours).
Data was synthesized from departmental interviews, HIPAA Security Rule mappings, and clinical downtime runbooks.

## System Impact Assessment

### 1. Active Directory
* **Patient Safety Impact:** * *1 Hour:* Minor delays; users rely on cached credentials.
  * *4 Hours:* Clinical staff unable to log into workstations to administer meds or access records.
  * *24 Hours:* Severe care degradation. Inability to admit new patients or route critical labs.
* **Regulatory Impact:** HIPAA Security Rule (Access Control 164.312(a)(1)).
* **Revenue Impact:** $50,000/hour (billing delays and lost productivity).
* **Operational Dependencies:** Underpins authentication for Epic EHR, LIS, PACS, and Email.
* **Maximum Tolerable Downtime (MTD):** 8 Hours. Patient care halts without identity verification.
* **Recovery Time Objective (RTO):** 2 Hours.
* **Recovery Point Objective (RPO):** 4 Hours.
* **Priority Tier:** Tier 1

### 2. Epic EHR
* **Patient Safety Impact:** * *1 Hour:* Shift to paper charting; minor risk of transcription error.
  * *4 Hours:* High risk of medication administration errors; historical patient data unavailable.
  * *24 Hours:* Critical patient diversion to other hospitals required.
* **Regulatory Impact:** HIPAA 164.308(a)(7) (Contingency Plan); Joint Commission EM.12.02.09.
* **Revenue Impact:** $120,000/hour.
* **Operational Dependencies:** Depends on Active Directory and Network Core.
* **MTD:** 8 Hours.
* **RTO:** 4 Hours.
* **RPO:** 15 Minutes.
* **Priority Tier:** Tier 1

### 3. Laboratory Information System (LIS)
* **Patient Safety Impact:** * *1 Hour:* STAT lab results delayed.
  * *4 Hours:* Critical diagnoses (e.g., sepsis, troponin levels) missed, increasing mortality.
  * *24 Hours:* Catastrophic impact on ICU and Emergency Department triaging.
* **Regulatory Impact:** CLIA (Clinical Laboratory Improvement Amendments), HIPAA.
* **Revenue Impact:** $30,000/hour.
* **Operational Dependencies:** Depends on AD and Network Core.
* **MTD:** 4 Hours.
* **RTO:** 2 Hours.
* **RPO:** 1 Hour.
* **Priority Tier:** Tier 1

### 4. PACS/RIS
* **Patient Safety Impact:** * *1 Hour:* Trauma assessments delayed.
  * *4 Hours:* Surgical operations delayed due to lack of pre-op imaging.
  * *24 Hours:* Inability to treat stroke or severe trauma patients.
* **Regulatory Impact:** HIPAA Privacy and Security Rules.
* **Revenue Impact:** $45,000/hour.
* **Operational Dependencies:** Depends on Epic EHR integration and AD.
* **MTD:** 12 Hours.
* **RTO:** 4 Hours.
* **RPO:** 1 Hour.
* **Priority Tier:** Tier 2

### 5. Pharmacy Dispensing System
* **Patient Safety Impact:** * *1 Hour:* Manual dispensing begins; high risk of adverse drug events.
  * *4 Hours:* Missed critical medication windows (e.g., antibiotics, insulin).
  * *24 Hours:* Severe patient harm due to unavailable specialized therapies.
* **Regulatory Impact:** DEA regulations for controlled substances; State Pharmacy Board rules.
* **Revenue Impact:** $25,000/hour.
* **Operational Dependencies:** Depends on AD and Epic EHR orders.
* **MTD:** 6 Hours.
* **RTO:** 2 Hours.
* **RPO:** 1 Hour.
* **Priority Tier:** Tier 1

### 6. Medical Device Integration Gateway
* **Patient Safety Impact:** * *1 Hour:* Nurses must manually check bedside monitors; early warning signs missed.
  * *4 Hours:* Undetected patient deterioration; alarm fatigue from local alerts.
  * *24 Hours:* High mortality risk in ICU due to unrouted critical alarms.
* **Regulatory Impact:** Joint Commission standard for alarm system management.
* **Revenue Impact:** $5,000/hour (primarily legal exposure).
* **Operational Dependencies:** Depends directly on Network Core.
* **MTD:** 2 Hours.
* **RTO:** 1 Hour.
* **RPO:** N/A (Data is real-time streaming).
* **Priority Tier:** Tier 1

### 7. Network Core
* **Patient Safety Impact:** * *1 Hour:* Complete hospital halt. Immediate shift to offline procedures.
  * *4 Hours:* Life safety jeopardized across all departments.
  * *24 Hours:* Full hospital evacuation required.
* **Regulatory Impact:** HIPAA 164.312(a)(1) and 164.308(a)(7).
* **Revenue Impact:** $200,000/hour.
* **Operational Dependencies:** Foundational for all internal and external systems.
* **MTD:** 2 Hours.
* **RTO:** 1 Hour.
* **RPO:** 1 Hour (for switch/router configurations).
* **Priority Tier:** Tier 1

### 8. Email and Secure Messaging
* **Patient Safety Impact:** * *1 Hour:* Internal communications delayed.
  * *4 Hours:* Missed physician consults and alert notifications.
  * *24 Hours:* Inability to coordinate external patient transfers.
* **Regulatory Impact:** HIPAA Privacy Rule (secure transmission).
* **Revenue Impact:** $10,000/hour.
* **Operational Dependencies:** Depends on AD and Network Core.
* **MTD:** 24 Hours.
* **RTO:** 8 Hours.
* **RPO:** 4 Hours.
* **Priority Tier:** Tier 3

### 9. Backup and DR Infrastructure
* **Patient Safety Impact:** * No immediate impact unless paired with a primary system failure.
* **Regulatory Impact:** HIPAA 164.308(a)(7) (Disaster Recovery Plan).
* **Revenue Impact:** $0 immediate impact.
* **Operational Dependencies:** Depends on Network Core.
* **MTD:** 48 Hours.
* **RTO:** 24 Hours.
* **RPO:** 24 Hours.
* **Priority Tier:** Tier 3

### 10. Security Operations Platform
* **Patient Safety Impact:** * Indirect impact; prolonged downtime increases vulnerability to ransomware.
* **Regulatory Impact:** HIPAA Audit Controls 164.312(b).
* **Revenue Impact:** Potential regulatory fines in the event of an undetected breach.
* **Operational Dependencies:** Depends on Network Core and AD.
* **MTD:** 72 Hours.
* **RTO:** 24 Hours.
* **RPO:** 24 Hours.
* **Priority Tier:** Tier 4

## Dependency Map
* **Level 0 (Infrastructure):** Network Core. If this fails, everything fails.
* **Level 1 (Identity):** Active Directory. Fails Epic, LIS, PACS, Email, Pharmacy.
* **Level 2 (Core Clinical):** Epic EHR. Fails connected Pharmacy and PACS workflows.
* **Level 3 (Ancillary/Support):** LIS, Secure Messaging, Security Operations.

## RTO / RPO / MTD Summary Table

| System | Priority Tier | MTD | RTO | RPO |
|--------|---------------|-----|-----|-----|
| Network Core | Tier 1 | 2 Hrs | 1 Hr | 1 Hr |
| Med Device Gateway | Tier 1 | 2 Hrs | 1 Hr | N/A |
| LIS | Tier 1 | 4 Hrs | 2 Hrs | 1 Hr |
| Pharmacy Dispensing | Tier 1 | 6 Hrs | 2 Hrs | 1 Hr |
| Active Directory | Tier 1 | 8 Hrs | 2 Hrs | 4 Hrs |
| Epic EHR | Tier 1 | 8 Hrs | 4 Hrs | 15 Mins |
| PACS/RIS | Tier 2 | 12 Hrs | 4 Hrs | 1 Hr |
| Email & Messaging | Tier 3 | 24 Hrs | 8 Hrs | 4 Hrs |
| Backup & DR | Tier 3 | 48 Hrs | 24 Hrs| 24 Hrs|
| SecOps Platform | Tier 4 | 72 Hrs | 24 Hrs| 24 Hrs|

## Assumptions and Limitations
* Financial impacts are estimates based on average daily billing cycles.
* MTD values assume standard staffing levels and the availability of paper-based downtime procedures.
* Network Core RPO assumes configurations are backed up daily.
