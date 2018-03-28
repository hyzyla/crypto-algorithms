
import math
import random
def gcd(a: int, b: int) -> int:
    return b if a == 0 else gcd(b % a, a) 
def euler_function(n: int) -> int:
    return sum(1 for i in range(n) if gcd(i, n) == 1)
def jacobi_symbol(a: int, p: int) -> int:
    if gcd(a, p) != 1: return 0
    if a == 1 or a == 0: return a
    if a < 0:
        s = ((-1) ** ((p - 1) // 2))
        return s * jacobi_symbol(-a, p)
    if a % 2 == 0:
        s = ((-1) ** ((p ** 2 - 1) // 8))
        return s * jacobi_symbol(a // 2, p)
    if a < p:
        s = ((-1) ** (((a - 1) // 2)  * ((p - 1) // 2)))
        return s * jacobi_symbol(p, a)
    return jacobi_symbol(a % p, p)
def jacobi_symbol_new(a: int , b: int) -> int:
    if gcd(a, b) != 1:
        return 0
    result = 1
    if a < 0:
        a = -a
        if b % 4 == 3:
            result = -result
    while True:
        temp = 0
        while a % 2 == 0:
            temp = temp + 1
            a = a // 2
        if temp % 2 != 0:
            if b % 8 == 3 or b % 8 == 5: 
                result = -result
                
        if a % 4 == b % 4 == 3:
            result = -result
        
        a, b = b % a, a
        if a == 0: 
            return result
def legendre_symbol(a: int, p: int):
    if a == 1 or a == 0: return a
    if a % 2 == 0:
        s = (-1) ** ((p ** 2 - 1) // 8)
        return s * legendre_symbol(a // 2, p)
    s = ((-1)**((a - 1) * (p - 1) // 4))
    return s * legendre_symbol(p % a, a)
def modular_eq(a, b, m):
    return (a % m) == (b % m)
def proths_theorem(n: int) -> bool:
    for i in range(10):
        a = randint(-1000, 1000)
        while modular_eq(a, 1, n):
            a = random.randint(1000, 1000)
        b = a ** ((n - 1) // 2)
        if modular_eq(b, -1, n):
            return True
        if modular_eq(b, 1, n):
            continue
        return False
    return False
def solovay_strassen_test(n: int, k: int = 2) -> bool:
    if n % 2 == 0: 
        return False
    for i in range(k):
        a = random.randint(2, n)
        x = jacobi_symbol_new(a, n)
        if x == 0 or not modular_eq(x, a ** ((n - 1) // 2), n):
            return False
    return True
def miller_rabin_test(n: int, k: int = 2) -> bool:
    t = n - 1
    s = 0
    while t % 2 == 0:
        s += 1
        t = t // 2
    for _ in range(k): 
        a = random.randint(2, n - 1)
        x = a ** t % n
        if x == 1 or x == n - 1: 
            continue
        for __ in range(s - 1):
            x  = x ** 2 % n
            if x == 1: 
                return False
            if x == n - 1:
                break 
        return False
    return True
def pollards_rho_algorithm(n: int) -> int:
    x = random.randint(1, n - 2)
    y = 1
    i = 0
    stage = 2
    while (gcd(n, abs(x - y)) == 1):
        if i == stage:
            y = x
            stage = stage * 2
        x = (x**2 + 1) % n
        i += 1
    return gcd(n, abs(x - y))
def extended_euclid(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = extended_euclid(b % a, a)
    return g, y - (b // a) * x, x
def multiplicative_inverse(b, n):
    g, x, y = extended_euclid(b, n)
    if g == 1:
        return x % n
def brute_force_primality_test(n):
    for i in range(2, n // 2):
        if n % i == 0: 
            return False
    return True
class RSA:
    def __init__(self):
        self.generate_keypair()
    def get_two_prime_numbers(self):
        prime_numbers = list(i for i in range(100, 1000) if brute_force_primality_test(i))
        return random.choice(prime_numbers), random.choice(prime_numbers)
    def get_e(self, phi):
        e = random.randint(1, phi)
        while gcd(e, phi) != 1:
            e = random.randint(1, phi)
        return e
    def encrypt(self, message):
        key, n = self.__private_keypair
        return [pow(ord(char), key, n) for char in message]
    def decrypt(self, message, keys=None):
        key, n = keys if keys else self.public_keypair
        return ''.join(chr(pow(char, key, n)) for char in message)
    def generate_keypair(self):
        p, q = self.get_two_prime_numbers()
        n = p * q
        phi = (p - 1) * (q - 1)
        e = self.get_e(phi)
        d = multiplicative_inverse(e, phi) 
        self.__private_keypair = d, n
        self.public_keypair = e, n
rsa = RSA()
rsa.decrypt(rsa.encrypt("as"))
