import hashlib

def sha1_hash(input_string):
    # Create a new sha1 hash object
    sha1 = hashlib.sha1()
    
    # Update the hash object with the bytes of the input string
    sha1.update(input_string.encode('utf-8'))
    
    # Return the hexadecimal digest of the hash
    return sha1.hexdigest()

# Example Usage
input_data = "Hello, SHA-1 hashing!"
hash_output = sha1_hash(input_data)

print(f"Input: {input_data}")
print(f"SHA-1 Hash: {hash_output}")
