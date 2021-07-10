def dptable2(dims, value):
    return [[value] * dims[1] for _ in range(dims[0])]


def solve():
    mod = 10**9 + 7

    T = "atcoder"

    N = int(input())
    S = input().strip()
    # print(N, S)

    dp = dptable2((N + 1, len(T) + 1), 0)
    dp[0][0] = 1

    for i in range(N):
        for j in range(len(T) + 1):
            if j < len(T) and S[i] == T[j]:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= mod

            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= mod

    print(dp[N][len(T)])


solve()
