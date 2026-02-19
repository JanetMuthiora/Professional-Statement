# install the packages required
# py -m pip install pycryptodome
import hashlib  # imports hash functions (MD5, SHA-256, RIPEMD-160 via new)
import hmac #imports keyed hashing method
from Crypto.Cipher import DES3 # imports Triple DES encryption algorithm
from Crypto.Random import get_random_bytes #imports for secure random key generation

# Encode the message string to UTF-8 cryptographic functions operate on bytes
message = "This is a Cryptography excercise".encode('utf-8')

# MD5 Hash method produces 128-bit hash which is fast bit not collision resistant
md5 = hashlib.md5(message).hexdigest()

# SHA256 hash method produces a 256-bit hash which is stronger and widely used for integrity checks
sha256 = hashlib.sha256(message).hexdigest()

#RIPEMD hash method produces a 160-bit hash used in specific cryptocurrency security context
ripemd = hashlib.new('ripemd160', message).hexdigest()

# HMAC hash method outputs a keyed hash and ensures both integrity and authenticity
key = "your-secret-key".encode('utf-8')
hmac_sha256 = hmac.new(key, message, hashlib.sha256).hexdigest()

# DES3 symmetric cryptographic algorithm encrypts with  a 192-bit key and ciphertext
key_DES3 = get_random_bytes(24)
cipher = DES3.new(key_DES3, DES3.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(message)


print("MD5 hash:", md5)
print("SHA-256 hash:", sha256)
print("RIPEMD-160 hash:", ripemd)
print("HMAC-SHA-256:", hmac_sha256)
print("DES3 Key:", key_DES3.hex())

print("DES3 Encrypted message:", ciphertext.hex())

# DES3 symmetric cryptographic algorithm decrypts ciphertext 
cipher = DES3.new(key_DES3, DES3.MODE_EAX, nonce=cipher.nonce)
plaintext = cipher.decrypt(ciphertext)
print("Plain message:", plaintext)

