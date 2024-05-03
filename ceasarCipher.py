# Setting the character mapping for uppercase alphabets
mapping = {}
for i in range(26):
    mapping[chr(65+i)] = i;

print(mapping)

# Ceasar cipher 
def ceasar_cipher(plain_text,shift):
    ciphered_text = ''
    for char in plain_text :
        mapped_value = (mapping[char] + shift) % 26
        ciphered_text += chr(65 + mapped_value)
    return ciphered_text

def ceasar_decipher(plain_text,shift):
    ciphered_text = ''
    for char in plain_text :
        mapped_value = (mapping[char] - shift) % 26
        ciphered_text += chr(65 + mapped_value)
    return ciphered_text
        

plain_text = 'ARADHYA'
print('Original Plaintext : ',plain_text)

ciphered_text = ceasar_cipher(plain_text=plain_text,shift=3)

print('Ciphered Text : ',ciphered_text)

decihered_text = ceasar_decipher(plain_text=ciphered_text,shift=3)
print('Deciphered Text : ',decihered_text)