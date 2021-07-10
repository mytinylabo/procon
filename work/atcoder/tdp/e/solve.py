def dptable3(dims, value):
    return [[[value] * dims[2] for _ in range(dims[1])] for _ in range(dims[0])]


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    mod = 10**9 + 7

    D = int(input())
    S = lmap(int, input().strip())
    N = len(S)
    # print(D, S, N)

    dp = dptable3((N + 1, 2, D), 0)
    dp[0][0][0] = 1

    for i in range(N):
        for j in range(D):
            # 以下、S=64385, i=2 として
            # 桁 DP の動きについてのみ解説する（D の条件については割愛）
            for k in range(10):
                # i 桁目までに S 未満が確定するような数字を選んだケースの遷移を考える。
                # S=55... や S=63... など。
                # この場合次の桁は何を選んでもよいので k は [0..9] で動かす。
                dp[i + 1][1][(j + k) % D] += dp[i][1][j]
                dp[i + 1][1][(j + k) % D] %= mod

            for k in range(S[i]):  # S[i]: 0-origin なので「S の左から i+1 桁目の数」
                # i 桁目までに S 未満が確定していない、
                # つまり S と同じ数字を選んだ S=64... のケースの遷移を考える。
                # この場合、次の桁 k が [0..3) = [0..2] の範囲なら
                # S 未満が言えるので、dp[i+1][1] への遷移ができる。
                # 遷移元は S=64... と選んできたので dp[i][0] である。
                dp[i + 1][1][(j + k) % D] += dp[i][0][j]
                dp[i + 1][1][(j + k) % D] %= mod

            # dp[i + 1][1] は左から 3 桁目までで S 未満が確定する場合で、
            # 上記までに
            # ・すでに未満が確定しているので次の桁が何であってもよい（最初の for）
            # ・i+1 桁目を適切に選ぶことで未満を確定させた（2 番目の for）
            # の遷移を処理した。

            # 最後に i+1 桁目まで S と同じ数字を選ぶ場合の遷移。
            # 同じ数字なので、上記までだと k で動かしていた部分が
            # S[i]（S の左から i+1 桁目の数）になっている。
            # 遷移元は S=64... と選んできたので dp[i][0] である。
            dp[i + 1][0][(j + S[i]) % D] = dp[i][0][j]

    print(dp)

    # dp[N][0][0]: S ちょうどが D の倍数であるケース（0 or 1）
    # dp[N][1][0]: S 未満で D の倍数だったケース
    # S 以下の正の整数を考えるので、全桁 0 を選んだ場合を除くため -1 する。
    print(dp[N][0][0] + dp[N][1][0] - 1)


solve()
