def lmap(fn, seq): return list(map(fn, seq))
def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    _ = int(input())
    T = lmap(int, input().split())
    M = int(input())
    D = [tmap(int, input().split()) for _ in range(M)]

    t = sum(T)

    for p, x in D:
        print(t - T[p - 1] + x)


solve()
