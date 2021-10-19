from collections import Counter


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N, K = map(int, input().split())
    A = lmap(int, input().split())

    cnt = Counter(A)

    if len(cnt) <= K:
        print(0)
        exit()

    scnt = sorted(cnt.items(), key=lambda c: c[1])
    print(sum(map(lambda c: c[1], scnt[:len(cnt) - K])))


solve()
