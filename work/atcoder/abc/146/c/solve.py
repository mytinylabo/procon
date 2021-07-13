def solve():
    A, B, X = map(int, input().split())

    left = 0
    right = 10**9 + 1

    while right - left > 1:
        mid = (right + left) // 2
        if A * mid + B * len(str(mid)) <= X:
            left = mid
        else:
            right = mid

    print(left)


solve()
