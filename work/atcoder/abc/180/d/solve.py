def solve():
    X, Y, A, B = map(int, input().split())

    ans = 0

    while X * A < Y and X * (A - 1) < B:
        X *= A
        ans += 1

    if Y - X > 0:
        ans += (Y - X - 1) // B

    print(ans)


solve()
