from collections import defaultdict


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


def lmap(fn, seq): return list(map(fn, seq))
def tmap(fn, seq): return tuple(map(fn, seq))
def lfilter(fn, seq): return list(filter(fn, seq))


def solve():
    inf = float('inf')
    mod = 998244353

    N, M, K = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(M)]

    iadj = adjlist(N, E)

    for

    print(N, M, K, E)


solve()
