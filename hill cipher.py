import numpy as np

# Helper function to calculate modular inverse of a number under modulo m
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

# Function to generate key matrix for the Hill cipher
def generate_key_matrix(key, size):
    key_matrix = []
    k = 0
    for i in range(size):
        row = []
        for j in range(size):
            row.append(ord(key[k]) % 65)  # Converting letters to numbers (A -> 0, B -> 1, ..., Z -> 25)
            k += 1
        key_matrix.append(row)
    return key_matrix

# Function to process the text into blocks of a given size
def process_text(text, size):
    # Removing spaces and padding with 'X' if necessary
    text = text.replace(" ", "").upper()
    while len(text) % size != 0:
        text += 'X'
    
    return text

# Function to encrypt the text using Hill cipher
def hill_encrypt(text, key_matrix, size):
    cipher_text = ""
    for i in range(0, len(text), size):
        block = [ord(text[j]) % 65 for j in range(i, i + size)]
        block_vector = np.dot(key_matrix, block) % 26  # Matrix multiplication followed by modulo 26
        cipher_text += ''.join([chr(num + 65) for num in block_vector])
    
    return cipher_text

# Function to decrypt the text using Hill cipher
def hill_decrypt(cipher_text, key_matrix, size):
    # Find the determinant and modular inverse of the key matrix
    det = int(np.round(np.linalg.det(key_matrix))) % 26
    det_inverse = mod_inverse(det, 26)
    
    # Find the adjugate matrix (transpose of cofactor matrix) and modular inverse of key matrix
    key_matrix_inverse = (
        det_inverse * np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    )
    
    # Decrypt the cipher text
    decrypted_text = ""
    for i in range(0, len(cipher_text), size):
        block = [ord(cipher_text[j]) % 65 for j in range(i, i + size)]
        block_vector = np.dot(key_matrix_inverse, block) % 26
        decrypted_text += ''.join([chr(int(num) + 65) for num in block_vector])
    
    return decrypted_text

# Example usage
key = input("enter the key =")# Key for the cipher (3x3 matrix in this example)
text = input("enter the text=")

# Set the matrix size based on the length of the key
size = int(len(key) ** 0.5)

# Generate the key matrix and process the input text
key_matrix = generate_key_matrix(key, size)
processed_text = process_text(text, size)

# Encrypt and Decrypt the text
cipher_text = hill_encrypt(processed_text, key_matrix, size)
decrypted_text = hill_decrypt(cipher_text, key_matrix, size)

print(f"Original Text: {text}")
print(f"Cipher Text: {cipher_text}")
print(f"Decrypted Text: {decrypted_text}")
