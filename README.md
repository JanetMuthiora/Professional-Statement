# Applied Cryptography

Hands-on cryptography labs and exercises completed as part of a Bachelor of Information Technology at Central Queensland University. This branch covers symmetric encryption, asymmetric (public-key) cryptography, hashing, and message authentication — all implemented in Python and via the OpenSSL command-line tool.

---

## Key Objectives

1. Understand core cryptographic primitives: hashing, symmetric encryption, and asymmetric encryption.
2. Apply block cipher modes (ECB, CBC, CTR) and reason about their security trade-offs.
3. Implement cryptographic algorithms in Python using industry-standard libraries.
4. Use OpenSSL from the command line to encrypt, decrypt, and inspect ciphertext.
5. Diagnose and fix real-world CLI and library errors encountered during hands-on work.

---

## Tools and Technologies

| Category | Tools / Libraries |
|---|---|
| Language | Python 3 |
| CLI Encryption | OpenSSL (v3+, including legacy provider for DES) |
| Python Crypto Library | `pycryptodome` (`Crypto.Cipher`, `Crypto.Random`) |
| Hashing | `hashlib` (MD5, SHA-256, RIPEMD-160), `hmac` |
| Symmetric Ciphers | DES-ECB, AES-128-CBC, AES-128-CTR, AES-256-CBC, 3DES (EAX mode) |
| Hex Inspection | `xxd` |
| Environment | Kali Linux (terminal), Python virtual environment |

---

## Projects and Labs

### 1. File Hashing, Integrity, and Authentication (`Hashing&Encryption.py`)
A Python script that demonstrates four cryptographic techniques applied to a sample message:

- **MD5** — 128-bit hash; fast but not collision-resistant. Used to illustrate why stronger algorithms are preferred.
- **SHA-256** — 256-bit hash; the standard for integrity verification in modern systems.
- **RIPEMD-160** — 160-bit hash; used in specific contexts such as cryptocurrency address generation.
- **HMAC-SHA-256** — Keyed hash that provides both integrity and authenticity. A secret key is combined with the message so that only parties who know the key can verify the hash.
- **3DES (Triple DES, EAX mode)** — Symmetric encryption using a randomly generated 192-bit key. The script encrypts a plaintext message and then decrypts it, demonstrating the full confidentiality cycle.

**Key concept demonstrated:** Hashing proves a message has not been altered; HMAC additionally proves *who* sent it; encryption makes the message unreadable without the key.

---

### 2. Symmetric Encryption with OpenSSL — DES and AES (`Symmetric-Encryption-OpenSSL.md`)
A command-line lab using OpenSSL to explore block cipher fundamentals:

- **DES-ECB** — Encrypted a 24-byte plaintext (exactly 3 DES blocks). Observed that identical plaintext blocks produce identical ciphertext blocks, demonstrating ECB's pattern-leakage weakness.
- **AES-128-CBC** — Encrypted the same plaintext with a randomly generated 128-bit key and IV. Observed PKCS#7 padding: 24-byte input padded to 32 bytes.
- **AES-128-CTR** — Stream-cipher mode; no padding required.
- Used `xxd` to inspect raw ciphertext in hex and verify byte counts.
- Diagnosed and resolved real CLI errors: missing flags, filename typos, incomplete arguments, and the OpenSSL v3 legacy-provider requirement for DES.

**Key concepts learned:**

| Concept | Detail |
|---|---|
| DES block size | 8 bytes |
| AES block size | 16 bytes |
| ECB weakness | Identical plaintext blocks produce identical ciphertext blocks |
| CBC chaining | Each block XOR'd with previous ciphertext before encryption; requires an IV |
| `-K` vs `-k` | `-K` takes a raw hex key; `-k` derives a key from a passphrase |
| OpenSSL v3 legacy provider | Required to enable deprecated algorithms such as DES |

---

### 3. Public-Key Cryptography (`PublicKeyCryptography.py`)
Exploration of asymmetric cryptography concepts implemented in Python, covering key-pair generation, encryption with a public key, and decryption with the corresponding private key — demonstrating how confidentiality can be achieved without sharing a secret key in advance.

---

## Reflection

Working through these labs gave me a practical, ground-level understanding of how cryptography functions in real systems — not just as theory, but as concrete command-line operations and executable code.

The OpenSSL DES/AES lab was particularly valuable: seeing ECB mode expose plaintext patterns in ciphertext made the weakness visceral rather than abstract. Padding behaviour under AES-CBC (24 bytes in, 32 bytes out) made block-size mechanics click in a way that textbook diagrams never quite managed.

The Python hashing script reinforced how thin the line is between integrity (hash) and authentication (HMAC). MD5's speed is precisely what makes it unsuitable for security — it is too easy to brute-force. Graduating from MD5 to SHA-256 to HMAC-SHA-256 within the same script illustrated the layered nature of cryptographic guarantees.

Encountering and fixing real OpenSSL CLI errors — wrong flag order, missing provider flags, filename mismatches — was an unplanned but important lesson: cryptographic tools fail loudly and specifically, which is by design. Learning to read those error messages carefully is part of becoming competent with these tools.

Going forward, I want to deepen my understanding of asymmetric cryptography (RSA, elliptic curves) and how TLS brings symmetric and asymmetric techniques together in practice.
