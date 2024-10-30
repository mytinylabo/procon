def lmap(fn, seq):
    return list(map(fn, seq))


def solve():
    N = int(input())
    H = lmap(int, input().split())

    count = H[0]

    for i in range(1, N):
        if H[i] >= H[i - 1]:
            count += H[i] - H[i - 1]

    print(count)


solve()
