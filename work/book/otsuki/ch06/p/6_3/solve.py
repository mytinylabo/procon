from bisect import bisect


def lmap(fn, seq): return list(map(fn, seq))


def solve():
    N, M = map(int, input().split())
    nums = lmap(int, input().split())
    # print(N, M, nums)

    S = set()
    for i in range(N):
        for j in range(i, N):
            S.add(nums[i] + nums[j])

    S = sorted(S)
    # print(S, S[0], S[-1])

    results = []
    for a in S:
        i = bisect(S, M - a)

        if i == 0:
            # どう選んでも超えてしまう
            continue

        # print(a, i, S[i - 1])
        results.append(S[i - 1] + a)

    print(max(results))


solve()
