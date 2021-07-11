from random import randint, choices

N = 10**5
Q = 10**5

nlist = list(range(1, N + 1))

print(N, Q)
print(*[randint(1, 10**9) for _ in range(N)])
for _ in range(Q):
    t = randint(1, 3)
    if t == 1:
        print(t, *choices(nlist, k=2))
    elif t == 2:
        print(t, 0, 0)
    else:
        print(t, randint(1, N), 0)
