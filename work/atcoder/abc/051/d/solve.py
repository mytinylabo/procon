def adjcost(n, edges, directed=False):
    """密グラフ用, cost が二次元リスト
    """
    adj = [set() for _ in range(n + 1)]

    inf = float('inf')
    cost = [[inf] * (n + 1) for _ in range(n + 1)]

    if directed:
        for s, t, c in edges:
            adj[s].add(t)
            cost[s][t] = c
    else:
        for s, t, c in edges:
            adj[s].add(t)
            adj[t].add(s)
            cost[s][t] = c
            cost[t][s] = c

    return adj, cost


def array(dim, value):
    if isinstance(dim, int):
        return [value] * dim
    elif len(dim) == 2:
        return [[value] * dim[1] for _ in range(dim[0])]
    else:
        return [[[value] * dim[2] for _ in range(dim[1])] for _ in range(dim[0])]


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    inf = float('inf')

    N, M = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(M)]

    vs = list(range(1, N + 1))

    dist = array((N + 1, N + 1), inf)
    for i in vs:
        dist[i][i] = 0
    for s, t, c in E:
        dist[s][t] = c
        dist[t][s] = c

    for k in vs:
        for i in vs:
            for j in vs:
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j])

    used = set()

    for i in vs:
        for s, t, c in E:
            if abs(dist[i][s] - dist[i][t]) == c:
                used.add((s, t))

    print(len({(s, t) for s, t, _ in E} - used))


solve()
