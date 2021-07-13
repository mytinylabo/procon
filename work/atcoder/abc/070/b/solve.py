def solve():
    A, B, C, D = map(int, input().split())
    print(len(set(range(A, B)) & set(range(C, D))))


solve()
