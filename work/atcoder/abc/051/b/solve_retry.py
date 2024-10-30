def solve():
    K, S = map(int, input().split())

    n = 0
    for i in range(K + 1):
        for j in range(K + 1):
            if 0 <= S - (i + j) <= K:
                n += 1

    print(n)


solve()
