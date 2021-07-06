def solve():
    A, B = map(int, input().split())

    if A + B >= 15 and B >= 8:
        ice_type = 1
    elif A + B >= 10 and B >= 3:
        ice_type = 2
    elif A + B >= 3:
        ice_type = 3
    else:
        ice_type = 4

    print(ice_type)


solve()
