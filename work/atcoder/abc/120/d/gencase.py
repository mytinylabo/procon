from random import choices

N = 10**5
M = 10**5

islands = list(range(1, N + 1))
E = {tuple(sorted(choices(islands, k=2))) for _ in range(M)}

print(N, len(E))
for a, b in E:
    print(a, b)
