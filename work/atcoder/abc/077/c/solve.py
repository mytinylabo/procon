from bisect import bisect, bisect_left


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    _ = int(input())
    A, B, C = [lmap(int, input().split()) for _ in range(3)]
    # print(N, A, B, C)

    A.sort()
    C.sort()

    result = 0
    for b in B:
        ai = bisect_left(A, b)
        ci = bisect(C, b)
        result += ai * (len(C) - ci)

    print(result)


solve()
