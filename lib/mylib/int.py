
def use_factorials(n, p):
    """法 p における 0! .. n! と
       その逆元のテーブルを生成する。
       p は素数であること。
    """
    m = n + 1
    fact = [0] * m
    ifact = [0] * m

    fact[0] = 1
    ifact[0] = 1

    for i in range(1, m):
        fact[i] = (fact[i - 1] * i) % p

    ifact[m - 1] = pow(fact[m - 1], p - 2, p)
    for i in reversed(range(1, m - 1)):
        # i = m-2, m-3, ... , 2, 1
        ifact[i] = (ifact[i + 1] * (i + 1)) % p

    return (fact, ifact)


def is_prime(n):
    if n < 2:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def use_primes(n):
    if n <= 3:
        return list(range(2, n + 1))

    flags = [True] * (n + 1)

    for i in [2, 3]:
        for j in range(2, n // i + 1):
            flags[i * j] = False

    for i in range(5, int(n**0.5) + 1, 6):
        for j in range(2, n // i + 1):
            flags[i * j] = False

        for j in range(2, n // (i + 2) + 1):
            flags[(i + 2) * j] = False

    return list(filter(lambda x: flags[x], range(2, n + 1)))


def use_prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    while n % 3 == 0:
        factors.append(3)
        n //= 3

    for i in range(5, int(n**0.5) + 1, 6):
        while n % i == 0:
            factors.append(i)
            n //= i

        while n % (i + 2) == 0:
            factors.append(i + 2)
            n //= i + 2

    if n > 1:
        factors.append(n)

    return factors
