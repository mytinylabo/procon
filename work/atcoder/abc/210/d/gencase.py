from random import randint

H = 1000
W = 1000
C = randint(1, 10**9)

print(H, W, C)
for _ in range(H):
    print(*[randint(1, 10**9) for _ in range(W)])
