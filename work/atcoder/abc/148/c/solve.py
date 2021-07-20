from math import gcd


def solve():
    N, M = map(int, input().split())
    print((N * M) // gcd(N, M))


solve()
