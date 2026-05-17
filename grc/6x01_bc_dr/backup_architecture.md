## MedDefense Backup Architecture

### Strategy Overview
This backup architecture aligns the MedDefense Disaster Recovery plan directly with the Maximum Tolerable Downtime (MTD) and Recovery Point Objectives (RPO) defined in the Business Impact Analysis (BIA). The fundamental design principle applied across all Tier 1 and Tier 2 systems is the 3-2-1 rule: three copies of data, stored on two different types of media, with at least one copy located off-site (AWS S3) to survive a full primary data center loss. To guarantee HIPAA compliance, all ePHI data at rest is encrypted using AES-256, and all ePHI in transit to secondary destinations is secured via TLS 1.2 or TLS 1.3.

The schedule enforces a strict RPO math verification: no system's backup interval exceeds its declared RPO. Furthermore, the architecture respects the system dependency chain. Because Epic EHR relies on Active Directory (AD) for authentication, AD's snapshot schedule (4 hours) could conflict with Epic's RPO (15 minutes). To resolve this, Epic EHR's local cache is synchronized with a highly available read-only domain controller (RODC) locally, preventing a total authentication block during short micro-outages.

### RPO Compliance Verification
| System | Priority Tier | Declared RPO | Backup Frequency | Compliant Y/N | Notes |
|--------|---------------|--------------|------------------|---------------|-------|
| Network Core | Tier 1 | 1 hour | 1 hour | Y | Configs exported hourly. |
| Med Device Gateway | Tier 1 | N/A | N/A | Y | Real-time stream; no data stored. |
| Laboratory Information System (LIS) | Tier 1 | 1 hour | 1 hour | Y | Incremental backups hourly. |
| Pharmacy Dispensing | Tier 1 | 1 hour | 1 hour | Y | Incremental backups hourly. |
| Active Directory | Tier 1 | 4 hours | 4 hours | Y | Snapshot every 4 hours. |
| Epic EHR | Tier 1 | 15 minutes | 15 minutes | Y | DB log shipping every 15 mins. |
| PACS/RIS | Tier 2 | 1 hour | 1 hour | Y | Incremental backups hourly. |

### Per-System Backup Specifications

#### Active Directory
| Field | Specification |
|---|---|
| Backup type | System state backup (full) + VSS snapshot |
| Schedule | System state: daily at 01:00; snapshot: every 4 hours |
| Retention | 30 days on-site; 1 year offsite cold archive |
| Primary destination | On-site NAS (RAID-6) at /backup/ad/ |
| Secondary destination | AWS S3 us-east-2, isolated backup account |
| Encryption at rest | AES-256 via Windows Server Backup |
| Encryption in transit | TLS 1.3 to S3 endpoint |
| Integrity verification | SHA-256 hash on completion; weekly restore test to isolated recovery VM |
| Restoration sequence | 1. Boot from media in DSRM; 2. Apply system state; 3. Verify SYSVOL replication |
| Responsible role | Systems Administrator (execution); Security Operations (weekly verification) |

#### Network Core
| Field | Specification |
|---|---|
| Backup type | Automated configuration export |
| Schedule | Every 1 hour via Ansible |
| Retention | 90 days on-site; 1 year offsite |
| Primary destination | On-site TFTP server / NAS |
| Secondary destination | AWS S3 us-east-2 |
| Encryption at rest | AES-256 |
| Encryption in transit | TLS 1.2 |
| Integrity verification | SHA-256 hash comparison; monthly isolated lab deployment |
| Restoration sequence | 1. Boot switch; 2. TFTP config load; 3. Validate routing tables |
| Responsible role | Network Engineer; Network Architect |

#### Epic EHR
| Field | Specification |
|---|---|
| Backup type | Full DB backup + Transaction Log Shipping |
| Schedule | Full: weekly; Incremental: daily; Logs: every 15 minutes |
| Retention | 30 days hot storage; 7 years compliance archive |
| Primary destination | Dedicated All-Flash SAN |
| Secondary destination | Geographically isolated colocation site |
| Encryption at rest | AES-256 |
| Encryption in transit | TLS 1.3 |
| Integrity verification | Daily automated restore test to staging environment |
| Restoration sequence | 1. Restore AD; 2. Restore DB engine; 3. Apply logs; 4. App layer spin up |
| Responsible role | DBA Team; Clinical IT Ops |

#### Laboratory Information System (LIS)
| Field | Specification |
|---|---|
| Backup type | Snapshot + Incremental DB sync |
| Schedule | Snapshot: every 4 hours; Incremental: every 1 hour |
| Retention | 30 days on-site; 5 years offsite |
| Primary destination | On-site NAS |
| Secondary destination | AWS S3 us-east-2 |
| Encryption at rest | AES-256 |
| Encryption in transit | TLS 1.2 |
| Integrity verification | SHA-256 hash; monthly recovery simulation |
| Restoration sequence | 1. Restore AD; 2. Restore LIS DB; 3. Reconnect to Medical Gateway |
| Responsible role | Systems Administrator; Clinical IT Ops |

#### Pharmacy Dispensing System
| Field | Specification |
|---|---|
| Backup type | Incremental DB Backup |
| Schedule | Every 1 hour |
| Retention | 60 days on-site; 7 years offsite |
| Primary destination | On-site NAS |
| Secondary destination | AWS S3 us-east-2 |
| Encryption at rest | AES-256 |
| Encryption in transit | TLS 1.2 |
| Integrity verification | SHA-256 hash; weekly restore to test bed |
| Restoration sequence | 1. Restore AD; 2. Restore DB; 3. Verify DEA compliance logs |
| Responsible role | Systems Administrator; Pharmacy IT Rep |

#### PACS/RIS
| Field | Specification |
|---|---|
| Backup type | Incremental file sync |
| Schedule | Every 1 hour |
| Retention | 1 year hot storage; 10 years deep archive |
| Primary destination | On-site Storage Array |
| Secondary destination | AWS S3 Glacier Deep Archive |
| Encryption at rest | AES-256 |
| Encryption in transit | TLS 1.2 |
| Integrity verification | MD5 hash; monthly automated mount test |
| Restoration sequence | 1. Restore AD; 2. Mount storage array; 3. Validate Epic integration |
| Responsible role | Storage Engineer; Clinical IT Ops |

### Full Data Center Loss: Restoration Sequence
| Order | System | Est. Recovery Time | Hard Dependency |
|---|---|---|---|
| 1 | Network Core | 45 min | None |
| 2 | Active Directory | 60 min | Network Core |
| 3 | Epic EHR | 4 hours | Active Directory, Network Core |
| 4 | Laboratory Information System (LIS) | 2 hours | Active Directory, Network Core |
| 5 | Pharmacy Dispensing System | 2 hours | Active Directory, Epic EHR |
| 6 | PACS/RIS | 4 hours | Active Directory, Epic EHR |

### Dependency Restore Constraints
Systems cannot begin recovery until their hard predecessors are online. The Network Core is the absolute base layer (Level 0). If the Network Core misses its 1-hour RTO, all subsequent system restorations are blocked, cascading into a total hospital failure. Epic EHR relies heavily on Active Directory for clinical staff login. If Active Directory's recovery exceeds its 2-hour RTO, Epic EHR can theoretically come online, but clinicians will be locked out, rendering the system effectively down. Operationally, missing these predecessor RTOs immediately triggers hospital-wide paper charting protocols and patient diversion to external facilities.
