def solve():
    N = int(input())

    if N < 10 or N % 2 == 1:
        print(0)
        exit()

    ans = 0
    m = 5
    while m <= N:
        ans += (N // m) // 2
        m *= 5

    print(ans)


solve()
