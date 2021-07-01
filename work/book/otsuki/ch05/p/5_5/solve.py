
# 整数 nums から総和を W にできるか判定する
# それぞれの整数は何度足してもよい（0 回でもよい）

def dptable2(dims, value):
    return [[value] * dims[1] for _ in range(dims[0])]


def solve():
    N, W = map(int, input().split())
    nums = [int(input()) for _ in range(N)]
    # print(N, W, nums)

    # dp[i][j] ==> i 番目までの整数で総和 j にできるかどうか
    #              それぞれの整数は何度足してもよい（0 回でもよい）
    dp = dptable2((N + 1, W + 1), False)
    dp[0][0] = True

    for i in range(1, N + 1):
        n = nums[i - 1]
        for j in range(W + 1):
            if j - n >= 0:
                dp[i][j] = (dp[i - 1][j - n] or dp[i - 1][j] or dp[i][j - n])
                # dp[i - 1][j - n]  i-1 番目までで総和を j-n にできているか（n を 1 回足せばよい）
                # dp[i - 1][j]      i-1 番目までで総和を j にできているか（n は足さなくてよい）
                # dp[i][j - n]      i 番目までで総和を j-n にできているか（n をさらに 1 回足せばよい）
            else:
                dp[i][j] = dp[i - 1][j]

    # print(dp)
    print("YES" if dp[N][W] else "NO")


solve()
