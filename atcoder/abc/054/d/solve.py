def solve():
    N, Ma, Mb = map(int, input().split())
    chems = [list(map(int, input().split())) for _ in range(N)]

    # 各成分の最大の重さ（全て買ったときの重さ）
    max_a, max_b, _ = map(sum, zip(*chems))

    INF = float('inf')
    dp = [[[INF] * (max_b + 1) for _ in range(max_a + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    # dp[i, ma, mb] => i 番目までの薬品から、成分がぴったり
    #                  ma, mb グラムになるように選んだ時の最小価格

    for i in range(1, N + 1):
        a, b, c = chems[i - 1]
        for j in range(max_a + 1):
            for k in range(max_b + 1):
                if j - a >= 0 and k - b >= 0:
                    dp[i][j][k] = min(dp[i - 1][j - a][k - b] + c,
                                      dp[i - 1][j][k])
                else:
                    dp[i][j][k] = dp[i - 1][j][k]

    # Ma:Mb の整数倍の重さの価格を調べて最小のものを返す
    n = 1
    results = []
    while True:
        if Ma * n > max_a or Mb * n > max_b:
            break
        cost = dp[N][Ma * n][Mb * n]
        if cost != INF:
            results.append(cost)
        n += 1

    return min(results) if results else -1


print(solve())


# def solve():
#     N, Ma, Mb = map(int, input().split())
#     chems = [list(map(int, input().split())) for _ in range(N)]
#     # print(N, Ma, Mb, chems)

#     # 各成分の最大の重さ（全て買ったときの重さ）
#     max_a, max_b, _ = map(sum, zip(*chems))
#     # print(max_a, max_b)

#     INF = float('inf')
#     dp = defaultdict(lambda: INF)
#     dp[-1, 0, 0] = 0
#     # dp[i, ma, mb] => i 番目までの薬品から、成分がぴったり
#     #                  ma, mb グラムになるように選んだ時の最小価格

#     for i in range(N):
#         a, b, c = chems[i]
#         for j in range(max_a + 1):
#             for k in range(max_b + 1):
#                 if j - a >= 0 and k - b >= 0:
#                     dp[i, j, k] = min(dp[i - 1, j - a, k - b] + c,
#                                       dp[i - 1, j, k])
#                 else:
#                     dp[i, j, k] = dp[i - 1, j, k]

#     # Ma:Mb の整数倍の重さの価格を調べて最小のものを返す
#     n = 1
#     results = []
#     while True:
#         if Ma * n > max_a or Mb * n > max_b:
#             break
#         if (cost := dp[N - 1, Ma * n, Mb * n]) != INF:
#             results.append(cost)
#         n += 1

#     return min(results) if results else -1


# print(solve())
