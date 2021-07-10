from random import random

H = 2000
W = 2000

wall_rate = 0.0

print(H, W)
for _ in range(H):
    print("".join(["." if random() > wall_rate else "#" for _ in range(W)]))
