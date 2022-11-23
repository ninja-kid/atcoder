#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    C = [input().split() for _ in range(4)]
    for i in range(4):
        val = []
        for j in range(4):
            val.append(C[3 - i][3 - j])
        print(*val)


if __name__ == "__main__":
    main()
