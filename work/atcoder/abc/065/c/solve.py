def factorials(n, p):
    """法 p における 0! .. n! と
       その逆元のテーブルを生成する。
       p は素数であること。
    """
    m = n + 1
    fact = [0] * m
    ifact = [0] * m

    fact[0] = 1
    ifact[0] = 1

    for i in range(1, m):
        fact[i] = (fact[i - 1] * i) % p

    ifact[m - 1] = pow(fact[m - 1], p - 2, p)
    for i in reversed(range(1, m - 1)):
        # i = m-2, m-3, ... , 2, 1
        ifact[i] = (ifact[i + 1] * (i + 1)) % p

    return (fact, ifact)


def solve():
    mod = 10**9 + 7

    N, M = map(int, input().split())

    fact, _ = factorials(max(N, M), mod)

    if abs(N - M) >= 2:
        print(0)
        exit()

    ans = (fact[N] * fact[M]) % mod

    print(ans if abs(N - M) % 2 == 1 else (ans * 2) % mod)


solve()
