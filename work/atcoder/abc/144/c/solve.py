def divisors(n):
    low = []
    high = []

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            low.append(i)
            if i != n // i:
                high.append(n // i)

    return low + high[::-1]


def solve():
    N = int(input())
    xs = sorted(map(lambda d: (d + (N // d) - 2, d), divisors(N)))

    print(xs[0][0])


solve()
