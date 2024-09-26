def rc2_key_schedule(key, bits):
    """ Generates the key schedule for RC2. """
    key = key.ljust(128 // 8, b'\x00')[:128 // 8]  # Ensure the key is 16 bytes
    S = [0] * 256
    
    for i in range(256):
        S[i] = i

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % bits]) % 256
        S[i], S[j] = S[j], S[i]  # Swap S[i] and S[j]

    return S

def rc2_encrypt_block(plain_text, S):
    """ Encrypts a single block of plaintext using RC2. """
    L = [0] * 8
    for i in range(8):
        L[i] = plain_text[i]

    for i in range(1, 12):
        L[0] = (L[0] + L[1]) % 256
        L[1] = (L[1] ^ S[L[0]]) % 256
        L[2] = (L[2] + L[3]) % 256
        L[3] = (L[3] ^ S[L[2]]) % 256
        L[4] = (L[4] + L[5]) % 256
        L[5] = (L[5] ^ S[L[4]]) % 256
        L[6] = (L[6] + L[7]) % 256
        L[7] = (L[7] ^ S[L[6]]) % 256

    return bytes(L)

def rc2_decrypt_block(cipher_text, S):
    """ Decrypts a single block of ciphertext using RC2. """
    L = [0] * 8
    for i in range(8):
        L[i] = cipher_text[i]

    for i in range(11, 0, -1):
        L[7] = (L[7] ^ S[L[6]]) % 256
        L[6] = (L[6] - L[7]) % 256
        L[5] = (L[5] ^ S[L[4]]) % 256
        L[4] = (L[4] - L[5]) % 256
        L[3] = (L[3] ^ S[L[2]]) % 256
        L[2] = (L[2] - L[3]) % 256
        L[1] = (L[1] ^ S[L[0]]) % 256
        L[0] = (L[0] - L[1]) % 256

    return bytes(L)

def rc2_encrypt(key, plain_text):
    """ Encrypts the plaintext using RC2. """
    bits = len(key) * 8
    S = rc2_key_schedule(key, bits)
    
    # Pad the plaintext to be a multiple of 8 bytes
    while len(plain_text) % 8 != 0:
        plain_text += b'\x00'
    
    cipher_text = bytearray()
    for i in range(0, len(plain_text), 8):
        block = plain_text[i:i+8]
        encrypted_block = rc2_encrypt_block(block, S)
        cipher_text.extend(encrypted_block)

    return bytes(cipher_text)

def rc2_decrypt(key, cipher_text):
    """ Decrypts the ciphertext using RC2. """
    bits = len(key) * 8
    S = rc2_key_schedule(key, bits)

    # Decrypt in blocks
    plain_text = bytearray()
    for i in range(0, len(cipher_text), 8):
        block = cipher_text[i:i+8]
        decrypted_block = rc2_decrypt_block(block, S)
        plain_text.extend(decrypted_block)

    return bytes(plain_text).rstrip(b'\x00')  # Remove padding

# Example Usage
key = b"mysecretkey"  # Key must be 1 to 16 bytes long
plain_text = b"Hello, RC2!"
cipher_text = rc2_encrypt(key, plain_text)
decrypted_text = rc2_decrypt(key, cipher_text)

print(f"Plaintext: {plain_text.decode('utf-8')}")
print(f"Ciphertext: {cipher_text.hex()}")
print(f"Decrypted text: {decrypted_text.decode('utf-8')}")
