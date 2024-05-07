mapping = {}
for i in range(26):
    mapping[chr(65+i)] = i;

print(mapping) 

def key_padding(plain_text,key):
    if len(key) < len(plain_text):
        i = 0
        while len(key) != len(plain_text):
            key += key[i]
            i += 1
    return key

def vernam_cipher(plain_text,key):
    ciphered_text = ''
    for char1,char2 in zip(plain_text,key):
       mapping_value1 = mapping[char1]
       mapping_value2 = mapping[char2]
       xor_value = (mapping_value1 ^ mapping_value2)
       if xor_value > 26:
           xor_value -= 26
       
       ciphered_text += chr(xor_value + 65)
    return ciphered_text 

def vernam_decipher(plain_text,key):
    ciphered_text = ''
    for char1,char2 in zip(plain_text,key):
       mapping_value1 = mapping[char1]
       mapping_value2 = mapping[char2]
       xor_value = (mapping_value1 ^ mapping_value2)
       if xor_value > 26:
           xor_value -= 26
       
       ciphered_text += chr(xor_value + 65)
    return ciphered_text 


print(2^18)
plain_text = 'OAK'
plain_text = plain_text.replace(' ','')
print(plain_text)
key = 'SON'
key = key_padding(plain_text,key)
print(key)
ciphered_text = vernam_cipher(plain_text,key)
print(ciphered_text)
deciphered_text = vernam_decipher(ciphered_text,key)
print(deciphered_text)