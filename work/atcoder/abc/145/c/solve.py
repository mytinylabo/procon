from math import sqrt
from itertools import combinations, permutations


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N = int(input())
    T = [tmap(int, input().split()) for _ in range(N)]

    dist = {}
    for (ai, (ax, ay)), (bi, (bx, by)) in combinations(enumerate(T), 2):
        d = sqrt((ax - bx)**2 + (ay - by)**2)
        dist[ai, bi] = d
        dist[bi, ai] = d

    total_d = 0
    path = list(permutations(range(N), N))
    for p in path:
        for i in range(N - 1):
            total_d += dist[p[i], p[i + 1]]

    print(total_d / len(path))


solve()
