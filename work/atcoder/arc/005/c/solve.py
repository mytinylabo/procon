from collections import deque


def array(dim, value):
    if isinstance(dim, int):
        return [value] * dim
    elif len(dim) == 2:
        return [[value] * dim[1] for _ in range(dim[0])]
    else:
        return [[[value] * dim[2] for _ in range(dim[1])] for _ in range(dim[0])]


def solve():
    inf = float('inf')

    H, W = map(int, input().split())
    A = []
    for y in range(H):
        line = input().strip()
        if "s" in line:
            sx, sy = line.index("s"), y
        if "g" in line:
            gx, gy = line.index("g"), y
        A.append(line)

    dist = array((H, W), inf)
    dist[sy][sx] = 0
    todo = deque([(sx, sy)])

    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    while todo:
        x, y = todo.pop()
        c = dist[y][x]

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < W and 0 <= ny < H:
                dc = 0 if A[ny][nx] != "#" else 1
                if c + dc < dist[ny][nx]:
                    dist[ny][nx] = c + dc
                    if dc:
                        todo.appendleft((nx, ny))
                    else:
                        todo.append((nx, ny))

    print("YES" if dist[gy][gx] <= 2 else "NO")


solve()
