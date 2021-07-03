def solve():
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]

    M = max(map(lambda h: h[0] + h[1] * N, H))

    left = 0
    right = M

    while right - left > 1:
        mid = (left + right) // 2
        # 時間制限が厳しい順にソート
        ts = sorted(map(lambda h: (mid - h[0]) // h[1], H))

        # print(left, mid, right)
        if all(map(lambda t: t[1] >= t[0], enumerate(ts))):
            # ペナルティ mid 以下ですべての風船を割れる
            # ==> 左の範囲を検索
            right = mid
        else:
            # 割れない
            # ==> 右の範囲を検索
            left = mid
        # print("  ==>", left, right, right - left)

    print(right)


solve()
