def solve():
    mod = 10**9 + 7

    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    # print(N, M, A)

    broken = [False] * (N + 2)
    for a in A:
        broken[a] = True

    dp = [0] * (N + 2)
    dp[0] = 1

    for i in range(N):
        for j in range(1, 3):
            if not broken[i + j]:
                dp[i + j] = (dp[i + j] + dp[i]) % mod

    print(dp[N])


solve()
