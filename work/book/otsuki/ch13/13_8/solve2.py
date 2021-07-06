
# 二部グラフ判定（深さ優先検索）


def tmap(fn, seq): return tuple(map(fn, seq))


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


def solve():
    N, M = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(M)]

    colors = [-1] * (N + 1)
    adj = adjlist(N, E)

    def dfs(node, color):
        colors[node] = color

        for t in adj[node]:
            if colors[t] == -1:
                if not dfs(t, (color + 1) % 2):
                    return False
            elif colors[t] == color:
                return False

        return True

    bipartite = dfs(0, 1)
    print("Yes" if bipartite else "No")


solve()
