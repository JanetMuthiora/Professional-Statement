# Network Security — NetSec Concepts

Practical network security labs and scripts completed as part of a Bachelor of Information Technology at Central Queensland University. This branch covers attack simulation, traffic analysis, cryptographic integrity, port scanning, and remote access — all carried out inside sandboxed virtual environments.

---

## Key Objectives

1. Understand key security concepts and principles underpinning modern network defence.
2. Analyse how common security attacks work and how defences mitigate them.
3. Apply cryptographic mechanisms (hashing, symmetric encryption, HMAC) to protect data in transit and at rest.
4. Implement access control technologies — firewalls, authentication, SSH — to secure computer networks.
5. Identify threats specific to wireless networks and describe appropriate countermeasures.

---

## Tools and Skills Learnt

| Category | Tools / Technologies |
|---|---|
| Virtualization | VirtualBox — Windows VM (target), Kali Linux (attacker) |
| Network Analysis | Wireshark |
| Scripting | Python 3 |
| Cryptography | OpenSSL (AES-256-CBC), `hashlib` (MD5, SHA-256), `hmac`, `pycryptodome` (3DES) |
| Reconnaissance | Python `socket` (port scanner), Nmap |
| Remote Access | SSH (OpenSSH, legacy key algorithm flags) |
| Attack Framework | Metasploitable 2 (vulnerable target VM) |

---

## Projects and Labs

### 1. Malware Delivery and Reverse-Connection Analysis
**Environment:** Kali Linux (attacker) + Windows VM (victim) — fully sandboxed, no internet connectivity.

Simulated a complete attack chain:
- Delivered a malicious payload to the Windows VM.
- Established a reverse connection from the victim back to the attacker machine.
- Observed the connection in Wireshark and analysed traffic to understand how reverse shells evade perimeter firewalls (outbound connections are typically less restricted than inbound).

**Key learning:** Firewalls configured to block inbound connections provide limited protection against reverse-shell payloads. Defence requires egress filtering, endpoint detection, and network segmentation.

---

### 2. Threat Attack Simulation — Self-Replicating Virus (`ThreatAttack.py` + `virus0.py` … `virus9.py`)
A Python script that replicates itself ten times in the same directory, naming each copy `virus0.py` through `virus9.py`. The simulation demonstrates the core behaviour of file-infecting malware: self-replication without requiring user interaction beyond the initial execution.

**Key concepts illustrated:**
- How malware propagates across a filesystem by copying itself.
- Why execution of untrusted scripts in uncontrolled environments is dangerous.
- The role of application whitelisting and least-privilege execution in containing replication.

> **Note:** All execution was performed in an isolated virtual machine with no network access or shared folders. No systems outside the sandbox were affected.

---

### 3. Port Scanner (`PortScanner.py`)
A Python TCP port scanner built using the `socket` library. It iterates over ports 1–1024 on a target IP, attempts a TCP connection to each, and reports which ports are open. A short timeout (0.1 s) keeps scanning practical.

**Concepts demonstrated:**
- How attackers and defenders use port scanning for reconnaissance and asset discovery.
- The difference between open, closed, and filtered ports.
- Why limiting open ports and implementing firewall rules reduces the attack surface.

---

### 4. File Hashing, Integrity, and Authentication (`Hashing&Encryption.py`)
A Python script applying multiple cryptographic techniques to a sample message:

- **MD5** — fast 128-bit hash; used here to show why speed is a liability for security hashing.
- **SHA-256** — 256-bit hash; the current standard for integrity verification.
- **RIPEMD-160** — 160-bit hash used in specialised contexts (e.g. cryptocurrency).
- **HMAC-SHA-256** — keyed hash that proves both integrity *and* the identity of the sender.
- **3DES (EAX mode)** — symmetric encryption with a randomly generated 192-bit key; the script encrypts and then decrypts to demonstrate the full confidentiality cycle.

---

### 5. File Integrity Verification with OpenSSL on Kali Linux (`Cryptography Basics`)
A hands-on terminal lab demonstrating how hashing and encryption protect files at rest:

- Generated MD5 and SHA-256 hashes of a file, then simulated tampering and verified the hashes changed — illustrating tamper detection.
- Encrypted a file using AES-256-CBC with OpenSSL, confirmed the ciphertext was unreadable, then decrypted and verified the output matched the original.

---

### 6. Remote Access via SSH (`Remote Access Using SSH`)
Connected to a Metasploitable 2 VM from Kali Linux using SSH, including the use of legacy key-algorithm flags (`-o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedAlgorithms=+ssh-rsa`) required because modern OpenSSH deprecates the older RSA signature scheme used by Metasploitable.

**Key learning:** Legacy systems on real networks often require explicit negotiation of older algorithms — understanding *why* a connection fails and which flags resolve it is a practical administrative skill.

---

## Reflection

Working through these labs shifted my understanding of network security from conceptual to operational. Each exercise required me to think from two angles simultaneously: the attacker trying to gain a foothold, and the defender trying to limit the blast radius.

The malware delivery and reverse-connection lab was the most striking. Seeing a reverse shell established and watching the packets flow from the victim outward to the attacker in Wireshark made the limitation of inbound-only firewall rules immediately obvious. A rule that blocks port 4444 inbound does nothing if the victim initiates the connection. That single observation reshaped how I think about defence-in-depth: perimeter controls matter, but endpoint detection and egress filtering matter just as much.

The self-replicating virus script (`ThreatAttack.py`) was deliberately simple, but that simplicity was the point. Replication does not require sophistication — a handful of lines of Python and the `shutil` module are enough to fill a directory. The defence is equally straightforward: least-privilege execution, application whitelisting, and monitoring for unexpected file-creation events.

The cryptography labs reinforced the layered nature of data protection. Hashing proves integrity. HMAC adds authentication. Encryption adds confidentiality. None of these alone is sufficient; real-world security requires all three, applied at the right layer.

The SSH lab highlighted something I had not considered before: modern security defaults can break access to legacy systems, and knowing how to safely negotiate downgraded algorithms — while understanding the risk of doing so — is a practical skill for anyone working in IT support or infrastructure.

Overall, this unit gave me a hands-on foundation in both offensive techniques (port scanning, malware simulation, reverse shells) and defensive countermeasures (cryptographic integrity, access control, network segmentation). That dual perspective is what I want to carry forward as I develop further in cybersecurity.
