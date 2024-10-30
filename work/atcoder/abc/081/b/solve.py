def lmap(fn, seq):
    return list(map(fn, seq))


def solve():
    inf = float("inf")

    N = int(input())
    A = lmap(int, input().split())

    min_n = inf

    for a in A:
        n = 0
        while a % 2 == 0:
            a //= 2
            n += 1
        min_n = min(n, min_n)

    print(min_n)


solve()
