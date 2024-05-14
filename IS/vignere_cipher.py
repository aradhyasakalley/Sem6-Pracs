# Mapping for assigning numbers to chars ex. A : 0 , B: 1 etc
mapping = {}
for i in range(26):
    mapping[chr(65 + i)] = i 
print(mapping)

# Key padding by repeating the key to make key as same length as plaintext 
# If key = KEY and plain text = APPLE, key = KEYKE 
def key_padding(plain_text,key):
    if len(key) < len(plain_text):
        i = 0
        while len(key) != len(plain_text):
            key += key[i]
            i += 1
    return key

# Cipher and decipher functions differ in just + and - of mapped values
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
        
# Handle the uppercase and lowercase by either converting all to uppercase or use seperate mapping for both
plain_text = 'Thirteen'
plain_text = plain_text.upper()
print('Plain text is : ',plain_text)
key = 'Security'
key = key_padding(plain_text,key)
key = key.upper()
print('The key is : ',key)
ciphered_text = vignere_cipher(plain_text,key)
print('Ciphered text is: ',ciphered_text)
deciphered_text = vignere_decipher(ciphered_text,key)
print('Deciphered text: ',deciphered_text)