# install required packages packages
py -m pip install seccure


import os #imports operating system functions
import random #imports random numner generation
import hashlib, secrets, binascii #imports hash algotrithims, cryptographically secure random values, converts boinary to hexadecimals
import rsa #imports RSA cryptography library
import seccure  #imports the ECC cryptography library

# UTF-8 converts the message into bytes 
message = "Public Key Cryptography excercise".encode('utf-8')


"""
Encryption and decryption using RSA
"""
# generate RSA key with 2048 bits considered secure for most applications the public key is used to encrypt and private used to decrypt

publickey, privatekey = rsa.newkeys(2048)
            
# convert RSA key from bytes to string 
private_key = privatekey.save_pkcs1().decode("utf-8")
public_key = publickey.save_pkcs1().decode("utf-8")
print("RSA private key: ", private_key)
print("RSA public key: ", public_key)

# reconstruct RSA object from the stored text format
privkey = rsa.PrivateKey.load_pkcs1(private_key.encode("utf-8"))
pubkey = rsa.PublicKey.load_pkcs1(public_key.encode("utf-8"))

# encrypt message using public key
crypto = rsa.encrypt(message, pubkey)
print("RSA encrypted message: 0x"+crypto.hex())

# decrypt message using private key
message = rsa.decrypt(crypto, privkey)
print("RSA decrypted message: ", message)

"""
Digitial signature using RSA
"""
# hash the message using SHA-256, sign the signature using private key
signature = rsa.sign(message, privkey, 'SHA-256')
try:
    # verify the signature using public key
    rsa.verify(message, signature, pubkey)
except rsa.pkcs1.VerificationError:
    print('Verification failed')
else:
    print('Verification succeed')
print('-----------------RSA test done--------------')    

# a salt to generate a unique private key
private_key_phrase = b'my private key'

# Parameters of  Elliptic Curve Cryptography
curve = seccure.Curve.by_name('secp160r1')
print("ECC a: ", hex(curve.a))
print("ECC b: ", hex(curve.b))
print("ECC prime: ", hex(curve.m))
print("ECC order: ", hex(curve.order))
print("ECC base x: ", hex(curve.base.x))
print("ECC base y: ", hex(curve.base.y))
print("ECC private key: ", hex(curve.passphrase_to_privkey(private_key_phrase).e))

"""
Encryption and decryption using ECC
"""
# generate key pair
public_key = seccure.passphrase_to_pubkey(private_key_phrase, curve='secp160r1')
public_key_bytes = public_key.to_string(0)

# encrypt using public key
ciphertext = seccure.encrypt(message, public_key_bytes)
print("ECC encrypted message: 0x"+ciphertext.hex())

# decrypt using private key
text = seccure.decrypt(ciphertext, private_key_phrase)
print("ECC decrypted message: ", text)

"""
Digitial signature using ECC
"""
signature = seccure.sign(message, private_key_phrase, curve='secp160r1')
print("ECC signature: 0x"+signature.hex())

verified = seccure.verify(message, signature, public_key_bytes, curve='secp160r1')
if verified:
    print('ECC verification succeed')
else:
    print('ECC verification failed')
print('-----------------ECC test done--------------')  
