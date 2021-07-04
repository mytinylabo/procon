from collections import defaultdict


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
        bins = defaultdict(set)
        for i, p in enumerate(map(self.root, range(len(self._parents)))):
            bins[p].add(i)
        return "<UnionFind> " + str(list(bins.values()))


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N, M = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(M)]

    n_bridges = 0
    for i in range(M):
        uf = UnionFind(N)
        for j in range(M):
            if i != j:
                s, t = E[j]
                uf.unite(s - 1, t - 1)  # 0-origin にする

        s, t = E[i]
        if not uf.connected(s - 1, t - 1):
            n_bridges += 1

    print(n_bridges)


solve()
