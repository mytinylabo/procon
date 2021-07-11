def dptable(dim, value):
    if isinstance(dim, int):
        return [value] * dim
    elif len(dim) == 2:
        return [[value] * dim[1] for _ in range(dim[0])]
    else:
        return [[[value] * dim[2] for _ in range(dim[1])] for _ in range(dim[0])]


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    A, B = map(int, input().split())
    # print(A, B)

    def include49(n):
        ds = lmap(int, str(n))
        ln = len(ds)

        dp = dptable((ln + 1, 2, 2), 0)
        dp[0][0][0] = 1

        for i in range(ln):
            for j in range(10):
                if j == 4 or j == 9:
                    dp[i + 1][1][1] += dp[i][1][0]
                else:
                    dp[i + 1][1][0] += dp[i][1][0]
                dp[i + 1][1][1] += dp[i][1][1]

            for j in range(ds[i]):
                if j == 4:
                    dp[i + 1][1][1] += dp[i][0][0]
                else:
                    dp[i + 1][1][0] += dp[i][0][0]
                dp[i + 1][1][1] += dp[i][0][1]

            if ds[i] == 9 or ds[i] == 4:
                dp[i + 1][0][1] += dp[i][0][0]
            else:
                dp[i + 1][0][0] += dp[i][0][0]
            dp[i + 1][0][1] += dp[i][0][1]

        return dp[ln][0][1] + dp[ln][1][1]

    print(include49(B) - include49(A - 1))


solve()
