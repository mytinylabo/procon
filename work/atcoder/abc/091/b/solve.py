def solve():
    N = int(input())
    B = [input().strip() for _ in range(N)]
    M = int(input())
    R = [input().strip() for _ in range(M)]

    score = map(lambda s: B.count(s) - R.count(s), B)

    print(max(0, max(score)))


solve()
