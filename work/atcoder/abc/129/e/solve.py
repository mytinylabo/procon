def dptable2(dims, value):
    return [[value] * dims[1] for _ in range(dims[0])]


def solve():
    mod = 10**9 + 7

    L = input().strip()
    N = len(L)

    dp = dptable2((N + 1, 2), 0)
    dp[0][0] = 1

    for i in range(N):
        # i までに未満が確定しているので
        # 次は 0,1 どっちでも未満を維持できる
        # 0 なら (a, b) の組み合わせは (0, 0) のみ
        # 1 なら (1, 0) または (0, 1) なので合計 3 分岐
        dp[i + 1][1] += (dp[i][1] * 3) % mod
        dp[i + 1][1] %= mod

        if L[i] == "1":
            # i までに未満が確定してないが、
            # 次が 1 なので 0 を選べば未満を確定できる
            # 0 を選ぶなら (a, b) の組み合わせは (0, 0) のみ
            dp[i + 1][1] += dp[i][0]
            dp[i + 1][1] %= mod

            # 引き続き入力値と同じ桁を選ぶ場合の遷移
            # 1 なら (1, 0) または (0, 1) の 2 分岐
            dp[i + 1][0] += (dp[i][0] * 2) % mod
            dp[i + 1][0] %= mod
        else:
            # 0 なら (0, 0) のみ
            dp[i + 1][0] += dp[i][0]
            dp[i + 1][0] %= mod

    print((dp[N][0] + dp[N][1]) % mod)


solve()
