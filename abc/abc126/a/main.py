#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, K= map(int, input().split())
    S = list(input())
    K -= 1
    S[K] = S[K].lower()
    print(''.join(S))


if __name__ == "__main__":
    main()
