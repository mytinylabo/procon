def dptable(dim, value):
    if isinstance(dim, int):
        return [value] * dim
    elif len(dim) == 2:
        return [[value] * dim[1] for _ in range(dim[0])]
    else:
        return [[[value] * dim[2] for _ in range(dim[1])] for _ in range(dim[0])]


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    S = input().strip()
    K = int(input())

    N = lmap(int, S)
    L = len(N)

    dp = dptable((L + 1, 2, K + 2), 0)
    dp[0][0][0] = 1

    for i in range(L):
        d = N[i]
        for k in range(K + 2):
            k1 = (k + 1) if k <= K else K + 1
            dp[i + 1][1][k1] += dp[i][1][k] * 9
            dp[i + 1][1][k] += dp[i][1][k]

            if d > 0:
                dp[i + 1][1][k1] += dp[i][0][k] * (d - 1)
                dp[i + 1][1][k] += dp[i][0][k]

            if d != 0:
                dp[i + 1][0][k1] += dp[i][0][k]
            else:
                dp[i + 1][0][k] += dp[i][0][k]

    print(dp[L][0][K] + dp[L][1][K])


solve()
