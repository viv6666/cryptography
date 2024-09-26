def generate_playfair_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
    matrix = []
    used_letters = []

    # Add key letters to the matrix
    for letter in key.upper():
        if letter not in used_letters and letter in alphabet:
            used_letters.append(letter)

    # Add remaining letters of the alphabet
    for letter in alphabet:
        if letter not in used_letters:
            used_letters.append(letter)

    # Split into 5x5 matrix
    for i in range(5):
        matrix.append(used_letters[i * 5:(i + 1) * 5])

    return matrix


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def prepare_text(text):

    text = text.replace(" ", "").upper().replace("J", "I")

    prepared_text = []
    i = 0
    while i < len(text):
        char1 = text[i]
        if i + 1 < len(text):
            char2 = text[i + 1]
        else:
            char2 = "X"

        if char1 == char2:
            prepared_text.append(char1 + "X")
            i += 1
        else:
            prepared_text.append(char1 + char2)
            i += 2

    if len(prepared_text[-1]) == 1:
        prepared_text[-1] += "X"

    return prepared_text


def encrypt_pair(matrix, char1, char2):
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]


def playfair_encrypt(text, key):
    matrix = generate_playfair_matrix(key)
    prepared_text = prepare_text(text)
    cipher_text = ""

    for pair in prepared_text:
        cipher_text += encrypt_pair(matrix, pair[0], pair[1])

    return cipher_text


# Example usage
key = input("Enter the play fair key =")
text =input("Enter the plain text =")
cipher = playfair_encrypt(text, key)
print("Cipher Text =",cipher)
