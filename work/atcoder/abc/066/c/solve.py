from collections import deque


def solve():
    N = int(input())
    A = map(int, input().split())

    bs = deque([])

    for i, a in enumerate(A):
        if (i + 1) % 2 == 1:
            bs.append(a)
        else:
            bs.appendleft(a)

    print(*(list(bs)[::-1] if N % 2 == 1 else bs))


solve()
