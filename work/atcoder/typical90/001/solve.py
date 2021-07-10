def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N, L = map(int, input().split())
    K = int(input())
    A = lmap(int, input().split())
    A.append(L)
    # print(N, L, K, A)

    def cut(t):
        prev = 0
        cnt = 0
        for i in range(N + 1):
            if A[i] - prev >= t:
                prev = A[i]
                cnt += 1

        return cnt >= K + 1

    left = 0
    right = L
    while right - left > 1:
        mid = (right + left) // 2
        if cut(mid):
            left = mid
        else:
            right = mid

    print(left)


solve()
