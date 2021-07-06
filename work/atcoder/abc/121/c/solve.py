def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N, M = map(int, input().split())
    S = [tmap(int, input().split()) for _ in range(N)]

    S.sort()

    drinks = 0
    pay = 0
    for a, b in S:
        n = min(b, M - drinks)
        if n == 0:
            break
        drinks += n
        pay += n * a

    print(pay)


solve()
