def solve():
    a, b, x = map(int, input().split())

    def ndivs(n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        return n // x + 1

    print(ndivs(b) - ndivs(a - 1))


solve()
