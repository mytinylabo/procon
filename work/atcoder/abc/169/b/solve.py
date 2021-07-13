def lmap(fn, seq): return list(map(fn, seq))


def solve():
    _ = int(input())
    A = lmap(int, input().split())

    if 0 in A:
        print(0)
        exit()

    limit = 10**18
    acc = 1

    for a in A:
        acc *= a
        if acc > limit:
            print(-1)
            exit()

    print(acc)


solve()
