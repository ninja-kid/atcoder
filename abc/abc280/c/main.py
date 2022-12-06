#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    S = list(input())
    T = list(input())
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i + 1)
            return
    print(len(S) + 1)


if __name__ == "__main__":
    main()
