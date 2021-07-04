class UnionFind:
    def __init__(self, n):
        self._parents = [-1] * n
        self._sizes = [1] * n

    def root(self, x):
        if self._parents[x] == -1:
            return x
        else:
            self._parents[x] = self.root(self._parents[x])
            return self.root(self._parents[x])

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


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N, M = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(M)]
    # print(N, M, E)

    n_pairs = N * (N - 1) // 2
    results = [n_pairs]
    uf = UnionFind(N)

    # 全ての島が分断されている状態から橋をリストの逆順に繋いでいく
    for a, b in E[::-1]:
        if uf.connected(a - 1, b - 1):
            # そもそも別の橋で繋がってるので飛ばしてよい
            results.append(results[-1])
            continue

        sa = uf.size(a - 1)
        sb = uf.size(b - 1)

        uf.unite(a - 1, b - 1)

        # 橋で繋がったぶんの不便さを減らす
        results.append(results[-1] - sa * sb)

    # 結果を反転すると橋が壊されていく記録になる
    for n in results[:-1][::-1]:
        print(n)


solve()
