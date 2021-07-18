def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N = int(input())
    A = [tmap(int, input().split()) for _ in range(N)]

    ans = 0
    for a, b in A:
        ans += (a + b) * (b - a + 1) // 2

    print(ans)


solve()
