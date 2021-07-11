def dptable(dim, value):
    if isinstance(dim, int):
        return [value] * dim
    elif len(dim) == 2:
        return [[value] * dim[1] for _ in range(dim[0])]
    else:
        return [[[value] * dim[2] for _ in range(dim[1])] for _ in range(dim[0])]


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N, A = map(int, input().split())
    X = lmap(int, input().split())
    K = sum(X)

    dp = dptable((N + 1, N + 1, K + 1), 0)
    dp[0][0][0] = 1

    for i in range(N):
        x = X[i]
        for j in range(0, i + 1):
            for k in range(K + 1):
                if k + x <= K:
                    # x を引いた場合
                    dp[i + 1][j + 1][k + x] += dp[i][j][k]
                # x を引かなかった場合
                dp[i + 1][j][k] += dp[i][j][k]

    # 平均を A にできる引き方を集計
    results = []
    for i in range(1, N + 1):
        if i * A <= K:
            results.append(dp[N][i][i * A])

    print(sum(results))


solve()
