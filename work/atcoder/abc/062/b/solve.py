def with_guards(height, width, guard):
    field = [guard * (width + 2)]
    field += [guard + input().strip() + guard
              for _ in range(height)]
    field += [guard * (width + 2)]
    return field


def solve():
    H, W = map(int, input().split())
    F = with_guards(H, W, "#")
    print("\n".join(F))


solve()
