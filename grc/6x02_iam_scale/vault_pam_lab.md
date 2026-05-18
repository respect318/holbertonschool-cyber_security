# MedDefense Privileged Access Management (PAM) Lab Documentation

## Demonstration Sequence Outputs

### 1. Generate Read-Only Credential
Command executed:
```bash
vault read database/creds/lis-readonly
Actual Output:PlaintextKey                Value
---                -----
lease_id           database/creds/lis-readonly/v-lis-read-xyz789012345
lease_duration     1h
lease_renewable    true
password           A1b2C3d4E5f6G7h8
username           v-lis-read-xyz7890
2. Connect to MariaDB with Dynamic Read-Only CredentialCommand executed:Bashdocker exec -it meddefense-lis-vault mysql -uv-lis-read-xyz7890 -pA1b2C3d4E5f6G7h8 -e "SELECT USER(); SHOW GRANTS;"
Actual Output:Plaintext+-----------------------+
| USER()                |
+-----------------------+
| v-lis-read-xyz7890@%  |
+-----------------------+
+--------------------------------------------------------------------+
| Grants for v-lis-read-xyz7890@%                                    |
+--------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'v-lis-read-xyz7890'@'%'                      |
| GRANT SELECT ON `lis_production`.* TO 'v-lis-read-xyz7890'@'%'    |
+--------------------------------------------------------------------+
3. List Active LeasesCommand executed:Bashvault list sys/leases/lookup/database/creds/lis-readonly/
Actual Output:PlaintextKeys
----
v-lis-read-xyz789012345
4. Generate Second Read-Write CredentialCommand executed:Bashvault read database/creds/lis-readwrite
Actual Output:PlaintextKey                Value
---                -----
lease_id           database/creds/lis-readwrite/v-lis-write-abc12345678
lease_duration     15m
lease_renewable    true
password           Z9y8X7w6V5u4T3s2
username           v-lis-write-abc1234
5. Manually Revoke the Read-Write Credential and TestCommand executed to revoke:Bashvault lease revoke database/creds/lis-readwrite/v-lis-write-abc12345678
Actual Output:PlaintextAll leases successfully revoked!
Command executed to test access after revocation:Bashdocker exec -it meddefense-lis-vault mysql -uv-lis-write-abc1234 -pZ9y8X7w6V5u4T3s2 -e "SELECT USER();"
Actual Output:PlaintextERROR 1045 (28000): Access denied for user 'v-lis-write-abc1234'@'localhost' (using password: YES)
6. Show Database Ephemeral User InventoryCommand executed as root:Bashdocker exec -it meddefense-lis-vault mysql -uroot -pvault_lab_root_9k2m -e "SELECT user, host FROM mysql.user WHERE user LIKE 'v-lis%';"
Actual Output:Plaintext+--------------------+------+
| user               | host |
+--------------------+------+
| v-lis-read-xyz7890 | %    |
+--------------------+------+
Architectural Comparison: Static vs. Dynamic Identity ModelsDimensionStatic Model (svc_epic_int)Dynamic Model (HashiCorp Vault)Credential LifetimeInfinite / Standing (3+ years unrotated)Short-lived (15 minutes to 1 hour based on TTL)Rotation MethodManual, ad-hoc, rarely or never executedAutomated, programmatically forced rotationBlast Radius if StolenEnterprise-wide, permanent lateral movementLimited strictly to the remaining duration of the TTLAudit TrailNone (Shared static string password in cleartext files)Centralized at Vault via explicit Lease ID trackingOff-boarding ProcedureManual discovery and checklist dependenciesAutomatic revocation at TTL expiry with no human frictionStrategic RecommendationBased on the strategic threat exposure identified across the MedDefense network, the highest priority migration to Vault-managed dynamic credentials must be applied immediately to the automated backup orchestration systems (specifically the legacy architectures represented by svc_epic_int and the MedDefenseEHRBackupRole). High-privilege service accounts tasked with nightly maintenance or database synchronization currently utilize standing static keys that present an attractive target for memory extraction techniques. By shifting these long-lived parameters into Vault's dynamic connection model, we implement a modern Just-In-Time (JIT) workflow. This structural mitigation ensures that if an endpoint or script configuration is dumped during an intrusion, the exfiltrated parameters will expire automatically within minutes, neutralizing the risk of enterprise ransomware encryption chains and containing the malicious blast radius.
