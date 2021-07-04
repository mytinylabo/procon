def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N = int(input())
    A = [tmap(int, input().split()) for _ in range(N)]
    B = [tmap(int, input().split()) for _ in range(N)]
    # print(N, A, B)

    A.sort(key=lambda a: a[1], reverse=True)
    B.sort()

    picked = [False] * N
    pairs = []
    for b in B:
        for i, a in enumerate(A):
            ax, ay = a
            bx, by = b
            if ax < bx and ay < by and not picked[i]:
                picked[i] = True
                pairs.append((a, b))
                break

    print(len(pairs))


solve()
