# Function of cipher and decipher is the same
# In Vernam cipher both the key and plaintext have to be same length (so no padding needed)

def vernam_cipher(plain_text,key):
    ciphered_text = ''
    for i in range(len(plain_text)):
        xor_value = chr(ord(plain_text[i]) ^ ord(key[i]))
        ciphered_text += xor_value
    return ciphered_text
    

plain_text = 'Thirteen'
plain_text = plain_text.replace(' ','')
print('Plain text is : ',plain_text)
key = 'Security'
print('The key is : ',key)
ciphered_text = vernam_cipher(plain_text,key)
print('Ciphered text is: ',ciphered_text)
deciphered_text = vernam_cipher(ciphered_text,key)
print('Deciphered text: ',deciphered_text)