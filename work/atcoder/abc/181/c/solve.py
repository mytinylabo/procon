from itertools import combinations


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N = int(input())
    A = [tmap(int, input().split()) for _ in range(N)]

    for (ax, ay), (bx, by), (cx, cy) in combinations(A, 3):
        x1, y1 = bx - ax, by - ay
        x2, y2 = cx - ax, cy - ay

        if x1 * y2 == x2 * y1:
            print("Yes")
            exit()

    print("No")


solve()
