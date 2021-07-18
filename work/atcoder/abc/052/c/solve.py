from collections import defaultdict


def count_prime_factors(n):
    factors = defaultdict(int)

    if n <= 1:
        return factors

    while n % 2 == 0:
        factors[2] += 1
        n //= 2

    while n % 3 == 0:
        factors[3] += 1
        n //= 3

    for i in range(5, int(n**0.5) + 1, 6):
        while n % i == 0:
            factors[i] += 1
            n //= i

        while n % (i + 2) == 0:
            factors[i + 2] += 1
            n //= i + 2

    if n > 1:
        factors[n] += 1

    return factors


def solve():
    mod = 10**9 + 7

    N = int(input())

    fs = defaultdict(int)
    for i in range(1, N + 1):
        for n, c in count_prime_factors(i).items():
            fs[n] += c

    result = 1
    for n, c in fs.items():
        result = (result * (c + 1)) % mod

    print(result)


solve()
