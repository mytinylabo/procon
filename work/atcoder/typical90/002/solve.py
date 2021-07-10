def solve():
    N = int(input())

    if N % 2 == 1:
        exit()

    def paren(n, s):
        if len(s) == N:
            print("".join(s))
            return

        if n == 0:
            paren(1, s + ["("])
        elif n == (N - len(s)):
            paren(n - 1, s + [")"])
        else:
            paren(n + 1, s + ["("])
            paren(n - 1, s + [")"])

    paren(0, [])


solve()
