def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N = int(input())
    W = [tmap(int, input().split()) for _ in range(N)]
    # print(N, W)

    W.sort(key=lambda w: w[1])

    cur = 0
    for d, t in W:
        cur += d
        # print(cur - d, d, t)
        if cur > t:
            print("No")
            exit()

    print("Yes")


solve()
