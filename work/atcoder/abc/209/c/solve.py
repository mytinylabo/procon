def lmap(fn, seq): return list(map(fn, seq))


def solve():
    mod = 10**9 + 7

    _ = int(input())
    C = lmap(int, input().split())
    # print(N, C)

    C.sort()

    result = 1
    for i, c in enumerate(C):
        if i >= c:
            print(0)
            exit()

        result = (result * (c - i)) % mod

    print(result)


solve()
