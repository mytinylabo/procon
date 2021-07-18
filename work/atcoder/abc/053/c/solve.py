def solve():
    x = int(input())

    ans = (x // 11) * 2
    x %= 11

    if x > 0:
        x -= 6
        ans += 1

    if x > 0:
        x -= 5
        ans += 1

    print(ans)


solve()
