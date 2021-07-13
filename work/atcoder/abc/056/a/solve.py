def solve():
    a, b = input().strip().split()
    if a == "H":
        print(b)
    else:
        print("D" if b == "H" else "H")


solve()
