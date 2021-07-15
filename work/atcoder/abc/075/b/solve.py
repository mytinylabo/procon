def solve():
    H, W = map(int, input().split())
    S = [list(input().strip()) for _ in range(H)]

    for y in range(H):
        for x in range(W):
            if S[y][x] == "#":
                continue
            bomb = 0
            for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if 0 <= y + dy < H and 0 <= x + dx < W:
                    if S[y + dy][x + dx] == "#":
                        bomb += 1
            S[y][x] = str(bomb)

    for s in S:
        print("".join(s))


solve()
