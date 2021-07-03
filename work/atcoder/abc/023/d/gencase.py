from random import randrange

# N, H, S = 10000, 10**9, 10**9
N, H, S = 100, 10**9, 10**9

print(N)
for i in range(N):
    print(randrange(H) + 1, randrange(S) + 1)
