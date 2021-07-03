from random import randint

N = 10**5
M = 10**9

print(N)
for _ in range(3):
    print(*[randint(1, M) for _ in range(N)])
