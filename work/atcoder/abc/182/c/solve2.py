
# ビット全探索


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    S = lmap(int, input().strip())
    L = len(S)

    digits = list(enumerate(S[::-1]))
    results = []

    for mask in range(1, 1 << L):
        picked = [d for i, d in digits if (1 << i) & mask]
        if sum(picked) % 3 == 0:
            results.append(L - len(picked))

    print(min(results) if results else -1)


solve()
