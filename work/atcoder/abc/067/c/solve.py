from itertools import accumulate


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    _ = int(input())
    A = lmap(int, input().split())

    sunuke = list(accumulate(A))
    racoon = list(accumulate(A[::-1]))[::-1]

    print(min(map(lambda a: abs(a[0] - a[1]), zip(sunuke[:-1], racoon[1:]))))


solve()
