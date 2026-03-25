
Symmetric Encryption with OpenSSL (DES & AES)
Skill area: Applied Cryptography | Tools: OpenSSL, xxd, bash  
Algorithms covered: DES-ECB, AES-128-CBC, AES-128-CTR
---
What I did
Hands-on encryption lab using OpenSSL from the command line, covering block cipher fundamentals with DES and AES across different modes.
---
Skills demonstrated
Created binary-exact plaintext files using Python's `sys.stdout.buffer.write` to avoid shell encoding issues
Encrypted files using DES in ECB mode with the OpenSSL legacy provider
Encrypted files using AES-128 in CBC mode with a randomly generated key and IV
Inspected raw ciphertext using `xxd` to read hex output
Diagnosed and corrected real CLI errors (missing flags, typos, incomplete arguments)
Understood PKCS#7 padding behaviour — 24-byte plaintext padded to 32 bytes under AES-CBC
---
Key concepts learned
Concept	Notes
DES block size	8 bytes — plaintext processed in 8-byte chunks
ECB weakness	Identical plaintext blocks → identical ciphertext blocks (pattern leakage)
AES block size	16 bytes — plaintext padded to next multiple of 16
CBC mode	Each block XOR'd with previous ciphertext before encryption; requires IV
Key vs passphrase	`-k` derives a key from a passphrase; `-K` takes a raw hex key directly
`-provider legacy`	Required in OpenSSL v3+ to enable deprecated algorithms like DES
`echo` vs Python	`echo` appends a newline (`\n`); Python's `sys.stdout.buffer.write` does not
---
Commands used
Create exact-byte plaintext
```bash
python3 -c "import sys; sys.stdout.buffer.write(b'A'*24)" > plain.txt
```
Encrypt with DES-ECB (legacy provider required)
```bash
openssl enc -des-ecb -provider legacy -provider default \
  -K <hex_key> -nosalt -in plain.txt -out cipher_des.bin
```
Generate a random 128-bit key
```bash
openssl rand -hex 16
```
Encrypt with AES-128-CBC
```bash
openssl enc -aes-128-cbc \
  -K aca5f5d534d2c3ed49068a19162e7f0f \
  -iv aca5f5d534d2c3ed49068a19162e7f0f \
  -in plain.txt -out cipher_aes.bin
```
Inspect ciphertext in hex
```bash
xxd cipher_aes.bin
```
---
Observations
DES ciphertext of 24-byte input = 24 bytes (exact block fit, no padding)
AES-CBC ciphertext of 24-byte input = 32 bytes (padded from 24 → 32)
ECB mode reveals patterns: three identical plaintext blocks produce three identical ciphertext blocks
Reusing the key as the IV (as done here) is acceptable for learning but insecure in practice — IV should always be random and unique per encryption
---
Errors encountered & fixed
Error	Cause	Fix
`enc: Use -help for summary`	Missing `-` before cipher name; `-out` had no space	`-aes-128-ctr`, `-out ciphertext.bin`
`No such file or directory`	Filename typo (`plaintext.txt` vs `plaintest.txt`)	Match filename exactly
`xxd: cipher_: No such file or directory`	Incomplete filename in xxd command	`xxd cipher_aes.bin`
Wrong file encrypted	`-in plain.txt` used instead of `-in plaintest.txt`	Always verify `-in` filename
