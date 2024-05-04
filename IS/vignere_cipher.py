mapping = {}
for i in range(26):
    mapping[chr(65 + i)] = i  # Uppercase letters
    mapping[chr(97 + i)] = i  # Lowercase letters


print(mapping)

def key_padding(plain_text,key):
    if len(key) < len(plain_text):
        i = 0
        while len(key) != len(plain_text):
            key += key[i]
            i += 1
    return key

def vignere_cipher(plain_text,key):
    ciphered_text = ''
    for char1,char2 in zip(plain_text,key) :
        mapped_value1 = mapping[char1]
        mapped_value2 = mapping[char2]
        ciphered_value = (mapped_value1 + mapped_value2) % 26
        ciphered_text += chr(ciphered_value+65)
    return ciphered_text

def vignere_decipher(plain_text,key):
    deciphered_text = ''
    for char1,char2 in zip(plain_text,key):
        mapped_value1 = mapping[char1]
        mapped_value2 = mapping[char2]
        deciphered_value = (mapped_value1 - mapped_value2) % 26
        deciphered_text += chr(deciphered_value+65)
    return deciphered_text
        

plain_text = 'ARADHYA SAKALLEY'
plain_text = plain_text.replace(' ','')
print(plain_text)
key = 'BEST'
key = key_padding(plain_text,key)
print(key)
ciphered_text = vignere_cipher(plain_text,key)
print(ciphered_text)
deciphered_text = vignere_decipher(ciphered_text,key)
print(deciphered_text)