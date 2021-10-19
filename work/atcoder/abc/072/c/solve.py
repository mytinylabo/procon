from collections import defaultdict


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    _ = int(input())
    A = lmap(int, input().split())

    cnt = defaultdict(int)
    for a in A:
        cnt[a] += 1
        cnt[a - 1] += 1
        cnt[a + 1] += 1

    ans = max(cnt.values())
    print(ans)


solve()
