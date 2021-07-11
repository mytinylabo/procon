def solve():
    N, K, X, Y = [int(input()) for _ in range(4)]

    k = max(0, N - K)
    n = N - k
    print(n * X + k * Y)


solve()
