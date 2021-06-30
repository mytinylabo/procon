def solve():
    N = int(input())
    schelude = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0, 0, 0] for _ in range(N + 1)]

    for i in range(1, N + 1):
        a, b, c = schelude[i - 1]

        dp[i][0] = max(dp[i - 1][1] + a,
                       dp[i - 1][2] + a)

        dp[i][1] = max(dp[i - 1][0] + b,
                       dp[i - 1][2] + b)

        dp[i][2] = max(dp[i - 1][0] + c,
                       dp[i - 1][1] + c)

    return max(dp[N])


print(solve())
