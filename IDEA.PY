from Crypto.Cipher import IDEA
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to encrypt using IDEA
def idea_encrypt(key, plaintext):
    # Create an IDEA cipher object
    cipher = IDEA.new(key, IDEA.MODE_ECB)
    
    # Pad the plaintext to make sure its length is a multiple of 8 bytes (64 bits)
    padded_text = pad(plaintext.encode(), IDEA.block_size)
    
    # Encrypt the plaintext
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

# Function to decrypt using IDEA
def idea_decrypt(key, ciphertext):
    # Create an IDEA cipher object
    cipher = IDEA.new(key, IDEA.MODE_ECB)
    
    # Decrypt the ciphertext
    decrypted_padded_text = cipher.decrypt(ciphertext)
    
    # Unpad the plaintext
    decrypted_text = unpad(decrypted_padded_text, IDEA.block_size)
    return decrypted_text.decode()

# Example usage
key = get_random_bytes(16)  # IDEA requires a 128-bit key (16 bytes)
plaintext = "Hello, IDEA Cipher!"

# Encrypt the plaintext
ciphertext = idea_encrypt(key, plaintext)
print(f"Cipher Text (in bytes): {ciphertext}")

# Decrypt the ciphertext
decrypted_text = idea_decrypt(key, ciphertext)
print(f"Decrypted Text: {decrypted_text}")
