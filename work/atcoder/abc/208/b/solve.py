from math import factorial


def solve():
    P = int(input())

    coins = {}
    for i in range(1, 11):
        coins[i] = factorial(i)

    count = 0
    p = P
    for i in reversed(range(1, 11)):
        count += p // coins[i]
        p = p % coins[i]

    print(count)


solve()
