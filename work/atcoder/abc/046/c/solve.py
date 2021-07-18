def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N = int(input())
    R = [tmap(int, input().split()) for _ in range(N)]

    vt, va = R[0]

    for t, a in R[1:]:
        r = max(-(-vt // t), -(-va // a))
        vt, va = r * t, r * a

    print(vt + va)


solve()
