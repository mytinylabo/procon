def lmap(fn, seq): return list(map(fn, seq))
def tmap(fn, seq): return tuple(map(fn, seq))
def lfilter(fn, seq): return list(filter(fn, seq))


def solve():
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(N)]

    A.sort()

    left = 0
    right = A[-1]
    while right - left > 1:
        mid = (right + left) // 2

        last_shed = 0
        n_put = 1
        for i in range(1, N):
            if A[i] - A[last_shed] >= mid:
                n_put += 1
                last_shed = i

        if n_put >= M:
            left = mid
        else:
            right = mid

    print(left)


solve()
