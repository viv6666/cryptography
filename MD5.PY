import hashlib

# Function to compute MD5 hash of a string
def md5_hash_string(input_string):
    # Create an MD5 hash object
    md5_hash = hashlib.md5()
    
    # Update the hash object with the bytes of the string
    md5_hash.update(input_string.encode())
    
    # Return the hexadecimal representation of the hash
    return md5_hash.hexdigest()

# Function to compute MD5 hash of a file
def md5_hash_file(file_path):
    # Create an MD5 hash object
    md5_hash = hashlib.md5()
    
    # Open the file in binary mode
    with open(file_path, 'rb') as f:
        # Read the file in chunks to avoid using too much memory
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    
    # Return the hexadecimal representation of the hash
    return md5_hash.hexdigest()

# Example Usage
string_to_hash = "Hello, World!"
md5_result_string = md5_hash_string(string_to_hash)
print(f"MD5 hash of '{string_to_hash}': {md5_result_string}")

# To hash a file, uncomment the following lines and provide a valid file path
# file_path = 'path/to/your/file.txt'
# md5_result_file = md5_hash_file(file_path)
# print(f"MD5 hash of file '{file_path}': {md5_result_file}")
