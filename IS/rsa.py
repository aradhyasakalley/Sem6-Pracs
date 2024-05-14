import math 

def private_key(e,phi):
    d = 2
    while d < phi:
        if (d*e)%phi == 1:
            break
        else:
            d += 1
    return d

def public_key(phi):
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

# make sure to pick a large prime number like 1013,1019 
p,q = 1013,1019
message = 44
n = p*q
phi = (p-1)*(q-1)

e = public_key(phi)
d = private_key(e,phi)

ciphered_text = rsa_encrypt(message,e,n)
deciphered_text = rsa_decrypt(ciphered_text,d,n)

print('Original message: ',message)
print('Ciphered text: ',ciphered_text)
print('Deciphered text: ',deciphered_text)