from collections import defaultdict


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    _ = int(input())
    A = lmap(int, input().split())

    C = defaultdict(int)
    for a in A:
        C[a] += 1

    result = 0
    for i in C.keys():
        for j in C.keys():
            if i > j:
                result += C[i] * C[j] * (i - j)**2

    print(result)


solve()


"""
# 累積和で解く方法
# 悪くないけど全探索のチャンスにもうちょっと気付きたい…

from itertools import accumulate

def lmap(fn, seq): return list(map(fn, seq))

def solve():
    N = int(input())
    A = lmap(int, input().split())

    acc_A = list(accumulate(A))
    acc_A2 = list(accumulate(map(lambda a: a * a, A)))

    result = 0
    for i in range(1, N):
        result += (A[i]**2) * i - 2 * A[i] * acc_A[i - 1] + acc_A2[i - 1]

    print(result)
"""
