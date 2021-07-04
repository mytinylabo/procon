def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N, K = map(int, input().split())
    A = lmap(int, input().split())

    d = K // N
    m = K % N
    p = sorted(A)[m]

    for a in A:
        if a < p:
            print(d + 1)
        else:
            print(d)


solve()
