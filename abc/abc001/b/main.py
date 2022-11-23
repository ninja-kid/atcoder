#!/usr/bin/env python3
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
mod1 = 10**9 + 7
mod2 = 998244353
from math import inf


def main():
    m = int(input())

    if m < 100:
        ans = 0
    elif m <= 5000:
        ans = m // 100
    elif m <= 30000:
        ans = m // 1000 + 50
    elif m <= 70000:
        ans = (m // 1000 - 30) // 5 + 80
    else:
        ans = 89
    print(str(ans).zfill(2))

if __name__ == "__main__":
    main()
