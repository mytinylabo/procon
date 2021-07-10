
# 最短路探索: ダイクストラ法（単純な実装）


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
    todo = set(range(N))

    while todo:
        # 未確定の頂点からもっとも dist が小さいものを選択
        # ここの実装が線形検索なので改善の余地がある
        # N=5000, M=25000 で 5 秒程度
        D = [(d, i) for i, d in enumerate(dist) if i in todo]
        D.sort()
        _, v = D[0]
        todo.remove(v)

        for t in adj[v]:
            c = cost[v, t]
            if dist[v] + c < dist[t]:
                dist[t] = dist[v] + c

    print(*dist)


solve()
