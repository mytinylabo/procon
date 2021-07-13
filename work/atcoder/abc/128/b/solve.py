
def astypes(line, *types):
    return tuple(map(lambda p: p[0](p[1]),
                     zip(types, line.strip().split(" "))))


def solve():
    N = int(input())
    R = [(i + 1, *astypes(input(), str, int)) for i in range(N)]

    R.sort(key=lambda r: r[2], reverse=True)
    R.sort(key=lambda r: r[1])

    for i, _, _ in R:
        print(i)


solve()
