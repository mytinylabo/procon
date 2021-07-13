def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N = int(input())
    A = lmap(int, input().split())

    s = x = n = right = 0
    pairs = []

    for left in range(N):
        while right < N and s + A[right] == x ^ A[right]:
            s += A[right]
            x ^= A[right]
            pairs.append((left, right))
            right += 1

        n += right - left

        if left == right:
            right += 1
        else:
            s -= A[left]
            x ^= A[left]

    print(n)


solve()
