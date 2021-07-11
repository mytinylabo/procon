def dptable(dim, value):
    if isinstance(dim, int):
        return [value] * dim
    elif len(dim) == 2:
        return [[value] * dim[1] for _ in range(dim[0])]
    else:
        return [[[value] * dim[2] for _ in range(dim[1])] for _ in range(dim[0])]


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    inf = float('inf')

    H, W = map(int, input().split())
    C = [lmap(int, input().split()) for _ in range(10)]
    A = [lmap(int, input().split()) for _ in range(H)]
    # print(H, W, C, A)

    dp = dptable((10, 10), inf)
    for i in range(10):
        for j in range(10):
            dp[i][j] = C[i][j]

    for k in range(10):
        for i in range(10):
            for j in range(10):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    cost = 0
    for y in range(H):
        for x in range(W):
            a = A[y][x]
            if a >= 0:
                cost += dp[a][1]

    print(cost)


solve()
