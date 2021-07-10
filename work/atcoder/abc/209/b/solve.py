def solve():
    N, X = map(int, input().split())
    A = [a - 1 if i % 2 == 1 else a for i, a in enumerate(map(int, input().split()))]

    print("Yes" if sum(A) <= X else "No")


solve()
