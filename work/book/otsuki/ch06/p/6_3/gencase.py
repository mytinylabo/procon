from random import randint

N = 1000
M = 2 * 10**8

print(N, M)
print(*[randint(1, 10**8) for _ in range(N)])
