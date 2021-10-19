from collections import Counter


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    _ = int(input())
    A = lmap(int, input().split())

    cnt = Counter(A)
    pairs = [k for k, v in sorted(cnt.items(), reverse=True) if v >= 2]

    if len(pairs) < 2:
        print(0)
    elif cnt[pairs[0]] >= 4:
        print(pairs[0]**2)
    else:
        print(pairs[0] * pairs[1])


solve()
