from random import randint

N = 10**5
M = 10**5

print(N)
for _ in range(N):
    print(randint(1, M // 4) * 2 - 1, randint(M // 4, M // 2) * 2 - 1)
