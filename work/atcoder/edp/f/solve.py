def solve():
    S = input().strip()
    T = input().strip()

    dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

    # 共通の文字を数える
    for i in range(len(S) + 1):
        for j in range(len(T) + 1):
            if i > 0 and j > 0:
                if S[i - 1] == T[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    # DP テーブルから共通文字を復元
    i = len(S)
    j = len(T)
    restore = []
    while i > 0 and j > 0:  # DP テーブルの端に着いたら終了（残っている文字は捨てる）
        if S[i - 1] == T[j - 1]:
            # 文字が一致しているので復元対象
            restore.append(T[j - 1])
            i -= 1  # 左上へ移動
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            # 上か左の DP 値が変わらない方へ移動する。
            # S[i - 1] == T[j - 1] になるまでどちらかの文字列の
            # 末尾を削っていく意味
            i -= 1  # 上へ移動
        else:
            # 上か左のどちらかは必ず DP 値が変わらないので
            # ここに倒れたら左へ移動
            j -= 1

    # print(dp)
    return "".join(restore)[::-1]


print(solve())
