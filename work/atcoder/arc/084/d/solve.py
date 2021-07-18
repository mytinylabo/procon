from collections import deque


def solve():
    inf = float('inf')

    K = int(input())

    dist = [inf] * K
    dist[1] = 1
    todo = deque([1])

    while todo:
        n = todo.pop()
        c = dist[n]

        m10 = (n * 10) % K
        if c < dist[m10]:
            dist[m10] = c
            todo.append(m10)

        m1 = (n + 1) % K
        if c + 1 < dist[m1]:
            dist[m1] = c + 1
            todo.appendleft(m1)

    print(dist[0])


solve()
