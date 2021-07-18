def lmap(fn, seq): return list(map(fn, seq))


def solve():
    mod = 10**9 + 7

    N = int(input())
    A = lmap(int, input().split())

    A.sort()
    n = 0

    while A:
        if len(A) >= 2:
            if (N - 1 - n * 2 == A.pop() == A.pop()):
                n += 1
            else:
                print(0)
                exit()
        elif len(A) == 1:
            if A.pop() != 0:
                print(0)
                exit()

    print(pow(2, n, mod))


solve()
