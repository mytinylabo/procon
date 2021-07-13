def solve():
    S = set(input().strip())
    A = set("abcdefghijklmnopqrstuvwxyz")

    unused = sorted(A - S)
    print(unused[0] if unused else "None")


solve()
