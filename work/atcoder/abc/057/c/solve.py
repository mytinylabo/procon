from math import sqrt, log10


def solve():
    N = int(input())

    def ndigits(x): return int(log10(x)) + 1

    lmin = ndigits(N)

    for a in range(2, int(sqrt(N)) + 1):
        if N % a != 0:
            continue

        b = N // a
        lmin = min(lmin, ndigits(max(a, b)))

    print(lmin)


solve()
