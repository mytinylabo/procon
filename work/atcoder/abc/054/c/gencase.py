from itertools import combinations

# 全部のノードが連結している場合のテストケースを作る

N = 8

edges = set(combinations(range(1, N + 1), 2))

print(N, len(edges))
for e in edges:
    print(*e)
