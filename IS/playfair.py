import numpy as np
# Splitting the plaintext into digraphs
def get_diagraphs(plain_text):
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
    return diagraphs


def playfair_matrix(key):
    matrix = [['' for _ in range(5)] for _ in range(5)]
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Exclude 'J'
    key_index = 0

    # Fill the matrix with unique characters from the key
    
    return matrix
    


plain_text = 'COMMUNICATE'
key = 'MONARCHY'
diagraphs = get_diagraphs(plain_text)
matrix = playfair_matrix(key)
print(matrix)
print(diagraphs)