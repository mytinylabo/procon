def solve():
    N = list("#".join(list(input().strip())))

    for i in range(8):
        for j in range(3):
            N[j * 2 + 1] = "+" if i & 1 << j else "-"

        f = "".join(N)

        if eval(f) == 7:
            print(f + "=7")
            exit()


solve()
