def lmap(fn, seq): return list(map(fn, seq))


def solve():
    B = lmap(int, input().split())
    B.sort()
    print(sum(B[:2]))


solve()
