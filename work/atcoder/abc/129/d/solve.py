def map_with_guards(height, width, guard, mapper):
    field = [[guard] * (width + 2)]
    field += [[guard] + list(map(mapper, input().strip())) + [guard]
              for _ in range(height)]
    field += [[guard] * (width + 2)]
    return field


def solve():
    H, W = map(int, input().split())
    S = map_with_guards(H, W, False, lambda c: c == ".")

    light = [[0] * (W + 2) for _ in range(H + 2)]

    for y in range(1, H + 2):
        cnt = 0
        for x in range(1, W + 2):
            if S[y][x]:
                cnt += 1
            else:
                for i in range(1, cnt + 1):
                    light[y][x - i] += cnt
                cnt = 0

    # print(light)

    for x in range(1, W + 2):
        cnt = 0
        for y in range(1, H + 2):
            if S[y][x]:
                cnt += 1
            else:
                for i in range(1, cnt + 1):
                    light[y - i][x] += cnt
                cnt = 0

    # print(light)
    print(max(map(max, light)) - 1)


solve()
