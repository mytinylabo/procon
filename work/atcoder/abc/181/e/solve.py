from itertools import accumulate
from bisect import bisect


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N, M = map(int, input().split())
    H = lmap(int, input().split())
    W = lmap(int, input().split())

    H.sort()

    even = [0]
    odd = [0]
    for i in range(N - 1):
        if i % 2 == 0:
            even.append(H[i + 1] - H[i])
            odd.append(0)
        else:
            even.append(0)
            odd.append(H[i + 1] - H[i])

    acc_e = list(accumulate(even))
    acc_o = list(accumulate(odd))

    diffs = []
    for w in W:
        i = bisect(H, w)

        if i == N:
            d = w - H[-1]
            d += acc_e[-1]

        elif i % 2 == 0:
            d = H[i] - w
            d += acc_e[i]
            d += acc_o[-1] - acc_o[i]

        else:
            d = w - H[i - 1]
            d += acc_e[i - 1]
            d += acc_o[-1] - acc_o[i]

        diffs.append(d)

    print(min(diffs))


solve()
