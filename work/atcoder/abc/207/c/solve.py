def tmap(fn, seq): return tuple(map(fn, seq))


def seg(t, left, right):
    if t >= 3:
        left += 0.1
    if t % 2 == 0:
        right -= 0.1
    return left, right


def solve():
    N = int(input())
    A = [tmap(int, input().split()) for _ in range(N)]

    cnt = 0

    for i in range(N - 1):
        il, ir = seg(*A[i])
        for j in range(i + 1, N):
            jl, jr = seg(*A[j])

            if il <= jr and jl <= ir:
                cnt += 1

    print(cnt)


solve()
