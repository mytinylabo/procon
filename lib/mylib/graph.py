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


def adjcostd(n, edges, directed=False):
    """疎グラフ用, cost が辞書
    """
    adj = [set() for _ in range(n + 1)]
    cost = {}

    if directed:
        for s, t, c in edges:
            adj[s].add(t)
            cost[s, t] = c
    else:
        for s, t in edges:
            adj[s].add(t)
            adj[t].add(s)
            cost[s, t] = c
            cost[t, s] = c

    return adj, cost


def tpsort(N, adj, origin=0):
    """トポロジカルソート
       N が大きい時は sys.setrecursionlimit で
       再帰の上限を増やしておくこと。
    """
    seen = [False] * (N + 1)
    order = []

    def dfs(v):
        seen[v] = True
        for t in adj[v]:
            if not seen[t]:
                dfs(t)
        order.append(v)

    vs = range(N) if origin == 0 else range(1, N + 1)
    for v in vs:
        if not seen[v]:
            dfs(v)

    order.reverse()
    return order


class UnionFind:
    def __init__(self, n):
        # 0/1-origin 両対応のため n + 1 で確保する
        self._parents = [-1] * (n + 1)
        self._sizes = [1] * (n + 1)

    def root(self, x):
        if self._parents[x] == -1:
            return x
        else:
            self._parents[x] = self.root(self._parents[x])
            return self._parents[x]

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)

        if rx == ry:
            return False
        elif self._sizes[rx] < self._sizes[ry]:
            self._parents[rx] = ry
            self._sizes[ry] += self._sizes[rx]
        else:
            self._parents[ry] = rx
            self._sizes[rx] += self._sizes[ry]

        return True

    def connected(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return self._sizes[self.root(x)]

    def __repr__(self):
        bins = {}
        for i, p in enumerate(map(self.root, range(len(self._parents)))):
            if p not in bins:
                bins[p] = set()
            bins[p].add(i)
        return f"UnionFind({', '.join(map(str, bins.values()))})"
