def solve():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    adj = {}
    for i, a in enumerate(A):
        adj[i + 1] = a

    btn = 1
    for i in range(N):
        btn = adj[btn]
        if btn == 2:
            print(i + 1)
            exit()

    print(-1)


solve()
