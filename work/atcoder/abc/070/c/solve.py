from math import gcd


def solve():
    N = int(input())
    T = [int(input()) for _ in range(N)]

    m = T[0]
    for t in T[1:]:
        m = m * t // gcd(m, t)

    print(m)


solve()
