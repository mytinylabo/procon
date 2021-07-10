
# 根無し木を根付き木として走査する


def adjlist(n, edges, digraph=False):
    adj = [set() for _ in range(n + 1)]

    if digraph:
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
    N, M, R = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(M)]

    adj = adjlist(N, E)
    # print(adj)

    depth = [0] * N
    subtree_size = [0] * N

    def dfs(v, p=-1, d=0):
        depth[v] = d
        subtree_size[v] = 1
        for c in adj[v]:
            if c != p:
                dfs(c, v, d + 1)
                subtree_size[v] += subtree_size[c]

    dfs(R)

    print(*depth)
    print(*subtree_size)


solve()
