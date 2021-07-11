def solve():
    S = input().strip()

    count = {c: S.count(c) for c in S}
    print("Yes" if all(map(lambda n: n % 2 == 0, count.values())) else "No")


solve()
