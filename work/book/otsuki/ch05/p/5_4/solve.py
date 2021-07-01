
# 整数 nums から K 個以下を選んで総和を W にできるか判定する

def dptable2(dims, value):
    return [[value] * dims[1] for _ in range(dims[0])]


def solve():
    inf = float('inf')

    N, K, W = map(int, input().split())
    nums = [int(input()) for _ in range(N)]
    # print(N, K, W, nums)

    # dp[i][j] ==> i 番目までの整数で総和を j にできるときの最小個数
    #              総和を j にできなければ inf
    dp = dptable2((N + 1, W + 1), inf)
    dp[0][0] = 0

    for i in range(1, N + 1):
        n = nums[i - 1]
        for j in range(W + 1):
            if j - n >= 0 and dp[i - 1][j - n] < K:
                dp[i][j] = min(dp[i - 1][j - n] + 1,
                               dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    print("YES" if dp[N][W] != inf else "NO")


solve()
