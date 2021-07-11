from math import pi, sqrt, sin, cos, atan2, degrees, isclose


def solve():
    T = int(input())
    L, X, Y = map(int, input().split())
    Q = int(input())
    E = [int(input()) for _ in range(Q)]
    # print(T, L, X, Y, Q, E)

    r = L / 2

    def pos(t):
        y = -sin(2 * pi * (t / T)) * r
        z = -cos(2 * pi * (t / T)) * r + r
        return y, z

    def dist(x, y):
        return sqrt((X - x)**2 + (Y - y)**2)

    for e in E:
        y, z = pos(e)
        d = dist(0, y)
        if isclose(0, d):
            print(90.0)
        else:
            a = atan2(abs(z), d)
            print(degrees(a))


solve()
