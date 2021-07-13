def solve():
    A, B = map(int, input().split())

    for n in range(1, 1300):
        if int(n * 0.08) == A and int(n * 0.1) == B:
            print(n)
            exit()

    print(-1)


solve()
