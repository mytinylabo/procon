def solve():
    _ = int(input())
    S = input().strip()

    i = S.index("1")

    print("Takahashi" if i % 2 == 0 else "Aoki")


solve()
