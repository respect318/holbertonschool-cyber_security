# MedDefense Cloud IAM Policy Analysis

## Policy 1: MedDefenseSIEMLogReader

### Violations Table
| Violation | Attack scenario enabled | Corrected statement |
|---|---|---|
| `s3:*` on `Resource: *` | Attacker who compromises this Lambda can read, write, delete and list every S3 bucket in the account, including the ePHI backup bucket | `s3:GetObject` and `s3:ListBucket` scoped to the SIEM log bucket ARN only |
| `logs:*` on `Resource: *` | Attacker can read, delete or modify CloudWatch log groups across all Lambda functions, masking activity | `CreateLogGroup`, `CreateLogStream`, `PutLogEvents` scoped to the function's own log group ARN |
| `cloudwatch:*` on `Resource: *` | Attacker can modify CloudWatch alarms, suppressing security alerts | Action removed entirely; this function does not need CloudWatch metrics access |

### Corrected Policy
See `siem_reader_policy.json`

### Security Improvement
The original policy violated the principle of least privilege by granting wildcard access across S3 and CloudWatch, allowing potential lateral movement or data exfiltration if the Lambda was compromised. The corrected policy strictly scopes access to reading the specific SIEM log bucket and writing logs only to the function's designated CloudWatch log group. This containment ensures that a compromise is isolated and the blast radius is minimal.

---

## Policy 2: MedDefenseEHRBackupRole

### Violations Table
| Violation | Attack scenario enabled | Corrected statement |
|---|---|---|
| `s3:*` on `Resource: *` | Attacker compromising the EC2 instance can delete existing backups or access other buckets containing sensitive data | `s3:PutObject` and `s3:ListBucket` strictly scoped to the EHR backup bucket ARN |
| `kms:*` on `Resource: *` | Attacker can delete KMS keys (crypto-shredding), causing permanent data loss across the organization | `kms:Encrypt` and `kms:GenerateDataKey` scoped only to the specific customer-managed key ARN |

### Corrected Policy
See `ehr_backup_policy.json`

### Security Improvement
The initial configuration allowed catastrophic potential, such as deleting the entire organization's KMS keys or downloading arbitrary buckets. By refining the policy, the EC2 instance is now restricted to only putting objects into its specific bucket and only using the designated KMS key for encryption operations. This drastically limits the impact of an instance takeover, protecting the broader AWS environment from malicious data deletion or ransomware-style crypto-shredding.

---

## Policy 3: MedDefenseBreakGlassAdmin

### Violations Table
| Violation | Attack scenario enabled | Corrected statement |
|---|---|---|
| Missing MFA Condition | An attacker who steals the emergency credentials can achieve instant Domain/Account Admin from anywhere | Added `"BoolIfExists": {"aws:MultiFactorAuthPresent": "true"}` to the condition block |
| Missing IP Restriction | An attacker can utilize the compromised credentials from a foreign or unauthorized network | Added `"IpAddress": {"aws:SourceIp": "198.51.100.0/24"}` to the condition block |

### Corrected Policy
See `break_glass_policy.json`

### Security Improvement
A break-glass account without MFA or network constraints is the most dangerous risk in any cloud infrastructure. By adding condition blocks that enforce MFA verification and strictly limit authentication requests to the authorized MedDefense on-premises IP range (198.51.100.0/24), we establish a strong "Zero Trust" perimeter. Even if the password is leaked, an external attacker cannot use it.
