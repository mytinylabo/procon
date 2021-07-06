from bisect import insort


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N, K = map(int, input().split())
    A = lmap(int, input().split())

    S = []

    for i, a in enumerate(A):
        insort(S, a)

        if i + 1 >= K:
            print(S[K - 1])


solve()

# N = 30000
# append ==> sort  N^2 log(N) : 2.800s
# bisect.insort    N log(N)   : 0.109s
