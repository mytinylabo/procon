def use_primes(n, container=list, as_table=False):
    if n <= 3:
        flags = [False, False, True, True]
        if as_table:
            return flags[0:n + 1]
        else:
            return container(filter(lambda x: flags[x], range(n + 1)))

    flags = [True] * (n + 1)
    flags[0] = False
    flags[1] = False

    for i in [2, 3]:
        for j in range(2, n // i + 1):
            flags[i * j] = False

    for i in range(5, int(n**0.5) + 1, 6):
        for j in range(2, n // i + 1):
            flags[i * j] = False

        for j in range(2, n // (i + 2) + 1):
            flags[(i + 2) * j] = False

    if as_table:
        return flags
    else:
        return container(filter(lambda x: flags[x], range(2, n + 1)))


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N = int(input())
    Q = [tmap(int, input().split()) for _ in range(N)]

    primes = use_primes(10**5, as_table=True)

    acc = [0]
    for i in range(1, 10**5 + 1, 2):
        like2017 = primes[i] and primes[(i + 1) // 2]
        acc.append(acc[-1] + (1 if like2017 else 0))

    for left, right in Q:
        print(acc[(right // 2) + 1] - acc[left // 2])


solve()
