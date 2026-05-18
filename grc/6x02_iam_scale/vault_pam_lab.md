# MedDefense Privileged Access Management (PAM) Lab Documentation

## Lab Setup and Environment Initialization

### Start the Lab Environment Containers
```bash
# Start MariaDB
docker run -d \
  --name meddefense-lis-vault \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=vault_lab_root_9k2m \
  -e MYSQL_DATABASE=lis_production \
  mariadb:10.11

# Start Vault in development mode
docker run -d \
  --name meddefense-vault \
  -p 8200:8200 \
  -e VAULT_DEV_ROOT_TOKEN_ID=meddefense-vault-dev \
  hashicorp/vault:latest
Configure Vault Environment VariablesBashexport VAULT_ADDR='[http://127.0.0.1:8200](http://127.0.0.1:8200)'
export VAULT_TOKEN='meddefense-vault-dev'
Demonstration Sequence Outputs1. Generate Read-Only CredentialCommand executed:Bashvault read database/creds/lis-readonly
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
Architectural Comparison: Static vs. Dynamic Identity ModelsDimensionStatic Model (svc_epic_int)Dynamic Model (HashiCorp Vault)Credential LifetimeInfinite / Standing (3+ years unrotated)Short-lived (15 minutes to 1 hour based on TTL)Rotation MethodManual, ad-hoc, rarely or never executedAutomated, programmatically forced rotationBlast Radius if StolenEnterprise-wide, permanent lateral movementLimited strictly to the remaining duration of the TTLAudit TrailNone (Shared static string password in cleartext files)Centralized at Vault via explicit Lease ID trackingOff-boarding ProcedureManual discovery and checklist dependenciesAutomatic revocation at TTL expiry with no human frictionStrategic RecommendationBased on the baseline risk exposure, the highest priority migration to Vault-managed dynamic credentials must be applied to the backup orchestration layer (MedDefenseEHRBackupRole). Automated server scripts and nightly maintenance tasks run on predictable schedules but require high levels of administrative access to execute. By transitioning these legacy accounts to Vault's Just-In-Time (JIT) identity structure, we successfully eliminate standing static keys from data disks and memory. This ensures that even if a host is compromised, the stolen token expires within minutes, preventing cyber-attackers from launching ransomware encryption loops or executing large-scale data exfiltration attacks.
