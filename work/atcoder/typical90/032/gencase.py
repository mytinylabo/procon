from random import randint

N = 10
M = 0

print(N)
for i in range(N):
    print(*[randint(1, 1000) for _ in range(N)])

print(M)
