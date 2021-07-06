def lmap(fn, seq): return list(map(fn, seq))


def solve():
    H, W = map(int, input().split())
    N = int(input())
    A = lmap(int, input().split())

    field = [[-1] * W for _ in range(H)]

    color = 0
    color_cnt = A[0]
    for y in range(H):
        for x in (range(W) if y % 2 == 0 else reversed(range(W))):
            field[y][x] = color + 1
            color_cnt -= 1
            if color_cnt <= 0:
                color += 1
                if color < N:
                    color_cnt = A[color]

    for line in field:
        print(*line)


solve()
