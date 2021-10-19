def solve():
    S = input().strip()
    T = input().strip()
    print("YES" if S == T[::-1] else "NO")


solve()
