from random import choice

N = 100

print(N)
print("".join([choice("()") for _ in range(N)]))
