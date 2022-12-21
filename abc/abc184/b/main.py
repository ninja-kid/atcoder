#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == "o":
            X += 1
        else:
            X = max(0, X - 1)
    print(X)


if __name__ == "__main__":
    main()
