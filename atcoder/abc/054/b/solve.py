import sys

N, M = map(int, input().split())
A = [input().strip() for _ in range(N)]
B = [input().strip() for _ in range(M)]

for i in range(0, N - M + 1):
    for j in range(0, N - M + 1):
        if all(map(lambda k: A[i + k][j:j + M] == B[k], range(M))):
            print("Yes")
            sys.exit()

print("No")
