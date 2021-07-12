def lmap(fn, seq): return list(map(fn, seq))


def solve():
    C = lmap(int, input().split())
    C.sort()
    print("Yes" if C[0] + C[1] == C[2] else "No")


solve()
