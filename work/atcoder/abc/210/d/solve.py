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

    H, W, C = map(int, input().split())
    A = [lmap(int, input().split()) for _ in range(H)]

    def calc(cs):
        dp = dptable((H + 1, W + 1), inf)
        dp[0][0] = cs[0][0]

        result = inf

        for y in range(H):
            for x in range(W):
                if y:
                    dp[y][x] = min(dp[y - 1][x] + C, cs[y][x])
                    result = min(result, dp[y - 1][x] + C + cs[y][x])
                if x:
                    dp[y][x] = min(dp[y][x - 1] + C, cs[y][x], dp[y][x])
                    result = min(result, dp[y][x - 1] + C + cs[y][x])

        return result

    print(min(calc(A), calc(A[::-1])))


solve()
