from random import randint, randrange, sample, choice, choices
from bisect import bisect_left, insort_left


def solve():
    K = int(input())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    sorted_B = sorted(B)
    N = len(B)

    pairs = []
    for a in A:
        i = bisect_left(sorted_B, K - a)
        if i < N:
            insort_left(pairs, (a + sorted_B[i], a, sorted_B[i]))

    print(pairs[0] if pairs else "NO")


solve()
