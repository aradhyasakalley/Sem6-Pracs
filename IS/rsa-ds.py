import math 
import hashlib

# Note that in RSA the encryption is done using the public key (e) and decrytion using the private key (d) but in RSA DS its the opposite.

def private_key(e,phi):
    d = 2
    while d < phi:
        if (d*e)%phi == 1:
            break
        else:
            d += 1
    return d

def public_keyy(phi):
    e = 2
    while e < phi:
        if math.gcd(e,phi) == 1:
            break
        else:
            e += 1
    return e

def rsa_encrypt(message,e,n):
    return pow(message,e)%n

def rsa_decrypt(message,d,n):
    return pow(message,d)%n

def sha1_hash(message):
    message = str(message)
    return int(hashlib.sha1(message.encode()).hexdigest()[:5],16)

# make sure to pick a large prime number like 1013,1019 
p,q = 1013,1019
message = 16
n = p*q
phi = (p-1)*(q-1)
e = public_keyy(phi)
d = private_key(e,phi)

md1 = sha1_hash(message)
print(md1)
dig_sign = rsa_encrypt(md1,d,n)
print(dig_sign)

# tampering the message to test error
# message = 11

# sending the digital signature and original message to b 
md2 = sha1_hash(message)
print(md2)
dig_sign_decrypted = rsa_decrypt(dig_sign,e,n)
print(dig_sign_decrypted)

if dig_sign_decrypted == md2:
    print('Message recieved successfully!')
else:
    print('Message was tampered with')