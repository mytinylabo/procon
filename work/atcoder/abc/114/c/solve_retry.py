import itertools


def solve():
    N = int(input())

    n753 = []

    for i in range(1, 10):
        n753 += [
            int("".join(seq))
            for seq in itertools.product("753", repeat=i)
            if len(set(seq)) == 3
        ]

    print(len([n for n in n753 if n <= N]))


solve()
