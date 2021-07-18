from collections import deque


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


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    inf = float('inf')

    N, M = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(M)]
    S, T = map(int, input().split())

    adj = adjlist(N, E, directed=True)

    dist = [[inf] * (N + 1) for _ in range(3)]
    todo = deque([(0, S, 0)])

    while todo:
        d, s, n = todo.pop()
        if d > dist[n][s]:
            continue

        for t in adj[s]:
            m = (n + 1) % 3
            c = d + 1
            if c < dist[m][t]:
                dist[m][t] = c
                todo.appendleft((c, t, m))

    d = dist[0][T]
    print(d // 3 if d != inf else -1)


solve()
