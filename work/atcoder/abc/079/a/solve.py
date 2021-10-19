def solve():
    N = input().strip()

    print("Yes"
          if len(set(N[:-1])) == 1 or len(set(N[1:])) == 1
          else "No")


solve()
