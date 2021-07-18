from random import randint, random

H = 500
W = 500

A = []
for _ in range(H):
    A.append([".#"[0 if random() < 0.2 else 1] for _ in range(W)])

sx = gx = randint(0, W - 1)
sy = gy = randint(0, H - 1)
while sx == gx and sy == gy:
    gx = randint(0, W - 1)
    gy = randint(0, H - 1)

A[sy][sx] = "s"
A[gy][gx] = "g"

print(H, W)
for a in A:
    print("".join(a))
