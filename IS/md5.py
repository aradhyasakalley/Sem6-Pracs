import random

def text_to_binary(text):
    binary = ''
    for char in text:
        binary += ''.join(format(ord(char), '08b'))
    return binary

def add_padding(message):
    original_length = len(message)
    padding_bits = (64 - (original_length + 1) % 64) % 64 - 8
    padded_message = message + '1' + '0' * padding_bits
    padded_message += format(original_length, '08b')  
    return padded_message

def get_16_sub_blocks(block):
    sub_blocks = []
    for i in range(0, len(block), 4):
        sub_blocks.append(block[i:i+4])
    return sub_blocks

def get_blocks(padded_message):
    blocks = []
    for i in range(0, len(padded_message), 64):
        blocks.append(padded_message[i:i+64])
    return blocks

def process_f(i, A, B, C, D):
    if i == 0:
        return ((int(A, 2) & int(B, 2)) | (~int(A, 2) & int(D, 2)))
    elif i == 1:
        return ((int(A, 2) & int(D, 2)) | (int(B, 2) & ~int(D, 2)))
    elif i == 2:
        return (int(A, 2) ^ int(B, 2) ^ int(D, 2))
    else:
        return (int(B, 2) ^ (int(A, 2) | ~int(D, 2)))

def circular_left_shift(binary_number, s):
    return binary_number[s:] + binary_number[:s]

def md5_hashing(padded_message):
    A = '1101'
    B = '1010'
    C = '0110'
    D = '1111'
    
    # Constants initialization
    K = [format(random.randint(0, 15), '04b') for _ in range(16)]
    
    blocks = get_blocks(padded_message)
    for block in blocks:
        sub_blocks = get_16_sub_blocks(block)
        for i in range(4):
            output_f = process_f(i, A, B, C, D)
            output_f += int(A)  
            for j in range(16):
                output_f += int(sub_blocks[j])
                output_f += int(K[j])
                output_f = circular_left_shift(output_f, 4)
                output_f += B  
                A, B, C, D = D, A, B, C  
        
        A = bin((int(A, 2) + int('1101', 2)) & 0xFFFFFFFF)[2:].zfill(32)
        B = bin((int(B, 2) + int('1010', 2)) & 0xFFFFFFFF)[2:].zfill(32)
        C = bin((int(C, 2) + int('0110', 2)) & 0xFFFFFFFF)[2:].zfill(32)
        D = bin((int(D, 2) + int('1111', 2)) & 0xFFFFFFFF)[2:].zfill(32)
    # Concatenate A, B, C, D to get the hash value
    hash_value = A + B + C + D
    return hash_value

# Example usage
message = "This is a test"
message_binary = text_to_binary(message)
print("Original binary message:", message_binary)
padded_message = add_padding(message_binary)  
print("Padded binary message:", padded_message)
print("Padded message length:", len(padded_message))

# Call md5_hashing with padded_message
hash_value = md5_hashing(padded_message)
print("Hash value:", hash_value)
