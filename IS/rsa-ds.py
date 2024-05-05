import hashlib

def rsa_encryption(message_hash):
    return (message_hash ** e) % n

def rsa_decryption(signature):
    return (signature ** d) % n

def md_generator(message):
    return int(hashlib.sha1(message.encode()).hexdigest(), 16)


p = 1013
q = 1019
n = p * q
phi = (p - 1) * (q - 1)
e = 13

# Calculate d using modular multiplicative inverse of e mod phi
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 if x1 >= 0 else x1 + m0

d = mod_inverse(e, phi)

public = (e, n)
private = (d, n)

message = 'hello there'
md1 = md_generator(message)
digital_signature = rsa_encryption(md1)
print("Original Message Hash:", md1)
print("Digital Signature:", digital_signature)

# Now, recipient verifies the digital signature
md2 = md_generator(message)
decrypted_md = rsa_decryption(digital_signature)
print("Received Message Hash:", md2)
print("Decrypted Message Hash:", decrypted_md)

if md2 == decrypted_md:
    print("Digital Signature Verified! The message is authentic.")
else:
    print("Digital Signature Verification Failed! The message may have been tampered with.")
