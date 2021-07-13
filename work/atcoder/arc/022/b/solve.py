def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N = int(input())
    A = lmap(int, input().split())

    flavors = set()
    maxlen = 0
    right = 0

    for left in range(N):
        while right < N and A[right] not in flavors:
            flavors.add(A[right])
            right += 1
            maxlen = max(maxlen, right - left)

        if left == right:
            right += 1
        else:
            flavors.remove(A[left])

    print(maxlen)


solve()
