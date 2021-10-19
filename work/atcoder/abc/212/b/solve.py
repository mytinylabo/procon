def lmap(fn, seq): return list(map(fn, seq))


def solve():
    X = lmap(int, input().strip())

    if len(set(X)) == 1:
        print("Weak")
        exit()

    weak = True
    for i in range(3):
        weak = weak and (X[i] + 1 == X[i + 1] or ((X[i], X[i + 1]) == (9, 0)))

    print("Weak" if weak else "Strong")


solve()
