def adjlist(n, edges):
    adj = [[] for _ in range(n + 1)]

    for s, t in edges:
        adj[s].append(t)
        adj[t].append(s)

    return adj


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N, M = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(M)]

    adj = adjlist(N, E)

    for es in adj[1:]:
        print(len(es))


solve()
