def solve():
    N = int(input())
    S = [int(input()) for _ in range(N)]

    score = sum(S)
    if score % 10 != 0:
        print(score)
    else:
        ts = sorted(filter(lambda s: s % 10 != 0, S))
        if len(ts) == 0:
            print(0)
        else:
            print(score - ts[0])


solve()
