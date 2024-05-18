def prepare_msg(msg):
    msg = msg.replace(" ", "").upper().replace("J", "I")
    i = 0
    while i < len(msg) - 1:
        if msg[i] == msg[i + 1]:
            msg = msg[:i + 1] + 'X' + msg[i + 1:]
        i += 2
    if len(msg) % 2 != 0:
        msg += 'X'
    return msg


def playfair_matrix(key):
    key = key.replace(" ", "").upper().replace("J", "I")
    key_set = set(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    alphabet = ''.join([char for char in alphabet if char not in key_set])

    matrix = []
    row = []

    for char in key + alphabet:
        row.append(char)
        if len(row) == 5:
            matrix.append(row)
            row = []
    return matrix


def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)


def encrypt(msg, key):
    matrix = playfair_matrix(key)
    msg = prepare_msg(msg)
    en_msg = ""

    for i in range(0, len(msg), 2):
        char1 = msg[i]
        char2 = msg[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            en_msg += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            en_msg += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            en_msg += matrix[row1][col2] + matrix[row2][col1]

    return en_msg


def decrypt(en_msg, key):
    matrix = playfair_matrix(key)
    de_msg = ""

    for i in range(0, len(en_msg), 2):
        char1 = en_msg[i]
        char2 = en_msg[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            de_msg += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            de_msg += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else: 
            de_msg += matrix[row1][col2] + matrix[row2][col1]

    return de_msg


if __name__ == '__main__':
    print()
    print("============================ Playfair Encryptor / Decrypter =====================================")
    print()

    key = input(" - Enter a key word <<< ")

    matrix = playfair_matrix(key)
    print(" - Playfair matrix >>> ")
    for row in matrix:
        print("\t" + "".join(row))
    
    message = input(" - Enter a message to encrypt <<< ")
    encrypted_msg = encrypt(message, key)

    print(" - Your encrypted message >>> ", encrypted_msg)
 
    print(" - Your message >>> ", decrypt(encrypted_msg, key))

    print()
    print("=========================================== END ==================================================")
    print()