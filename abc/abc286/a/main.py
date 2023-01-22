#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, P, Q, R, S = map(int, input().split())
    A = list(map(int, input().split()))

    print(*(A[0:P-1] + A[R-1:S] + A[Q:R-1] + A[P-1:Q] + A[S:]))


if __name__ == "__main__":
    main()
