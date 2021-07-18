from itertools import combinations


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N, M, X = map(int, input().split())
    A = [tmap(int, input().split()) for _ in range(N)]

    ans = []
    for i in range(1, N + 1):
        for bs in combinations(A, i):
            cost, *xs = tmap(sum, (zip(*bs)))
            if all(map(lambda x: x >= X, xs)):
                ans.append(cost)

    print(min(ans) if ans else -1)


solve()
