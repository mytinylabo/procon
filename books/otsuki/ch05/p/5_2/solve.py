def solve():
    N, W = map(int, input().split())
    nums = [int(input()) for _ in range(N)]
    # print(N, W, nums)

    dp = [[False] * (W + 1) for _ in range(N + 1)]
    dp[0][0] = True

    for i in range(1, N + 1):
        n = nums[i - 1]
        for j in range(W + 1):
            if j - n >= 0:
                dp[i][j] = dp[i - 1][j - n] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return "YES" if dp[N][W] else "NO"


print(solve())
