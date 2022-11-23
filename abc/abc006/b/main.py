#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from functools import lru_cache
from math import inf

import sys

sys.setrecursionlimit(10**6)


def main():
    N = int(input())

    A = [0, 0, 1]
    for i in range(3, N):
        A.append((A[-1] + A[-2] + A[-3]) % 10007)
    print(A[N - 1])


if __name__ == "__main__":
    main()
