def solve():
    cards = {
        "a": list(input().strip()),
        "b": list(input().strip()),
        "c": list(input().strip()),
    }

    cur = "a"
    while cards[cur]:
        cur = cards[cur].pop(0)

    print(cur.upper())


solve()
