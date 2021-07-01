def dptable2(dims, value):
    return [[value] * dims[1] for _ in range(dims[0])]


def solve():
    inf = float('inf')

    N, W = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]

    V = sum(list(zip(*items))[1])

    # dp[i][j] ==> i 番目までの商品で価値の総和を j にできるときの重さの総和の最小値
    dp = dptable2((N + 1, V + 1), inf)
    dp[0][0] = 0

    for i in range(1, N + 1):
        w, v = items[i - 1]
        for j in range(V + 1):
            if j - v >= 0:
                dp[i][j] = min(dp[i - 1][j - v] + w,
                               dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    # 総重量 W 以下で選べたときの価値の総和を集め、最大値を答えとする
    picks = []
    for j in range(0, V + 1):
        if dp[N][j] <= W:
            picks.append(j)

    print(max(picks))


solve()
