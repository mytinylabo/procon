
# トポロジカルソート（深さ優先探索）


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


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N, M = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(M)]

    adj = adjlist(N, E, digraph=True)

    order = []
    seen = [False] * N

    def dfs(node):
        seen[node] = True
        # print(node, "in")
        for t in adj[node]:
            if not seen[t]:
                dfs(t)
        # print(node, "out")
        order.append(node)

    for i in range(N):
        if not seen[i]:
            dfs(i)

    # 一意には定まらない
    print(*order[::-1])


solve()
