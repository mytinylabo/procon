def solve():
    S = input().strip()
    T = input().strip()

    print("Yes" if all([S[i] == T[i] for i in range(len(S))]) else "No")


solve()
