S = input().strip()

diffs = map(lambda i: abs(753 - int(S[i:i + 3])), range(len(S) - 2))
print(sorted(diffs)[0])
