from collections import deque


def solve():
    sx, sy, tx, ty = map(int, input().split())

    w = tx - sx + 1
    h = ty - sy + 1
    base = deque("U" * h + "R" * w + "D" * h + "L" * w)

    base.rotate(-1)
    r1 = "".join(base)
    base.rotate(2)
    r2 = "".join(base)

    print(r1 + r2)


solve()
