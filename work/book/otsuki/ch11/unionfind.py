from collections import defaultdict


class UnionFindSimple:
    # 工夫なしの実装
    def __init__(self, n):
        self.parents = [-1] * n
        self.sizes = [1] * n

    def root(self, x):
        if self.parents[x] == -1:
            return x
        else:
            return self.root(self.parents[x])

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)

        if rx == ry:
            return False
        elif rx < ry:
            self.parents[rx] = ry
        else:
            self.parents[ry] = rx

        return True

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def __str__(self):
        bins = defaultdict(set)
        for i, p in enumerate(map(self.root, range(len(self.parents)))):
            bins[p].add(i)
        return "<UnionFind> " + str(list(bins.values()))

    __repr__ = __str__
