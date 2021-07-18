from random import randint

N = 10**5
P = (1, 10**9)

print(N)
for _ in range(N):
    print(randint(*P), randint(*P))
