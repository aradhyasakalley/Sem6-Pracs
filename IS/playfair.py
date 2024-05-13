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

# Removing duplicates from key
def unique_key(key):
    u_key = set()
    res = ''
    for char in key:
        if char not in u_key:
            u_key.add(char)
            res += char
    return res

# Gnerating the playfair matrix
def playfair_matrix(key):
    key = key.upper().replace('J', 'I') 
    matrix = [['' for _ in range(5)] for _ in range(5)]  
    
    key_index = 0
    for i in range(5):
        for j in range(5):
            if key_index < len(key):
                matrix[i][j] = key[key_index]
                key_index += 1
    
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' 
    for letter in alphabet:
        if letter not in key:
            for row in matrix:
                if '' in row:
                    row[row.index('')] = letter
                    break
            else:
                break
    return matrix
  
# Finding position of char in matrix  
def find_position(matrix,char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return (i,j)


# Encrypting based on the 3 rules
def playfair_encryption(diagraphs, matrix):
    for diagraph in diagraphs:
        x1, y1 = find_position(matrix, diagraph[0])
        x2, y2 = find_position(matrix, diagraph[1])

        if x1 == x2:
            diagraph[0] = matrix[x1][(y1+1)%5]
            diagraph[1] = matrix[x1][(y2+1)%5]
        elif y1 == y2:
            diagraph[0] = matrix[(x1+1)%5][y1]
            diagraph[1] = matrix[(x2+1)%5][y1]
        else:
            diagraph[0] = matrix[x1][y2]
            diagraph[1] = matrix[x2][y1]

    return diagraphs

def playfair_decryption(diagraphs, matrix):
    for diagraph in diagraphs:
        x1, y1 = find_position(matrix, diagraph[0])
        x2, y2 = find_position(matrix, diagraph[1])

        if x1 == x2:
            diagraph[0] = matrix[x1][(y1-1)%5]
            diagraph[1] = matrix[x1][(y2-1)%5]
        elif y1 == y2:
            diagraph[0] = matrix[(x1-1)%5][y1]
            diagraph[1] = matrix[(x2-1)%5][y1]
        else:
            diagraph[0] = matrix[x1][y2]
            diagraph[1] = matrix[x2][y1]

    return diagraphs

plain_text = 'INSTRUMENTSZ'
print('Plaintext : ',plain_text)
key = 'MONARCHY'
diagraphs = get_diagraphs(plain_text)
print(diagraphs)

u_key = unique_key(key)
matrix = playfair_matrix(u_key)

diagraphs_encrypted = playfair_encryption(diagraphs, matrix)
print(diagraphs_encrypted)

encrypted_text = ''
for diagraph in diagraphs_encrypted:
    encrypted_text += diagraph[0]
    encrypted_text += diagraph[1]
    
diagraphs_encrypted = playfair_decryption(diagraphs_encrypted, matrix)
print(diagraphs_encrypted)
decrypted_text = ''

for diagraph in diagraphs_encrypted:
    decrypted_text += diagraph[0]
    decrypted_text += diagraph[1]
print('Decrypted text : ',decrypted_text)