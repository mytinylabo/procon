from bisect import bisect


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N, M = map(int, input().split())
    A = lmap(int, input().split())
    B = lmap(int, input().split())

    B.sort()

    ans = []
    for a in A:
        i = bisect(B, a)
        if i == 0:
            ans.append(abs(a - B[i]))
        elif i == M:
            ans.append(abs(a - B[i - 1]))
        elif a == B[i]:
            ans.append(0)
        else:
            ans.append(min(abs(a - B[i]), abs(a - B[i - 1])))

    print(min(ans))


solve()
