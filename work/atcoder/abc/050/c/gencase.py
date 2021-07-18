from random import shuffle

N = 10**5

ns = list(range(1, N, 2)) + list(range(1, N, 2))
shuffle(ns)

print(N)
print(*ns)
