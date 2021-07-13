def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N = int(input())
    A = lmap(int, input().split()) + [0]

    n_pairs = 0
    right = 0

    for left in range(N):
        while A[right] < A[right + 1]:
            right += 1

        n_pairs += right - left + 1
        if left == right:
            right += 1

    print(n_pairs)


solve()
