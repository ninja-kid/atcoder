#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import Counter, defaultdict
from math import inf


def main():
    N = int(input())
    cnt = defaultdict(list)
    E = []
    for _ in range(N):
        m = int(input())
        d = {}
        for _ in range(m):
            p, e = map(int, input().split())
            d[p] = e
            if not cnt[p] or cnt[p][0] < e:
                cnt[p] = [e, 1]
            elif cnt[p][0] == e:
                cnt[p][1] += 1
        E.append(d)

    flg = False
    ans = 0
    for dd in E:
        is_single = False
        for k in dd:
            if cnt[k][0] == dd[k] and cnt[k][1] == 1:
                is_single = True
                break
        if is_single:
            ans += 1
        elif not flg:
            ans += 1
            flg = True
    print(ans)


if __name__ == "__main__":
    main()
