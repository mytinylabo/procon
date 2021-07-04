def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    inf = float("inf")
    N, M = map(int, input().split())
    S = [tmap(int, input().split()) for _ in range(N)]
    C = [tmap(int, input().split()) for _ in range(M)]
    # print(N, M, S, C)

    for sx, sy in S:
        dmin = inf
        for i, (cx, cy) in enumerate(C):
            d = abs(sx - cx) + abs(sy - cy)
            if d < dmin:
                dmin = d
                imin = i + 1
        print(imin)


solve()
