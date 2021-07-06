def is_prime(n):
    if n < 2:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def solve():
    N = int(input())

    for i in range(N, N * 2 + 1):
        if is_prime(i):
            print(i)
            exit()


solve()
