def solve():
    N = int(input())

    memo = {}

    def lucas(n):
        if n in memo:
            return memo[n]

        if n == 0:
            ret = 2
        elif n == 1:
            ret = 1
        else:
            ret = lucas(n - 1) + lucas(n - 2)

        memo[n] = ret
        return ret

    print(lucas(N))


solve()
