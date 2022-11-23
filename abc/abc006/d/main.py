#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from bisect import bisect_left
from math import inf


def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    def get_lis(arr):
        L = [inf] * (len(arr) + 1)
        L[0] = -inf
        ret = 0
        for a in arr:
            idx = bisect_left(L, a)
            ret = max(ret, idx)
            L[idx] = a
        return ret

    val = get_lis(A)
    print(N - val)


if __name__ == "__main__":
    main()
