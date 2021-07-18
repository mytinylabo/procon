def lmap(fn, seq): return list(map(fn, seq))


def solve():
    _ = int(input())
    A = lmap(int, input().split())

    rates = [(1, 399),
             (400, 799),
             (800, 1199),
             (1200, 1599),
             (1600, 1999),
             (2000, 2399),
             (2400, 2799),
             (2800, 3199)]

    cnt = {r: 0 for r in rates}
    predator = 0

    for a in A:
        for r in rates:
            left, right = r
            if left <= a <= right:
                cnt[r] += 1
                break

        if a >= 3200:
            predator += 1

    unused = list(cnt.values()).count(0)
    ans_min = len(rates) - unused

    print(max(1, ans_min), ans_min + predator)


solve()
