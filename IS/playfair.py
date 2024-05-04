import numpy as np
matrix = np.zeros((5,5))
print(matrix)
plain_text = 'COMMUNICATE'

# unique_char = ''.join(set(plain_text))
# print(unique_char)
# Splitting the plaintext into digraphs
diagraphs = []
i = 0
while i < len(plain_text):
    diagraph = []
    if i == len(plain_text) - 1:  
        diagraph.append(plain_text[i])
        diagraph.append('X')
        i += 1
    elif plain_text[i] != plain_text[i+1]:  
        diagraph.append(plain_text[i])
        diagraph.append(plain_text[i+1])
        i += 2
    else:  
        diagraph.append(plain_text[i])
        diagraph.append('X')
        i += 1
    diagraphs.append(diagraph)

print(diagraphs)


def create_playfair_matrix(key):
    key = key.replace(" ", "").upper()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    key_set = set(key)
    remaining_chars = [char for char in alphabet if char not in key_set]
    key += ''.join(remaining_chars[:25 - len(key)])
    return np.array([list(key[i:i+5]) for i in range(0, 25, 5)])

keyword = 'ARADHYA'
matrix = create_playfair_matrix(key=keyword)
print(matrix)