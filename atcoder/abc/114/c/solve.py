from itertools import product
N = int(input())

result = []
for i in range(1, 10):
    n753 = [int("".join(seq)) for seq in product("753", repeat=i) if len(set(seq)) == 3]
    result += [n for n in n753 if n <= N]

print(len(result))

# 再帰による別解
#
# def count753(s):
#     if s != "" and int(s) > N:
#         return 0

#     # s が七五三数なら数える
#     cnt = 1 if len(set(s)) == 3 else 0

#     for c in "753":
#         cnt += count753(s + c)

#     return cnt


# print(count753(""))
