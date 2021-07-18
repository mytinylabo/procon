def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N, K = map(int, input().split())
    E = lmap(int, input().split())

    adj = {}
    for i, t in enumerate(E):
        adj[i + 1] = t

    dist = [0] * (N + 1)
    s = 1
    k = 0

    while True:
        k += 1
        s = adj[s]

        if k == K:
            break

        if dist[s] > 0:
            p = k - dist[s]
            m = (K - k) % p
            for _ in range(m):
                s = adj[s]
            break

        dist[s] = k

    print(s)


solve()
