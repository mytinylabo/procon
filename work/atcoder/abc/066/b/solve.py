def solve():
    S = input().strip()

    def odds(s):
        return len(s) % 2 == 0 and s[:len(s) // 2] == s[len(s) // 2:]

    x = 1
    while not odds(S[:len(S) - x]):
        x += 1

    print((len(S) - x))


solve()
