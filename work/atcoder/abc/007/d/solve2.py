def dptable(dim, value):
    if isinstance(dim, int):
        return [value] * dim
    elif len(dim) == 2:
        return [[value] * dim[1] for _ in range(dim[0])]
    else:
        return [[[value] * dim[2] for _ in range(dim[1])] for _ in range(dim[0])]


def solve():
    A, B = map(int, input().split())
    # print(A, B)

    def include49(n):
        ds = list(str(n))
        ln = len(ds)

        dp = dptable((ln + 1, 2), 0)

        for i in range(ln):
            d = int(ds[i])
            num = int("".join(ds[:i])) if i > 0 else 0

            for j in range(10):
                if j == 4 or j == 9:
                    dp[i + 1][1] += num
                else:
                    dp[i + 1][1] += dp[i][1]

            for j in range(d):
                if j == 4:
                    dp[i + 1][1] += 1
                else:
                    dp[i + 1][1] += dp[i][0]

            if d == 9 or d == 4:
                dp[i + 1][0] += 1
            else:
                dp[i + 1][0] += dp[i][0]

        return dp[ln][0] + dp[ln][1]

    print(include49(B) - include49(A - 1))


solve()
