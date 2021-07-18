def solve():
    N = int(input())
    S = [input().strip() for _ in range(N)]

    ans = []
    for c in "abcdefghijklmnopqrstuvwxyz":
        cnt = [s.count(c) for s in S]
        ans.append(c * min(cnt))

    print("".join(ans))


solve()
