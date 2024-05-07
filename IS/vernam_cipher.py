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

def vernam_cipher(plain_text, key):
    ciphered_text = ''
    for char1, char2 in zip(plain_text, key):
        mapping_value1 = mapping[char1.upper()]
        mapping_value2 = mapping[char2.upper()]
        encrypted_value = (mapping_value1 + mapping_value2) % 26  
        ciphered_text += chr(encrypted_value + 65)
    return ciphered_text 

def vernam_decipher(ciphered_text, key):
    deciphered_text = ''
    for char1, char2 in zip(ciphered_text, key):
        mapping_value1 = mapping[char1.upper()]
        mapping_value2 = mapping[char2.upper()]
        decrypted_value = (mapping_value1 - mapping_value2) % 26  
        deciphered_text += chr(decrypted_value + 65)
    return deciphered_text 



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