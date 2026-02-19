# install the packages required
# py -m pip install pycryptodome
import hashlib
import hmac
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

message = "COIT12202(HT2, 2023) Network Security Concepts Week 3 Hash algorithms".encode('utf-8')

# MD5 Hash method
md5 = hashlib.md5(message).hexdigest()

# SHA256 hash method
sha256 = hashlib.sha256(message).hexdigest()

#RIPEMD hash method
ripemd = hashlib.new('ripemd160', message).hexdigest()

# HMAC hash method
key = "your-secret-key".encode('utf-8')
hmac_sha256 = hmac.new(key, message, hashlib.sha256).hexdigest()

# DES3 symmetric cryptographic algorithm
key_DES3 = get_random_bytes(24)
cipher = DES3.new(key_DES3, DES3.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(message)


print("MD5 hash:", md5)
print("SHA-256 hash:", sha256)
print("RIPEMD-160 hash:", ripemd)
print("HMAC-SHA-256:", hmac_sha256)
print("DES3 Key:", key_DES3.hex())

print("DES3 Encrypted message:", ciphertext.hex())

cipher = DES3.new(key_DES3, DES3.MODE_EAX, nonce=cipher.nonce)
plaintext = cipher.decrypt(ciphertext)
print("Plain message:", plaintext)

