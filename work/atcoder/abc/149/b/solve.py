def solve():
    A, B, K = map(int, input().split())

    print(max(0, A - K), max(0, B + min(0, A - K)))


solve()
