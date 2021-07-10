
# トポロジカルソート（幅優先探索）


from collections import deque


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N, M = map(int, input().split())
    E = [tmap(int, input().split()) for _ in range(M)]

    adj = [set() for _ in range(N)]
    cnt = [0] * N  # cnt[i] ==> ノード i に入ってくる辺の数

    for s, t in E:
        adj[s].add(t)
        cnt[t] += 1

    # cnt[0] ならトポロジカルソートの先頭になれる
    todo = deque([cnt.index(0)])
    order = []

    while todo:
        node = todo.pop()
        order.append(node)  # 次の順番として採用
        for t in adj[node]:
            cnt[t] -= 1  # 採用したノードを削除する
            if cnt[t] == 0:
                # 削除して 0 になったら次の順番になれるので
                # チェックリストに追加する
                todo.appendleft(t)

    print(*order)


solve()
