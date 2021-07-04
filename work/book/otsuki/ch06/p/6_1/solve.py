from bisect import bisect_left


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    _ = int(input())
    A = lmap(int, input().split())
    # print(N, A)

    sorted_A = sorted(A)

    order = []
    for a in A:
        order.append(bisect_left(sorted_A, a))

    print(*order)


solve()
