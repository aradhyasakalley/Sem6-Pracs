mapping = {}
for i in range(26):
    mapping[chr(65+i)] = i

# Generates a sequence based on the mapping of char in key
def sequence_generator(key):
    sequence = []
    for char in key:
        sequence.append(mapping[char])
    return sequence

# Basically returns the column index to pick next
def column_choice(sequence):
    min_value = min(sequence)
    min_index = sequence.index(min_value)
    sequence[min_index] = 100
    return min_index

# Appending columnwise values based on sequence
def columnar_cipher(matrix, sequence, n):
    ciphered_text = ''
    if n > 0:
        min_index = column_choice(sequence)
        for i in range(len(matrix)):
            if matrix[i][min_index] != 'X':
                ciphered_text += matrix[i][min_index]
        return ciphered_text + columnar_cipher(matrix, sequence, n - 1)
    else:
        return ''

# Generating the transposition matrix nxn
def columnar_transposition_matrix(plain_text,n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            index = i*n + j
            if index < len(plain_text):
                row.append(plain_text[index])
            else:
                row.append('X')
        matrix.append(row)
    return matrix


plain_text = 'GEEKS FOR GEEKS'
key = 'HACK'
n = len(key)
matrix = columnar_transposition_matrix(plain_text,n)
print(matrix)
sequence = sequence_generator(key)
print(sequence)
ciphered_text = columnar_cipher(matrix,sequence,n)
print(ciphered_text.replace(' ',''))