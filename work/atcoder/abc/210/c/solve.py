from collections import defaultdict


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N, K = map(int, input().split())
    C = lmap(int, input().split())

    count = defaultdict(int)
    for c in C[:K]:
        count[c] += 1
    n = len(set(C[:K]))
    maxn = n

    for i in range(1, N - K + 1):
        count[C[i - 1]] -= 1
        if count[C[i - 1]] == 0:
            n -= 1

        count[C[i + K - 1]] += 1
        if count[C[i + K - 1]] == 1:
            n += 1

        maxn = max(maxn, n)

    print(maxn)


solve()
