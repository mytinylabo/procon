def solve():
    A, B = map(int, input().split())
    m = [A % 3, B % 3, (A + B) % 3]

    print("Possible" if 0 in m else "Impossible")


solve()
