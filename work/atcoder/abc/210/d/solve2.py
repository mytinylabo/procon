from itertools import chain

# 提出すると WA になる版
# ランダム生成データでの手元検証だと solve.py と同じ答えになるので
# なんらかのコーナーケースが拾えてない。わからん。


def dptable(dim, value):
    if isinstance(dim, int):
        return [value] * dim
    elif len(dim) == 2:
        return [[value] * dim[1] for _ in range(dim[0])]
    else:
        return [[[value] * dim[2] for _ in range(dim[1])] for _ in range(dim[0])]


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    inf = float('inf')

    H, W, C = map(int, input().split())
    A = [lmap(int, input().split()) for _ in range(H)]

    def calc(cs):
        dp_se = dptable((H, W), inf)
        dp_se[0][0] = cs[0][0]

        for y in range(H):
            for x in range(W):
                if y + 1 < H:
                    dp_se[y + 1][x] = min(dp_se[y][x] + C, cs[y + 1][x])
                if x + 1 < W:
                    dp_se[y][x + 1] = min(dp_se[y][x] + C, cs[y][x + 1])

        dp = dptable((H, W), inf)

        for y in range(H):
            for x in range(W):
                if x == y == 0:
                    continue

                costs = []
                finish = cs[y][x] + C

                if y > 0:
                    costs.append(dp_se[y - 1][x] + finish)
                if x > 0:
                    costs.append(dp_se[y][x - 1] + finish)

                dp[y][x] = min(costs)

        return min(chain(*dp))

    print(min(calc(A), calc(A[::-1])))
