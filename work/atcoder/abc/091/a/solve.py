def solve():
    N, M = sorted(map(int, input().split()))

    if N * M == 1:
        print(1)
    elif N == 1:
        print(M - 2)
    else:
        print(N * M - N * 2 - M * 2 + 4)


solve()
