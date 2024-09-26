from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def aes_ecb_encrypt(plaintext, key):
    # Create an AES cipher object in ECB mode
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    # Pad plaintext to be a multiple of block size (16 bytes)
    padding_length = 16 - len(plaintext) % 16
    padded_plaintext = plaintext + bytes([padding_length] * padding_length)

    # Encrypt the padded plaintext
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    
    return ciphertext

def aes_ecb_decrypt(ciphertext, key):
    # Create an AES cipher object in ECB mode
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
    # Remove padding
    padding_length = padded_plaintext[-1]
    return padded_plaintext[:-padding_length]  # Return the original plaintext

# Example Usage
key = os.urandom(32)  # Generate a random 256-bit key
plaintext = b"Hello, ECB mode encryption!"
print(f"Original plaintext: {plaintext}")

# Encrypt the plaintext
ciphertext = aes_ecb_encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")

# Decrypt the ciphertext
decrypted_text = aes_ecb_decrypt(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")
