#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from collections import deque
from math import inf


def main():
    N = int(input())
    A = list(range(1, 7))
    N %= 30
    for i in range(N):
        a = (i % 5)
        b = a + 1
        A[a], A[b] = A[b], A[a]
    print(*A, sep='')


if __name__ == "__main__":
    main()
