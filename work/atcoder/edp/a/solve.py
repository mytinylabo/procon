N = int(input())
hs = list(map(int, input().split()))

dp = [0, abs(hs[1] - hs[0])]

for i in range(2, N):
    dp.append(min(dp[i - 2] + abs(hs[i] - hs[i - 2]),
                  dp[i - 1] + abs(hs[i] - hs[i - 1])))

print(dp[-1])
