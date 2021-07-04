from math import sin, pi


def solve():
    A, B, C = map(int, input().split())

    def f(t):
        return A * t + B * sin(C * pi * t)

    left = 0
    right = 101
    while right - left > 10**(-12):
        mid = (right + left) / 2
        if f(mid) >= 100:
            right = mid
            # print(right)
        else:
            left = mid

    print(right)

    # error = abs(f(right) - 100)
    # print(error <= 10**(-6))


solve()
