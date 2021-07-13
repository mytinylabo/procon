from itertools import accumulate


def solve():
    _ = int(input())
    S = map(lambda c: 1 if c == "I" else -1, input().strip())

    print(max(accumulate(S, initial=0)))


solve()
