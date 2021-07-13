def lmap(fn, seq): return list(map(fn, seq))


def solve():
    _, K = map(int, input().split())
    L = lmap(int, input().split())

    L.sort()
    L.reverse()
    print(sum(L[:K]))


solve()
