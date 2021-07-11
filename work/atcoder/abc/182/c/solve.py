def lmap(fn, seq): return list(map(fn, seq))


def solve():
    S = lmap(int, input().strip())
    L = len(S)

    cnt = [0, 0, 0]
    for d in S:
        cnt[d % 3] += 1

    m = (cnt[1] + cnt[2] * 2) % 3
    result = -1

    if m == 0:
        result = 0
    elif m == 1:
        if cnt[1] >= 1:
            result = 1
        elif cnt[2] >= 2:
            result = 2
    else:
        if cnt[2] >= 1:
            result = 1
        elif cnt[1] >= 2:
            result = 2

    # 全部の桁は消せない
    if result >= L:
        result = -1

    print(result)


solve()
