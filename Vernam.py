import random


def generate_key(msg):
    key = ''.join([chr(random.randint(32,126)) for n in range(len(msg))])
    return key


def encrypt(msg, key):
    en_msg = ''
    for i in range(len(msg)):
        en_msg += chr((ord(msg[i]) + ord(key[i])) % 127)
    return en_msg


def decrypt(crypted, key):
    de_msg = ''
    for i in range(len(crypted)):
        de_msg += chr((ord(crypted[i]) - ord(key[i])) % 127)
    return de_msg


if __name__ == '__main__':
    print()
    print("============================== Vernam Encryptor / Decrypter ======================================")
    print()

    message = input(" - Enter a message to encrypt <<< ")
    
    key = generate_key(message)
    print(" - Your key >>> ", key)
    
    encrypted_msg = encrypt(message, key)

    print(" - Your encrypted message >>> ", encrypted_msg)
 
    print(" - Your message >>> ", decrypt(encrypted_msg, key))

    print()
    print("=========================================== END ==================================================")
    print()