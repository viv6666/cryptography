def rail_fence_encrypt(plaintext, rails):
    # Create a 2D list for rails
    rail = [['\n' for _ in range(len(plaintext))]
            for _ in range(rails)]

    # Direction: True for going down, False for going up
    dir_down = None
    row, col = 0, 0

    for char in plaintext:
        # If we're at the top or bottom rail, reverse direction
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False

        # Place the character in the current position
        rail[row][col] = char
        col += 1

        # Move up or down
        if dir_down:
            row += 1
        else:
            row -= 1

    # Read the rails to get the ciphertext
    ciphertext = ""
    for i in range(rails):
        for j in range(len(plaintext)):
            if rail[i][j] != '\n':
                ciphertext += rail[i][j]

    return ciphertext


def rail_fence_decrypt(ciphertext, rails):
    # Create a 2D list for rails
    rail = [['\n' for _ in range(len(ciphertext))]
            for _ in range(rails)]

    # Mark the positions of the rails
    dir_down = None
    row, col = 0, 0

    for char in ciphertext:
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    # Fill the marked positions with the ciphertext characters
    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if (rail[i][j] == '*' and index < len(ciphertext)):
                rail[i][j] = ciphertext[index]
                index += 1

    # Read the plaintext from the rails
    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False

        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    return ''.join(result)


# Example Usage
plaintext = "HELLO WORLD"
rails = 3

# Encrypt the plaintext
ciphertext = rail_fence_encrypt(plaintext, rails)
print(f"Encrypted: {ciphertext}")

# Decrypt the ciphertext
decrypted_text = rail_fence_decrypt(ciphertext, rails)
print(f"Decrypted: {decrypted_text}")
