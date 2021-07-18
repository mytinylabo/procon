def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N, K = map(int, input().split())
    A = [tmap(int, input().split()) for _ in range(N)]

    A.sort()

    i = 0
    while K > 0:
        n, c = A[i]
        K -= c
        i += 1

    print(A[i - 1][0])


solve()
