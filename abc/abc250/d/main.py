#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from bisect import bisect_left, bisect_right
from math import inf


def main():
    N = int(input())

    def eratos(n):
        val = [True] * (n + 1)
        val[0] = False
        val[1] = False
        for i in range(n + 1):
            if not val[i]:
                continue
            for j in range(2 * i, n + 1, i):
                val[j] = False
        ret = [i for i in range(n + 1) if val[i]]
        return ret

    sosus = eratos(int(N ** (1 / 3)))

    ans = 0
    for i in range(len(sosus)):
        j = bisect_right(sosus, N // (sosus[i] ** 3))
        ans += min(i, j)
    print(ans)


if __name__ == "__main__":
    main()
