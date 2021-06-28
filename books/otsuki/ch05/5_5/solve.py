# 文字列 S, T 間の編集距離を求める

def edit_distance(s, t, memo):
    key = (s, t)
    if cache := memo.get(key):
        return cache

    if not s:
        result = len(t)
    elif not t:
        result = len(s)

    elif s[0] == t[0]:
        result = edit_distance(s[1:], t[1:], memo)

    else:
        result = min(edit_distance(s[1:], t[1:], memo) + 1,
                     edit_distance(s[1:], t, memo) + 1,
                     edit_distance(s, t[1:], memo) + 1)

    memo[key] = result
    return result


S = input().strip()
T = input().strip()

print(edit_distance(S, T, {}))


# 普通の DP バージョン
#
# from collections import defaultdict
#
# # dp[(n,m)] => S の最初の n 文字と T の最初の m 文字の編集距離（1-origin）
# dp = defaultdict(int)
#
# for i in range(len(S) + 1):
#     # s => S の i 文字目まで
#     # t => T の i 文字目まで
#     # として以下のコメントを書く
#     for j in range(len(T) + 1):
#         if i == 0:
#             # s が 0 文字なので t をあるだけ削除するしかない
#             dp[(i, j)] = j
#         elif j == 0:
#             # t が 0 文字なので s をあるだけ削除するしかない
#             dp[(i, j)] = i
#         else:
#             if S[i - 1] == T[j - 1]:
#                 # 比較位置が同じ文字なので何もしない
#                 dp[(i, j)] = dp[i - 1, j - 1]
#             else:
#                 # なんらかの編集が必要。コストが最小のものを採用する
#                 dp[(i, j)] = min(dp[i - 1, j - 1] + 1,  # 比較位置の文字を同じにする
#                                  dp[i - 1, j] + 1,      # s を 1 文字削る
#                                  dp[i, j - 1] + 1)      # t を 1 文字削る
#
# print(dp[(len(S), len(T))])
