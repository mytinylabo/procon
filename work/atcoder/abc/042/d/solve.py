def bexp(base, exponent, mod):
    """法 mod において二分累乗法で base**exponent を計算する
    """
    result = 1
    powb = base
    i = 0
    while shifted := exponent >> i:
        if shifted & 1:
            result = (result * powb) % mod
        powb = (powb * powb) % mod
        i += 1

    return result


def use_fact(n, mod):
    """法 mod における 0! .. n! のテーブルを生成する
    """
    m = n + 1
    fact = [0] * m
    ifact = [0] * m

    fact[0] = 1
    ifact[0] = 1

    for i in range(1, m):
        fact[i] = (fact[i - 1] * i) % mod

    ifact[m - 1] = bexp(fact[m - 1], mod - 2, mod)
    for i in reversed(range(1, m - 1)):
        # i = m-2, m-3, ... , 2, 1
        ifact[i] = (ifact[i + 1] * (i + 1)) % mod

    return (fact, ifact)


limit = 10**9 + 7
H, W, A, B = map(int, input().split(" "))

fact, ifact = use_fact(H + W, limit)


def n_comb(n, r):
    denom = ifact[r] * ifact[n - r] % limit
    return fact[n] * denom % limit


n_paths = 0
for y in range(H - A):
    # スタートから中継地点まで
    pa = n_comb(B + y - 1, y)
    # 中継地点からゴールまで
    pb = n_comb((W - B - 1) + (H - y - 1), H - y - 1)

    n_paths = (n_paths + pa * pb) % limit


print(n_paths)
