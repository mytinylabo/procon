def solve():
    S = input().strip()
    L = len(S)
    # print(S)

    for i in range(L - 1):
        if S[i] == S[i + 1]:
            print(i + 1, i + 2)
            exit()
        elif i < L - 2 and S[i] == S[i + 2]:
            print(i + 1, i + 3)
            exit()

    print(-1, -1)


solve()
