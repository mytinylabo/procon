
# 最短路探索: ベルマンフォード法


def adjcostd(n, edges, digraph=False):
    """疎グラフ用, cost が辞書
    """
    adj = [set() for _ in range(n + 1)]
    cost = {}

    if digraph:
        for s, t, c in edges:
            adj[s].add(t)
            cost[s, t] = c
    else:
        for s, t in edges:
            adj[s].add(t)
            adj[t].add(s)
            cost[s, t] = c
            cost[t, s] = c

    return adj, cost


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    inf = float('inf')

    N, M, s = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(M)]

    adj, cost = adjcostd(N, E, digraph=True)

    dist = [inf] * N
    dist[s] = 0
    negcycle = False

    for i in range(N):
        update = False
        for v in range(N):
            if dist[v] == inf:
                continue

            for t in adj[v]:
                c = cost[v, t]
                # print(i, v, t, dist[v] + c, dist[t])
                if dist[v] + c < dist[t]:
                    dist[t] = dist[v] + c
                    update = True
                # print(update, "==>", dist[t])

        if not update:
            break

        negcycle = i == N - 1 and update

    print(*dist)
    print(negcycle)


solve()
