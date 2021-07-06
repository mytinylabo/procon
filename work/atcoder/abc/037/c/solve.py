from itertools import accumulate


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N, K = map(int, input().split())
    A = lmap(int, input().split())

    acc = list(accumulate(A, initial=0))
    result = sum([acc[i + K] - acc[i] for i in range(0, N - K + 1)])

    print(result)


solve()
