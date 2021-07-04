def solve():
    _ = int(input())
    S = input().strip()
    # print(S)

    sp = 0
    n_left = 0
    for p in S:
        if p == "(":
            sp += 1
        else:
            sp -= 1
            if sp < 0:
                # ")" 過多になるたび、あとで文頭に "(" を
                # 追加することにして sp を 0 に補正する
                n_left += 1
                sp = 0

    print("(" * n_left + S + ")" * sp)


solve()
