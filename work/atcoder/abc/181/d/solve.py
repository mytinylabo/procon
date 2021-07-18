from collections import defaultdict
from itertools import permutations


def solve():
    S = input().strip()

    cnt = defaultdict(int)
    for s in S:
        cnt[int(s)] += 1

    T = []
    for n, c in cnt.items():
        T.extend([str(n)] * min(c, 3))

    for tri in permutations(T, min(len(S), 3)):
        if int("".join(tri)) % 8 == 0:
            print("Yes")
            exit()

    print("No")


solve()
