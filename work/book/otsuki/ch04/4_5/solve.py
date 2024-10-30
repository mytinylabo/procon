def lmap(fn, seq):
    return list(map(fn, seq))


def solve():
    N, K = map(int, input().split())
    A = lmap(int, input().split())

    memo = dict()

    def check(n, k):
        if n == 0:
            return k == 0
        if k < 0:
            return False

        if (n, k) in memo:
            return memo[(n, k)]

        answer = check(n - 1, k) or check(n - 1, k - A[n - 1])

        memo[(n, k)] = answer
        return answer

    print("Yes" if check(N, K) else "No")


solve()
