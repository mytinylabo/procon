def lmap(fn, seq): return list(map(fn, seq))


def solve():
    _ = int(input())
    A = lmap(int, input().split())
    A.sort()
    print(A[-1] - A[0])


solve()
