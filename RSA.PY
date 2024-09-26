from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# RSA Key Generation
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# RSA Encryption
def rsa_encrypt(public_key, plaintext):
    rsa_public_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_public_key)
    
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext

# RSA Decryption
def rsa_decrypt(private_key, ciphertext):
    rsa_private_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_private_key)
    
    decrypted_text = cipher.decrypt(ciphertext)
    return decrypted_text.decode()

# Example usage
# Step 1: Generate RSA key pair
private_key, public_key = generate_rsa_keys()

# Print the keys (optional)
print(f"Private Key: {private_key.decode()}")
print(f"Public Key: {public_key.decode()}")

# Step 2: Encrypt a message using the public key
plaintext = input("ENTER THE PLAIN TEXT=")
ciphertext = rsa_encrypt(public_key, plaintext)
print(f"Cipher Text: {ciphertext}")

# Step 3: Decrypt the message using the private key
decrypted_text = rsa_decrypt(private_key, ciphertext)
print(f"Decrypted Text: {decrypted_text}")
