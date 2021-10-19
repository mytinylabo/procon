def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N = int(input())
    A = lmap(int, input().split())

    A.append(-1)

    cnt = 0
    for i in range(N):
        if A[i] == i + 1:
            A[i], A[i + 1] = A[i + 1], A[i]
            cnt += 1

    print(cnt)


solve()
