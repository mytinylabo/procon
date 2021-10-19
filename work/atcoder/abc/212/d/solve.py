from heapq import heappush, heappop


def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    Q = int(input())

    hs = []
    q2 = 0

    for _ in range(Q):
        q = tmap(int, input().split())

        if q[0] == 1:
            heappush(hs, q[1] - q2)

        elif q[0] == 2:
            q2 += q[1]

        else:
            n = heappop(hs)
            print(n + q2)


solve()
