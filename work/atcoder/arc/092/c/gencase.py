from random import randint

N = 100

print(N)
for _ in range(N * 2):
    print(randint(0, N * 2), randint(0, N * 2))
