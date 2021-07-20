from collections import deque


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


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    inf = float('inf')

    N, u, v = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(N - 1)]

    adj = adjlist(N, E)

    def bfs(s, es):
        dist = [inf] * (N + 1)
        dist[s] = 0
        todo = deque([s])
        while todo:
            v = todo.pop()
            for t in es[v]:
                if dist[v] + 1 < dist[t]:
                    dist[t] = dist[v] + 1
                    todo.appendleft(t)
        return dist

    # 幅優先検索で u, v からの単一始点最短経路を求める
    dist_u = bfs(u, adj)
    dist_v = bfs(v, adj)

    # u と v の中間点を出し、u から到達不能とする。
    # 中間点が 2 個ある場合は v に近い方を刈る
    adj_u = adjlist(N, E)
    mid = dist_u[v] // 2
    for i in range(1, N + 1):
        if dist_v[i] == mid:
            for t in adj_u[i]:
                # 中間点じゃない点も刈っているが、
                # u が行けない場所なので影響なし
                adj_u[t].remove(i)
            adj_u[i] = set()

    # adj_u は u が v に捕まらずに移動できる部分木の隣接リストになっている。
    # adj_u で到達できる点のうち、元のグラフで v からの最長距離で
    # あるような点を選び、u の目標地点 goal とする。
    # ゲームは v が goal に最短で到達したときに終わるとみなせるので、
    # 最初に求めた dist_v から ans を出す
    dist_u2 = bfs(u, adj_u)
    dist_v2 = [dist_v[i] for i in range(1, N + 1) if dist_u2[i] != inf]
    goal = dist_v.index(max(dist_v2))
    ans = dist_v[goal]

    # u が動いて終わるか v が動いて終わるかはノードの偶奇で決まるが、
    # どっちにしても ans - 1 が v の動く回数になる
    print(ans - 1)


solve()
