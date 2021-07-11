
# 自前で順列列挙
# PyPy で TLE ギリギリ


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


def solve():
    N = int(input())
    A = [lmap(int, input().split()) for _ in range(N)]
    M = int(input())
    E = [lmap(int, input().split()) for _ in range(M)]

    adj = adjlist(N, E)
    times = []

    def rec(runners, last, time):
        if len(runners) == 0:
            times.append(time)
            return

        for r in runners:
            if last not in adj[r]:
                i = N - len(runners)
                rec(runners - {r}, r, time + A[r - 1][i])

    rec(set(range(1, N + 1)), -1, 0)
    print(min(times) if times else -1)


solve()
