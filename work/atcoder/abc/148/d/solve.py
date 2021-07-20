def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N = int(input())
    A = lmap(int, input().split())

    n = 0
    for a in A:
        if a == n + 1:
            n += 1

    print(N - n if n else -1)


solve()
