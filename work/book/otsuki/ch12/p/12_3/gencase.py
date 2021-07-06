from random import randint, choices

N = 30000
K = randint(1, N + 1)

print(N, K)
print(*[n for n in choices(range(N * 10), k=N)])
