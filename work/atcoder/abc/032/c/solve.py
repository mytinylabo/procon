def solve():
    inf = float("inf")
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]

    if 0 in A:
        print(N)
        exit()

    A.append(inf)

    prod = 1
    maxlen = 0
    right = 0

    for left in range(N):
        while right < N and prod * A[right] <= K:
            prod *= A[right]
            right += 1
            maxlen = max(maxlen, right - left)

        if left == right:
            right += 1
        else:
            prod //= A[left]

    print(maxlen)


solve()
