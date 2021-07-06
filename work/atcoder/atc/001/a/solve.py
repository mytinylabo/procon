from collections import deque


def solve():
    H, W = map(int, input().split())

    C = ["#" * (W + 2)]
    for y in range(H):
        C.append("#" + input().strip() + "#")
        x = C[-1].find("s")
        if x >= 0:
            start = (x, y + 1)
    C.append("#" * (W + 2))
    # print(H, W, C, start)

    seen = [[False] * (W + 2) for _ in range(H + 2)]
    todo = deque([start])

    while todo:
        x, y = todo.pop()
        seen[y][x] = True
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if (c := C[ny][nx]) == "g":
                print("Yes")
                exit()
            if not seen[ny][nx] and c != "#":
                todo.append((nx, ny))

    print("No")


solve()
