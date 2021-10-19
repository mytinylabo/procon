def solve():
    X, Y, Z = map(int, input().split())
    print((X * 2 - Z * 2) // ((Y + Z) * 2))


solve()
