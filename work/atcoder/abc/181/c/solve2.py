from collections import defaultdict
from fractions import Fraction

# Fraction でゴリ押しした最初の AC 回答。遅い


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    inf = float('inf')

    N = int(input())
    A = [tmap(lambda n: int(n) + 1000, input().split()) for _ in range(N)]

    cnt = defaultdict(int)

    for i in range(N):
        for j in range(i, N):
            if i == j:
                continue

            (x1, y1), (x2, y2) = sorted([A[i], A[j]])

            if x1 == x2:
                cnt[(inf, x1)] += 1
            else:
                s = Fraction(y2 - y1, x2 - x1)
                t = y1 - s * x1
                cnt[(s, t)] += 1

    print("Yes" if any(map(lambda c: c >= 2, cnt.values())) else "No")


solve()
