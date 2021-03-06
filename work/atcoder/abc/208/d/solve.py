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
    inf = 1 << 60

    N, M = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(M)]

    adj, cost = adjcost(N, E, directed=True)

    V = list(range(1, N + 1))
    dp = dptable((N + 1, N + 1, N + 1), inf)
    for i in V:
        for j in V:
            if i == j:
                dp[0][i][j] = 0
            elif j in adj[i]:
                dp[0][i][j] = cost[i][j]

    result = 0
    for k in range(N):
        for i in V:
            dpk = dp[k]
            dpki = dpk[i]
            dpk1i = dp[k + 1][i]
            dpkk1 = dpk[k + 1]
            for j in V:
                a = dpki[j]
                b = dpki[k + 1] + dpkk1[j]
                dpk1i[j] = a if a < b else b
                result += 0 if dpk1i[j] == inf else dpk1i[j]

    print(result)


solve()
