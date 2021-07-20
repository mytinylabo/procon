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
    N, u, v = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(N - 1)]

    adj = adjlist(N, E)

    dist_u = ssspbfs(N, u, adj)
    dist_v = ssspbfs(N, v, adj)

    ans = max([vw for uw, vw in zip(dist_u[1:], dist_v[1:]) if uw < vw])
    print(ans - 1)


solve()
