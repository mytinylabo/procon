def lmap(fn, seq): return list(map(fn, seq))


def solve():
    _ = int(input())
    K = int(input())
    X = lmap(int, input().split())

    print(sum(map(lambda x: min(x, abs(x - K)) * 2, X)))


solve()
