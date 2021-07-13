def solve():
    x, y = map(int, input().split())
    G = [-1, 1, 3, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1]
    #        1  2  3  4  5  6  7  8  9  10 11 12
    print("Yes" if G[x] == G[y] else "No")


solve()
