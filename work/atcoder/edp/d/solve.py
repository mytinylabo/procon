def solve():
    N, W = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(N)]

    dp = [0] * (W + 1)
    for i in range(N):
        w, v = items[i]
        for sum_w in range(W - w, -1, -1):
            if dp[sum_w + w] < dp[sum_w] + v:
                dp[sum_w + w] = dp[sum_w] + v

    return dp[W]


print(solve())


# 素直に解くパターン
# AtCoder だと時間が足りない…
#
# from collections import defaultdict

# N, W = map(int, input().split())
# items = [tuple(map(int, input().split())) for _ in range(N)]

# dp = defaultdict(int)

# for i in range(N):
#     w, v = items[i]
#     for sum_w in range(W + 1):
#         if sum_w - w >= 0:
#             # items[i] を選べる
#             dp[(i, sum_w)] = max(dp[(i - 1, sum_w - w)] + v,  # 選ぶ
#                                  dp[(i - 1, sum_w)])         # 選ばない
#         else:
#             # items[i] を選べない
#             dp[(i, sum_w)] = dp[(i - 1, sum_w)]

# print(dp[(N - 1, W)])
