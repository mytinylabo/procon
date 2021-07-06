def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    inf = float("inf")
    N = int(input())
    E = [tmap(int, input().split()) for _ in range(N)]

    cost = inf
    for i, (ia, ib) in enumerate(E):
        for j, (ja, jb) in enumerate(E):
            if i == j:
                cost = min(cost, ia + ib)
            else:
                cost = min(cost, max(ia, jb), max(ib, ja))

    print(cost)


solve()


"""
# ソートして場合分けする方法
# ややこしかったので計算量が間に合うなら
# 全探索でサクッと実装した方がいい

def lmap(fn, seq): return list(map(fn, seq))
def tmap(fn, seq): return tuple(map(fn, seq))

def solve():
    N = int(input())
    E = [tmap(int, input().split()) for _ in range(N)]

    E2 = lmap(lambda e: (e[0], e[1][0], e[1][1]), enumerate(E))

    A = sorted(E2, key=lambda e: e[1])
    B = sorted(E2, key=lambda e: e[2])

    plans = []
    if A[0][0] == B[0][0]:
        plans.append(max(A[0][1], B[1][2]))
        plans.append(max(A[1][1], B[0][2]))
        plans.append(A[0][1] + B[0][2])
    else:
        plans.append(max(A[0][1], B[0][2]))

    print(min(plans))
"""
