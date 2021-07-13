def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N, T = map(int, input().split())
    A = lmap(int, input().split())

    result = T
    for i in range(1, N):
        result += T
        if A[i] < A[i - 1] + T:
            result -= A[i - 1] + T - A[i]

    print(result)


solve()
