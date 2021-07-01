
# 整数 nums から総和を W にできるか判定する
# それぞれの整数は指定回数まで足してよい

def dptable2(dims, value):
    return [[value] * dims[1] for _ in range(dims[0])]


def solve():
    N, W = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(N)]
    # print(N, W, nums)

    # dp[i][j] ==> i 番目までの整数で作れる総和の j 以下の最大値
    #              それぞれの整数は指定回数まで足してよい（0 回でもよい）
    dp = dptable2((N + 1, W + 1), 0)

    for i in range(1, N + 1):
        n, m = nums[i - 1]
        for j in range(W + 1):
            if j - n >= 0:
                p = n * min(j // n, m)  # m 回まで足せるだけ n を足す
                dp[i][j] = max(dp[i - 1][j - p] + p,
                               dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp)
    print("YES" if dp[N][W] == W else "NO")


solve()
