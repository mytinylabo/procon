def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    W, H, N = map(int, input().split())
    P = [tmap(int, input().split()) for _ in range(N)]

    left, top, right, bottom = 0, H, W, 0

    for x, y, a in P:
        if a == 1:
            left = max(left, x)
        elif a == 2:
            right = min(right, x)
        elif a == 3:
            bottom = max(bottom, y)
        else:
            top = min(top, y)

    w = max(0, right - left)
    h = max(0, top - bottom)

    print(w * h)


solve()
