def solve():
    N, M = map(lambda s: int(s, 16), input().split())

    if N < M:
        print("<")
    elif N > M:
        print(">")
    else:
        print("=")


solve()
