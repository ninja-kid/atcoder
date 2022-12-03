#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from functools import lru_cache
from math import inf

import sys

sys.setrecursionlimit(10**6 + 100)


def main():
    A, B, C = map(int, input().split())

    @lru_cache(maxsize=None)
    def dfs(x, y, z):
        if x == 100 or y == 100 or z == 100:
            return 0
        ret = 0
        S = x + y + z
        ret += x / S * (dfs(x + 1, y, z) + 1)
        ret += y / S * (dfs(x, y + 1, z) + 1)
        ret += z / S * (dfs(x, y, z + 1) + 1)
        return ret

    ans = dfs(A, B, C)
    print(ans)


if __name__ == "__main__":
    main()
