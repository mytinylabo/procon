from collections import defaultdict


def solve():
    N, M = map(int, input().split())
    edges = defaultdict(set)
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a].add(b)
        edges[b].add(a)

    n_paths = 0
    seen = [False] * (N + 1)
    # ノード番号が 1-origin なので 0 は True にしておく
    seen[0] = True

    def dfs(node):
        seen[node] = True

        if all(seen):
            nonlocal n_paths
            n_paths += 1

        for next in edges[node]:
            if not seen[next]:
                dfs(next)

        seen[node] = False

    dfs(1)
    print(n_paths)


solve()
