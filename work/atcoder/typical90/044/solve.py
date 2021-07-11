def lmap(fn, seq): return list(map(fn, seq))
def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N, Q = map(int, input().split())
    A = lmap(int, input().split())
    qs = [tmap(int, input().split()) for _ in range(Q)]

    offset = 0

    for t, x, y in qs:
        if t == 1:
            x2 = (offset + x - 1) % N
            y2 = (offset + y - 1) % N
            A[x2], A[y2] = A[y2], A[x2]

        elif t == 2:
            offset = (offset + N - 1) % N

        else:
            print(A[(offset + x - 1) % N])


solve()
