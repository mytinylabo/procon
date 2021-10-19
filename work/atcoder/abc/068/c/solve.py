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


def ssspbfs(n, s, adj):
    """BFS による単一始点最短経路
    """
    from collections import deque
    inf = float('inf')

    dist = [inf] * (n + 1)
    dist[s] = 0
    todo = deque([s])
    while todo:
        v = todo.pop()
        for t in adj[v]:
            if dist[v] + 1 < dist[t]:
                dist[t] = dist[v] + 1
                todo.appendleft(t)
    return dist


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N, M = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(M)]

    adj = adjlist(N, E)
    dist = ssspbfs(N, 1, adj)

    print("POSSIBLE" if dist[N] == 2 else "IMPOSSIBLE")


solve()
