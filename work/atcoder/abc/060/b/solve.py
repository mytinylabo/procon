def solve():
    A, B, C = map(int, input().split())

    valid = C in [(x * A) % B for x in range(200)]
    print("YES" if valid else "NO")


solve()
