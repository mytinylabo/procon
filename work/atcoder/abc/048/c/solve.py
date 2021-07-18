def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N, x = map(int, input().split())
    A = lmap(int, input().split())

    result = 0
    for i in range(1, N):
        n = A[i - 1] + A[i]
        if n > x:
            ai = min(A[i], n - x)
            ai1 = 0 if A[i] > ai else A[i - 1] - x

            result += ai + ai1

            A[i] -= ai
            A[i - 1] -= ai1

    print(result)


solve()
