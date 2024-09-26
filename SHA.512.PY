import struct

# Constants for SHA-512
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa11, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
]

# Initial hash values for SHA-512
H = [
    0x6a09e667f3bcc908, 0xbb67ae8584caa73b,
    0x3c6ef372fe94f82b, 0xa54ff53a5f1d36f1,
    0x510e527fade682d1, 0x9b05688c2b3e6c1f,
    0x1f83d9abfb41bd6b, 0x5be0cd19137e2179,
]

def right_rotate(value, amount):
    return ((value >> amount) | (value << (64 - amount))) & 0xFFFFFFFFFFFFFFFF

def sha512(message):
    # Preprocessing: Padding the message
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8

    # Append the bit '1' to the message
    message += b'\x80'

    # Append zeros until the message length is 112 mod 128
    while (len(message) * 8) % 1024 != 896:
        message += b'\x00'

    # Append the original message length as a 128-bit integer
    message += struct.pack('>Q', original_bit_len >> 64)  # High 64 bits
    message += struct.pack('>Q', original_bit_len & 0xFFFFFFFFFFFFFFFF)  # Low 64 bits

    # Process each 1024-bit chunk
    for i in range(0, len(message), 128):
        chunk = message[i:i+128]
        w = list(struct.unpack('>16Q', chunk)) + [0] * 48

        # Extend the first 16 words into the remaining 48 words
        for j in range(16, 64):
            s0 = right_rotate(w[j-15], 1) ^ right_rotate(w[j-15], 8) ^ (w[j-15] >> 7)
            s1 = right_rotate(w[j-2], 19) ^ right_rotate(w[j-2], 61) ^ (w[j-2] >> 6)
            w[j] = (w[j-16] + s0 + w[j-7] + s1) & 0xFFFFFFFFFFFFFFFF

        # Initialize working variables to current hash value
        a, b, c, d, e, f, g, h = H

        # Compression function main loop
        for j in range(64):
            S1 = right_rotate(e, 14) ^ right_rotate(e, 18) ^ right_rotate(e, 41)
            ch = (e & f) ^ (~e & g)
            temp1 = (h + S1 + ch + K[j] + w[j]) & 0xFFFFFFFFFFFFFFFF
            S0 = right_rotate(a, 28) ^ right_rotate(a, 34) ^ right_rotate(a, 39)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xFFFFFFFFFFFFFFFF

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFFFFFFFFFF
            d = (c + temp2) & 0xFFFFFFFFFFFFFFFF
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFFFFFFFFFF

        # Add the compressed chunk to the current hash value
        H[0] = (H[0] + a) & 0xFFFFFFFFFFFFFFFF
        H[1] = (H[1] + b) & 0xFFFFFFFFFFFFFFFF
        H[2] = (H[2] + c) & 0xFFFFFFFFFFFFFFFF
        H[3] = (H[3] + d) & 0xFFFFFFFFFFFFFFFF
        H[4] = (H[4] + e) & 0xFFFFFFFFFFFFFFFF
        H[5] = (H[5] + f) & 0xFFFFFFFFFFFFFFFF
        H[6] = (H[6] + g) & 0xFFFFFFFFFFFFFFFF
        H[7] = (H[7] + h) & 0xFFFFFFFFFFFFFFFF

    # Produce the final hash value (big-endian)
    return b''.join(struct.pack('>Q', h) for h in H)

# Example Usage
input_data = "Hello, SHA-512 hashing!".encode('utf-8')
hash_output = sha512(input_data)

print(f"Input: {input_data.decode('utf-8')}")
print(f"SHA-512 Hash: {hash_output.hex()}")
