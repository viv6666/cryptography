from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def aes_encrypt(plaintext, key):
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)
    
    # Create AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Pad plaintext to be a multiple of block size (16 bytes)
    padding_length = 16 - len(plaintext) % 16
    padded_plaintext = plaintext + bytes([padding_length] * padding_length)

    # Encrypt the padded plaintext
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    
    return iv + ciphertext  # Prepend IV to the ciphertext for use in decryption

def aes_decrypt(ciphertext, key):
    # Extract the IV from the beginning of the ciphertext
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]

    # Create AES cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Decrypt the ciphertext
    padded_plaintext = decryptor.update(actual_ciphertext) + decryptor.finalize()
    
    # Remove padding
    padding_length = padded_plaintext[-1]
    return padded_plaintext[:-padding_length]  # Return the original plaintext

# Example Usage
key = os.urandom(32)  # Generate a random 256-bit key
plaintext = b"Hello, AES encryption!"
print(f"Original plaintext: {plaintext}")

# Encrypt the plaintext
ciphertext = aes_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

# Decrypt the ciphertext
decrypted_text = aes_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")
