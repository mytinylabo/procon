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


def dptable(dim, value):
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
    V = range(1, N + 1)

    adj, cost = adjcost(N, E)

    dp = dptable((N + 1, N + 1), inf)

    for i in V:
        for j in V:
            if i == j:
                dp[i][j] = 0
            elif j in adj[i]:
                dp[i][j] = cost[i][j]

    for k in V:
        for i in V:
            dpi = dp[i]
            for j in V:
                a = dpi[j]
                b = dpi[k] + dp[k][j]
                dpi[j] = a if a < b else b

    print(min([max(dp[i][1:]) for i in V]))


solve()
