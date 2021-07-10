from itertools import accumulate


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N = int(input())
    W = lmap(int, input().split())

    acc = list(accumulate(W))

    diffs = []
    for i in range(N - 1):
        diffs.append(abs(acc[i] - (acc[-1] - acc[i])))

    print(min(diffs))


solve()
