from collections import defaultdict


def tmap(fn, seq):
    return tuple(map(fn, seq))


def solve():
    N, M = map(int, input().split())
    C = [tmap(int, input().split()) for _ in range(M)]

    SC = sorted(C, key=lambda x: x[1])

    count = defaultdict(int)
    city_num = dict()

    for pref, year in SC:
        count[pref] += 1
        # 同じ年に誕生した都市はないので、誕生年に対して県内での誕生順を紐付ける
        city_num[year] = count[pref]

    for pref, year in C:
        print(f"{pref:06}{city_num[year]:06}")


solve()
