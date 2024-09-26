# Function to encrypt the text using Caesar Cipher
def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        # Check if character is an uppercase letter
        if char.isupper():
            ciphertext += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            ciphertext += char  # Non-alphabetical characters remain the same
    return ciphertext

# Function to decrypt the text using Caesar Cipher
def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        # Check if character is an uppercase letter
        if char.isupper():
            plaintext += chr((ord(char) - shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            plaintext += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plaintext += char  # Non-alphabetical characters remain the same
    return plaintext

shift = int(input('ENTER THE SHIFT='))
plaintext = input("ENTER THE TEXT =")
ciphertext = caesar_encrypt(plaintext, shift)
print(f"Encrypted Text: {ciphertext}")

# Decrypt the text
decrypted_text = caesar_decrypt(ciphertext, shift)
print(f"Decrypted Text: {decrypted_text}")
