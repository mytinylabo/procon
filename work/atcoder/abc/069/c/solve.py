def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N = int(input())
    A = lmap(int, input().split())

    cnt2 = 0
    cnt4 = 0
    for a in A:
        if a % 4 == 0:
            cnt4 += 1
        elif a % 2 == 0:
            cnt2 += 1

    if cnt4 + 1 >= N - cnt2 - cnt4 + (1 if cnt2 else 0):
        print("Yes")
    else:
        print("No")


solve()
