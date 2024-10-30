def lmap(fn, seq):
    return list(map(fn, seq))


def solve():
    N, K = map(int, input().split())
    A = lmap(int, input().split())

    memo_flag = [[False] * (K + 1) for _ in range(N + 1)]
    memo_value = [[False] * (K + 1) for _ in range(N + 1)]

    def check(n, k):
        if n == 0:
            return k == 0
        if k < 0:
            return False

        if memo_flag[n][k]:
            return memo_value[n][k]

        answer = check(n - 1, k) or check(n - 1, k - A[n - 1])

        memo_flag[n][k] = True
        memo_value[n][k] = answer
        return answer

    print("Yes" if check(N, K) else "No")


solve()
