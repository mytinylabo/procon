from bisect import bisect


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N = int(input())
    A = lmap(int, input().split())
    Q = int(input())
    B = [int(input()) for _ in range(Q)]
    # print(N, A, Q, B)

    A.sort()

    for b in B:
        i = bisect(A, b)

        if i == 0:
            print(abs(A[i] - b))
        elif i == N:
            print(abs(A[-1] - b))
        else:
            print(min(abs(A[i] - b), abs(A[i - 1] - b)))


solve()
