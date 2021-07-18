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


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N = int(input())
    T = [tmap(int, input().split()) for _ in range(N)]

    Tx = sorted(enumerate(T), key=lambda t: t[1][0])
    Ty = sorted(enumerate(T), key=lambda t: t[1][1])
    E = []

    for i in range(1, N):
        # X の昇順に隣り合う頂点同士に辺を張る（コストは X 座標の差分）
        E.append((Tx[i - 1][0], Tx[i][0], Tx[i][1][0] - Tx[i - 1][1][0]))
        # Y の昇順も同様
        E.append((Ty[i - 1][0], Ty[i][0], Ty[i][1][1] - Ty[i - 1][1][1]))

    # クラスカル法で最小全域木を作る
    E.sort(key=lambda e: e[2])

    uf = UnionFind(N)
    ans = 0

    for s, t, w in E:
        if uf.connected(s, t):
            continue

        uf.unite(s, t)
        ans += w

    print(ans)


solve()
