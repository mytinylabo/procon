
N = 3 * 10**5

print(N)
print(*[200 if i % 2 == 0 else 0 for i in range(N)])
