from random import choices

N = 100
print(N)
print(*choices(range(1000), k=N))
