def solve():
    X = int(input())

    i = d = 0
    while d < X:
        i += 1
        d += i

    print(i)


solve()
