N = int(input())
nums = [*map(int, input().split(" "))]

costs = []
for x in range(min(nums), max(nums) + 1):
    costs.append((sum(map(lambda n: (n - x)**2, nums)), x))

print(sorted(costs)[0][0])
