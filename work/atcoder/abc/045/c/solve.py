def solve():
    S = list(input())

    total = 0

    for i in range(2 ** (len(S) - 1)):
        formula = ""
        for j in range(len(S) - 1):
            formula += S[j]
            if (i >> j) & 0b1:
                formula += "+"
        formula += S[-1]
        total += sum(map(int, formula.split("+")))

    print(total)


solve()
