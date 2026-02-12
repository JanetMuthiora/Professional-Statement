# SFIA Knowledge and Skill Evidence Mapping (Network Security Files)

## Scope reviewed
- `Janet Muthiora Network Security Assignment .docx` (extracted to `analysis/Janet_Muthiora_Network_Security_Assignment_.txt`).
- `Janet Muthiora Network Security Fundamentals.docx` (extracted to `analysis/Janet_Muthiora_Network_Security_Fundamentals.txt`).

## Evidence-based mapping

### Knowledge (K)
- **K0002 Risk management processes — Demonstrated.** Identifies phishing and DDoS risks, attack paths, and mitigation technologies (VPN, NGFW, SIEM, segmentation, MFA, PKI) showing assess-and-mitigate workflow.  
  Evidence: assignment lines 29-61, 64-75, 83-97, 105-124.
- **K0003 Cybersecurity/privacy laws, regulations, policy, ethics — Partially demonstrated.** Compliance and auditability are referenced, but explicit legal/regulatory frameworks are not deeply analysed.  
  Evidence: assignment lines 95-97; fundamentals line 46 (PII mention).
- **K0004 Cybersecurity and privacy principles — Demonstrated.** CIA (confidentiality/integrity/availability), least privilege, defence controls, monitoring and incident response are explicitly discussed.  
  Evidence: assignment lines 28, 46, 50, 52-61, 95.
- **K0019 Cryptography and key management — Demonstrated.** Covers hashing (MD5/SHA1/SHA256), TLS certificate/public-private key use, pre-master/master secret/session keys, and PKI trust chain.  
  Evidence: fundamentals lines 22-30, 55-59; assignment lines 118-124.
- **K0038 Cybersecurity/privacy risk principles for data lifecycle — Demonstrated.** Addresses risks in transmission (VPN encryption, hashing), processing/storage access controls (RBAC, MFA), and monitoring.  
  Evidence: assignment lines 46-50, 57-61, 84-97, 107-117.
- **K0049 IT security principles and methods (firewalls/DMZ/encryption) — Demonstrated.** Details NGFW capabilities, on-prem/cloud firewall deployment, filtering, IPS, and encryption-based VPN.  
  Evidence: assignment lines 46-56, 64-75.
- **K0056 Network access, IAM (PKI/OAuth/OpenID/SAML/SPML) — Partially demonstrated.** Strong on PKI, MFA, RBAC; no direct implementation of OAuth/OpenID/SAML/SPML.  
  Evidence: assignment lines 83-93, 107-119.
- **K0075 Security system design tools/methods/techniques — Demonstrated.** Produces hybrid architecture with segmented zones, layered controls, and cloud/on-prem tool selection rationale.  
  Evidence: assignment lines 28, 44-75, 79-93.
- **K0104 VPN security — Demonstrated.** Explains VPN purpose, encryption/authentication/integrity contributions, and remote access use in hybrid network.  
  Evidence: assignment lines 45-50.
- **K0158 Organizational IT user security policies — Demonstrated.** Defines role-based permissions, user/group assignment, password configuration, monitoring and audit approach.  
  Evidence: assignment lines 84-93, 97, 101.
- **K0160 Common network-layer attack vectors — Demonstrated.** Discusses phishing-enabled credential theft, SYN/ICMP/UDP flood vectors, reconnaissance, and service disruption.  
  Evidence: assignment lines 31-42; fundamentals lines 42-43, 64-65.
- **K0179 Network security architecture (topology/protocols/components/defence-in-depth) — Demonstrated.** Specifies hybrid topology, segmentation, VPN, firewall tiers, access points, SIEM, and layered control strategy.  
  Evidence: assignment lines 28, 44-75, 79-82.
- **K0203 Security models (Bell-LaPadula/Biba/Clark-Wilson) — Not evidenced.** No formal model analysis present.
- **K0260 PII security standards — Partially demonstrated.** PII handling awareness is explicit, but formal standards mapping is absent.  
  Evidence: fundamentals line 46.
- **K0261 PCI data security standards — Not evidenced.** No PCI DSS mapping.
- **K0262 PHI data security standards — Not evidenced.** No PHI standards analysis.
- **K0263 IT risk management policy/requirements/procedures — Partially demonstrated.** Practical risk treatment and controls are present, but organisational policy/procedure frameworks are not detailed.  
  Evidence: assignment lines 44-75, 95-100.
- **K0274 Transmission records and jamming techniques (Bluetooth/RFID/IR/Wi‑Fi/VoIP etc.) — Partially demonstrated.** Wi‑Fi access point security and segmentation discussed; no jamming/transmission-record analysis.  
  Evidence: assignment lines 79-82.
- **K0276 Security management — Demonstrated.** Includes governance-oriented mechanisms: centralized monitoring (SIEM), role governance (RBAC), auditability, and conditional access.  
  Evidence: assignment lines 57-61, 84-97, 107-117.
- **K0284 User credential management systems — Demonstrated.** Addresses user-group role assignment, MFA, credential protection against phishing, and practical account setup examples.  
  Evidence: assignment lines 84-93, 101, 107-117.
- **K0297 Countermeasure design for identified risks — Demonstrated.** Maps phishing/DDoS threats to specific preventive and detective controls (MFA, NGFW, SIEM, VPN, segmentation).  
  Evidence: assignment lines 29-42, 44-75, 107-117.
- **K0333 Network design processes/security-operational trade-offs — Demonstrated.** Discusses hybrid architecture decisions, scalability/security goals, and pros/cons for RBAC, MFA, PKI implementation choices.  
  Evidence: assignment lines 28, 94-100, 108-115, 120-128.

### Skills (S)
- **S0027 Determine system behaviour/resilience/dependability under change — Demonstrated.** Explains impact of DDoS on availability and operational outcomes; proposes resilience controls (filtering, monitoring, segmentation).  
  Evidence: assignment lines 37-42, 64-75.
- **S0031 Develop/apply access controls — Demonstrated.** Designs RBAC role structures, user/group assignment workflow, and MFA conditions for remote/cloud access.  
  Evidence: assignment lines 84-93, 107-117.
- **S0036 Evaluate adequacy of security designs — Demonstrated.** Compares technology fit and trade-offs (advantages/disadvantages for RBAC, MFA, PKI) to assess solution suitability.  
  Evidence: assignment lines 94-100, 108-115, 120-128, 132.
- **S0040 Implement/maintain/improve network security practices — Demonstrated.** States hands-on Azure firewall and RBAC lab deployment and reflection on applied secure design practice.  
  Evidence: assignment lines 76, 101, 130-134.
- **S0076 Configure software-based protection tools — Demonstrated.** Uses SIEM and cloud monitoring/Sentinel concepts; practical Azure firewall configuration with rule testing is described.  
  Evidence: assignment lines 57-61, 75-76, 130.
- **S0077 Secure network communications — Demonstrated.** Uses VPN encryption, TLS/PKI concepts, and hashing-integrity mechanisms for secure communication channels.  
  Evidence: assignment lines 46-50, 118-124; fundamentals lines 55-59.
- **S0079 Protect network against malware — Demonstrated.** Identifies malware behaviours and applies NGFW/IPS and filtering controls against malware and suspicious traffic.  
  Evidence: fundamentals lines 2, 7-20; assignment lines 55, 68, 73.
- **S0084 Configure/utilize network protection components (firewalls/VPN/NIDS etc.) — Demonstrated.** Specifies VPN/firewall architecture and reports practical firewall inbound/outbound rule setup outcomes.  
  Evidence: assignment lines 45-50, 64-76, 130-131.
- **S0141 Assess security system designs — Demonstrated.** Performs design-level review of controls for hybrid mining environment and records rationale in report/reflection.  
  Evidence: assignment lines 26-28, 44-75, 129-134.
- **S0147 Assess controls using cybersecurity principles/tenets — Partially demonstrated.** Applies principles (least privilege, CIA, defence layers), but does not map explicitly to CIS/NIST controls.  
  Evidence: assignment lines 28, 46, 95, 117, 121.
- **S0167 Recognize vulnerabilities in security systems — Demonstrated.** Identifies phishing indicators, open-port weaknesses (HTTP/80), credential theft paths, and DDoS exposure.  
  Evidence: assignment lines 31-42; fundamentals lines 43, 62-65.
- **S0170 Configure/utilize computer protection components (hardware firewalls/servers/routers) — Demonstrated.** Recommends hardware on-prem firewall at gateway and cloud firewall controls, with routing/rule configuration evidence.  
  Evidence: assignment lines 64-76, 130-131.
- **S0367 Apply cybersecurity/privacy principles to organisational requirements (CIAAAN) — Demonstrated.** Security design aligns organisational needs with confidentiality, integrity, availability, authentication, and non-repudiation controls.  
  Evidence: assignment lines 28, 46, 50, 107, 124.

## Consolidated judgement
- **Strongly demonstrated (core strength):** K0002, K0004, K0019, K0038, K0049, K0075, K0104, K0158, K0160, K0179, K0276, K0284, K0297, K0333, S0027, S0031, S0036, S0040, S0076, S0077, S0079, S0084, S0141, S0167, S0170, S0367.
- **Partially demonstrated (present but incomplete evidence):** K0003, K0056, K0260, K0263, K0274, S0147.
- **Not evidenced in supplied files:** K0203, K0261, K0262.
