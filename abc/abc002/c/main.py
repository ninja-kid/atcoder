#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    xa, ya, xb, yb, xc, yc = map(int, input().split())
    x1 = xb - xa
    x2 = xc - xa
    y1 = yb - ya
    y2 = yc - ya
    ans = abs(x1 * y2 - x2 * y1) / 2
    print(ans)


if __name__ == "__main__":
    main()
