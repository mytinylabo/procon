def solve():
    N = int(input())
    print(sum(map(lambda i: N / (N - i), range(1, N))))


solve()
