from itertools import permutations


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
def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N = int(input())
    A = [lmap(int, input().split()) for _ in range(N)]
    M = int(input())
    E = [tmap(int, input().split()) for _ in range(M)]

    adj = adjlist(N, E)
    times = []

    for order in permutations(range(1, N + 1), N):
        valid = True
        time = A[order[0] - 1][0]

        for i in range(1, N):
            valid = valid and (order[i - 1] not in adj[order[i]])
            time = time + A[order[i] - 1][i]

        if valid:
            times.append(time)

    print(min(times) if times else -1)


solve()
