
# 二部グラフ判定（UnionFind）


class UnionFind:
    def __init__(self, n):
        self._parents = [-1] * n
        self._sizes = [1] * n

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


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N, M = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(M)]

    uf = UnionFind(N * 2)

    for s, t in E:
        uf.unite(s, t + N)  # 「s を白で塗る」「t を黒で塗る」をグループ化
        uf.unite(s + N, t)  # 「s を黒で塗る」「t を白で塗る」をグループ化

        # 1-2, 2-3, 3-1 の順に処理した場合
        #
        # 1白-2黒, 1黒-2白
        # 1白-2黒-3白, 1黒-2白-3黒
        # ---- ここまでは矛盾なしない
        # 1白-2黒-3白-1黒-2白-3黒
        # ---- 各頂点が白にも黒にもなり、矛盾

    bipartite = all(map(lambda e: not uf.connected(*e), E))
    print(uf)

    print("Yes" if bipartite else "No")


solve()
