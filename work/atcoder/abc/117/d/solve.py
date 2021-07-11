from math import log2


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

    N, K = map(int, input().split())
    A = lmap(int, input().split())

    # 桁 DP
    L = int(log2(max(max(A), K))) + 1

    dp = dptable((L + 1, 2), -inf)
    dp[0][0] = 0

    for i in range(L):
        d = L - i - 1
        mask = 1 << d
        zeros, ones = 0, 0

        # A[j] を mask した桁のみ f を計算する。
        # 0 と 1 の数を数えておいて、対応する X の桁が
        #   0 の場合: 1 の数 * mask がこの桁の f の結果
        #   1 の場合: A がビット反転するため、
        #             0 の数 * mask がこの桁の f の結果
        for j in range(N):
            if A[j] & mask:
                ones += 1
            else:
                zeros += 1

        # 未満がすでに確定
        dp[i + 1][1] = max(dp[i][1] + zeros * mask,  # 1 を選ぶ場合
                           dp[i][1] + ones * mask)   # 0 を選ぶ場合

        if K & mask:
            # 0 を選んで未満を確定させる
            # ↑ の未満 => 未満の遷移の値があるため、max で選択する
            dp[i + 1][1] = max(dp[i + 1][1], dp[i][0] + ones * mask)

            # 引き続き S と同じ数を選ぶ（1）
            dp[i + 1][0] = dp[i][0] + zeros * mask
        else:
            # 引き続き S と同じ数を選ぶ（0）
            dp[i + 1][0] = dp[i][0] + ones * mask

    print(max(dp[L][0], dp[L][1]))


solve()
