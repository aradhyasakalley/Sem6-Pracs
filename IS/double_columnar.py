mapping = {}
for i in range(26):
    mapping[chr(65+i)] = i
# print(mapping)

# Generating sequence of picking column to add
def sequence_gen(key):
    sequence = []
    for char in key:
        sequence.append(mapping[char])
    return sequence

# Creating the columnar matrix 
def columnar_matrix(n,plain_text):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            index = i*n + j
            if index < len(plain_text):
                row.append(plain_text[index])
            else:
                row.append('@')
        matrix.append(row)
    return matrix        

# Picking the column to start using as per teh sequence
def column_choice(sequence):
    min_value = min(sequence)
    min_index = sequence.index(min_value)
    sequence[min_index] = 100
    return min_index

# Recursively getting the ciphered text
def columnar_cipher(matrix,sequence,n):    
    ciphered_text = ''
    if n > 0:
        min_index = column_choice(sequence)
        for i in range(len(matrix)):
            ciphered_text += matrix[i][min_index]
        return ciphered_text + columnar_cipher(matrix,sequence,n-1)
    else:
        return ''

# Decipher (reading columns based on the same sequence)
def columnar_decipher(sequence, ciphered_text, n):
    matrix = [['' for _ in range(n)] for _ in range(n)]
    text_index = 0
    deciphered_text = ''
    while n > 0:
        min_index = column_choice(sequence)
        for i in range(len(matrix)):
            if text_index < len(ciphered_text):
                matrix[i][min_index] = ciphered_text[text_index]
                text_index += 1
        n -= 1
        
    for row in matrix:
        for item in row:
            deciphered_text += item
    
    return deciphered_text
            
# Using first key to cipher 
plain_text = 'WEAREDISCOVEREDFLEEATONCE'
key = 'ZEBRAS'
n = len(key)
sequence = sequence_gen(key)
print(sequence)
matrix = columnar_matrix(n,plain_text)
print('Columnar matrix: ',matrix)
ciphered_text = columnar_cipher(matrix,sequence,n)
print('Ciphered text:',ciphered_text)

# Using second key to cipher and creating the new matrix
key2 = 'STRIPE'
n = len(key2)
sequence2 = sequence_gen(key2)
print(sequence2)
matrix2 = columnar_matrix(n,ciphered_text)
print('Columnar matrix 2: ',matrix2)
ciphered_text2 = columnar_cipher(matrix2,sequence2,n)
print(ciphered_text2)


# Deciphering using the second key
sequence2 = sequence_gen(key2)
deciphered_text2 = columnar_decipher(sequence2, ciphered_text2, n)
print('Deciphered text: ',deciphered_text2.replace('@',''))

# Deciphering using the first key
sequence = sequence_gen(key)
deciphered_text1 = columnar_decipher(sequence, deciphered_text2, n)
print('Deciphered text: ',deciphered_text1.replace('@',''))