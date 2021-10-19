from random import randint

Q = 2 * 10**5

print(Q + 1)
for _ in range(Q // 2):
    print(1, randint(1, 10**9))

for _ in range(Q // 2):
    print(2, randint(1, 10**9))

print(3)


# Q = 2 * 10**5


# print(Q)

# n = 0
# for _ in range(Q):
#     q = randint(1, 3 if n > 0 else 2)
#     if q == 1:
#         n += 1
#         print(q, randint(1, 10**9))
#     if q == 2:
#         print(q, randint(1, 10**9))
#     else:
#         n -= 1
#         print(3)
