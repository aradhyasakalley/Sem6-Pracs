mapping = {}
for i in range(26):
    mapping[chr(65+i)] = i

print(mapping)

def ceasar_cipher(text,shift):
    ciphered_text = ''
    for char in text :
        if char.isupper():
            chiphered_value = (mapping[char] + shift ) % 26 
            ciphered_text += chr(65 + chiphered_value)
        elif char.islower():
            chiphered_value = (mapping[char.upper()] + shift ) % 26 
            ciphered_text += chr(65 + chiphered_value)
            
    return ciphered_text

def ceasar_decipher(text,shift):
    deciphered_text = ''
    for char in text :
        if char.isupper():
            dechiphered_value = (mapping[char] - shift ) % 26 
            deciphered_text += chr(65 + dechiphered_value)
        elif char.islower():
            dechiphered_value = (mapping[char.upper()] - shift ) % 26 
            deciphered_text += chr(65 + dechiphered_value)
            
    return deciphered_text

plain_text = 'aradhya'
ciphered_text = ceasar_cipher(plain_text,3)
print(ciphered_text)
deciphered_text = ceasar_decipher(ciphered_text,3)
print(deciphered_text)