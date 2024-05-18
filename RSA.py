import random

# Алгоритм Евклида для определения наибольшего общего делителя
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Расширенный алгоритм Евклида для нахождения мультипликативно обратной величины двух чисел
def xgcd(a, b):
    if a == 0:
        return 0, 1, b
    if b == 0:
        return 1, 0, a

    px, ppx = 0, 1
    py, ppy = 1, 0

    while b:
        q = a // b
        a, b = b, a % b
        x = ppx - q * px
        y = ppy - q * py
        ppx, px = px, x
        ppy, py = py, y

    return ppx, ppy, a


# Проверка чисел на простоту
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


# Генерация ключа
def generate_key_pair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    n = p * q

    # Phi - это совокупность n
    phi = (p-1) * (q-1)

    # e и phi(n) должны быть взаимно простыми
    e = random.randrange(1, phi)

    # алгоритм Евклида, чтобы убедиться, что e и phi (n) взаимно просты
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # расширенный алгоритм Евклида для генерации закрытого ключа
    d = xgcd(e, phi)[0]

    # публичный ключ (e, n), а секретный ключ (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    key, n = pk
    # Преобразует каждую букву в обычном тексте в цифры 
    # на основе символа, используя a ^ b mod m
    cipher = [pow(ord(char), key, n) for char in plaintext]
    # Возвращает массив байт
    return cipher


def decrypt(pk, ciphertext):
    key, n = pk
    # Расшифровывет текст на основе зашифрованного текста и ключа, 
    # используя a ^ b mod m
    aux = [str(pow(char, key, n)) for char in ciphertext]
    # Возвращает массив байтов в виде строки
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)


if __name__ == '__main__':
    print()
    print("=============================== RSA Encryptor / Decrypter ========================================")
    print()

    p = int(input(" - Enter a prime number <<< "))
    q = int(input(" - Enter another prime number (Not one you entered above) <<< "))

    public, private = generate_key_pair(p, q)

    print(" - Your public key >>> ", public, " and your private key >>> ", private)

    message = input(" - Enter a message to encrypt with your public key <<< ")
    encrypted_msg = encrypt(public, message)

    print(" - Your encrypted message >>> ", ''.join(map(lambda x: str(x), encrypted_msg)))
 
    print(" - Your message >>> ", decrypt(private, encrypted_msg))

    print()
    print("=========================================== END ==================================================")
    print()