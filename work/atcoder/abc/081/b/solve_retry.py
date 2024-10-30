def lmap(fn, seq):
    return list(map(fn, seq))


def solve():
    inf = float("inf")

    N = int(input())
    A = lmap(int, input().split())

    def n_shiftable(num):
        i = 0
        while not (num >> i) & 0b1:
            i += 1
        return i

    print(min(map(n_shiftable, A)))


solve()
