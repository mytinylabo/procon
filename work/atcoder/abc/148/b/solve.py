from itertools import chain


def solve():
    _ = int(input())
    S, T = input().strip().split()

    print("".join(chain.from_iterable(zip(S, T))))


solve()
