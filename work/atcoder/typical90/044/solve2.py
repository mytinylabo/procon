
# deque 版
# Python だと TLE


from collections import deque


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N, Q = map(int, input().split())
    A = deque(map(int, input().split()))
    qs = [tmap(int, input().split()) for _ in range(Q)]

    for t, x, y in qs:
        if t == 1:
            A[x - 1], A[y - 1] = A[y - 1], A[x - 1]
        elif t == 2:
            A.rotate()
        else:
            print(A[x - 1])


solve()
