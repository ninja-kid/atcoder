#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import defaultdict
from math import inf


def main():
    N, M = map(int, input().split())
    P = []
    for i in range(M):
        p, y = map(int, input().split())
        P.append((y, p, i))
    P.sort()
    d = defaultdict(int)
    ans = [""] * M
    for y, p, i in P:
        d[p] += 1
        ans[i] = str(p).zfill(6) + str(d[p]).zfill(6)
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
