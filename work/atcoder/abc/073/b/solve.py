def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N = int(input())
    A = [tmap(int, input().split()) for _ in range(N)]

    print(sum(map(lambda a: a[1] - a[0] + 1, A)))


solve()
