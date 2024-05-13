mapping = {}
for i in range(26):
    mapping[chr(65+i)] = i
print(mapping)


def sequence_gen(key):
    sequence = []
    for char in key:
        sequence.append(mapping[char])
    return sequence


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
        
def column_choice(sequence):
    min_value = min(sequence)
    min_index = sequence.index(min_value)
    sequence[min_index] = 100
    return min_index

def columnar_cipher(matrix,sequence,n):    
    ciphered_text = ''
    if n > 0:
        min_index = column_choice(sequence)
        for i in range(len(matrix)):
            ciphered_text += matrix[i][min_index]
        return ciphered_text + columnar_cipher(matrix,sequence,n-1)
    else:
        return ''

def columnar_decipher(sequence, ciphered_text, n):
    matrix = [['' for _ in range(n)] for _ in range(n)]
    text_index = 0
    deciphered_text = ''
    while n > 0:
        min_index = column_choice(sequence)
        print(min_index)
        for i in range(len(matrix)):
            if text_index < len(ciphered_text):
                matrix[i][min_index] = ciphered_text[text_index]
                text_index += 1
        n -= 1
        
    for row in matrix:
        for item in row:
            deciphered_text += item
    
    return deciphered_text
            
    
plain_text = 'BBL DRIZZY'
key = 'HACK'
n = len(key)
sequence = sequence_gen(key)
matrix = columnar_matrix(n,plain_text)
print(matrix)
ciphered_text = columnar_cipher(matrix,sequence,n)
print(ciphered_text)
print(sequence)
sequence = sequence_gen(key)
deciphered_text = columnar_decipher(sequence, ciphered_text, n)
print(deciphered_text.replace('@',''))