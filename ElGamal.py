import random  


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
def generate_key_pair(p):
    if not is_prime(p):
        raise ValueError('The number must be prime.')
    
    d = random.randint(1, p-1)   #Private Key
    e1 = random.randint(1, p-1)  #Public Key
    e2 = pow(e1,d,p)
    
    return d, e1, e2


# Расширенный алгоритм Евклида
# Возвращает (x, y, g) : a * x + b * y = gcd(a, b) = g.
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


# Возвращает 1 / a (mod n) (a и n должны быть взаимнопростыми)
def invmod(a, n):
    if n < 2:
        raise ValueError("modulus must be greater than 1")

    x, y, g = xgcd(a, n)

    if g != 1:
        raise ValueError("no invmod for given a and n")
    else:
        return x % n


def encrypt(msg, p, e1, e2): 
  
    en_msg = [] 
    r = random.randint(1,p-1) 
    c1 = pow(e1, r,p)
    
    for i in range(0, len(msg)): 
        en_msg.append(msg[i]) 
        
    for i in range(0, len(en_msg)): 
        en_msg[i] = (pow(e2,r) * ord(en_msg[i])) % p
  
    return en_msg, c1


def decrypt(en_msg, p, d, e1, c1): 
  
    de_msg = [] 
    for i in range(0, len(en_msg)):         
        de_msg.append(chr((int(en_msg[i]) * invmod(pow(c1, d, p), p)) % p))
        
    return de_msg 
  


if __name__ == '__main__':
    print()
    print("=============================== ElGamal Encryptor / Decrypter ====================================")
    print()

    p = int(input(" - Enter a prime number (it must be greater than your message) <<< "))

    d, e1, e2 = generate_key_pair(p)

    print(" - Your public key >>> (", p,",", e1, ",", e2, ") and your private key >>> ",d)

    message = input(" - Enter a message to encrypt with your public key <<< ")
    encrypted_msg, c1 = encrypt(message, p, e1, e2)

    print(" - Your encrypted message >>> ", ''.join(map(lambda x: str(x), encrypted_msg)))

    print(" - Your message >>> ", ''.join(decrypt(encrypted_msg, p, d, e1, c1)))

    print()
    print("=========================================== END ==================================================")
    print()