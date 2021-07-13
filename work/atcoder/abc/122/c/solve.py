def tmap(fn, seq): return tuple(map(fn, seq))


def solve():
    N, M = map(int, input().split())
    S = input().strip()
    Q = [tmap(int, input().split()) for _ in range(M)]

    acc = [0, 0]
    for i in range(1, N):
        if S[i - 1] == "A" and S[i] == "C":
            acc.append(acc[-1] + 1)
        else:
            acc.append(acc[-1])

    for ql, qr in Q:
        print(acc[qr] - acc[ql])


solve()
