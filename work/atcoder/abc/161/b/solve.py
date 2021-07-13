def lmap(fn, seq): return list(map(fn, seq))
def lfilter(fn, seq): return list(filter(fn, seq))


def solve():
    N, M = map(int, input().split())
    A = lmap(int, input().split())

    total = sum(A)
    nominee = lfilter(lambda v: v >= total / (4 * M), A)

    print("Yes" if len(nominee) >= M else "No")


solve()
