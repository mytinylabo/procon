
# DP


def dptable(dim, value):
    if isinstance(dim, int):
        return [value] * dim
    elif len(dim) == 2:
        return [[value] * dim[1] for _ in range(dim[0])]
    else:
        return [[[value] * dim[2] for _ in range(dim[1])] for _ in range(dim[0])]


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    inf = float('inf')

    S = lmap(int, input().strip())
    L = len(S)

    dp = dptable((L + 1, 3), inf)
    dp[0][0] = 0

    for i in range(L):
        d = S[i]
        for j in range(3):
            if L - dp[i][j] >= 2:
                # 2 桁以上残っているなら消す場合を考える
                dp[i + 1][j] = min(dp[i + 1][j],
                                   dp[i][j] + 1)

            # 消さない場合
            k = (j * 10 + d) % 3
            dp[i + 1][k] = min(dp[i + 1][k],
                               dp[i][j])

    print(dp[L][0] if dp[L][0] != inf else -1)


solve()
