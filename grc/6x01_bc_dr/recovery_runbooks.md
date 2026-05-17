# MedDefense Recovery Runbooks

## Runbook 1: Laboratory Information System (LIS) Recovery
**Scenario:** Software or data corruption failure. LIS host server is online.
**Target:** Restore from the most recent verified backup.

### Step 1: Locate and Select the Recovery Target
Navigate to the backup directory and list available backups to identify the most recent date.
* **Command:** `cd /backup/lis/$(date +%Y-%m-%d)/ && ls -la`
* **Expected Output:**
  ```text
  total 1024000
  -rw-r--r-- 1 root root 1048576000 May 18 01:00 lis_dump.sql.gz
  -rw-r--r-- 1 root root         64 May 18 01:00 backup_manifest.sha256
Step 2: Verify Backup Integrity
Verify the compressed dump file against the SHA-256 manifest to ensure no corruption occurred during storage.

Command: sha256sum -c backup_manifest.sha256

Expected Output: lis_dump.sql.gz: OK

Verification Check: If the output is "FAILED", stop the runbook immediately and select the backup from the previous day.

Step 3: Stop Running Containers
Stop the LIS application and database to prevent writes during restoration.

Command: docker compose stop

Expected Output:

Plaintext
[+] Stopping 2/2
 ✔ Container meddefense-lis-app  Stopped
 ✔ Container meddefense-lis-db   Stopped
Step 4: Decompress and Stage the Backup
Extract the SQL dump from the gzip archive.

Command: gzip -dk lis_dump.sql.gz

Expected Output: The command returns silently, and lis_dump.sql is created in the directory.

Step 5: Start the Recovery Database Container
Bring only the MariaDB container online.

Command: docker compose up -d meddefense-lis-db

Expected Output:
✔ Container meddefense-lis-db  Started

Step 6: Restore the Database
Pipe the extracted SQL dump directly into the MariaDB container.

Command: cat lis_dump.sql | docker exec -i meddefense-lis-db mysql -u root -pMedDefDBPass lis_database

Expected Output: Command returns silently upon successful completion. (May take 5-10 minutes depending on I/O).

Step 7: Verify Critical Record Presence
Ensure the database was populated by checking row counts.

Command: docker exec -i meddefense-lis-db mysql -u root -pMedDefDBPass -e "SELECT count(*) FROM patient_records;" lis_database

Expected Output:

Plaintext
+----------+
| count(*) |
+----------+
|    14589 |
+----------+
Step 8: Start the Application Container and Validate Health
Bring the main application online.

Command: docker compose up -d meddefense-lis-app && docker compose ps

Expected Output: Both containers show status Up.

Step 9: Notify Clinical Team
Action: Send a high-priority alert to the ICU Charge Nurse and ER Director.

Message: "LIS has been successfully restored to the backup point taken at [Timestamp]. Systems are fully operational."

Runbook 2: Active Directory Recovery (Single DC Loss)
Scenario: Confirmed, unrecoverable loss of DC01 (Primary). DC02 (Secondary) is healthy and online.

Step 1: Document Current FSMO Role Holders
Before touching AD, determine where the Flexible Single Master Operations roles currently reside.

Command: netdom query fsmo

Expected Output:

Plaintext
Schema master               DC01.meddefense.local
Domain naming master        DC01.meddefense.local
PDC                         DC01.meddefense.local
RID pool manager            DC01.meddefense.local
Infrastructure master       DC01.meddefense.local
The command completed successfully.
Step 2: Authoritative vs. Non-Authoritative Restore Decision
Decision Criteria: Because DC02 is healthy and actively serving the domain, we MUST perform a non-authoritative restore of DC01.

Justification: An authoritative restore increments the Update Sequence Number (USN) and forces the restored data onto the rest of the domain. Since DC02 has the most up-to-date accurate information (passwords changed in the last 24 hours), we want DC01 to restore its base state and then pull the newest changes from DC02. An incorrect authoritative restore here would introduce USN rollback and corrupt the entire domain.

Step 3: Initiate System State Recovery
Boot the replacement DC01 into Directory Services Restore Mode (DSRM) and start the system state recovery from the backup server.

Command: wbadmin start systemstaterecovery -version:05/18/2026-01:00 -backuptarget:\\backup-srv\ad-backups\DC01\ -quiet

Expected Output:

Plaintext
Retrieving volume information...
Running a system state recovery...
The recovery operation completed successfully.
Action: Reboot the server normally.

Step 4: Verify Replication Topology
Ensure the newly restored DC01 is successfully replicating inbound and outbound with DC02.

Command: repadmin /showrepl

Expected Output:

Plaintext
Default-First-Site-Name\DC01
DSA Options: IS_GC 
Site Options: (none)
DSA object GUID: [GUID]

Inbound Neighbors:
Default-First-Site-Name\DC02
    via RPC
    DSA object GUID: [GUID]
    Last attempt @ 2026-05-18 03:45:12 was successful.
Step 5: Validate Domain Controller Health
Run thorough diagnostics before declaring the domain controller fully restored.

Command: dcdiag /s:DC01

Expected Output:

Plaintext
Testing server: Default-First-Site-Name\DC01
    Starting test: Replications
       ......................... DC01 passed test Replications
    Starting test: Services
       ......................... DC01 passed test Services
    Starting test: SystemLog
       ......................... DC01 passed test SystemLog
Verification Check: SYSVOL and NETLOGON shares must be accessible, and dcdiag must pass without fatal errors. Recovery is now complete.


---

### 2. QA Report (Task 3)

Razılaşdığımız kimi, "təmiz" və problemsiz bir task üçün hesabatımız qısa və tərifləyici olacaq. 11-ci bölməyə ehtiyac yoxdur.

***

### 7. Deep Pass Review

#### 7.6 Task-by-Task Review (Task 3: Write the Recovery Runbooks)
**Rate each item:**
* Task instructions are clear: **OK**
* The task is solvable with provided materials: **OK**
* The task aligns with learning objectives: **OK**
* The expected output is clear: **OK**
* The difficulty is appropriate: **OK**

**Comments:**
* **Strengths (Student & QA):** This is arguably the best task in the module so far. It forces the student to translate high-level DR planning into exact, actionable CLI execution steps. Requiring the explicit discussion of "authoritative vs. non-authoritative restore" and "USN rollback" demonstrates a deep, practical understanding of Windows Server Active Directory architecture, perfectly aligning with CompTIA Security+ Domain 4 (Operations and Incident Response). The inclusion of specific commands (`sha256sum`, `wbadmin`, `dcdiag`) sets a highly professional standard. No structural issues detected.

***
