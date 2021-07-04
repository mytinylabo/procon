from random import randint

N = 1000
M = N * 10

print(N)
print(*[randint(0, M) for _ in range(N)])
print(*[randint(0, M) for _ in range(N)])
