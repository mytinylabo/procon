def solve():
    X, A, B = map(int, input().split())
    if B - A >= X + 1:
        print("dangerous")
    elif B - A >= 1:
        print("safe")
    else:
        print("delicious")


solve()
