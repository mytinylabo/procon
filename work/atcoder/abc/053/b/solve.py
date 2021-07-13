def solve():
    S = input().strip()
    print(S.rindex("Z") - S.index("A") + 1)


solve()
