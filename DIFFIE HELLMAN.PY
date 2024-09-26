import random

# Function to compute modular exponentiation (base^exp % mod)
def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

# Function to simulate Diffie-Hellman key exchange
def diffie_hellman():
    # Publicly agreed prime number (p) and base (g)
    p = int(input("enter the prime number1=")) # Example small prime number
    g = int(input("ENTER THE SMALL PRIME NUMBER="))
    
    print(f"Public values: Prime (p) = {p}, Base (g) = {g}")
    
    # Alice's private key (random)
    a_private = random.randint(1, p - 1)
    # Bob's private key (random)
    b_private = random.randint(1, p - 1)
    
    print(f"Alice's private key: {a_private}")
    print(f"Bob's private key: {b_private}")
    
    # Alice computes A = g^a mod p
    A = mod_exp(g, a_private, p)
    # Bob computes B = g^b mod p
    B = mod_exp(g, b_private, p)
    
    print(f"Alice sends: {A}")
    print(f"Bob sends: {B}")
    
    # Alice computes the shared secret: s = B^a mod p
    alice_shared_secret = mod_exp(B, a_private, p)
    # Bob computes the shared secret: s = A^b mod p
    bob_shared_secret = mod_exp(A, b_private, p)
    
    print(f"Alice's computed shared secret: {alice_shared_secret}")
    print(f"Bob's computed shared secret: {bob_shared_secret}")
    
    if alice_shared_secret == bob_shared_secret:
        print(f"Shared secret key established: {alice_shared_secret}")
    else:
        print("Error: Shared secret mismatch!")

# Example usage
diffie_hellman()
