def lmap(fn, seq): return list(map(fn, seq))


def solve():
    _ = int(input())
    A, B = [lmap(int, input().split()) for _ in range(2)]
    # print(N, A, B)

    A.sort()
    B.sort()

    print(sum(map(lambda p: abs(p[0] - p[1]), zip(A, B))))


solve()
