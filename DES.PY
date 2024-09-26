from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to encrypt using DES
def des_encrypt(key, plaintext):
    # Ensure the key is exactly 8 bytes
    if len(key) != 8:
        raise ValueError("Key must be exactly 8 bytes long.")
    
    # Create a DES cipher object
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    
    # Pad the plaintext to be a multiple of 8 bytes (64 bits)
    padded_text = pad(plaintext.encode('utf-8'), DES.block_size)
    
    # Encrypt the plaintext
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

# Function to decrypt using DES
def des_decrypt(key, ciphertext):
    # Ensure the key is exactly 8 bytes
    if len(key) != 8:
        raise ValueError("Key must be exactly 8 bytes long.")
    
    # Create a DES cipher object
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    
    # Decrypt the ciphertext and remove padding
    decrypted_padded_text = cipher.decrypt(ciphertext)
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)
    
    return decrypted_text.decode('utf-8')

# Example usage
key = input("ENTER THE KEY (8 bytes)= ")  # DES uses a key of exactly 8 bytes (64 bits)
plaintext = input("ENTER THE PLAINTEXT= ")

try:
    # Encrypt the plaintext
    ciphertext = des_encrypt(key, plaintext)
    print(f"Cipher Text (in bytes): {ciphertext}")

    # Decrypt the ciphertext
    decrypted_text = des_decrypt(key, ciphertext)
    print(f"Decrypted Text: {decrypted_text}")
except ValueError as e:
    print(f"Error: {e}")
