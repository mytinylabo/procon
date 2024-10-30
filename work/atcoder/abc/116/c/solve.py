def lmap(fn, seq):
    return list(map(fn, seq))


def solve():
    N = int(input())
    H = lmap(int, input().split())

    def split(hs):
        # 0 をデリミタとしてリストを分割する
        # [4, 23, 75, 0, 23, 0, 0, 50 100]
        # -> [[4, 23, 75], [23], [50, 100]]
        result = []
        subset = []
        for h in hs:
            if h == 0:
                if subset:
                    result.append(subset)
                    subset = []
            else:
                subset.append(h)

        if subset:
            result.append(subset)

        return result

    def water(hs):
        # 水やり回数を求める
        # [考え方]
        # 与えられた状態から水を奪っていき、全ての高さを 0 にするまでの回数を求める
        # 0 からはそれ以上奪えないので、0 を含まない部分列に分割して再帰的に回数を求めていく

        # hs がすべて 0 ならループは回らず、水やり回数は 0 回となる（再帰の基底条件）
        count = 0

        for sub_hs in split(hs):
            sub_count = min(sub_hs)
            count += sub_count
            count += water(lmap(lambda x: x - sub_count, sub_hs))

        return count

    print(water(H))


solve()
