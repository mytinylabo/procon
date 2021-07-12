def solve():
    X, Y = map(int, input().split())

    i = 1
    while X * 2**(i - 1) <= Y:
        i += 1

    print(i - 1)


solve()

"""
X * 2^(n-1) =< Y の n を求める
n-1 =< Y/X
n =< log2(Y/X) + 1

print(int(math.log2(Y/X) + 1))
これは 1 WA だった…
"""
