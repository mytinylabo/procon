from collections import defaultdict

N, M = map(int, input().split())
edges = defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].add(b)
    edges[b].add(a)

ps = {(1, (1,))}  # 次に調べるリスト
completes = set()  # 完走リスト

while ps:
    next_ps = set()
    for node, history in ps:
        next_nodes = edges[node] - set(history)
        if next_nodes:
            # 移動できる
            for n in next_nodes:
                # それぞれに移動した場合の履歴を作成して
                # 次に調べるリストに入れる
                next_ps.add((n, history + (n,)))
        else:
            # 移動できない
            if len(history) == N:
                # 履歴に全ノードが入っていたら完走
                completes.add(history)

    ps = next_ps

print(len(completes))
