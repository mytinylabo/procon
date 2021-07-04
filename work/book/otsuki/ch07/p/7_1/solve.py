from bisect import bisect


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    _ = input().strip()
    A, B = [lmap(int, input().split()) for _ in range(2)]
    # print(N, A, B)

    A.sort()
    B.sort(reverse=True)

    right = len(A)
    pairs = []
    for b in B:
        right = bisect(A, b, 0, right) - 1
        if right < 0:
            # 残った最大の b より大きい a がないので終了
            break
        pairs.append((A[right], b))

    # print(pairs)
    print(len(pairs))


solve()
