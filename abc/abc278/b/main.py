#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    H, M = map(int, input().split())

    while True:
        h = str(H).zfill(2)
        m = str(M).zfill(2)
        hh = int(h[0] + m[0])
        mm = int(h[1] + m[1])
        if 0 <= hh < 24 and 0 <= mm < 60:
            print(H, M)
            return
        M += 1
        H += M // 60
        H %= 24
        M %= 60


if __name__ == "__main__":
    main()
