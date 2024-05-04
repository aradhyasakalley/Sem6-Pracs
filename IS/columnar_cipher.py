mapping = {}
for i in range(26):
    mapping[chr(65+i)] = i

def column_choice(sequence):
    min_element = min(sequence)
    min_index = sequence.index(min_element)
    sequence[min_index] = 100
    return min_index

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

def sequence_generator(key):
    sequence = []
    for char in key:
        sequence.append(mapping[char])
    # sequence.sort()
    return sequence

def columnar_transposition_matrix(plain_text, n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            index = i * n + j
            if index < len(plain_text):
                row.append(plain_text[index])
            else:
                row.append('X')  # Add padding character if the index goes out of range
        matrix.append(row)
    return matrix

plain_text = 'Aradhya Sakalley'
key = 'HACK'
n = len(key)
matrix = columnar_transposition_matrix(plain_text, n)
sequence = sequence_generator(key)
print("Ciphered text:", columnar_cipher(matrix, sequence, n).replace(' ',''))
