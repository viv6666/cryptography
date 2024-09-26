from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.utils import Prehashed

# Generate DSA private key
private_key = dsa.generate_private_key(key_size=2048)

# Generate public key from private key
public_key = private_key.public_key()

# Message to be signed
message = b"This is a message to be signed."

# Sign the message using DSA and private key
signature = private_key.sign(
    message,
    hashes.SHA256()  # Using SHA-256 hash algorithm
)

# Verify the signature using public key
def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message,
            hashes.SHA256()  # Using the same hash algorithm
        )
        return True
    except:
        return False

# Example Usage
is_valid = verify_signature(public_key, message, signature)
print(f"Is the signature valid? {is_valid}")
