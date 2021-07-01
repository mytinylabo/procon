
# 整数 nums から総和を W にできるか判定する
# それぞれの整数は何度足してもよい（0 回でもよい）

def dptable2(dims, value):
    return [[value] * dims[1] for _ in range(dims[0])]


def solve():
    N, W = map(int, input().split())
    nums = [int(input()) for _ in range(N)]
    # print(N, W, nums)

    # dp[i][j] ==> i 番目までの整数で作れる総和の j 以下の最大値
    #              それぞれの整数は何度足してもよい（0 回でもよい）
    dp = dptable2((N + 1, W + 1), 0)

    for i in range(1, N + 1):
        n = nums[i - 1]
        for j in range(W + 1):
            if j - n >= 0:
                m = n * (j // n)  # 足せるだけ n を足す
                dp[i][j] = max(dp[i - 1][j - m] + m,
                               dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    # print(dp)
    print("YES" if dp[N][W] == W else "NO")


solve()
