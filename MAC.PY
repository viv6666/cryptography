import hmac
import hashlib

# Function to generate HMAC
def generate_hmac(secret_key, message):
    # Create a new HMAC object using the secret key and SHA-256 as the hash function
    hmac_obj = hmac.new(secret_key, message.encode(), hashlib.sha256)
    
    # Return the hexadecimal representation of the HMAC
    return hmac_obj.hexdigest()

# Function to verify HMAC
def verify_hmac(secret_key, message, received_hmac):
    # Recompute the HMAC for the given message
    computed_hmac = generate_hmac(secret_key, message)
    
    # Check if the received HMAC matches the computed HMAC
    return hmac.compare_digest(computed_hmac, received_hmac)

# Example usage
secret_key = b'supersecretkey'  # Secret key must be in bytes
message = "This is a sensitive message"

# Generate HMAC for the message
hmac_value = generate_hmac(secret_key, message)
print(f"Generated HMAC: {hmac_value}")

# Verify the HMAC
is_valid = verify_hmac(secret_key, message, hmac_value)
print(f"Is the HMAC valid? {is_valid}")
