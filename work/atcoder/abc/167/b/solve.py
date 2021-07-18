def solve():
    A, B, C, K = map(int, input().split())

    ans = min(A, K)
    K = max(K - A - B, 0)
    ans -= K

    print(ans)


solve()
