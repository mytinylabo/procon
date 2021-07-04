from itertools import chain, zip_longest


def solve():
    SO = input().strip()
    SE = input().strip()

    print("".join(filter(None, chain.from_iterable(zip_longest(SO, SE)))))


solve()
