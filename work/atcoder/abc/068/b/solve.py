def prime_factors(n):
    if n <= 1:
        return []

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


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N = int(input())

    score = lmap(lambda n: prime_factors(n).count(2), range(1, N + 1))

    print(score.index(max(score)) + 1)


solve()
