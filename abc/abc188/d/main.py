#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import defaultdict
from math import inf


def main():
    N, C = map(int, input().split())
    d = defaultdict(int)
    days = set()
    for _ in range(N):
        a, b, c = map(int, input().split())
        d[a] += c
        d[b + 1] -= c
        days.add(a)
        days.add(b + 1)
    days = list(days)
    days.sort()
    now = 0
    a = 0
    ans = 0
    for day in days:
        ans += min(a, C) * (day - now)
        a += d[day]
        now = day
    print(ans)


if __name__ == "__main__":
    main()
