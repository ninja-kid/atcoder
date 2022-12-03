#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    X = int(input())
    val = 0
    i = 0
    while val < X:
        i += 1
        val = (1 + i) * i // 2
    print(i)


if __name__ == "__main__":
    main()
