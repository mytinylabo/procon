from itertools import accumulate


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N = int(input())
    A = lmap(int, input().split())

    delta = list(accumulate(A))
    pos = list(accumulate(accumulate(A)))

    dmax = 0
    pmax = 0
    for i in range(N):
        if delta[i] > dmax:
            dmax = delta[i]
        if pos[i] + dmax > pmax:
            pmax = pos[i] + dmax

    print(pmax)


solve()
