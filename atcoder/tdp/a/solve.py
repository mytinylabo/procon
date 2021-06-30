def solve():
    N = int(input())
    ps = list(map(int, input().split()))

    W = sum(ps)

    dp = [[False] * (W + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(1, N + 1):
        p = ps[i - 1]
        for j in range(W + 1):
            if j - p >= 0:
                dp[i][j] = dp[i - 1][j - p] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[i].count(True)


print(solve())
