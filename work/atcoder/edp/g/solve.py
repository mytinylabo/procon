import sys
sys.setrecursionlimit(10**6)


def adjlist(n, edges, directed=False):
    adj = [set() for _ in range(n + 1)]

    if directed:
        for s, t in edges:
            adj[s].add(t)
    else:
        for s, t in edges:
            adj[s].add(t)
            adj[t].add(s)

    return adj


def tpsort(N, adj):
    seen = [False] * (N + 1)
    order = []

    def dfs(v):
        seen[v] = True
        for t in adj[v]:
            if not seen[t]:
                dfs(t)
        order.append(v)

    for v in range(1, N + 1):
        if not seen[v]:
            dfs(v)

    order.reverse()
    return order


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N, M = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(M)]

    adj = adjlist(N, E, directed=True)
    order = tpsort(N, adj)

    dp = [0] * (N + 1)

    for v in order:
        for t in adj[v]:
            if dp[v] + 1 > dp[t]:
                dp[t] = dp[v] + 1

    print(max(dp))


solve()
